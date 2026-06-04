import os
import glob
import re

# Find all html files excluding backups
html_files = glob.glob('*.html')
html_files = [f for f in html_files if '_backup_' not in f]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 1. Remove the header script loader and its optional comment
    # Match the comment optionally
    content = re.sub(r'<!--\s*Google\s*AdSense\s*-->\s*', '', content)
    content = re.sub(r'<script\s+async\s+src="https://pagead2\.googlesyndication\.com/pagead/js/adsbygoogle\.js[^"]*"\s*(?:crossorigin="anonymous"\s*)?></script>\s*', '', content)
    
    # 2. Find and remove the AdSense container block
    # We look for <div class="container" style="text-align: center; margin: 2rem auto;">
    # that contains 'adsbygoogle' or 'reklama_1'.
    
    # Let's locate all occurrences of the div
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
        
        if 'adsbygoogle' in block or 'reklama_1' in block:
            # Let's check if there is a preceding <!-- AdSense --> comment we should clean up
            comment_before = '<!-- AdSense -->'
            # Search a bit before the block for the comment
            pre_search_start = max(0, start_pos - 100)
            comment_pos = content.rfind(comment_before, pre_search_start, start_pos)
            
            if comment_pos != -1:
                # Remove from the comment start to the end of the block
                content = content[:comment_pos] + content[end_pos:]
                idx = comment_pos # Adjust index since length decreased
            else:
                content = content[:start_pos] + content[end_pos:]
                idx = start_pos # Adjust index since length decreased
        else:
            # Move index forward
            idx = end_pos
            
    if content != original_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Removed AdSense from {file}")
    else:
        print(f"No AdSense found in {file}")
