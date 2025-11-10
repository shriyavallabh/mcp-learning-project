#!/usr/bin/env python3
"""
Update book markdown with premium images and correct author name
"""

from pathlib import Path
import shutil

def main():
    print("\n" + "="*80)
    print("📚 UPDATING BOOK WITH PREMIUM IMAGES")
    print("="*80)

    # Read the current book
    book_path = Path("THE_ULTIMATE_MCP_AI_AGENTS_BOOK_WITH_IMAGES.md")
    with open(book_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"\n📖 Read book: {len(content)} characters")

    # Backup
    backup_path = Path("THE_ULTIMATE_MCP_AI_AGENTS_BOOK_WITH_IMAGES.md.backup")
    shutil.copy(book_path, backup_path)
    print(f"💾 Backed up to: {backup_path.name}")

    # Replace image paths with premium versions
    replacements = {
        # Cover
        "images/book/cover.png": "images/premium/cover_final.png",

        # Chapter 1
        "images/book/ch1_what_is_programming.png": "images/premium/ch1_programming.png",
        "images/book/ch1_python_ecosystem.png": "images/premium/ch1_ecosystem.png",
        "images/book/ch1_first_program_flow.png": "images/premium/ch1_execution.png",

        # Chapter 2
        "images/book/ch2_variables_references.png": "images/premium/ch2_variables.png",
        "images/book/ch2_data_types.png": "images/premium/ch2_types.png",
        "images/book/ch2_type_conversion.png": "images/premium/ch2_conversion.png",

        # Chapter 3
        "images/book/ch3_collections_overview.png": "images/premium/ch3_collections.png",
        "images/book/ch3_list_operations.png": "images/premium/ch3_lists.png",

        # End page
        "images/book/end_page.png": "images/premium/end_page_final.png"
    }

    modified_content = content
    replacements_made = 0

    for old_path, new_path in replacements.items():
        count = modified_content.count(old_path)
        if count > 0:
            modified_content = modified_content.replace(old_path, new_path)
            replacements_made += count
            print(f"   ✅ Replaced: {Path(old_path).name} → {Path(new_path).name} ({count} times)")

    # Write new version
    new_book_path = Path("THE_ULTIMATE_AI_DEVELOPMENT_GUIDE_PREMIUM.md")
    with open(new_book_path, 'w', encoding='utf-8') as f:
        f.write(modified_content)

    print(f"\n✅ Created: {new_book_path.name}")
    print(f"📊 Made {replacements_made} image path replacements")
    print(f"📏 Book size: {len(modified_content)} characters")

    print("\n" + "="*80)
    print("✅ BOOK UPDATED WITH PREMIUM IMAGES!")
    print("="*80)

    return new_book_path


if __name__ == "__main__":
    result = main()
    print(f"\n📖 Premium book ready: {result}")
