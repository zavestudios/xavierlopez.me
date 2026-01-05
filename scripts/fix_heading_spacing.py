#!/usr/bin/env python3
"""
Add blank lines above and below headings and lists in markdown files.
"""

import os
import re
from pathlib import Path


def is_list_item(line):
    """Check if a line is a list item."""
    stripped = line.lstrip()
    # Bulleted list: starts with -, *, or +
    # Numbered list: starts with number followed by . or )
    return (stripped.startswith('- ') or
            stripped.startswith('* ') or
            stripped.startswith('+ ') or
            re.match(r'^\d+[\.\)] ', stripped))


def fix_spacing(content):
    """Add blank lines above and below headings and lists."""
    lines = content.split('\n')
    result = []
    in_frontmatter = False
    frontmatter_count = 0
    in_list = False
    in_code_block = False

    for i, line in enumerate(lines):
        # Track code blocks
        if line.strip().startswith('```'):
            in_code_block = not in_code_block

        # Track YAML front matter
        if line.strip() == '---' and not in_code_block:
            frontmatter_count += 1
            if frontmatter_count == 1:
                in_frontmatter = True
            elif frontmatter_count == 2:
                in_frontmatter = False

        # Skip processing inside code blocks or front matter
        if in_code_block or in_frontmatter:
            result.append(line)
            continue

        # Check if current line is a heading
        is_heading = line.strip().startswith('#')

        # Check if current line is a list item
        is_list = is_list_item(line)

        # Check if we're starting a list
        was_in_list = in_list
        if is_list:
            in_list = True
        elif line.strip() == '':
            # Blank line, maintain list state for now
            pass
        else:
            in_list = False

        # Add blank line before heading if needed
        if is_heading:
            if result and result[-1].strip() != '':
                result.append('')
            result.append(line)
            # Add blank line after heading
            if i < len(lines) - 1 and lines[i + 1].strip() != '':
                result.append('')
            continue

        # Add blank line before list starts
        if is_list and not was_in_list:
            if result and result[-1].strip() != '':
                result.append('')

        result.append(line)

        # Add blank line after list ends
        if was_in_list and not is_list and line.strip() != '':
            # Previous line was a list, current is not and not blank
            # Check if we need to add a blank line before current
            if result and len(result) >= 2 and is_list_item(result[-2]):
                # Insert blank line before the current line
                current = result.pop()
                result.append('')
                result.append(current)

    return '\n'.join(result)


def process_posts():
    """Process all posts in _posts directory."""
    posts_dir = Path('_posts')

    if not posts_dir.exists():
        print(f"Directory {posts_dir} not found")
        return

    for post_file in sorted(posts_dir.glob('*.md')):
        print(f"Processing {post_file.name}...")

        with open(post_file, 'r', encoding='utf-8') as f:
            content = f.read()

        fixed_content = fix_spacing(content)

        if content != fixed_content:
            with open(post_file, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            print(f"  ✓ Updated {post_file.name}")
        else:
            print(f"  - No changes needed for {post_file.name}")


if __name__ == '__main__':
    process_posts()
