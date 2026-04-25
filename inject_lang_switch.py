import os
import re

file_pairs = {
    "index.html": "index-en.html",
    "about.html": "about-en.html",
    "cennik.html": "pricing-en.html",
    "education.html": "education-en.html",
    "noitom.html": "noitom-en.html",
    "publikacje.html": "publications-en.html",
    "portfolio.html": "portfolio-en.html",
    "contact.html": "contact-en.html",
}

# Add all articles dynamically
html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for f in html_files:
    if f.startswith('artykul-'):
        en_version = f.replace('artykul-', 'article-').replace('.html', '-en.html')
        file_pairs[f] = en_version

def update_file(filename, is_pl):
    if not os.path.exists(filename):
        return

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine PL and EN files
    if is_pl:
        pl_file = filename
        en_file = file_pairs.get(filename, "english.html")
    else:
        en_file = filename
        pl_file = next((pl for pl, en in file_pairs.items() if en == filename), "index.html")

    # Generate the switcher HTML
    if is_pl:
        switcher = f'<div class="lang-switch" style="display: inline-flex; gap: 0.5rem; align-items: center; font-weight: bold; margin-left: auto;"><strong>PL</strong> <span style="color: var(--text-muted);">|</span> <a href="{en_file}" style="color: var(--text-muted); text-decoration: none;">EN</a></div>'
    else:
        switcher = f'<div class="lang-switch" style="display: inline-flex; gap: 0.5rem; align-items: center; font-weight: bold; margin-left: auto;"><a href="{pl_file}" style="color: var(--text-muted); text-decoration: none;">PL</a> <span style="color: var(--text-muted);">|</span> <strong>EN</strong></div>'

    # If it already has a lang-switch, skip
    if 'class="lang-switch"' in content:
        print(f"Skipping {filename}, already has lang-switch.")
        return

    # Insert it before the contact button
    # PL contact button regex
    content = re.sub(
        r'(<a\s+href="contact\.html"\s+class="btn\s+btn-primary"[^>]*>Kontakt</a>)',
        f'{switcher}\n                    \\1',
        content
    )
    # EN contact button regex
    content = re.sub(
        r'(<a\s+href="contact-en\.html"\s+class="btn\s+btn-primary"[^>]*>Contact</a>)',
        f'{switcher}\n                    \\1',
        content
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Injected switcher into {filename}")

for f in html_files:
    is_pl = f in file_pairs or f.startswith('artykul-')
    update_file(f, is_pl)

print("Language switch injection complete.")
