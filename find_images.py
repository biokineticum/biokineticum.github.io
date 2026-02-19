
import re

file_path = r"c:\Users\Lenovo\Documents\biokineticum_website\Biomechanics analysis software online physiotherapy.htm"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
except UnicodeDecodeError:
    with open(file_path, "r", encoding="latin-1") as f:
        content = f.read()

images_to_check = [
    "2bdf424f-cc8c-4aee-a063-84d8b942314f_2x",
    "9af05b2b-c4c5-4d21-a549-f3aa5ebdaa69_2x",
    "f6f36343-7b9d-4a1f-b4bb-637eb831c293_2x",
    "photo-1541534741688-6078c6bfb5c5"
]

print(f"File length: {len(content)}")

for img in images_to_check:
    print(f"\n--- Searching for: {img} ---")
    matches = [m.start() for m in re.finditer(re.escape(img), content)]
    print(f"Found {len(matches)} matches.")
    
    for i, match_idx in enumerate(matches[:3]): # Show first 3 matches
        start = max(0, match_idx - 500)
        end = min(len(content), match_idx + 500)
        print(f"Match {i+1} Context:")
        print(content[start:end])
        print("-" * 50)
