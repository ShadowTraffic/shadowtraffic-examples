#!/usr/bin/env python3

import re
import json
import os

def extract_examples_from_readme():
    """Extract example names and their corresponding JSON files from README.md"""
    
    with open('README.md', 'r') as f:
        content = f.read()
    
    # Pattern to match example sections and their config file links
    # Looking for: ### Example Title followed by [![Demo](badge-config)](config-file.json)
    pattern = r'### ([^\n]+)\n\n\[\[!Demo\][^]]+config[^]]+\]\(([^)]+\.json)\)'
    
    matches = re.findall(pattern, content)
    print(f"Found {len(matches)} matches with pattern")
    
    # Debug: Let's also try a simpler approach
    lines = content.split('\n')
    examples = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith('### ') and i > 10:  # Skip the initial TOC sections
            title = line[4:].strip()  # Remove "### "
            
            # Look for the config badge in the next few lines
            for j in range(i+1, min(i+10, len(lines))):
                if 'config-🎁' in lines[j] and '.json)' in lines[j]:
                    # Extract JSON filename from the badge link
                    match = re.search(r'\(([^)]+\.json)\)', lines[j])
                    if match:
                        config_file = match.group(1)
                        examples.append({
                            'title': title,
                            'config_file': config_file
                        })
                        print(f"Found: {title} -> {config_file}")
                        break
        i += 1
    
    return examples

def build_consolidated_file():
    """Build a consolidated file with all examples and their configs"""
    
    examples = extract_examples_from_readme()
    
    output_lines = []
    
    for example in examples:
        title = example['title']
        config_file = example['config_file']
        
        # Check if config file exists
        if os.path.exists(config_file):
            try:
                with open(config_file, 'r') as f:
                    config_content = f.read().strip()
                
                # Add example name with markdown heading
                output_lines.append(f"### {title}")
                output_lines.append("")  # Empty line after title
                # Add config content with JSON code block
                output_lines.append("```json")
                output_lines.append(config_content)
                output_lines.append("```")
                # Add separator with double newline
                output_lines.append("")
                output_lines.append('-----')
                output_lines.append("")  # Extra empty line for double spacing
                
            except Exception as e:
                print(f"Error reading {config_file}: {e}")
        else:
            print(f"Config file not found: {config_file}")
    
    # Write consolidated file
    with open('combined-examples.txt', 'w') as f:
        f.write('\n'.join(output_lines))
    
    print(f"Consolidated {len(examples)} examples into combined-examples.txt")

if __name__ == '__main__':
    build_consolidated_file()
