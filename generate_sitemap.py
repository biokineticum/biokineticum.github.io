import os
import glob

def main():
    directory = r'c:\Users\Lenovo\Documents\biokineticum.github.io'
    html_files = glob.glob(os.path.join(directory, '*.html'))

    urls = []
    
    # Add root URL explicitly
    urls.append("""   <url>
      <loc>https://biokineticum.com/</loc>
      <lastmod>2026-07-30</lastmod>
      <changefreq>monthly</changefreq>
      <priority>1.0</priority>
   </url>""")

    for filepath in html_files:
        filename = os.path.basename(filepath)
        # exclude backups and old english.html
        if 'backup' in filename or filename == 'english.html':
            continue
            
        url = f"https://biokineticum.com/{filename}"
        priority = "0.8"
        if filename in ['index.html', 'index-pl.html']:
            priority = "1.0"
        elif 'telerehabilitacja' in filename or 'telerehabilitation' in filename:
            priority = "0.9"
            
        urls.append(f"""   <url>
      <loc>{url}</loc>
      <lastmod>2026-07-30</lastmod>
      <changefreq>monthly</changefreq>
      <priority>{priority}</priority>
   </url>""")

    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(urls)}
</urlset>
"""

    with open(os.path.join(directory, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write(sitemap_content)
        
    print("Sitemap generated.")

if __name__ == '__main__':
    main()
