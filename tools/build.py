import sys, datetime
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
html_path, out_pdf, commit = sys.argv[1], sys.argv[2], sys.argv[3]
soup = BeautifulSoup(open(html_path, encoding="utf-8"), "html.parser")

# Map chapter anchor -> part caption from the sidebar nav
nav = soup.select_one(".wy-menu-vertical")
parts = []  # (caption, [(href, title, [(href,title)])])
cur = None
for el in nav.children:
    if getattr(el, "name", None) == "p" and "caption" in el.get("class", []):
        cur = (el.get_text(strip=True), []); parts.append(cur)
    elif getattr(el, "name", None) == "ul" and cur:
        for li in el.find_all("li", recursive=False):
            a = li.find("a")
            cur[1].append((a["href"], a.get_text(strip=True)))
first_of_part = {href.split("#")[-1]: cap for cap, chs in parts for href, _ in chs[:1]}

main = soup.select_one('div[itemprop="articleBody"]') or soup.select_one(".document")
# Drop web-only landing bits: title, image gallery, offline-download tip, "search top left" text
for el in main.select(".tocdescr, .admonition.tip"): el.decompose()
main.find("h1").decompose()
for para in main.find_all("p"):
    if "table of content on the left" in para.get_text(): para.decompose()
# Insert part dividers before the first chapter of each part
for anchor, cap in first_of_part.items():
    target = main.find(id=anchor)
    d = soup.new_tag("h1", attrs={"class": "part-divider"})
    d.string = cap
    target.insert_before(d)

# Cover + TOC
front = BeautifulSoup(f"""
<div class="cover">
  <h1 class="cover-title">Kinovea Reference Manual</h1>
  <div class="cover-sub">Video annotation &amp; motion analysis</div>
  <div class="cover-meta">Compiled from the official documentation source<br>
  github.com/Kinovea/kinovea-docs @ {commit[:10]}<br>
  (published at kinovea.readthedocs.io) &middot; License CC0 1.0<br>
  Built {datetime.date.today().isoformat()}</div>
</div>
<div class="toc"><h1 class="toc-h">Contents</h1>
{''.join(f'<div class="toc-part">{cap}</div>' + ''.join(f'<div class="toc-ch"><a href="{h}">{t}</a></div>' for h,t in chs) for cap, chs in parts)}
</div>""", "html.parser")
main.insert(0, front)

style = soup.new_tag("style")
style.string = """
@page { size: A4; margin: 16mm 15mm 18mm 15mm; }
.wy-nav-side,.wy-nav-top,.rst-versions,.wy-breadcrumbs,footer,.rst-footer-buttons,.headerlink,[role=navigation]{display:none!important}
.wy-nav-content-wrap{margin-left:0!important;background:#fff!important}
.wy-nav-content{max-width:none!important;padding:0!important}
html,body{background:#fff!important}
.wy-table-responsive{overflow:visible!important}
.wy-table-responsive table td,.wy-table-responsive table th,.rst-content table.docutils td,.rst-content table.docutils th{white-space:normal!important;word-break:break-word}
.rst-content table.docutils{width:100%!important;table-layout:fixed}
.rst-content table.docutils code{white-space:normal;word-break:break-all;font-size:85%}
.rst-content pre,.highlight pre{white-space:pre-wrap!important;word-break:break-all;overflow:visible!important;font-size:10px}
.rst-content img{max-width:100%!important;height:auto}
.rst-content h1.cover-title{font-size:52px;font-weight:700;color:#2c3e50;margin:0}
.rst-content h2{break-before:page;font-size:24px;border-bottom:2px solid #2980b9;padding-bottom:4px}
h2,h3,h4{break-after:avoid}
figure,img,pre,.admonition,tr{break-inside:avoid}
.cover{padding-top:85mm;text-align:center;break-after:page}

.cover-sub{font-size:28px;color:#2980b9;margin:10px 0 60px}
.cover-meta{font-size:13px;color:#666;line-height:1.8}
.toc{break-after:page}.toc-h{display:block!important;font-size:28px}
.toc-part{font-weight:700;margin:12px 0 2px;color:#2c3e50;text-transform:uppercase;font-size:12px;letter-spacing:.05em}
.toc-ch{margin-left:16px;font-size:13px;line-height:1.5}.toc-ch a{text-decoration:none}
.rst-content h1.part-divider{break-before:page;break-after:page;padding-top:100mm;text-align:center;font-size:44px;font-weight:700;color:#2980b9}
.part-divider + span + section > h2{break-before:avoid}
"""
soup.head.append(style)
out_html = html_path.replace("index.html", "book.html")
open(out_html, "w", encoding="utf-8").write(str(soup))

with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
    pg = b.new_page()
    pg.goto("file://" + out_html, wait_until="networkidle")
    pg.emulate_media(media="print")
    pg.pdf(path=out_pdf, format="A4", print_background=True, outline=True, tagged=True,
           display_header_footer=True, header_template="<span></span>",
           footer_template='<div style="font-size:8px;width:100%;text-align:center;color:#888">Kinovea Reference Manual &middot; <span class="pageNumber"></span> / <span class="totalPages"></span></div>',
           margin={"top":"16mm","bottom":"18mm","left":"15mm","right":"15mm"})
    b.close()
print("parts", len(parts), "chapters", sum(len(c) for _,c in parts))
