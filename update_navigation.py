import os
import glob
import re

def replacer(match):
    val = match.group(1)
    if val == "index.html":
        return 'href="index-pl.html"'
    elif val == "index-en.html":
        return 'href="index.html"'
    return match.group(0)

def main():
    directory = r'c:\Users\Lenovo\Documents\biokineticum.github.io'
    html_files = glob.glob(os.path.join(directory, '*.html'))

    for filepath in html_files:
        filename = os.path.basename(filepath)
        if 'backup' in filename:
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        is_en = filename.endswith('-en.html') or filename == 'index.html'

        # Fix absolute canonicals and og:url first
        content = content.replace('https://biokineticum.com/index.html', 'https://biokineticum.com/INDEX_PL_TEMP')
        content = content.replace('https://biokineticum.com/index-en.html', 'https://biokineticum.com/INDEX_EN_TEMP')
        
        content = content.replace('INDEX_PL_TEMP', 'index-pl.html')
        content = content.replace('INDEX_EN_TEMP', 'index.html')
        
        # Fix canonical URL based on language
        if is_en:
            content = content.replace('rel="canonical" href="https://biokineticum.com/index-pl.html"', 'rel="canonical" href="https://biokineticum.com/index.html"')

        # Fix local hrefs
        content = re.sub(r'href="(index\.html|index-en\.html)"', replacer, content)

        # Insert new nav item
        if is_en:
            if 'telerehabilitation-en.html' not in content:
                # Menu
                content = re.sub(r'(<a href="index\.html"(?: class="active")?>Home</a>)', r'\1\n                    <a href="telerehabilitation-en.html">Telerehabilitation</a>', content)
                # Footer
                content = re.sub(r'(<li><a href="index\.html">Home</a></li>)', r'\1\n                        <li><a href="telerehabilitation-en.html">Telerehabilitation</a></li>', content)
        else:
            if 'telerehabilitacja.html' not in content:
                # Menu
                content = re.sub(r'(<a href="index-pl\.html"(?: class="active")?>Główna</a>)', r'\1\n                    <a href="telerehabilitacja.html">Telerehabilitacja</a>', content)
                # Footer
                content = re.sub(r'(<li><a href="index-pl\.html">Główna</a></li>)', r'\1\n                        <li><a href="telerehabilitacja.html">Telerehabilitacja</a></li>', content)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    print("Done updating navigation.")

if __name__ == '__main__':
    main()
