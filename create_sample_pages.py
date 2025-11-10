#!/usr/bin/env python3
"""
Create sample preview pages from the book for marketing
Extract key pages as standalone images
"""

from pathlib import Path
import markdown2
import weasyprint
from PIL import Image
import io

def create_sample_pages():
    """Create sample page previews for marketing"""

    print("\n" + "="*80)
    print("📄 CREATING SAMPLE PAGE PREVIEWS")
    print("="*80)

    # Read the book with images
    book_path = Path("THE_ULTIMATE_MCP_AI_AGENTS_BOOK_WITH_IMAGES.md")
    with open(book_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"📖 Read book: {len(content)} characters")

    # Extract specific sections for samples
    samples = {
        "table_of_contents": {
            "start": "## Table of Contents",
            "end": "# PART I: PYTHON MASTERY",
            "title": "Table of Contents Preview"
        },
        "chapter1_intro": {
            "start": "# Chapter 1: Introduction to Programming and Python",
            "end": "### The Fundamental Concept",
            "title": "Chapter 1 Opening"
        },
        "interactive_example": {
            "start": "### 🎯 TRY THIS NOW!",
            "end": "### Making It Interactive",
            "title": "Interactive Learning Example"
        }
    }

    # Create samples directory
    Path("images/samples").mkdir(parents=True, exist_ok=True)

    print(f"\n📑 Creating {len(samples)} sample previews...")

    for sample_name, sample_info in samples.items():
        try:
            # Extract section
            start_idx = content.find(sample_info["start"])
            end_idx = content.find(sample_info["end"])

            if start_idx == -1 or end_idx == -1:
                print(f"   ⚠️  Could not find markers for {sample_name}")
                continue

            section = content[start_idx:end_idx]

            # Convert to HTML
            html = markdown2.markdown(section, extras=["fenced-code-blocks", "code-friendly"])

            # Style it
            styled_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{
            font-family: 'Helvetica', 'Arial', sans-serif;
            font-size: 11pt;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 40px;
            background: white;
        }}
        h1 {{
            color: #1E3A8A;
            font-size: 24pt;
            border-bottom: 3px solid #3B82F6;
            padding-bottom: 10pt;
        }}
        h2 {{
            color: #2563EB;
            font-size: 18pt;
            border-bottom: 2px solid #60A5FA;
            padding-bottom: 8pt;
        }}
        h3 {{
            color: #3B82F6;
            font-size: 14pt;
        }}
        code {{
            background-color: #F3F4F6;
            padding: 3px 6px;
            border-radius: 4px;
            font-family: 'Monaco', monospace;
            color: #DC2626;
        }}
        pre {{
            background-color: #1F2937;
            color: #F9FAFB;
            border-left: 4px solid #3B82F6;
            padding: 15px;
            border-radius: 6px;
        }}
        pre code {{
            background-color: transparent;
            color: #F9FAFB;
        }}
        ul, ol {{
            padding-left: 25px;
        }}
        li {{
            margin: 5px 0;
        }}
    </style>
</head>
<body>
    <div style="text-align: center; color: #6B7280; font-size: 10pt; margin-bottom: 20px;">
        SAMPLE PREVIEW FROM THE BOOK
    </div>
    {html}
    <div style="text-align: center; color: #6B7280; font-size: 10pt; margin-top: 30px; padding-top: 20px; border-top: 2px solid #E5E7EB;">
        This is a preview. Get the complete book to continue learning!
    </div>
</body>
</html>
"""

            # Generate PNG
            output_path = f"images/samples/{sample_name}_preview.png"

            weasyprint.HTML(string=styled_html).write_png(
                output_path,
                resolution=150  # Higher resolution for crisp preview
            )

            print(f"   ✅ Created: {sample_info['title']} → {output_path}")

        except Exception as e:
            print(f"   ❌ Error creating {sample_name}: {e}")

    print(f"\n📁 Sample previews saved in: images/samples/")
    print(f"💡 Use these for:")
    print(f"   • Website preview galleries")
    print(f"   • Social media content teasers")
    print(f"   • Email marketing campaigns")
    print(f"   • Amazon 'Look Inside' feature")

    print("\n" + "="*80)
    print("✅ SAMPLE PAGES CREATED!")
    print("="*80)


if __name__ == "__main__":
    create_sample_pages()
