import os
import re
import shutil

file_pairs = {
    "index.html": "index-en.html",
    "about.html": "about-en.html",
    "cennik.html": "pricing-en.html",
    "education.html": "education-en.html",
    "noitom.html": "noitom-en.html",
    "portfolio.html": "portfolio-en.html",
    "contact.html": "contact-en.html",
}

for pl_file, en_file in file_pairs.items():
    if not os.path.exists(pl_file):
        continue
    
    # Create the copy
    shutil.copy2(pl_file, en_file)
    
    with open(en_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Update lang="pl" to lang="en"
    content = content.replace('<html lang="pl">', '<html lang="en">')
    
    # Update hreflang
    content = re.sub(
        r'<link rel="alternate" hreflang="en" href="[^"]+" />',
        f'<link rel="alternate" hreflang="en" href="https://biokineticum.com/{en_file}" />',
        content
    )
    content = re.sub(
        r'<link rel="alternate" hreflang="pl" href="[^"]+" />',
        f'<link rel="alternate" hreflang="pl" href="https://biokineticum.com/{pl_file}" />',
        content
    )
    
    # Translate the menu links
    content = content.replace('>Główna</a>', '>Home</a>')
    content = content.replace('>O mnie</a>', '>About Me</a>')
    content = content.replace('"cennik.html">Cennik</a>', '"pricing-en.html">Pricing</a>')
    content = content.replace('"education.html">Education</a>', '"education-en.html">Education</a>')
    content = content.replace('"education.html" class="active">Education Software</a>', '"education-en.html" class="active">Education Software</a>')
    content = content.replace('"noitom.html">Noitom Polska</a>', '"noitom-en.html">Noitom Polska</a>')
    content = content.replace('"publikacje.html">Publikacje</a>', '"publications-en.html">Publications</a>')
    content = content.replace('"publikacje.html" class="active">Publikacje</a>', '"publications-en.html" class="active">Publications</a>')
    content = content.replace('"portfolio.html">Portfolio</a>', '"portfolio-en.html">Portfolio</a>')
    content = content.replace('"contact.html" class="btn btn-primary">Kontakt</a>', '"contact-en.html" class="btn btn-primary">Contact</a>')
    
    # Update hrefs to point to English versions
    content = content.replace('"index.html"', '"index-en.html"')
    content = content.replace('"about.html"', '"about-en.html"')
    content = content.replace('"cennik.html"', '"pricing-en.html"')
    content = content.replace('"education.html"', '"education-en.html"')
    content = content.replace('"noitom.html"', '"noitom-en.html"')
    content = content.replace('"portfolio.html"', '"portfolio-en.html"')
    content = content.replace('"contact.html"', '"contact-en.html"')
    content = content.replace('"publikacje.html"', '"publications-en.html"')
    
    with open(en_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created {en_file}")
