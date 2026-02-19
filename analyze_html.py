
import re

file_path = r"c:\Users\Lenovo\Documents\biokineticum_website\Biomechanics analysis software online physiotherapy.htm"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
except UnicodeDecodeError:
    with open(file_path, "r", encoding="latin-1") as f:
        content = f.read()

keywords = [
    "Fizjoterapia",
    "Analiza ruchu", 
    "Testy motoryczne",
    "Kontakt",
    "Dr Dariusz Mosler",
    "Cennik",
    "Oprogramowanie", 
    "Noitom"
]

print(f"File length: {len(content)}")

for keyword in keywords:
    print(f"\n--- Searching for: {keyword} ---")
    matches = [m.start() for m in re.finditer(re.escape(keyword), content)]
    print(f"Found {len(matches)} matches.")
    
    for i, match_idx in enumerate(matches[:3]): # Show first 3 matches
        start = max(0, match_idx - 500)
        end = min(len(content), match_idx + 500)
        print(f"Match {i+1} Context:")
        print(content[start:end])
        print("-" * 50)

print("\n--- Image Links ---")
# Find img tags with src
img_matches = re.finditer(r'<img[^>]+src="([^"]+)"', content)
shown_imgs = 0
for m in img_matches:
    if shown_imgs < 10:
        print(m.group(0))
        shown_imgs += 1

print("\n--- Navigation Links ---")
# Find common nav links
nav_matches = re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', content)
shown_links = 0
for m in nav_matches:
    link_text = m.group(2)
    link_href = m.group(1)
    if len(link_text) < 50 and "http" not in link_text and shown_links < 20:
         print(f"Link: {link_text} -> {link_href}")
         shown_links += 1
