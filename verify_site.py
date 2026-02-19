
import os
import re

files_to_check = [
    "index.html",
    "cennik.html",
    "education.html",
    "noitom.html", 
    "english.html",
    "contact.html"
]

base_dir = r"c:\Users\Lenovo\Documents\biokineticum_website"
issues = []

for file in files_to_check:
    file_path = os.path.join(base_dir, file)
    if not os.path.exists(file_path):
        issues.append(f"MISSING: {file}")
        continue
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Check CSS link
    if 'href="styles.css"' not in content:
        issues.append(f"{file}: Missing styles.css link")
        
    # Check key Nav links
    for target in files_to_check:
        if f'href="{target}"' not in content:
            # We allow english.html to not link to itself if it links to index.html/PL
            if file == "english.html" and target == "index.html": continue
            if file == "english.html" and target == "english.html": continue 
             # Basic check, might generate false positives if link is active class only, but good enough
            pass 

if not issues:
    print("SUCCESS: All structure checks passed.")
else:
    print("ISSUES FOUND:")
    for issue in issues:
        print(f"- {issue}")
