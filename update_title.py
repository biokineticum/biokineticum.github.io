import os
import re

directory = r'c:\Users\Lenovo\Documents\biokineticum.github.io'

def process_files():
    # Matches 'dr', 'Dr', 'dr.', 'Dr.' followed by 'Dariusz Mosler' or 'Dariusza Moslera'
    pattern = re.compile(r'\b([dD]r\.?)\s+(Dariusz(?:a)?\s+Mosler(?:a)?)\b')
    
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                def repl(match):
                    title = match.group(1)
                    name = match.group(2)
                    # If it has a dot (English standard), keep it and add hab.
                    if title.endswith('.'):
                        return f"{title} hab. {name}"
                    # If no dot (Polish standard), just add hab.
                    else:
                        return f"{title} hab. {name}"
                
                new_content, subs = pattern.subn(repl, content)
                
                if subs > 0:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated {subs} occurrences in {file}")
                    count += 1
                    
    print(f"Total files updated: {count}")

if __name__ == '__main__':
    process_files()
