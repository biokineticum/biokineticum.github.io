import os
import glob
import re

html_files = glob.glob('*.html')

color_replacements = {
    r'color:\s*#0f172a': 'color: var(--text-light)',
    r'color:\s*#1e3a8a': 'color: var(--primary-light)',
    r'color:\s*#475569': 'color: var(--text-main)',
    r'color:\s*#334155': 'color: var(--text-main)',
    r'color:\s*#111(?![0-9a-fA-F])': 'color: var(--text-light)',
    r'background-color:\s*#f8fafc': 'background-color: var(--bg-surface)',
    r'background-color:\s*#f1f5f9': 'background-color: var(--bg-surface)',
    r'background-color:\s*#1e3a8a': 'background-color: var(--primary)',
    r'background:\s*#1e3a8a': 'background: var(--primary)',
    r'border-bottom:\s*1px solid #e2e8f0': 'border-bottom: 1px solid var(--border-color)',
    r'border-top:\s*2px solid #e2e8f0': 'border-top: 2px solid var(--border-color)',
    r'border:\s*1px solid #e2e8f0': 'border: 1px solid var(--border-color)',
}

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    for pattern, replacement in color_replacements.items():
        content = re.sub(pattern, replacement, content)
        
    # specific fix for .trust-btn in about.html
    content = content.replace('background-color: white;', 'background-color: var(--bg-body);')
    content = content.replace('background-color: #f8fafc;', 'background-color: var(--bg-surface);')
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

for f in html_files:
    if 'backup' in f: continue
    process_file(f)

# Update styles.css to ensure pure black/high contrast dark theme
with open('styles.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

css_content = re.sub(r'--bg-body:\s*#[0-9a-fA-F]+;', '--bg-body: #050505;', css_content)
css_content = re.sub(r'--bg-surface:\s*#[0-9a-fA-F]+;', '--bg-surface: #111111;', css_content)
css_content = re.sub(r'--primary:\s*#[0-9a-fA-F]+;', '--primary: #3b82f6;', css_content)
css_content = re.sub(r'--primary-light:\s*#[0-9a-fA-F]+;', '--primary-light: #60a5fa;', css_content)
css_content = re.sub(r'--text-main:\s*#[0-9a-fA-F]+;', '--text-main: #f3f4f6;', css_content)
css_content = re.sub(r'--text-muted:\s*#[0-9a-fA-F]+;', '--text-muted: #9ca3af;', css_content)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css_content)
print("Updated styles.css")

print("Done.")
