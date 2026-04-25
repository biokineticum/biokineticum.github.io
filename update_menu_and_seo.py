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
        print(f"Skipping {filename}, does not exist.")
        return

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove "English" from navigation links
    content = re.sub(r'<a\s+href="english\.html"[^>]*>English</a>\s*', '', content)

    # 2. Update hreflang tags if it's a known pair
    if is_pl and filename in file_pairs:
        en_file = file_pairs[filename]
        # Replace the old english.html hreflang with the specific en_file
        content = re.sub(
            r'<link rel="alternate" hreflang="en" href="https://biokineticum.com/english.html"\s*/>',
            f'<link rel="alternate" hreflang="en" href="https://biokineticum.com/{en_file}" />',
            content
        )
    elif not is_pl:
        # Find the PL pair
        pl_file = None
        for pl, en in file_pairs.items():
            if en == filename:
                pl_file = pl
                break
        
        if pl_file:
            # Note: English files probably already point to their PL equivalents if they were translated
            pass

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

for f in html_files:
    is_pl = f in file_pairs or f.startswith('artykul-')
    update_file(f, is_pl)

print("Menu update complete.")
