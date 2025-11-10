#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Preformatted
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from pathlib import Path
import re

class FooterCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self.pages = []
    def showPage(self):
        self.pages.append(dict(self.__dict__))
        self._startPage()
    def save(self):
        for state in self.pages:
            self.__dict__.update(state)
            self.saveState()
            self.setFont('Helvetica', 8)
            self.setFillColor(HexColor('#6B7280'))
            self.drawRightString(A4[0] - 15*mm, 12*mm, "Author: Shriyavallabh Pethkar")
            self.restoreState()
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

print("Creating comprehensive PDF with ALL chapters and anime images...")

with open("COMPLETE_BOOK_ALL_CHAPTERS.md", 'r') as f:
    content = f.read()

doc = SimpleDocTemplate("FINAL_BOOK_ALL_CHAPTERS.pdf", pagesize=A4,
                        rightMargin=20*mm, leftMargin=20*mm,
                        topMargin=20*mm, bottomMargin=25*mm)

styles = getSampleStyleSheet()
h1 = ParagraphStyle('H1', parent=styles['Heading1'], fontSize=20, textColor=HexColor('#1E3A8A'), spaceAfter=12, spaceBefore=15, fontName='Helvetica-Bold')
body = ParagraphStyle('Body', parent=styles['Normal'], fontSize=10, alignment=TA_JUSTIFY, spaceAfter=6, leading=13)

story = []
lines = content.split('\n')
in_code = False
code_buf = []

print(f"Processing {len(lines)} lines...")

for i, line in enumerate(lines):
    if i % 200 == 0 and i > 0:
        print(f"  {i}/{len(lines)} lines...")
    
    line = line.strip()
    
    if line.startswith('```'):
        if in_code:
            if code_buf:
                try:
                    story.append(Preformatted('\n'.join(code_buf), styles['Code']))
                except: pass
            code_buf = []
            in_code = False
        else:
            in_code = True
        continue
    
    if in_code:
        code_buf.append(line)
        continue
    
    if line.startswith('![') and '](' in line:
        match = re.search(r'!\[.*?\]\((.*?)\)', line)
        if match:
            img_path = match.group(1)
            if Path(img_path).exists():
                try:
                    story.append(Spacer(1, 3*mm))
                    story.append(Image(img_path, width=160*mm, height=90*mm))
                    story.append(Spacer(1, 5*mm))
                except: pass
        continue
    
    if line.startswith('# '):
        title = line.lstrip('#').strip()
        try:
            story.append(Paragraph(title, h1))
        except: pass
    elif line and not line.startswith('#'):
        cleaned = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
        cleaned = re.sub(r'\*(.*?)\*', r'<i>\1</i>', cleaned)
        if cleaned:
            try:
                story.append(Paragraph(cleaned, body))
            except: pass

print("Building PDF...")
doc.build(story, canvasmaker=FooterCanvas)

size = Path("FINAL_BOOK_ALL_CHAPTERS.pdf").stat().st_size / (1024 * 1024)
print(f"\n✅ PDF Complete: FINAL_BOOK_ALL_CHAPTERS.pdf ({size:.2f} MB)")
