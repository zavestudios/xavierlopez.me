#!/usr/bin/env python3
"""
Add language identifiers to code blocks in markdown files.
"""

import re
from pathlib import Path


def detect_language(code_lines):
    """
    Detect the language of a code block based on content patterns.
    Returns the language identifier or None if uncertain.
    """
    code = '\n'.join(code_lines).strip()

    if not code:
        return None

    # SQL patterns
    sql_keywords = r'\b(SELECT|INSERT|UPDATE|DELETE|FROM|WHERE|JOIN|CREATE|ALTER|DROP|TABLE|DATABASE)\b'
    if re.search(sql_keywords, code, re.IGNORECASE):
        return 'sql'

    # Bash/Shell patterns
    bash_indicators = [
        r'^\$\s',  # Shell prompt
        r'^sudo\s',
        r'\bgit\s',
        r'\bnpm\s',
        r'\bbundle\s',
        r'\bpip\s',
        r'\bapt-get\s',
        r'\byum\s',
        r'\bbrew\s',
        r'\bcd\s',
        r'\bls\s',
        r'\bgrep\s',
        r'\bawk\s',
        r'\bsed\s',
        r'\bcat\s',
        r'\becho\s',
        r'\bexport\s',
        r'\bsource\s',
        r'\|\s',  # Pipes
        r'&&',
        r'#!/bin/(bash|sh)',
        r'^kill\s',
        r'^docker\s',
        r'^kubectl\s',
        r'^helm\s',
        r'^aws\s',
        r'^rvm\s',
        r'^tmux\s',
        r'^ssh\s',
        r'^scp\s',
        r'^vagrant\s',
    ]
    for pattern in bash_indicators:
        if re.search(pattern, code, re.MULTILINE):
            return 'bash'

    # Ruby/Rails patterns
    ruby_indicators = [
        r'\bdef\s',
        r'\bend\b',
        r'\brequire\s',
        r'\.each\b',
        r'\.map\b',
        r'\.select\b',
        r'\.where\(',
        r'\.find\(',
        r'\.pluck\(',
        r'@\w+\s*=',  # Instance variables
        r'::',  # Ruby namespace
        r'\bdo\s*\|',
        r'^\s*class\s+\w+',
        r'^\s*module\s+\w+',
    ]
    for pattern in ruby_indicators:
        if re.search(pattern, code, re.MULTILINE):
            return 'ruby'

    # YAML patterns
    if re.search(r'^\s*\w+:', code, re.MULTILINE) and re.search(r'^\s*-\s+\w+:', code, re.MULTILINE):
        return 'yaml'

    # Kubernetes YAML
    if re.search(r'apiVersion:', code) or re.search(r'kind:\s+(Deployment|Service|Pod|ConfigMap)', code):
        return 'yaml'

    # Python patterns
    python_indicators = [
        r'^\s*import\s',
        r'^\s*from\s+\w+\s+import',
        r'^\s*def\s+\w+\(.*\):',
        r'^\s*class\s+\w+.*:',
        r'^\s*if\s+.*:',
        r'^\s*for\s+.*:',
        r'^\s*while\s+.*:',
        r'\bprint\(',
        r'__init__',
        r'__main__',
        r'^\s*#\s*coding:',
    ]
    for pattern in python_indicators:
        if re.search(pattern, code, re.MULTILINE):
            return 'python'

    # JavaScript/TypeScript patterns
    js_indicators = [
        r'\bconst\s+\w+\s*=',
        r'\blet\s+\w+\s*=',
        r'\bvar\s+\w+\s*=',
        r'\bfunction\s*\(',
        r'=>\s*{',
        r'\.then\(',
        r'\.catch\(',
        r'async\s+function',
        r'await\s+',
        r'console\.log\(',
        r'require\([\'"]',
        r'module\.exports',
    ]
    for pattern in js_indicators:
        if re.search(pattern, code):
            return 'javascript'

    # JSON patterns
    if code.strip().startswith('{') and code.strip().endswith('}'):
        if re.search(r'"\w+":\s*["\[\{]', code):
            return 'json'

    # HTML/XML patterns
    if re.search(r'<\w+.*>.*</\w+>', code, re.DOTALL):
        return 'html'

    # CSS patterns
    if re.search(r'\{[^}]*\}', code) and re.search(r'[\w-]+\s*:\s*[^;]+;', code):
        return 'css'

    # Dockerfile patterns
    if re.search(r'^\s*FROM\s+', code, re.MULTILINE | re.IGNORECASE):
        return 'dockerfile'

    # Terraform patterns
    terraform_keywords = r'\b(resource|provider|variable|output|module|data)\s+"'
    if re.search(terraform_keywords, code):
        return 'hcl'

    # Configuration files (generic)
    if re.search(r'^\w+\s*=\s*', code, re.MULTILINE) and not re.search(r'[{}()]', code):
        return 'ini'

    # VimScript
    if re.search(r'^:\w+', code, re.MULTILINE):
        return 'vim'

    return None


def process_markdown_file(file_path, dry_run=False):
    """
    Process a markdown file to add language identifiers to code blocks.
    Returns tuple of (modified, uncertain_blocks)
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    result_lines = []
    in_code_block = False
    in_frontmatter = False
    frontmatter_count = 0
    current_code_block = []
    modified = False
    uncertain_blocks = []
    block_start_line = 0
    pending_opening = None
    pending_code_lines = []

    for i, line in enumerate(lines):
        # Track YAML front matter
        if line.strip() == '---' and i < 30 and frontmatter_count < 2:
            frontmatter_count += 1
            if frontmatter_count == 1:
                in_frontmatter = True
            elif frontmatter_count == 2:
                in_frontmatter = False
            result_lines.append(line)
            continue

        if in_frontmatter:
            result_lines.append(line)
            continue

        # Check for code block markers
        if line.strip().startswith('```'):
            if not in_code_block:
                # Opening backticks
                in_code_block = True
                block_start_line = i + 1
                current_code_block = []
                pending_code_lines = []

                # Check if it already has a language
                lang = line.strip()[3:].strip()
                if lang:
                    # Already has a language, keep as-is
                    result_lines.append(line)
                    pending_opening = None
                else:
                    # No language, store for later
                    pending_opening = line
            else:
                # Closing backticks - NEVER MODIFY
                in_code_block = False

                # Now try to detect language for the block we just collected
                if pending_opening is not None and current_code_block:
                    detected_lang = detect_language(current_code_block)
                    if detected_lang:
                        # Add the opening with language
                        result_lines.append(f'```{detected_lang}')
                        # Add all the code lines we held back
                        result_lines.extend(pending_code_lines)
                        modified = True
                    else:
                        # Couldn't detect language, use original
                        result_lines.append(pending_opening)
                        result_lines.extend(pending_code_lines)
                        uncertain_blocks.append({
                            'line': block_start_line,
                            'code': '\n'.join(current_code_block[:3])  # First 3 lines
                        })
                    pending_opening = None
                    pending_code_lines = []

                current_code_block = []
                result_lines.append(line)
        else:
            if in_code_block:
                # Inside code block, collect lines for analysis
                current_code_block.append(line)
                if pending_opening is not None:
                    # Hold back these lines until we know the language
                    pending_code_lines.append(line)
                else:
                    # Already has language, add normally
                    result_lines.append(line)
            else:
                result_lines.append(line)

    # Write back if modified and not dry run
    if modified and not dry_run:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(result_lines))

    return modified, uncertain_blocks


def process_all_posts(dry_run=False):
    """Process all posts in _posts directory."""
    posts_dir = Path('_posts')

    if not posts_dir.exists():
        print(f"Directory {posts_dir} not found")
        return

    total_modified = 0
    total_uncertain = 0

    for post_file in sorted(posts_dir.glob('*.md')):
        modified, uncertain = process_markdown_file(post_file, dry_run=dry_run)

        if modified or uncertain:
            print(f"\n{post_file.name}:")
            if modified:
                print(f"  ✓ Added language identifiers")
                total_modified += 1
            if uncertain:
                print(f"  ⚠ {len(uncertain)} code block(s) need manual review")
                total_uncertain += len(uncertain)
                for block in uncertain[:2]:  # Show first 2
                    print(f"    Line {block['line']}: {block['code'][:60]}...")

    print(f"\n{'=' * 60}")
    print(f"Summary:")
    print(f"  Modified: {total_modified} files")
    print(f"  Uncertain blocks: {total_uncertain}")
    if dry_run:
        print(f"\n(DRY RUN - no files were modified)")


if __name__ == '__main__':
    import sys
    dry_run = '--dry-run' in sys.argv
    process_all_posts(dry_run=dry_run)
