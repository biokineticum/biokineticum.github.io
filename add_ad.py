import os
import glob

html_files = glob.glob('*.html')
html_files = [f for f in html_files if '_backup_' not in f]

ad_code = """
    <div class="container" style="text-align: center; margin: 2rem auto;">
        <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6881554784265771"
             crossorigin="anonymous"></script>
        <!-- reklama_1 -->
        <ins class="adsbygoogle"
             style="display:block"
             data-ad-client="ca-pub-6881554784265771"
             data-ad-slot="7700312728"
             data-ad-format="auto"
             data-full-width-responsive="true"></ins>
        <script>
             (adsbygoogle = window.adsbygoogle || []).push({});
        </script>
    </div>
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<!-- reklama_1 -->' in content:
        print(f"Ad already in {file}")
        continue

    # Find the footer tag
    footer_idx = content.rfind('<footer')
    if footer_idx != -1:
        new_content = content[:footer_idx] + ad_code + content[footer_idx:]
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
    else:
        print(f"Footer not found in {file}")
