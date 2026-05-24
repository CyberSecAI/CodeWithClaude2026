import os
import re

def convert_vtt_to_txt(vtt_file, txt_file):
    seen = set()
    with open(vtt_file, 'r') as f:
        lines = f.readlines()
    
    output_lines = []
    for line in lines:
        line = line.strip()
        # Skip VTT headers and timestamps
        if not line or line.startswith('WEBVTT') or line.startswith('Kind:') or line.startswith('Language:') or '-->' in line:
            continue
        
        # Clean HTML tags
        clean = re.sub('<[^>]*>', '', line)
        # Unescape HTML entities
        clean = clean.replace('&amp;', '&').replace('&gt;', '>').replace('&lt;', '<')
        
        if clean and clean not in seen:
            output_lines.append(clean)
            seen.add(clean)
            
    with open(txt_file, 'w') as f:
        f.write('\n'.join(output_lines))

transcripts_dir = 'transcripts'
for filename in os.listdir(transcripts_dir):
    if filename.endswith('.en.vtt'):
        vtt_path = os.path.join(transcripts_dir, filename)
        txt_filename = filename.replace('.en.vtt', '.txt')
        txt_path = os.path.join(transcripts_dir, txt_filename)
        print(f"Converting {filename} to {txt_filename}")
        convert_vtt_to_txt(vtt_path, txt_path)
