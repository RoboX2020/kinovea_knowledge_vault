# Kinovea knowledge vault

The [Kinovea](https://www.kinovea.org) documentation (video annotation and motion analysis software) in two forms:

- **`vault/`** — an [Obsidian](https://obsidian.md) vault: 380 notes in a Zettelkasten structure. Open the `vault` folder with *Open folder as vault* and start at `000 Kinovea Index`.
- **`Kinovea_Reference_Manual.pdf`** — the same material as a 249-page PDF, with bookmarks and a clickable table of contents.

## What's inside

| Part | Source |
|---|---|
| 1–13: User interface → Miscellaneous | The official manual, [Kinovea/kinovea-docs](https://github.com/Kinovea/kinovea-docs) @ `375e293` (published at kinovea.readthedocs.io) |
| 14: API and integration reference | **Not in the official manual.** Compiled from the Kinovea source code, [Kinovea/Kinovea](https://github.com/Kinovea/Kinovea) @ `13d0236`: the full remote-control command list (`WM_COPYDATA`), the UDP trigger, the complete command line, KVA format 2.1, and the custom posture-tool XML format |
| 15: Legacy (vault only) | The previous manual's tracking pages. Obsolete, but the only written coverage of tracking for now |

## Known gaps

The official manual is a 2025 rewrite that is still in progress. **23 pages or sections are empty or outline-only upstream**, including 7 of the 8 Tracking chapters. In the vault they're tagged `status/stub` and carry a warning callout; legacy notes are tagged `status/obsolete`. Search `tag:#status/stub` in Obsidian to list them.

## Vault structure

- **Folgezettel IDs** encode the hierarchy, alternating numbers and letters: `5` (part) → `5b` (chapter) → `5b1` (atomic note) → `5b1a`. Folders mirror the same tree.
- **Atomic notes** (`type/permanent`) cover one topic each. **Structure notes** (`type/structure`) list their children with one-line summaries.
- Every note has `up:` frontmatter and ⬆ / ⬅ / ➡ navigation links. Cross-references are `[[wikilinks]]`, footnotes are native, and images are embedded from `vault/_attachments/`.

## Rebuilding

`tools/` holds the pipeline. Build the official docs with Sphinx (`singlehtml`), with the chapters in `api-docs-src/` added under `source/api/` (see `index.rst.patched` for the toctree entries). Then:

```bash
python tools/build.py   <singlehtml>/index.html Kinovea_Reference_Manual.pdf <docs-commit>   # PDF (Playwright + Chromium)
python tools/to_vault.py <singlehtml> vault <docs-commit> <sphinx-source-dir>                # Obsidian vault (needs pandoc)
python tools/gen_commands.py <Kinovea source checkout>                                       # remote-control command tables
```

## Licensing

The official documentation content is CC0 1.0 (per kinovea-docs). Part 14 describes the behavior of Kinovea, which is GPL-2.0 software; it contains documentation and short illustrative examples, not Kinovea source code.
