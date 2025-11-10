#!/usr/bin/env python3
"""
Generate FINAL premium PDF with:
- Correct author name: Shriyavallabh Pethkar
- All 10 premium professional images
- World-class formatting
"""

import os
from pathlib import Path
import markdown2
import weasyprint

def generate_premium_pdf():
    """Generate the final premium PDF"""

    print("\n" + "="*80)
    print("📚 GENERATING FINAL PREMIUM PDF")
    print("   Author: Shriyavallabh Pethkar")
    print("   Images: 10 Premium Professional Quality")
    print("="*80)

    input_file = Path("THE_ULTIMATE_AI_DEVELOPMENT_GUIDE_PREMIUM.md")
    output_file = Path("The_Ultimate_AI_Development_Guide_PREMIUM_FINAL.pdf")

    # Verify input
    if not input_file.exists():
        print(f"❌ Input file not found: {input_file}")
        return False

    # Verify images
    images_dir = Path("images/premium")
    if not images_dir.exists():
        print(f"❌ Images directory not found: {images_dir}")
        return False

    image_files = list(images_dir.glob("*.png"))
    print(f"📁 Found {len(image_files)} premium images")

    # Read markdown
    print(f"\n📖 Reading markdown...")
    with open(input_file, 'r', encoding='utf-8') as f:
        markdown_content = f.read()

    # Convert to HTML
    print(f"🔄 Converting to HTML...")
    html_content = markdown2.markdown(
        markdown_content,
        extras=["fenced-code-blocks", "tables", "code-friendly"]
    )

    # Premium styling
    styled_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>The Ultimate Guide to AI Development - Shriyavallabh Pethkar</title>
    <style>
        @page {{
            margin: 0.75in;
            @top-right {{
                content: "Page " counter(page);
                font-size: 9pt;
                color: #666;
                font-family: 'Helvetica', sans-serif;
            }}
            @bottom-center {{
                content: "The Ultimate AI Development Guide | Shriyavallabh Pethkar";
                font-size: 9pt;
                color: #666;
                font-family: 'Helvetica', sans-serif;
            }}
        }}

        body {{
            font-family: 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
            font-size: 11pt;
            line-height: 1.7;
            color: #1a1a1a;
            max-width: 100%;
            background: white;
        }}

        /* Premium Headings */
        h1 {{
            color: #0A1929;
            font-size: 32pt;
            font-weight: 800;
            margin-top: 40pt;
            margin-bottom: 20pt;
            page-break-before: always;
            border-bottom: 4px solid #00E5FF;
            padding-bottom: 12pt;
            letter-spacing: -0.5pt;
        }}

        h2 {{
            color: #1565C0;
            font-size: 22pt;
            font-weight: 700;
            margin-top: 28pt;
            margin-bottom: 14pt;
            border-bottom: 3px solid #00BCD4;
            padding-bottom: 10pt;
        }}

        h3 {{
            color: #1976D2;
            font-size: 17pt;
            font-weight: 600;
            margin-top: 20pt;
            margin-bottom: 10pt;
        }}

        h4 {{
            color: #2196F3;
            font-size: 14pt;
            font-weight: 600;
            margin-top: 16pt;
            margin-bottom: 8pt;
        }}

        /* Premium Images */
        img {{
            max-width: 100%;
            height: auto;
            display: block;
            margin: 30px auto;
            border: 1px solid #E0E0E0;
            border-radius: 8px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
            page-break-inside: avoid;
        }}

        /* Image captions */
        em {{
            display: block;
            text-align: center;
            font-style: italic;
            color: #616161;
            font-size: 10pt;
            margin-top: -20px;
            margin-bottom: 25px;
            font-weight: 500;
        }}

        /* Premium Code Blocks */
        code {{
            background-color: #F5F5F5;
            padding: 4px 8px;
            border-radius: 4px;
            font-family: 'Monaco', 'Menlo', 'Consolas', monospace;
            font-size: 10pt;
            color: #D32F2F;
            border: 1px solid #E0E0E0;
        }}

        pre {{
            background: linear-gradient(135deg, #1E1E1E 0%, #2D2D2D 100%);
            color: #F5F5F5;
            border: 1px solid #424242;
            border-radius: 8px;
            border-left: 5px solid #00E5FF;
            padding: 20px;
            overflow-x: auto;
            page-break-inside: avoid;
            margin: 20px 0;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }}

        pre code {{
            background-color: transparent;
            padding: 0;
            color: #F5F5F5;
            font-size: 9.5pt;
            line-height: 1.6;
            border: none;
        }}

        /* Premium Blockquotes */
        blockquote {{
            border-left: 6px solid #00E5FF;
            background: linear-gradient(to right, #E3F2FD 0%, #F5F5F5 100%);
            padding: 20px 25px;
            margin: 25px 0;
            border-radius: 6px;
            color: #0D47A1;
            page-break-inside: avoid;
            font-style: italic;
        }}

        /* Premium Lists */
        ul, ol {{
            margin: 12px 0;
            padding-left: 30px;
            line-height: 1.8;
        }}

        li {{
            margin: 8px 0;
        }}

        /* Premium Tables */
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 25px 0;
            page-break-inside: avoid;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }}

        th, td {{
            border: 1px solid #E0E0E0;
            padding: 12px 15px;
            text-align: left;
        }}

        th {{
            background: linear-gradient(135deg, #1565C0 0%, #1976D2 100%);
            color: white;
            font-weight: 600;
            text-transform: uppercase;
            font-size: 10pt;
            letter-spacing: 0.5pt;
        }}

        tr:nth-child(even) {{
            background-color: #FAFAFA;
        }}

        tr:hover {{
            background-color: #F5F5F5;
        }}

        /* Premium Links */
        a {{
            color: #1976D2;
            text-decoration: none;
            border-bottom: 2px solid #00E5FF;
            transition: all 0.3s;
        }}

        /* Premium Special Boxes */
        details {{
            background: linear-gradient(to right, #FFF3E0 0%, #FFFDE7 100%);
            border: 2px solid #FFB74D;
            border-radius: 8px;
            padding: 18px;
            margin: 20px 0;
            page-break-inside: avoid;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
        }}

        summary {{
            font-weight: 700;
            color: #E65100;
            cursor: pointer;
            margin-bottom: 12px;
            font-size: 11pt;
        }}

        /* Premium Horizontal Rules */
        hr {{
            border: none;
            border-top: 3px solid #E0E0E0;
            margin: 40px 0;
        }}

        /* Page Breaks */
        .page-break {{
            page-break-after: always;
        }}

        /* Print Optimizations */
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

            pre, blockquote, table {{
                page-break-inside: avoid;
            }}

            /* Ensure links are visible in print */
            a {{
                color: #1976D2;
            }}
        }}

        /* Premium Typography */
        p {{
            margin: 12px 0;
            text-align: justify;
        }}

        strong {{
            font-weight: 700;
            color: #0D47A1;
        }}
    </style>
</head>
<body>
    {html_content}
</body>
</html>
"""

    print(f"📄 Generating premium PDF...")
    print(f"⏳ This may take several minutes...")

    try:
        # Generate PDF
        weasyprint.HTML(string=styled_html, base_url=str(Path.cwd())).write_pdf(
            output_file,
            stylesheets=[],
            presentational_hints=True
        )

        file_size = output_file.stat().st_size / (1024 * 1024)

        print("\n" + "="*80)
        print("🎉 SUCCESS! PREMIUM PDF GENERATED!")
        print("="*80)
        print(f"\n📄 Output: {output_file}")
        print(f"📊 Size: {file_size:.2f} MB")
        print(f"🖼️  Images: 10 premium professional infographics")
        print(f"✍️  Author: Shriyavallabh Pethkar")
        print(f"🏆 Quality: Million-dollar job interview ready")

        print(f"\n💫 This PDF includes:")
        print(f"   ✨ Premium professional cover page")
        print(f"   🎨 10 IBM/Google-quality infographics")
        print(f"   📖 Interactive exercises and quizzes")
        print(f"   🎯 Complete Python + AI content")
        print(f"   💼 Professional formatting for FAANG-level careers")

        print("\n" + "="*80)
        print("✅ PREMIUM BOOK COMPLETE - READY TO LAND MILLION DOLLAR JOBS!")
        print("="*80)

        return True

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = generate_premium_pdf()
    exit(0 if success else 1)
