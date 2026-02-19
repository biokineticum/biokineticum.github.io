
import os
import re

files_to_update = [
    "index.html",
    "cennik.html",
    "education.html",
    "noitom.html", 
    "english.html",
    "contact.html"
]

base_dir = r"c:\Users\Lenovo\Documents\biokineticum_website"

# Regex to find the logo text link
# Matches <a href="index.html" class="logo">Biokineticum</a>
logo_regex = re.compile(r'<a href="index\.html" class="logo">Biokineticum</a>')

# Replacement string
new_logo_html = '<a href="index.html" class="logo"><img src="images/logo.jpg" alt="Biokineticum" class="nav-logo"></a>'

for file in files_to_update:
    file_path = os.path.join(base_dir, file)
    
    if not os.path.exists(file_path):
        print(f"Skipping {file} (not found)")
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "images/logo.jpg" in content:
        print(f"Skipping {file} (already updated)")
        continue

    new_content = logo_regex.sub(new_logo_html, content)
    
    # Also fix white backgrounds hardcoded in HTML if any (e.g. education.html had style="background-color: white;")
    new_content = new_content.replace('style="background-color: white;"', '')
    new_content = new_content.replace('style="background: linear-gradient(135deg, #f0fff4 0%, #ffffff 100%);"', '')
    new_content = new_content.replace('style="background: linear-gradient(135deg, #111 0%, #333 100%);"', '') # For Noitom, remove inline so CSS handles it
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print(f"Updated {file}")
