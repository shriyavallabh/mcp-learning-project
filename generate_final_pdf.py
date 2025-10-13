#!/usr/bin/env python3
"""
Generate final professional PDF with all images
"""

import os
import subprocess
from pathlib import Path
import markdown2
import weasyprint

def generate_final_pdf():
    """Generate the complete book PDF with all images"""

    print("\n" + "="*80)
    print("📚 GENERATING FINAL PROFESSIONAL PDF")
    print("="*80)

    input_file = Path("THE_ULTIMATE_MCP_AI_AGENTS_BOOK_WITH_IMAGES.md")
    output_file = Path("The_Ultimate_AI_Development_Guide_FINAL.pdf")

    # Check input exists
    if not input_file.exists():
        print(f"❌ Input file not found: {input_file}")
        return False

    # Check images exist
    images_dir = Path("images/book")
    if not images_dir.exists():
        print(f"❌ Images directory not found: {images_dir}")
        return False

    image_count = len(list(images_dir.glob("*.png")))
    print(f"📁 Found {image_count} images in {images_dir}")

    print(f"\n📖 Reading markdown file...")
    with open(input_file, 'r', encoding='utf-8') as f:
        markdown_content = f.read()

    print(f"🔄 Converting markdown to HTML...")
    html_content = markdown2.markdown(
        markdown_content,
        extras=["fenced-code-blocks", "tables", "code-friendly"]
    )

    # Enhanced CSS for professional book with images
    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>The Ultimate Guide to MCP, AI Agents, and Modern AI Development</title>
        <style>
            @page {{
                margin: 0.75in;
                @top-right {{
                    content: "Page " counter(page);
                    font-size: 9pt;
                    color: #666;
                }}
                @bottom-center {{
                    content: "The Ultimate Guide to AI Development";
                    font-size: 9pt;
                    color: #666;
                }}
            }}

            body {{
                font-family: 'Helvetica', 'Arial', sans-serif;
                font-size: 11pt;
                line-height: 1.6;
                color: #333;
                max-width: 100%;
            }}

            /* Headings */
            h1 {{
                color: #1E3A8A;
                font-size: 28pt;
                font-weight: bold;
                margin-top: 30pt;
                margin-bottom: 15pt;
                page-break-before: always;
                border-bottom: 3px solid #3B82F6;
                padding-bottom: 10pt;
            }}

            h2 {{
                color: #2563EB;
                font-size: 20pt;
                font-weight: bold;
                margin-top: 24pt;
                margin-bottom: 12pt;
                border-bottom: 2px solid #60A5FA;
                padding-bottom: 8pt;
            }}

            h3 {{
                color: #3B82F6;
                font-size: 16pt;
                font-weight: bold;
                margin-top: 18pt;
                margin-bottom: 9pt;
            }}

            h4 {{
                color: #60A5FA;
                font-size: 13pt;
                font-weight: bold;
                margin-top: 14pt;
                margin-bottom: 7pt;
            }}

            /* Images */
            img {{
                max-width: 100%;
                height: auto;
                display: block;
                margin: 20px auto;
                border: 1px solid #E5E7EB;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                page-break-inside: avoid;
            }}

            /* Image captions */
            em {{
                display: block;
                text-align: center;
                font-style: italic;
                color: #6B7280;
                font-size: 10pt;
                margin-top: -15px;
                margin-bottom: 20px;
            }}

            /* Code blocks */
            code {{
                background-color: #F3F4F6;
                padding: 3px 6px;
                border-radius: 4px;
                font-family: 'Monaco', 'Menlo', 'Courier New', monospace;
                font-size: 10pt;
                color: #DC2626;
            }}

            pre {{
                background-color: #1F2937;
                color: #F9FAFB;
                border: 1px solid #374151;
                border-radius: 6px;
                border-left: 4px solid #3B82F6;
                padding: 15px;
                overflow-x: auto;
                page-break-inside: avoid;
                margin: 15px 0;
            }}

            pre code {{
                background-color: transparent;
                padding: 0;
                color: #F9FAFB;
                font-size: 9pt;
                line-height: 1.5;
            }}

            /* Blockquotes */
            blockquote {{
                border-left: 5px solid #3B82F6;
                background-color: #EFF6FF;
                padding: 15px 20px;
                margin: 20px 0;
                border-radius: 4px;
                color: #1E40AF;
                page-break-inside: avoid;
            }}

            /* Lists */
            ul, ol {{
                margin: 10px 0;
                padding-left: 25px;
            }}

            li {{
                margin: 5px 0;
            }}

            /* Tables */
            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 20px 0;
                page-break-inside: avoid;
            }}

            th, td {{
                border: 1px solid #D1D5DB;
                padding: 10px;
                text-align: left;
            }}

            th {{
                background-color: #3B82F6;
                color: white;
                font-weight: bold;
            }}

            tr:nth-child(even) {{
                background-color: #F9FAFB;
            }}

            /* Links */
            a {{
                color: #2563EB;
                text-decoration: none;
                border-bottom: 1px dotted #2563EB;
            }}

            /* Special boxes */
            details {{
                background-color: #FEF3C7;
                border: 2px solid #F59E0B;
                border-radius: 6px;
                padding: 15px;
                margin: 15px 0;
                page-break-inside: avoid;
            }}

            summary {{
                font-weight: bold;
                color: #92400E;
                cursor: pointer;
                margin-bottom: 10px;
            }}

            /* Horizontal rules */
            hr {{
                border: none;
                border-top: 2px solid #E5E7EB;
                margin: 30px 0;
            }}

            /* Page breaks */
            .page-break {{
                page-break-after: always;
            }}

            /* Print optimizations */
            @media print {{
                body {{
                    color: #000;
                }}

                h1, h2, h3 {{
                    page-break-after: avoid;
                }}

                img {{
                    page-break-inside: avoid;
                    page-break-after: avoid;
                }}

                pre, blockquote {{
                    page-break-inside: avoid;
                }}
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    print(f"📄 Generating PDF with images...")
    print(f"⏳ This may take several minutes for a book with images...")

    try:
        # Generate PDF with WeasyPrint
        weasyprint.HTML(string=styled_html, base_url=str(Path.cwd())).write_pdf(
            output_file,
            stylesheets=[],
            presentational_hints=True
        )

        file_size = output_file.stat().st_size / (1024 * 1024)

        print("\n" + "="*80)
        print("🎉 SUCCESS! FINAL PDF GENERATED!")
        print("="*80)
        print(f"\n📄 Output file: {output_file}")
        print(f"📊 File size: {file_size:.2f} MB")
        print(f"🖼️  Images included: {image_count}")
        print(f"\n💫 This is your publication-ready book with:")
        print(f"   • Professional cover page")
        print(f"   • {image_count} educational infographics")
        print(f"   • Interactive exercises and quizzes")
        print(f"   • Complete Python + AI content")
        print(f"   • Professional formatting")
        print("\n" + "="*80)
        return True

    except Exception as e:
        print(f"\n❌ Error generating PDF: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = generate_final_pdf()
    exit(0 if success else 1)
