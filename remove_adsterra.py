import os
import glob

# Find all html files excluding backups
html_files = glob.glob('*.html')
html_files = [f for f in html_files if '_backup_' not in f]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # We look for <div class="container" style="text-align: center; margin: 2rem auto;">
    # that contains '623af1f726c06c948199ad8ebd38226e' or 'highperformanceformat'
    div_start_pattern = '<div class="container" style="text-align: center; margin: 2rem auto;">'
    
    idx = 0
    while True:
        start_pos = content.find(div_start_pattern, idx)
        if start_pos == -1:
            break
        
        # Find the next </div>
        end_div_pos = content.find('</div>', start_pos)
        if end_div_pos == -1:
            break
        
        end_pos = end_div_pos + len('</div>')
        block = content[start_pos:end_pos]
        
        if '623af1f726c06c948199ad8ebd38226e' in block or 'highperformanceformat' in block:
            # Check for preceding comment
            comment_before = '<!-- Adsterra -->'
            pre_search_start = max(0, start_pos - 100)
            comment_pos = content.rfind(comment_before, pre_search_start, start_pos)
            
            if comment_pos != -1:
                content = content[:comment_pos] + content[end_pos:]
                idx = comment_pos
            else:
                content = content[:start_pos] + content[end_pos:]
                idx = start_pos
        else:
            idx = end_pos
            
    if content != original_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Removed Adsterra from {file}")
    else:
        print(f"No Adsterra found in {file}")
