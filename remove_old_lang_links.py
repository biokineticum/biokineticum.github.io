import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in html_files:
    if filename.startswith('artykul-') or filename.startswith('article-'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove the [ Read in English ] div
        content = re.sub(
            r'<div style="text-align: right; margin-bottom: 0\.5rem;"><a href="[^"]+" style="color: var\(--accent-light\); font-weight: bold; text-decoration: none;">\[ Read in English \]</a></div>\s*',
            '',
            content
        )
        # Remove the [ Czytaj po polsku ] div
        content = re.sub(
            r'<div style="text-align: right; margin-bottom: 0\.5rem;"><a href="[^"]+" style="color: var\(--accent-light\); font-weight: bold; text-decoration: none;">\[ Czytaj po polsku \]</a></div>\s*',
            '',
            content
        )
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

print("Old language links removed from articles.")
