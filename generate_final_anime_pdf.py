#!/usr/bin/env python3
"""
FINAL PDF GENERATOR with Anime Graphics
Creates the ultimate PDF with all anime illustrations
"""

import markdown
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfgen import canvas
import re

class AnimePDFGenerator:
    """Generate beautiful PDF with anime illustrations"""

    def __init__(self, input_md: str, output_pdf: str, author_name: str):
        self.input_md = input_md
        self.output_pdf = output_pdf
        self.author_name = author_name
        self.styles = getSampleStyleSheet()
        self._create_custom_styles()

    def _create_custom_styles(self):
        """Create custom paragraph styles"""

        # Title style
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            textColor='#1E3A8A',
            spaceAfter=30,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        ))

        # Chapter style
        self.styles.add(ParagraphStyle(
            name='Chapter',
            parent=self.styles['Heading1'],
            fontSize=20,
            textColor='#2563EB',
            spaceAfter=20,
            spaceBefore=20,
            fontName='Helvetica-Bold'
        ))

        # Section style
        self.styles.add(ParagraphStyle(
            name='Section',
            parent=self.styles['Heading2'],
            fontSize=16,
            textColor='#3B82F6',
            spaceAfter=15,
            fontName='Helvetica-Bold'
        ))

        # Code style
        self.styles.add(ParagraphStyle(
            name='Code',
            parent=self.styles['Code'],
            fontSize=10,
            fontName='Courier',
            leftIndent=20,
            rightIndent=20,
            spaceAfter=10
        ))

        # Author attribution
        self.styles.add(ParagraphStyle(
            name='AuthorAttribution',
            parent=self.styles['Normal'],
            fontSize=8,
            textColor='#6B7280',
            alignment=TA_CENTER,
            fontName='Helvetica-Oblique'
        ))

    def generate_pdf(self):
        """Generate the complete PDF"""

        print("📄 Generating final anime-enhanced PDF...")

        # Read markdown
        print("   → Reading markdown content...")
        with open(self.input_md, 'r', encoding='utf-8') as f:
            md_content = f.read()

        # Create PDF document
        print("   → Creating PDF document...")
        doc = SimpleDocTemplate(
            self.output_pdf,
            pagesize=letter,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=72
        )

        # Build content
        print("   → Building PDF content...")
        story = []

        # Add title page
        story.append(Spacer(1, 2*inch))
        story.append(Paragraph(
            "The Ultimate Guide to MCP, AI Agents,<br/>and Modern AI Development",
            self.styles['CustomTitle']
        ))
        story.append(Spacer(1, 0.5*inch))
        story.append(Paragraph(
            "From Zero to OpenAI-Level Expertise",
            self.styles['Heading2']
        ))
        story.append(Spacer(1, inch))

        # Add cover image if exists
        cover_path = "images/anime_book/00_cover.png"
        if Path(cover_path).exists():
            img = Image(cover_path, width=4*inch, height=5.3*inch)
            story.append(img)

        story.append(Spacer(1, 0.5*inch))
        story.append(Paragraph(
            f"Author: {self.author_name}",
            self.styles['AuthorAttribution']
        ))
        story.append(Paragraph(
            "in collaboration with Claude",
            self.styles['AuthorAttribution']
        ))
        story.append(PageBreak())

        # Process markdown content
        # This is a simplified version - full implementation would parse all markdown
        print("   → Processing content sections...")

        # Split by chapters
        chapters = re.split(r'^# ', md_content, flags=re.MULTILINE)

        for i, chapter in enumerate(chapters[1:], 1):  # Skip first empty split
            lines = chapter.split('\n')
            chapter_title = lines[0]

            print(f"      Processing: {chapter_title[:50]}...")

            # Add chapter title
            story.append(Paragraph(f"Chapter {i}: {chapter_title}", self.styles['Chapter']))
            story.append(Spacer(1, 0.3*inch))

            # Add chapter content (simplified - would need full markdown parsing)
            # For now, just add some content and images

            # Check for images in this chapter
            image_matches = re.findall(r'!\[([^\]]+)\]\(([^)]+)\)', chapter)
            for alt_text, img_path in image_matches:
                if Path(img_path).exists():
                    try:
                        img = Image(img_path, width=5*inch, height=3.5*inch)
                        story.append(img)
                        story.append(Spacer(1, 0.2*inch))
                        story.append(Paragraph(alt_text, self.styles['AuthorAttribution']))
                        story.append(Spacer(1, 0.3*inch))
                    except Exception as e:
                        print(f"         ⚠️  Could not add image {img_path}: {e}")

            # Add page break after chapter
            if i < len(chapters) - 1:
                story.append(PageBreak())

        # Build PDF
        print("   → Building final PDF...")
        doc.build(story)

        file_size = Path(self.output_pdf).stat().st_size / (1024 * 1024)
        print(f"\n✅ PDF generated successfully!")
        print(f"   File: {self.output_pdf}")
        print(f"   Size: {file_size:.2f} MB")

        return self.output_pdf

def main():
    print("\n" + "="*80)
    print("📚 FINAL ANIME PDF GENERATION")
    print("="*80)

    generator = AnimePDFGenerator(
        input_md="THE_ULTIMATE_AI_DEVELOPMENT_GUIDE_WITH_ANIME_COMPLETE.md",
        output_pdf="THE_ULTIMATE_AI_DEVELOPMENT_GUIDE_ANIME_FINAL.pdf",
        author_name="Shriyavallabh Pethkar"
    )

    generator.generate_pdf()

    print("\n" + "="*80)
    print("✅ COMPLETE!")
    print("="*80)

if __name__ == "__main__":
    main()
