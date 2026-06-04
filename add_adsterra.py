import os
import glob

# Find all html files excluding backups
html_files = glob.glob('*.html')
html_files = [f for f in html_files if '_backup_' not in f]

adsterra_code = """
    <!-- Adsterra -->
    <div class="container" style="text-align: center; margin: 2rem auto;">
        <script type="text/javascript">
            atOptions = {
                'key' : '623af1f726c06c948199ad8ebd38226e',
                'format' : 'iframe',
                'height' : 300,
                'width' : 160,
                'params' : {}
            };
        </script>
        <script type="text/javascript" src="https://www.highperformanceformat.com/623af1f726c06c948199ad8ebd38226e/invoke.js"></script>
    </div>
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '623af1f726c06c948199ad8ebd38226e' in content:
        print(f"Adsterra ad already in {file}")
        continue

    # Find the footer tag case-insensitively
    footer_idx = content.lower().rfind('<footer')
    if footer_idx != -1:
        new_content = content[:footer_idx] + adsterra_code + content[footer_idx:]
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
    else:
        print(f"Footer not found in {file}")
