
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

# New Social Media HTML block
new_socials_html = """<h4>Social Media</h4>
                    <ul>
                        <li><a href="https://www.youtube.com/@Biokineticum" target="_blank">YouTube</a></li>
                        <li><a href="https://www.instagram.com/biokineticum/" target="_blank">Instagram</a></li>
                        <li><a href="https://www.tiktok.com/@biokineticum" target="_blank">TikTok</a></li>
                        <li><a href="https://www.linkedin.com/in/dariusz-mosler-b3856768/?locale=pl" target="_blank">LinkedIn</a></li>
                    </ul>"""

# Regex to find the existing Social Media block
# It looks for <h4>Social Media</h4> and the following <ul>...</ul> block
# We use DOTALL to match across lines
socials_regex = re.compile(r'<h4>Social Media</h4>\s*<ul>.*?</ul>', re.DOTALL)

for file in files_to_update:
    file_path = os.path.join(base_dir, file)
    
    if not os.path.exists(file_path):
        print(f"Skipping {file} (not found)")
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "youtube.com/@Biokineticum" in content:
        print(f"Skipping {file} (already updated)")
        continue

    # Perform substitution
    new_content = socials_regex.sub(new_socials_html, content)
    
    if content == new_content:
        print(f"Warning: No replacement made in {file}. Regex might not match.")
    else:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {file}")
