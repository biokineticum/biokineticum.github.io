import re

for filename in ['publikacje.html', 'publications-en.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match the div containing the PL | EN toggle in the hero
    content = re.sub(
        r'<div style="text-align: right; font-size: 1\.1rem; margin-bottom: 1rem;">.*?</div>\s*',
        '',
        content,
        flags=re.DOTALL
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Removed duplicate language toggle from hero sections.")
