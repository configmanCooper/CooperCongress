"""Check generated static pages and local references."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PAGES = sorted(ROOT.glob("*.html"))


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1 = 0
        self.title = 0
        self.description = 0
        self.main = 0
        self.links = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "h1":
            self.h1 += 1
        if tag == "title":
            self.title += 1
        if tag == "main":
            self.main += 1
        if tag == "meta" and attributes.get("name") == "description":
            self.description += 1
        for key in ("href", "src"):
            if key in attributes:
                self.links.append(attributes[key])


errors = []
for page in PAGES:
    parser = PageParser()
    parser.feed(page.read_text(encoding="utf-8"))
    for key in ("h1", "title", "description", "main"):
        if getattr(parser, key) != 1:
            errors.append(f"{page.name}: expected one {key}, got {getattr(parser, key)}")
    for url in parser.links:
        parts = urlsplit(url)
        if parts.scheme or parts.netloc or url.startswith("#"):
            continue
        target = (page.parent / unquote(parts.path)).resolve()
        if not target.is_file():
            errors.append(f"{page.name}: missing target {url}")
        elif parts.fragment and target.suffix == ".html":
            html = target.read_text(encoding="utf-8")
            if f'id="{parts.fragment}"' not in html:
                errors.append(f"{page.name}: missing anchor {url}")

if not PAGES:
    errors.append("No HTML pages found")
if not (ROOT / ".nojekyll").exists():
    errors.append(".nojekyll is missing")

if errors:
    raise SystemExit("\n".join(errors))
print(f"Checked {len(PAGES)} pages and all local links.")
