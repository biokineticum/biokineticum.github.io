import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and not f.startswith('english_backup') and not f.startswith('cennik_backup') and not f.startswith('education_backup') and not f.startswith('index_backup') and not f.startswith('noitom_backup') and not f.startswith('contact_backup')]

def check_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    issues = []

    # Title
    if '<title>' not in content or '</title>' not in content:
        issues.append("Missing <title> tag")

    # Meta description
    if 'name="description"' not in content:
        issues.append("Missing meta description")

    # Canonical
    if '<link rel="canonical"' not in content:
        issues.append("Missing canonical link")

    # Hreflang PL
    if '<link rel="alternate" hreflang="pl"' not in content:
        issues.append("Missing hreflang PL")

    # Hreflang EN
    if '<link rel="alternate" hreflang="en"' not in content:
        issues.append("Missing hreflang EN")

    # Schema
    if 'application/ld+json' not in content:
        issues.append("Missing Schema.org JSON-LD")

    # Google Tag
    if 'www.googletagmanager.com/gtag/js' not in content:
        issues.append("Missing Google Tag Manager script")

    # AdSense Head
    if 'pagead2.googlesyndication.com/pagead/js/adsbygoogle.js' not in content:
        issues.append("Missing AdSense script")
        
    # AdSense Block (some pages might not have the display block if they are short, but let's check)
    if '<ins class="adsbygoogle"' not in content:
        issues.append("Missing AdSense <ins> display block")

    return issues

results = {}
for f in html_files:
    results[f] = check_file(f)

for f, issues in results.items():
    if issues:
        print(f"{f} HAS ISSUES:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print(f"{f} is PERFECT")

