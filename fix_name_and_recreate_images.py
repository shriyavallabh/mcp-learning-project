#!/usr/bin/env python3
"""
Fix author name and recreate all images with premium quality
"""

import os
import re
from pathlib import Path
import shutil

def fix_author_name():
    """Replace incorrect name with correct one everywhere"""

    print("\n" + "="*80)
    print("📝 FIXING AUTHOR NAME EVERYWHERE")
    print("="*80)

    incorrect = "Shriyavallabh Pethkar"
    correct = "Shriyavallabh Pethkar"

    # Files to update
    files_to_update = []

    # Find all markdown and Python files
    for ext in ['*.md', '*.py']:
        files_to_update.extend(Path('.').rglob(ext))

    total_replacements = 0
    files_updated = 0

    for file_path in files_to_update:
        try:
            # Skip backup files and directories
            if '.backup' in str(file_path) or 'pdf_env' in str(file_path):
                continue

            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Count occurrences
            count = content.count(incorrect)

            if count > 0:
                # Replace
                new_content = content.replace(incorrect, correct)

                # Write back
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

                print(f"   ✅ {file_path}: {count} replacements")
                total_replacements += count
                files_updated += 1

        except Exception as e:
            print(f"   ⚠️  Error with {file_path}: {e}")

    print(f"\n✅ Name correction complete!")
    print(f"   📝 Files updated: {files_updated}")
    print(f"   🔄 Total replacements: {total_replacements}")
    print(f"   ✨ New name everywhere: {correct}")

    return total_replacements

if __name__ == "__main__":
    fix_author_name()
