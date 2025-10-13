#!/usr/bin/env python3
"""
Integrate generated images into the book markdown
"""

from pathlib import Path
import shutil

def integrate_images():
    """Add images to the markdown book at appropriate locations"""

    print("\n" + "="*80)
    print("📚 INTEGRATING IMAGES INTO BOOK")
    print("="*80)

    # Read the original book
    book_path = Path("THE_ULTIMATE_MCP_AI_AGENTS_BOOK.md")
    with open(book_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"\n📖 Read book: {len(content)} characters")

    # Backup original
    backup_path = book_path.with_suffix('.md.backup')
    shutil.copy(book_path, backup_path)
    print(f"💾 Backed up to: {backup_path}")

    # Image insertions (marker → image markdown)
    insertions = {
        # Cover page at the very beginning (after title)
        "## From Zero to OpenAI-Level Expertise": """## From Zero to OpenAI-Level Expertise

![Book Cover](images/book/cover.png)
""",

        # Chapter 1 images
        "### Why Computers Need Instructions": """### Why Computers Need Instructions

![What is Programming](images/book/ch1_what_is_programming.png)
*Figure 1.1: Programming is giving explicit, step-by-step instructions to a computer*
""",

        "### 6. Easy Integration with Everything": """### 6. Easy Integration with Everything

![Python Ecosystem](images/book/ch1_python_ecosystem.png)
*Figure 1.2: Python's Dominant Position in the AI/ML Ecosystem*
""",

        "**Overall execution flow:**": """**Overall execution flow:**

![Program Execution Flow](images/book/ch1_first_program_flow.png)
*Figure 1.3: How Python executes your first program*
""",

        # Chapter 2 images
        "### Variables Are Labels, Not Boxes": """### Variables Are Labels, Not Boxes

![Variables as References](images/book/ch2_variables_references.png)
*Figure 2.1: Variables are references/labels, not containers*
""",

        "## 2.3 Python Data Types (Complete Understanding)": """## 2.3 Python Data Types (Complete Understanding)

![Python Data Types](images/book/ch2_data_types.png)
*Figure 2.2: Overview of Python's Built-in Data Types*
""",

        "### Converting to Integer: int()": """### Converting to Integer: int()

![Type Conversion](images/book/ch2_type_conversion.png)
*Figure 2.3: Type Conversion Between Different Python Types*
""",

        # Chapter 3 images
        "Python provides four main collection types:": """Python provides four main collection types:

![Collections Overview](images/book/ch3_collections_overview.png)
*Figure 3.1: Python's Four Main Collection Types*
""",

        "### Creating Lists": """### Creating Lists

![List Operations](images/book/ch3_list_operations.png)
*Figure 3.2: Common List Operations and Methods*
""",

        # End page at the very end
        "## Using Typora (GUI Application)": """## Using Typora (GUI Application)

---

![End Page](images/book/end_page.png)

---

**Thank you for reading!**

This book was created by **Shriyavallabh Pethkar** in collaboration with **Claude**.

---
"""
    }

    # Apply insertions
    modified_content = content
    insertions_applied = 0

    for marker, replacement in insertions.items():
        if marker in modified_content:
            modified_content = modified_content.replace(marker, replacement, 1)
            insertions_applied += 1
            print(f"✅ Inserted image at: {marker[:50]}...")
        else:
            print(f"⚠️  Marker not found: {marker[:50]}...")

    # Write the new version
    new_book_path = Path("THE_ULTIMATE_MCP_AI_AGENTS_BOOK_WITH_IMAGES.md")
    with open(new_book_path, 'w', encoding='utf-8') as f:
        f.write(modified_content)

    print(f"\n✅ Created new book with images: {new_book_path}")
    print(f"📊 Applied {insertions_applied}/{len(insertions)} image insertions")
    print(f"📏 New book size: {len(modified_content)} characters")

    return new_book_path


if __name__ == "__main__":
    result = integrate_images()
    print(f"\n🎉 Book with images ready: {result}")
    print("="*80)
