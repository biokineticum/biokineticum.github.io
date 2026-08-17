import os
import re
import json

ignore_files = {
    'english_backup_20260219.html', 'cennik_backup_20260219.html',
    'education_backup_20260219.html', 'index_backup_20260219.html',
    'noitom_backup_20260219.html', 'contact_backup_20260219.html',
    'english.html'
}

html_files = [f for f in sorted(os.listdir('.')) if f.endswith('.html') and f not in ignore_files]

print(f"Auditing {len(html_files)} production HTML files...\n")

audit_results = []

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    file_report = {
        'file': filename,
        'title': None,
        'title_len': 0,
        'description': None,
        'desc_len': 0,
        'h1': [],
        'canonical': None,
        'hreflang_pl': None,
        'hreflang_en': None,
        'json_ld': [],
        'images_without_alt': [],
        'og_tags': {},
        'issues': []
    }
    
    # Title
    title_m = re.search(r'<title>(.*?)</title>', content, re.DOTALL | re.IGNORECASE)
    if title_m:
        file_report['title'] = title_m.group(1).strip()
        file_report['title_len'] = len(file_report['title'])
        if file_report['title_len'] < 30 or file_report['title_len'] > 70:
            file_report['issues'].append(f"Title length ({file_report['title_len']} chars) outside recommended 30-70 range")
    else:
        file_report['issues'].append("Missing <title> tag")
        
    # Meta Description
    desc_m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE | re.DOTALL)
    if not desc_m:
        desc_m = re.search(r'<meta\s+content=["\'](.*?)["\']\s+name=["\']description["\']', content, re.IGNORECASE | re.DOTALL)
    if desc_m:
        file_report['description'] = desc_m.group(1).strip()
        file_report['desc_len'] = len(file_report['description'])
        if file_report['desc_len'] < 70 or file_report['desc_len'] > 165:
            file_report['issues'].append(f"Meta description length ({file_report['desc_len']} chars) outside 70-165 range")
    else:
        file_report['issues'].append("Missing meta description")
        
    # H1
    h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
    clean_h1s = [re.sub(r'<[^>]+>', '', h).strip() for h in h1s]
    file_report['h1'] = clean_h1s
    if len(clean_h1s) == 0:
        file_report['issues'].append("Missing <h1> tag")
    elif len(clean_h1s) > 1:
        file_report['issues'].append(f"Multiple ({len(clean_h1s)}) <h1> tags found")
        
    # Canonical
    canon_m = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', content, re.IGNORECASE)
    if canon_m:
        file_report['canonical'] = canon_m.group(1).strip()
    else:
        file_report['issues'].append("Missing canonical link")
        
    # Hreflang
    hr_pl = re.search(r'<link\s+rel=["\']alternate["\']\s+hreflang=["\']pl["\']\s+href=["\'](.*?)["\']', content, re.IGNORECASE)
    if hr_pl:
        file_report['hreflang_pl'] = hr_pl.group(1).strip()
    hr_en = re.search(r'<link\s+rel=["\']alternate["\']\s+hreflang=["\']en["\']\s+href=["\'](.*?)["\']', content, re.IGNORECASE)
    if hr_en:
        file_report['hreflang_en'] = hr_en.group(1).strip()
        
    if not hr_pl or not hr_en:
        file_report['issues'].append("Missing hreflang tags (PL/EN)")
        
    # JSON-LD Schema
    schemas = re.findall(r'<script\s+type=["\']application/ld\+json["\']\s*>(.*?)</script>', content, re.DOTALL | re.IGNORECASE)
    for s in schemas:
        try:
            parsed = json.loads(s.strip())
            file_report['json_ld'].append(parsed)
        except Exception as e:
            file_report['issues'].append(f"Invalid JSON-LD syntax: {e}")
            
    # Images without alt
    img_tags = re.findall(r'<img\s+[^>]*>', content, re.IGNORECASE)
    for img in img_tags:
        if 'alt=' not in img or re.search(r'alt=["\']\s*["\']', img):
            file_report['images_without_alt'].append(img)
    if file_report['images_without_alt']:
        file_report['issues'].append(f"{len(file_report['images_without_alt'])} images missing non-empty alt attribute")
        
    audit_results.append(file_report)

# Print Summary
print("=== SEO AUDIT SUMMARY ===")
files_with_issues = [r for r in audit_results if r['issues']]
print(f"Total production files: {len(audit_results)}")
print(f"Files with potential warnings/issues: {len(files_with_issues)}\n")

for r in audit_results:
    status = "⚠️ WARNINGS" if r['issues'] else "✅ PASSED"
    print(f"[{status}] {r['file']}")
    print(f"   Title ({r['title_len']} chars): {r['title']}")
    print(f"   H1: {r['h1']}")
    print(f"   Canonical: {r['canonical']}")
    print(f"   Schema Types: {[item.get('@type') if isinstance(item, dict) else [x.get('@type') for x in item] for item in r['json_ld']]}")
    if r['issues']:
        for iss in r['issues']:
            print(f"   - {iss}")
    print()
