#!/usr/bin/env python3
"""
PDF Generator for "The Ultimate Guide to MCP, AI Agents, and Modern AI Development"

This script converts the markdown book to a beautiful, professional PDF.
It handles dependency checking, installation, and formatting automatically.

Author: AI-Generated
Date: 2025
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

class PDFGenerator:
    """Handles PDF generation from markdown with automatic dependency management."""

    def __init__(self, input_file, output_file):
        """
        Initialize the PDF generator.

        Parameters:
            input_file (str): Path to the markdown file
            output_file (str): Path for the output PDF
        """
        self.input_file = Path(input_file)
        self.output_file = Path(output_file)
        self.system = platform.system()

    def print_header(self):
        """Print a beautiful header for the script."""
        print("=" * 80)
        print(" " * 15 + "📚 THE ULTIMATE AI DEVELOPMENT GUIDE")
        print(" " * 20 + "PDF Generation Script")
        print("=" * 80)
        print()

    def check_pandoc(self):
        """Check if pandoc is installed."""
        print("🔍 Checking for pandoc installation...")
        try:
            result = subprocess.run(
                ["pandoc", "--version"],
                capture_output=True,
                text=True,
                check=True
            )
            version = result.stdout.split('\n')[0]
            print(f"✅ Pandoc found: {version}")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("❌ Pandoc not found!")
            return False

    def install_pandoc(self):
        """Provide instructions to install pandoc based on OS."""
        print("\n📦 Pandoc Installation Instructions:")
        print("-" * 80)

        if self.system == "Darwin":  # macOS
            print("For macOS, install using Homebrew:")
            print("  brew install pandoc")
            print("  brew install basictex")
            print("\nOr download from: https://pandoc.org/installing.html")

        elif self.system == "Linux":
            print("For Linux (Ubuntu/Debian):")
            print("  sudo apt-get update")
            print("  sudo apt-get install pandoc texlive-latex-base texlive-fonts-recommended")
            print("\nFor other Linux distros:")
            print("  Visit: https://pandoc.org/installing.html")

        elif self.system == "Windows":
            print("For Windows:")
            print("  1. Download installer from: https://pandoc.org/installing.html")
            print("  2. Run the installer")
            print("  3. Restart this script")

        else:
            print(f"Unknown OS: {self.system}")
            print("Visit: https://pandoc.org/installing.html")

        print("-" * 80)

    def check_latex(self):
        """Check if LaTeX is installed."""
        print("\n🔍 Checking for LaTeX installation...")
        try:
            result = subprocess.run(
                ["pdflatex", "--version"],
                capture_output=True,
                text=True,
                check=True
            )
            print("✅ LaTeX found")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("⚠️  LaTeX not found (optional, but recommended for better formatting)")
            return False

    def check_file_exists(self):
        """Check if input markdown file exists."""
        print(f"\n🔍 Checking for input file: {self.input_file}")
        if self.input_file.exists():
            size_mb = self.input_file.stat().st_size / (1024 * 1024)
            print(f"✅ File found ({size_mb:.2f} MB)")
            return True
        else:
            print(f"❌ File not found: {self.input_file}")
            return False

    def generate_pdf_simple(self):
        """Generate PDF using simple pandoc command (no LaTeX required)."""
        print("\n🎨 Generating PDF (Simple Mode)...")
        print("This may take a few minutes for large files...")

        command = [
            "pandoc",
            str(self.input_file),
            "-o", str(self.output_file),
            "--pdf-engine=wkhtmltopdf",
            "--toc",
            "--toc-depth=3",
            f"--metadata=title:The Ultimate Guide to MCP, AI Agents, and Modern AI Development",
            f"--metadata=subtitle:From Zero to OpenAI-Level Expertise",
            f"--metadata=author:Comprehensive Industry Guide",
            "--standalone"
        ]

        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Error: {e.stderr}")
            return False

    def generate_pdf_professional(self):
        """Generate PDF using LaTeX engine for professional output."""
        print("\n🎨 Generating PDF (Professional Mode with LaTeX)...")
        print("This may take a few minutes for large files...")

        command = [
            "pandoc",
            str(self.input_file),
            "-o", str(self.output_file),
            "--pdf-engine=xelatex",
            "-V", "geometry:margin=1in",
            "-V", "fontsize=11pt",
            "-V", "mainfont=Arial",
            "-V", "monofont=Courier New",
            "-V", "documentclass=report",
            "-V", "papersize=letter",
            "-V", "linkcolor=blue",
            "--toc",
            "--toc-depth=3",
            "--highlight-style=tango",
            f"--metadata=title:The Ultimate Guide to MCP, AI Agents, and Modern AI Development",
            f"--metadata=subtitle:From Zero to OpenAI-Level Expertise",
            f"--metadata=author:Comprehensive Industry Guide",
            f"--metadata=date:{self._get_date()}",
            "--standalone"
        ]

        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Error: {e.stderr}")
            return False

    def _get_date(self):
        """Get current date in readable format."""
        from datetime import datetime
        return datetime.now().strftime("%Y")

    def generate(self):
        """Main generation workflow."""
        self.print_header()

        # Check if input file exists
        if not self.check_file_exists():
            print("\n❌ Cannot proceed without input file!")
            return False

        # Check for pandoc
        if not self.check_pandoc():
            self.install_pandoc()
            print("\n❌ Please install pandoc and run this script again.")
            return False

        # Check for LaTeX
        has_latex = self.check_latex()

        # Generate PDF
        success = False
        if has_latex:
            print("\n📝 Using professional LaTeX engine for best quality...")
            success = self.generate_pdf_professional()
        else:
            print("\n📝 Using simple mode (install LaTeX for better formatting)...")
            success = self.generate_pdf_simple()

        if success:
            file_size = self.output_file.stat().st_size / (1024 * 1024)
            print("\n" + "=" * 80)
            print("🎉 SUCCESS! PDF generated successfully!")
            print("=" * 80)
            print(f"\n📄 Output file: {self.output_file}")
            print(f"📊 File size: {file_size:.2f} MB")
            print(f"\n💡 Tip: Open with your favorite PDF reader!")
            print("\n" + "=" * 80)
            return True
        else:
            print("\n" + "=" * 80)
            print("❌ PDF generation failed!")
            print("=" * 80)
            print("\n🔧 Troubleshooting:")
            print("  1. Make sure pandoc is properly installed")
            print("  2. Try installing LaTeX for better compatibility")
            print("  3. Check that the markdown file is valid")
            print("\n" + "=" * 80)
            return False


def main():
    """Main entry point."""
    # Configuration
    input_file = "THE_ULTIMATE_MCP_AI_AGENTS_BOOK.md"
    output_file = "The_Ultimate_AI_Development_Guide.pdf"

    # Create generator
    generator = PDFGenerator(input_file, output_file)

    # Generate PDF
    success = generator.generate()

    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
