import os
from bs4 import BeautifulSoup

directory = r'c:\Users\Lenovo\Documents\biokineticum.github.io'

def audit_seo():
    html_files = [f for f in os.listdir(directory) if f.endswith('.html')]
    issues = {}
    
    for filename in html_files:
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            
            file_issues = []
            
            # Check Title
            if not soup.title or not soup.title.string.strip():
                file_issues.append("Missing or empty <title>")
                
            # Check Meta Description
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            if not meta_desc or not meta_desc.get('content', '').strip():
                file_issues.append("Missing or empty <meta name='description'>")
                
            # Check Canonical
            canonical = soup.find('link', attrs={'rel': 'canonical'})
            if not canonical or not canonical.get('href', '').strip():
                file_issues.append("Missing <link rel='canonical'>")
                
            # Check H1 Count
            h1s = soup.find_all('h1')
            if len(h1s) == 0:
                file_issues.append("Missing <h1> tag")
            elif len(h1s) > 1:
                file_issues.append(f"Multiple <h1> tags found: {len(h1s)}")
                
            # Check Images Alternative Texts
            imgs_without_alt = [img for img in soup.find_all('img') if not img.get('alt', '').strip()]
            if imgs_without_alt:
                file_issues.append(f"Found {len(imgs_without_alt)} images missing 'alt' attribute")

            # Check HTML lang
            html_tag = soup.find('html')
            if not html_tag or not html_tag.get('lang'):
                file_issues.append("Missing 'lang' attribute in <html> tag")
                
            if file_issues:
                issues[filename] = file_issues
                
    if not issues:
        print("PERFECT: All critical SEO tags present in all HTML files.")
    else:
        print("SEO ISSUES FOUND:")
        for filename, errs in issues.items():
            print(f"\n{filename}:")
            for err in errs:
                print(f" - {err}")

if __name__ == '__main__':
    audit_seo()
