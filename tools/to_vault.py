"""Convert the Sphinx singlehtml build of the Kinovea manual into a Zettelkasten-style Obsidian vault.

Hierarchy:  part (1..N)  ->  chapter (1a, 1b..)  ->  atomic note (1a1, 1a2..)   [Folgezettel IDs]
Usage: python -I to_vault.py <singlehtml dir> <vault dir> <commit> <sphinx source dir>
"""
import json, os, re, shutil, string, subprocess, sys
from bs4 import BeautifulSoup, NavigableString, Tag

html_dir, vault, commit, docsrc = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
soup = BeautifulSoup(open(os.path.join(html_dir, "index.html"), encoding="utf-8"), "html.parser")
main = soup.select_one('div[itemprop="articleBody"]')

API_PART = "API and integration reference"
LEGACY_PART = "Legacy documentation (obsolete)"
DOCS_COMMIT = "375e293"

# Where to look instead, for chapters that are empty stubs in the official manual (titles of other notes).
STUB_SEE_ALSO = {
    "Recording triggers": ["UDP network trigger", "Automation", "Integration overview"],
    "Trajectory object": ["Tracking point trajectories"],
    "Trackable drawings": ["Tracking distances and angles"],
    "Tracked coordinates": ["Tracked coordinate system"],
    "Tracking algorithms": ["Tracking parameters"],
    "Context variables": ["Image naming", "Video naming"],
    "Capture folders": ["Image naming", "Video naming"],
    "Calibration validation": ["Guidelines to minimize errors"],
}

# ---------------------------------------------------------------- structure
nav = soup.select_one(".wy-menu-vertical")
parts = []
for el in nav.children:
    if not isinstance(el, Tag):
        continue
    if el.name == "p" and "caption" in el.get("class", []):
        parts.append({"title": el.get_text(strip=True), "chapters": []})
    elif el.name == "ul" and parts:
        for li in el.find_all("li", recursive=False):
            parts[-1]["chapters"].append(li.find("a")["href"].lstrip("#"))

def clean_title(t):
    t = re.sub(r"[\ue000-\uf8ff¶]", "", t).strip()  # theme icon glyphs
    t = re.sub(r'[\\/:*?"<>|#^\[\]]', "-", t)
    return re.sub(r"\s+", " ", t)

def heading_text(sec):
    h = sec.find(re.compile(r"^h[1-6]$"), recursive=False)
    return clean_title(h.get_text()) if h else "Untitled"

notes = []          # dicts: id, title, kind, part, parent, children, html_nodes, level, folder, source
by_anchor = {}      # element id -> [(note, heading text or None), ...]  (ids repeat across pages in singlehtml)

def register_ids(note, node, nested_heading=None):
    if isinstance(node, Tag):
        if node.get("id"):
            by_anchor.setdefault(node["id"], []).append((note, nested_heading))
        for d in node.find_all(id=True):
            h = None
            if d.name == "section" and d is not node:
                h = heading_text(d)
            by_anchor.setdefault(d["id"], []).append((note, h or nested_heading))

SPLIT_CHARS = 3500  # below a chapter, only split notes this long that have sub-sections

def is_wrapper(c):
    return isinstance(c, Tag) and c.name == "div" and "toctree-wrapper" in c.get("class", [])

def is_heading(c):
    return isinstance(c, Tag) and re.match(r"^h[1-6]$", c.name)

def sub_sections(sec):
    """Direct sub-sections, plus sub-documents Sphinx inlined inside a toctree wrapper."""
    out = []
    for c in sec.children:
        if isinstance(c, Tag) and c.name == "section":
            out.append(c)
        elif is_wrapper(c):
            out += c.find_all("section", recursive=False)
    return out

def build(sec, nid, parent, pnote, src, depth, doc_span=None):
    """Create the note for `sec`; recurse into sub-sections when the note is a chapter or too long to be atomic."""
    h = sec.find(re.compile(r"^h[1-6]$"), recursive=False)
    level = int(h.name[1]) if h else depth
    subs = sub_sections(sec)
    split = bool(subs) and (depth == 2 or len(sec.get_text()) > SPLIT_CHARS)
    if split:
        nodes = [c for c in sec.children if not (isinstance(c, Tag) and (c.name == "section" or is_wrapper(c))) and not is_heading(c)]
    else:
        nodes = [c for c in sec.children if not is_heading(c)]
    note = {"id": nid, "title": heading_text(sec), "kind": "chapter" if split else "leaf", "children": [],
            "parent": parent, "part": pnote, "nodes": nodes, "level": level, "source": src}
    parent["children"].append(note)
    notes.append(note)
    for anchor_id in ([doc_span["id"]] if doc_span is not None else []) + [sec.get("id")]:
        if anchor_id:
            by_anchor.setdefault(anchor_id, []).insert(0, (note, None))
    for n in nodes:
        register_ids(note, n)
    if split:
        for i, child in enumerate(subs):
            # Folgezettel: letters at even depths (chapters 1a, 1a1a…), numbers at odd depths (1a1, 1a1a1…).
            suffix = string.ascii_lowercase[i] if depth % 2 == 1 else str(i + 1)
            prev = child.find_previous_sibling()
            span = prev if isinstance(prev, Tag) and prev.name == "span" and prev.get("id", "").startswith("document-") else None
            build(child, nid + suffix, note, pnote, src, depth + 1, span)

root_note = {"id": "000", "title": "Kinovea Index", "kind": "index", "children": [], "parent": None, "part": None}
notes.append(root_note)

for pi, part in enumerate(parts, 1):
    pid = str(pi)
    src = {API_PART: "kinovea-source-code", LEGACY_PART: "official-manual-legacy"}.get(part["title"], "official-manual")
    pnote = {"id": pid, "title": clean_title(part["title"]), "kind": "part", "children": [], "parent": root_note,
             "part": None, "source": src}
    pnote["part"] = pnote
    root_note["children"].append(pnote)
    notes.append(pnote)
    for ci, anchor in enumerate(part["chapters"]):
        span = main.find(id=anchor)
        build(span.find_next_sibling("section"), pid + string.ascii_lowercase[ci], pnote, pnote, src, 2, span)

for n in notes:
    n["name"] = f'{n["id"]} {n["title"]}'

# Folders: every note with children (part, chapter, sub-structure) gets its own folder; leaves sit in their parent's.
for n in notes:
    if n["kind"] == "index":
        n["folder"] = ""
    elif n["children"]:
        n["folder"] = os.path.join(n["parent"]["folder"], n["name"])
    else:
        n["folder"] = n["parent"]["folder"]

# ---------------------------------------------------------------- html -> markdown
tokens = {}
extra_images = set()
def token(md):
    k = f"ZZTOK{len(tokens):05d}ZZ"
    tokens[k] = md
    return k

def pandoc(html):
    r = subprocess.run(["pandoc", "-f", "html", "-t", "gfm", "--wrap=none"], input=html,
                       capture_output=True, text=True, check=True, cwd=html_dir)
    return r.stdout

def convert(nodes, note, level):
    frag = BeautifulSoup("<div id='frag'></div>", "html.parser")
    box = frag.div
    for n in nodes:
        box.append(BeautifulSoup(str(n), "html.parser"))
    return convert_box(box, note, level)

def convert_box(box, note, level):
    for a in box.select("a.headerlink"):
        a.decompose()
    # Footnotes -> Obsidian/Markdown footnotes ([^n] references, "[^n]: text" definitions at the end).
    for a in box.select("a.footnote-reference"):
        a.replace_with(token(f"[^{a.get_text().strip('[] ')}]"))
    for p in box.select("p.rubric"):
        if p.get_text().strip().lower() in ("footnotes", "references"):
            p.decompose()
    defs = []
    for fn in box.select("aside.footnote"):
        label = fn.select_one("span.label").get_text().strip("[] ")
        fn.select_one("span.label").decompose()
        defs.append((label, fn))
    for fl in box.select("aside.footnote-list"):
        fl.extract()
    if defs:
        box.append(BeautifulSoup("<p>ZZFOOTNOTESZZ</p>", "html.parser"))
    # Code blocks (keep language).
    for div in box.find_all("div", class_=re.compile(r"^highlight-")):
        lang = [c for c in div["class"] if c.startswith("highlight-")][0][10:]
        lang = "" if lang in ("default", "none", "text") else lang
        code = div.find("pre").get_text().rstrip("\n")
        div.replace_with(BeautifulSoup(f"<p>{token(f'```{lang}\n{code}\n```')}</p>", "html.parser"))
    # Admonitions -> Obsidian callouts.
    for adm in box.find_all("div", class_="admonition"):
        if adm.find_parent("div", class_="admonition"):
            continue
        kind = next((c for c in adm["class"] if c in ("note", "tip", "warning", "important", "caution", "danger", "hint")), "note")
        title = adm.find("p", class_="admonition-title")
        if title:
            title.decompose()
        inner = convert_box(adm, note, level).strip()
        body = "\n".join("> " + l if l else ">" for l in inner.splitlines())
        adm.replace_with(BeautifulSoup(f"<p>{token(f'> [!{kind}]\n{body}')}</p>", "html.parser"))
    # Images -> embeds.
    for a in box.select("a.image-reference"):
        a.unwrap()
    for img in box.find_all("img"):
        fn = os.path.basename(img["src"])
        if img["src"].startswith("images/"):  # referenced from the source tree, not copied by Sphinx
            if not os.path.exists(os.path.join(docsrc, img["src"])):
                # Missing from the upstream repo (broken on the official site too): keep the alt text.
                alt = img.get("alt", "").strip()
                img.replace_with(f"[{alt}]" if alt and not alt.startswith("images/") else "")
                continue
            extra_images.add(img["src"])
        img.replace_with(token(f"![[{fn}]]"))
    # Inline UI markup.
    for c in box.find_all("code"):
        c.string = c.get_text()  # flatten Sphinx <span class="pre"> wrappers
    for k in box.find_all("kbd"):
        k.name = "code"
        k.attrs = {}
    for s in box.find_all("span", class_=["menuselection", "guilabel"]):
        s.name = "strong"
        s.attrs = {}
    # Internal links -> wikilinks.
    for a in box.find_all("a", href=True):
        href = a["href"]
        if href.startswith("#"):
            cands = by_anchor.get(href[1:], [])
            text = a.get_text().strip()
            if not cands:
                a.unwrap()
                continue
            chapter = note if note.get("kind") in ("chapter", "part", "index") else note["parent"]
            def chap(t):
                return t if t.get("kind") in ("chapter", "part", "index") else t["parent"]
            tnote, head = next((c for c in cands if c[0] is note), None) or \
                next((c for c in cands if chap(c[0]) is chapter), None) or cands[0]
            if tnote is note and not head:
                a.replace_with(text)
                continue
            dest = tnote["name"] + (f"#{head}" if head else "")
            a.replace_with(token(f"[[{dest}|{text}]]" if text else f"[[{dest}]]"))
    # Footnote/citation decorations.
    for a in box.find_all("a", attrs={"role": "doc-backlink"}):
        a.decompose()
    for sp in box.find_all("span", class_="fn-bracket"):
        sp.unwrap()
    # Drop layout wrappers and attributes so pandoc emits plain Markdown, not raw HTML.
    for t in box.find_all(["div", "span", "section", "aside", "figure", "blockquote"]):
        if t is not box:
            t.unwrap()
    for t in box.find_all(True):
        t.attrs = {k: v for k, v in t.attrs.items() if k in ("href", "src", "alt", "colspan", "rowspan", "id") and not (k == "id" and t is not box)}
    # Re-level headings so the note title is H1.
    for h in box.find_all(re.compile(r"^h[1-6]$")):
        new = max(2, min(6, int(h.name[1]) - level + 1))
        h.name = f"h{new}"
    md = pandoc(str(box))
    if defs:
        fdefs = []
        for label, fn in defs:
            fn.name = "div"
            text = convert_box(fn, note, level).strip().replace("\n\n", " ")
            fdefs.append(f"[^{label}]: {text}")
        md = md.replace("ZZFOOTNOTESZZ", "\n".join(fdefs))
    md = re.sub(r"<div id=\"frag\">\n?|</div>\s*$", "", md).strip()
    md = re.sub(r"^<div[^>]*>\s*$|^</div>\s*$", "", md, flags=re.M)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md

def detokenize(md):
    for _ in range(4):  # tokens can nest (callout containing code)
        md2 = re.sub(r"ZZTOK\d{5}ZZ", lambda m: tokens[m.group(0)], md)
        if md2 == md:
            break
        md = md2
    return md

def summary(md):
    for para in md.split("\n\n"):
        p = para.strip()
        if not p or p.startswith(("!", ">", "|", "```", "#", "<", "-", "*", "1.")):
            continue
        p = re.sub(r"\[\[[^|\]]*\|([^\]]*)\]\]", r"\1", p)
        p = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", p).replace("**", "").replace("`", "")
        s = re.split(r"(?<=[.!?])\s", p)[0]
        return (s[:157] + "…") if len(s) > 160 else s
    return ""

for n in notes:
    if "nodes" in n:
        n["md"] = detokenize(convert(n["nodes"], n, n["level"]))
        n["summary"] = summary(n["md"])

# ---------------------------------------------------------------- write
if os.path.exists(vault):
    shutil.rmtree(vault)
os.makedirs(os.path.join(vault, "_attachments"))
os.makedirs(os.path.join(vault, ".obsidian"))
json.dump({"attachmentFolderPath": "_attachments", "newLinkFormat": "shortest", "useMarkdownLinks": False},
          open(os.path.join(vault, ".obsidian", "app.json"), "w"), indent=2)
for f in os.listdir(os.path.join(html_dir, "_images")):
    shutil.copy(os.path.join(html_dir, "_images", f), os.path.join(vault, "_attachments", f))
for src in extra_images:
    shutil.copy(os.path.join(docsrc, src), os.path.join(vault, "_attachments", os.path.basename(src)))

def link(n):
    return f"[[{n['name']}]]"

def slug(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")

def siblings(n):
    if not n["parent"]:
        return None, None
    sib = n["parent"]["children"]
    i = sib.index(n)
    return (sib[i - 1] if i > 0 else None), (sib[i + 1] if i + 1 < len(sib) else None)

TYPE = {"index": "structure", "part": "structure", "chapter": "structure", "leaf": "permanent"}

def is_stub(md):
    """Empty or outline-only: fewer than 5 words of prose once URLs are removed, and no images."""
    if "![[" in md:
        return False
    prose = re.sub(r"<?https?://\S+", "", md)
    prose = re.sub(r"\[\[[^|\]]*\|([^\]]*)\]\]", r"\1", prose)
    return len(re.findall(r"[A-Za-z0-9]{2,}", prose)) < 5

def write(n, body):
    prev, nxt = siblings(n)
    tags = ["kinovea", f"type/{TYPE[n['kind']]}"]
    if n.get("part"):
        tags.append(f"kinovea/{slug(n['part']['title'])}")
    if n.get("source") == "kinovea-source-code":
        tags.append("source/code-derived")
    callouts = ""
    if n.get("source") == "official-manual-legacy":
        tags.append("status/obsolete")
        callouts += ("> [!warning] Obsolete\n> From the *previous* Kinovea manual. These pages are no longer linked from the official docs "
                     "and may describe older behavior; they are kept because the current manual's tracking chapters are still empty stubs.\n\n")
    if n["kind"] == "leaf" and is_stub(body):
        tags.append("status/stub")
        see = []
        for t in STUB_SEE_ALSO.get(n["title"], []):
            m = next((x for x in notes if x["title"] == t and x is not n and x.get("kind") != "part"), None)
            if m:
                see.append(link(m))
        callouts += (f"> [!warning] Stub\n> This page is empty or only an outline in the official Kinovea manual "
                     f"(kinovea-docs @ `{DOCS_COMMIT}`, a work in progress)."
                     + (f"\n> Related notes: {', '.join(see)}" if see else "") + "\n\n")
    fm = ["---", f'id: "{n["id"]}"', f'title: "{n["title"]}"', f'aliases: ["{n["title"]}"]',
          "tags: [" + ", ".join(tags) + "]"]
    if n["parent"]:
        fm.append(f'up: "{link(n["parent"])}"')
    if n.get("source"):
        fm.append(f"source: {n['source']}")
    fm.append("---")
    navl = []
    if n["parent"]:
        navl.append(f"⬆ {link(n['parent'])}")
    if prev:
        navl.append(f"⬅ {link(prev)}")
    if nxt:
        navl.append(f"➡ {link(nxt)}")
    out = "\n".join(fm) + f"\n\n# {n['title']}\n\n" + callouts + body.strip() + "\n"
    if navl:
        out += "\n---\n" + " · ".join(navl) + "\n"
    path = os.path.join(vault, n["folder"], n["name"] + ".md")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(out)

def child_list(n):
    lines = []
    for c in n["children"]:
        s = c.get("summary", "")
        lines.append(f"- {link(c)}" + (f" — {s}" if s else ""))
    return "\n".join(lines)

for n in notes:
    if n["kind"] == "leaf":
        write(n, n["md"])
    elif n["kind"] == "chapter":
        scope = "chapter" if n["parent"]["kind"] == "part" else "section"
        body = n["md"] + f"\n\n## Notes in this {scope}\n\n" + child_list(n)
        write(n, body)
    elif n["kind"] == "part":
        n["summary"] = ""
        body = f"Structure note for the **{n['title']}** part.\n\n## Chapters\n\n"
        for c in n["children"]:
            body += f"- {link(c)}" + (f" — {c['summary']}" if c.get("summary") else "") + "\n"
            for g in c["children"]:
                body += f"    - {link(g)}\n"
        write(n, body)

intro = main.find("section")
intro_md = detokenize(convert([p for p in intro.find_all("p", recursive=False)], root_note, 1))
count = sum(1 for n in notes if n["kind"] == "leaf")
idx = intro_md + "\n\n## Parts\n\n" + "\n".join(
    f"- {link(p)} — {len(p['children'])} chapters" for p in root_note["children"])
idx += f"\n\n## About this vault\n\nSee [[001 How this vault works]]. {len(notes) - 1} notes, of which {count} are atomic notes.\n"
write(root_note, idx)

n_stub = sum(1 for n in notes if n["kind"] == "leaf" and "md" in n and is_stub(n["md"]))
n_obs = sum(1 for n in notes if n.get("source") == "official-manual-legacy")
guide = f"""---
id: "001"
title: "How this vault works"
tags: [kinovea, type/meta]
---

# How this vault works

This vault is a Zettelkasten built from the Kinovea reference manual (source: github.com/Kinovea/kinovea-docs @ `{commit[:7]}`) plus an API and integration reference compiled from the Kinovea source code (github.com/Kinovea/Kinovea @ `13d0236`).

## Note IDs (Folgezettel)

Every note has an ID that encodes its position in the tree, alternating numbers and letters:

| ID | Level | Example |
|---|---|---|
| `5` | Part (structure note) | [[5 Measurement]] |
| `5c` | Chapter (structure note, or an atomic note if it has no sub-notes) | [[5c Lens distortion calibration]] |
| `5c2` | Atomic note: one topic | a section of that chapter |

IDs never change, so links stay stable. To add your own note *between* or *under* existing ones, branch the ID: a note continuing `5c2` becomes `5c2a`, the next one `5c2b`, and so on.

## Note types (tag `type/…`)

- `type/structure` — the [[000 Kinovea Index]], part notes and chapter notes. They hold the hierarchy and link down to their children with a one-line summary.
- `type/permanent` — atomic notes with the actual content.
- `source/code-derived` — notes from the API part, written from the Kinovea source code rather than the official manual. Where the two disagree, the code is what actually runs.

## Status tags: read these before trusting a note

The official manual is a 2025 rewrite that is still in progress (kinovea-docs @ `{commit[:7]}`, latest commit "wip glossary and other pages"). The vault marks its gaps instead of hiding them:

- `status/stub` — {n_stub} notes that are **empty or outline-only in the official manual**, including 7 of the 8 Tracking chapters. Each carries a warning callout and, where possible, links to related notes that do cover the topic. Search `tag:#status/stub` to list them.
- `status/obsolete` — {n_obs} notes from the **previous** manual's tracking pages ([[15 Legacy documentation (obsolete)]]). No longer linked from the official docs and possibly outdated, but the only written coverage of tracking until the stubs are filled.

Three images referenced by the official manual were never committed to its repository; they appear as their alt text (e.g. `[Record]`).

## Navigation

- Frontmatter `up:` and the footer line give **⬆ parent**, **⬅ previous** and **➡ next** sibling, so you can read a chapter in sequence.
- Cross-references from the manual are converted to `[[wikilinks]]`; open the **Backlinks** pane to see every note that points to the current one.
- Use **Graph view** filtered by `tag:#kinovea/<part>` to see one part's cluster.
- Images live in `_attachments/` and are embedded with `![[…]]`.
"""
open(os.path.join(vault, "001 How this vault works.md"), "w", encoding="utf-8").write(guide)

# Drop attachments no note embeds (e.g. the web landing-page gallery).
embedded = set()
for dirpath, _, files in os.walk(vault):
    for f in files:
        if f.endswith(".md"):
            embedded |= set(re.findall(r"!\[\[([^\]|#]+)", open(os.path.join(dirpath, f), encoding="utf-8").read()))
for f in os.listdir(os.path.join(vault, "_attachments")):
    if f not in embedded:
        os.remove(os.path.join(vault, "_attachments", f))

print(f"parts {len(parts)}  notes {len(notes) + 1}  atomic {count}  images {len(os.listdir(os.path.join(vault, '_attachments')))}")
