#!/usr/bin/env python3
"""
Alternative PDF Generator - Pure Python Approach
Uses markdown2 and weasyprint (Python packages)

This script requires:
- markdown2 (for converting MD to HTML)
- weasyprint (for converting HTML to PDF)

Install with: pip install markdown2 weasyprint
"""

import os
import sys
from pathlib import Path

def print_banner():
    """Print script banner."""
    print("=" * 80)
    print(" " * 15 + "📚 THE ULTIMATE AI DEVELOPMENT GUIDE")
    print(" " * 18 + "Python PDF Generator")
    print("=" * 80)
    print()

def check_dependencies():
    """Check if required packages are installed."""
    missing = []

    try:
        import markdown2
        print("✅ markdown2 found")
    except ImportError:
        missing.append("markdown2")
        print("❌ markdown2 not found")

    try:
        import weasyprint
        print("✅ weasyprint found")
    except ImportError:
        missing.append("weasyprint")
        print("❌ weasyprint not found")

    return missing

def install_instructions(missing):
    """Print installation instructions."""
    print("\n📦 Missing Dependencies Installation:")
    print("-" * 80)
    print("Run this command to install missing packages:")
    print()
    print(f"  pip install {' '.join(missing)}")
    print()
    print("Or install individually:")
    for pkg in missing:
        print(f"  pip install {pkg}")
    print("-" * 80)

def generate_pdf():
    """Generate PDF using Python libraries."""
    try:
        import markdown2
        import weasyprint
    except ImportError as e:
        print(f"\n❌ Error: {e}")
        return False

    input_file = Path("THE_ULTIMATE_MCP_AI_AGENTS_BOOK.md")
    output_file = Path("The_Ultimate_AI_Development_Guide.pdf")

    # Check if input exists
    if not input_file.exists():
        print(f"\n❌ Input file not found: {input_file}")
        return False

    print(f"\n📖 Reading markdown file...")
    with open(input_file, 'r', encoding='utf-8') as f:
        markdown_content = f.read()

    print(f"🔄 Converting markdown to HTML...")
    html_content = markdown2.markdown(
        markdown_content,
        extras=["fenced-code-blocks", "tables", "code-friendly"]
    )

    # Add CSS styling
    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>The Ultimate Guide to MCP, AI Agents, and Modern AI Development</title>
        <style>
            @page {{
                margin: 1in;
                @top-right {{
                    content: "Page " counter(page);
                }}
            }}
            body {{
                font-family: Arial, sans-serif;
                font-size: 11pt;
                line-height: 1.6;
                color: #333;
            }}
            h1 {{
                color: #2c3e50;
                font-size: 24pt;
                margin-top: 24pt;
                margin-bottom: 12pt;
                page-break-before: always;
            }}
            h2 {{
                color: #34495e;
                font-size: 18pt;
                margin-top: 18pt;
                margin-bottom: 9pt;
            }}
            h3 {{
                color: #7f8c8d;
                font-size: 14pt;
                margin-top: 14pt;
                margin-bottom: 7pt;
            }}
            code {{
                background-color: #f4f4f4;
                padding: 2px 4px;
                border-radius: 3px;
                font-family: 'Courier New', monospace;
                font-size: 10pt;
            }}
            pre {{
                background-color: #f8f8f8;
                border: 1px solid #ddd;
                border-radius: 5px;
                padding: 10px;
                overflow-x: auto;
                page-break-inside: avoid;
            }}
            pre code {{
                background-color: transparent;
                padding: 0;
            }}
            blockquote {{
                border-left: 4px solid #3498db;
                padding-left: 15px;
                margin-left: 0;
                color: #555;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 15px 0;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #3498db;
                color: white;
            }}
            a {{
                color: #3498db;
                text-decoration: none;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    print(f"📄 Generating PDF...")
    print(f"⏳ This may take a few minutes for large files...")

    try:
        weasyprint.HTML(string=styled_html).write_pdf(output_file)

        file_size = output_file.stat().st_size / (1024 * 1024)

        print("\n" + "=" * 80)
        print("🎉 SUCCESS! PDF generated successfully!")
        print("=" * 80)
        print(f"\n📄 Output file: {output_file}")
        print(f"📊 File size: {file_size:.2f} MB")
        print(f"\n💡 Tip: Open with your favorite PDF reader!")
        print("\n" + "=" * 80)
        return True

    except Exception as e:
        print(f"\n❌ Error generating PDF: {e}")
        return False

def main():
    """Main entry point."""
    print_banner()

    print("🔍 Checking dependencies...")
    missing = check_dependencies()

    if missing:
        install_instructions(missing)
        print("\n❌ Please install missing dependencies and run again.")
        return 1

    print("\n✅ All dependencies found!\n")

    success = generate_pdf()
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())
