#!/usr/bin/env python3
"""Generate a single valid sitemap.xml for biokineticum.com (root + blog)."""
from __future__ import annotations

import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://biokineticum.com"
TODAY = datetime.date.today().isoformat()

EXCLUDE_SUBSTRINGS = ("backup",)
EXCLUDE_NAMES = {"english.html"}
EXCLUDE_SUFFIXES = (".htm",)

CORE = {
    "index.html",
    "index-pl.html",
    "about.html",
    "about-en.html",
    "contact.html",
    "contact-en.html",
    "education.html",
    "education-en.html",
    "noitom.html",
    "noitom-en.html",
    "portfolio.html",
    "portfolio-en.html",
    "cennik.html",
    "pricing-en.html",
    "publikacje.html",
    "publications-en.html",
    "telerehabilitacja.html",
    "telerehabilitation-en.html",
}


def should_exclude(path: Path) -> bool:
    name = path.name
    if name in EXCLUDE_NAMES:
        return True
    if any(s in name for s in EXCLUDE_SUBSTRINGS):
        return True
    if name.endswith(EXCLUDE_SUFFIXES):
        return True
    return False


def lastmod_for(path: Path) -> str:
    if path.name in CORE or path.name.startswith("article-") or path.name.startswith("artykul-"):
        return TODAY
    try:
        return datetime.date.fromtimestamp(path.stat().st_mtime).isoformat()
    except OSError:
        return TODAY


def loc_for(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return f"{SITE}/"
    if rel == "blog/index.html":
        return f"{SITE}/blog/"
    return f"{SITE}/{rel}"


def priority_for(path: Path) -> str:
    name = path.name
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.html" or name == "index-pl.html":
        return "1.0"
    if "telerehabilit" in name:
        return "0.9"
    if name in CORE:
        return "0.8"
    if rel.startswith("blog/"):
        if name in ("index.html", "index-pl.html"):
            return "0.8"
        return "0.6"
    if name.startswith("article-") or name.startswith("artykul-"):
        return "0.6"
    return "0.5"


def changefreq_for(path: Path) -> str:
    if path.name in CORE or path.name in ("index.html", "index-pl.html"):
        return "weekly"
    return "monthly"


def collect_urls():
    urls = []
    seen = set()

    root_html = sorted(ROOT.glob("*.html"))
    blog_dir = ROOT / "blog"
    blog_html = sorted(blog_dir.glob("*.html")) if blog_dir.is_dir() else []

    home = f"{SITE}/"
    urls.append((home, TODAY, "weekly", "1.0"))
    seen.add(home)

    for path in root_html + blog_html:
        if should_exclude(path):
            continue
        loc = loc_for(path)
        if loc in seen:
            continue
        if path.name == "index.html" and path.parent == ROOT:
            continue
        seen.add(loc)
        urls.append((loc, lastmod_for(path), changefreq_for(path), priority_for(path)))

    return urls


def main():
    urls = collect_urls()
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for loc, lastmod, cf, pr in urls:
        lines.append("   <url>")
        lines.append(f"      <loc>{loc}</loc>")
        lines.append(f"      <lastmod>{lastmod}</lastmod>")
        lines.append(f"      <changefreq>{cf}</changefreq>")
        lines.append(f"      <priority>{pr}</priority>")
        lines.append("   </url>")
    lines.append("</urlset>")
    lines.append("")
    out = ROOT / "sitemap.xml"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Sitemap generated with {len(urls)} URLs -> {out}")


if __name__ == "__main__":
    main()
