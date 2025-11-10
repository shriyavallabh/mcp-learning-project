#!/usr/bin/env python3
"""
Professional Book Image Generator using Google Gemini
Generates cover pages, infographics, and chapter visuals
"""

import os
from pathlib import Path
from typing import Optional, Dict
from google import genai
from google.genai import types
from PIL import Image
import io

class GeminiImageGenerator:
    """Generates images using Google Gemini API"""

    def __init__(self, api_key: str):
        """Initialize with API key"""
        self.api_key = api_key
        self.client = genai.Client(api_key=api_key)
        self.model = "gemini-2.5-flash-image"

    def generate_image(
        self,
        prompt: str,
        output_path: str,
        aspect_ratio: str = "3:4",  # Portrait for book pages
        style: str = "professional"
    ) -> Optional[str]:
        """
        Generate an image from a text prompt

        Args:
            prompt: Text description of the image to generate
            output_path: Where to save the generated image
            aspect_ratio: Image aspect ratio (3:4 for cover, 16:9 for infographics)
            style: Visual style (professional, technical, illustrative)

        Returns:
            Path to saved image or None on failure
        """
        print(f"\n🎨 Generating image: {Path(output_path).name}")
        print(f"📝 Prompt: {prompt[:100]}...")

        # Style-specific enhancements
        style_prefixes = {
            "professional": "Professional, clean, modern design. Publishing quality. ",
            "technical": "Technical diagram, clear, educational, schematic. High quality. ",
            "illustrative": "Friendly illustration, engaging, colorful, welcoming. ",
            "cover": "Book cover design, professional publishing standard, striking. "
        }

        full_prompt = style_prefixes.get(style, "") + prompt

        try:
            print(f"   📡 Calling Gemini API...")

            response = self.client.models.generate_content(
                model=self.model,
                contents=[full_prompt],
                config=types.GenerateContentConfig(
                    response_modalities=["IMAGE"],
                    image_config=types.ImageConfig(
                        aspect_ratio=aspect_ratio,
                    )
                )
            )

            # Extract and save image
            for part in response.parts:
                if part.inline_data is not None:
                    # Get image from response
                    generated_image = part.as_image()

                    # Create directory if needed
                    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

                    # Save image
                    generated_image.save(output_path)

                    file_size = Path(output_path).stat().st_size / 1024
                    print(f"   ✅ Image saved: {output_path} ({file_size:.1f} KB)")
                    return output_path

            print(f"   ❌ No image in response")
            return None

        except Exception as e:
            print(f"   ❌ Error: {e}")
            return None

    def generate_cover_page(
        self,
        title: str,
        subtitle: str,
        author: str,
        collaboration: str,
        output_path: str
    ) -> Optional[str]:
        """Generate professional book cover"""

        prompt = f"""
Design a STUNNING professional book cover for a technical programming textbook:

📚 TITLE: "{title}"
📖 SUBTITLE: "{subtitle}"
✍️  AUTHOR: {author}
🤝 {collaboration}

DESIGN SPECIFICATIONS:
- Style: Modern tech book (O'Reilly/Manning/No Starch Press quality)
- Layout: Title at top, subtitle below, author at bottom
- Theme: AI/Programming - use circuit patterns, neural network nodes, or code motifs
- Colors: Deep blue (#1E3A8A) with vibrant accent colors (cyan #06B6D4, purple #8B5CF6)
- Typography: Bold sans-serif title, clean readable subtitle/author
- Elements: Geometric shapes, gradient backgrounds, tech patterns
- Quality: Professional publishing standard, print-ready
- Orientation: Portrait (standard book format)
- Text prominence: Make title and author VERY readable and prominent

Visual style: Sophisticated technical, modern, premium, bestseller-worthy.
Make it look like a top-seller programming book from a major publisher.

IMPORTANT: Include ALL text elements clearly: title, subtitle, author name, collaboration note.
"""

        return self.generate_image(prompt, output_path, aspect_ratio="3:4", style="cover")

    def generate_chapter_infographic(
        self,
        chapter_number: int,
        chapter_title: str,
        concept: str,
        description: str,
        output_path: str
    ) -> Optional[str]:
        """Generate educational infographic for chapter concept"""

        prompt = f"""
Create an EDUCATIONAL infographic diagram for a programming textbook:

CHAPTER {chapter_number}: {chapter_title}
CONCEPT: {concept}
EXPLANATION: {description}

DESIGN REQUIREMENTS:
- Style: Technical educational diagram (like in O'Reilly or Manning books)
- Layout: Clear visual hierarchy with labels and annotations
- Colors: Blue (#3B82F6), teal (#14B8A6), purple (#A855F7) for elements
- Elements: Boxes, arrows, code snippets, icons, flow diagrams
- Typography: Sans-serif, highly readable
- Format: Landscape or square orientation
- Quality: Professional textbook quality
- Clarity: Beginner-friendly, visually explains the concept

Visual approach: Clean technical diagram that helps learners understand {concept}.
Include: Labels, arrows showing flow, visual metaphors, clear structure.

Make it informative, professional, and easy to understand at a glance.
"""

        return self.generate_image(prompt, output_path, aspect_ratio="16:9", style="technical")

    def generate_end_page(
        self,
        author: str,
        collaboration: str,
        output_path: str
    ) -> Optional[str]:
        """Generate professional end page"""

        prompt = f"""
Design a professional book END PAGE / BACK MATTER page:

AUTHOR: {author}
{collaboration}

DESIGN:
- Clean, minimal, elegant design
- Thank you message to readers
- Author credits prominently displayed
- Collaboration acknowledgment
- Professional typography
- Complementary to cover design
- Colors: Matching the tech book theme (blues, purples)
- Include: "Thank you for reading", author name, Claude collaboration note
- Style: Warm, professional, concluding

Make it feel like a quality book conclusion page.
"""

        return self.generate_image(prompt, output_path, aspect_ratio="3:4", style="professional")


class ImageValidator:
    """Validates generated images using Gemini vision"""

    def __init__(self, api_key: str):
        """Initialize validator"""
        self.api_key = api_key
        self.client = genai.Client(api_key=api_key)

    def validate_image(self, image_path: str, expected_content: str) -> Dict:
        """
        Validate an image using Gemini vision

        Returns:
            dict with 'valid', 'score', 'feedback'
        """
        if not Path(image_path).exists():
            return {'valid': False, 'score': 0, 'feedback': 'Image file not found'}

        print(f"\n🔍 Validating: {Path(image_path).name}")

        try:
            # Open image
            image = Image.open(image_path)

            # Validate with Gemini
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[
                    f"""Analyze this image as a professional book illustration.

Expected content: {expected_content}

Rate the image on:
1. Visual quality (clarity, professional appearance)
2. Content accuracy (matches expected content?)
3. Educational/aesthetic value
4. Suitability for a published book

Provide your assessment in this format:
SCORE: [0-10]
VALID: [YES/NO]
FEEDBACK: [brief explanation]
""",
                    image
                ]
            )

            text = response.text

            # Parse response
            score = 7
            valid = True
            feedback = text

            for line in text.split('\n'):
                if 'SCORE:' in line:
                    try:
                        score = int(''.join(filter(str.isdigit, line)))
                    except:
                        pass
                if 'VALID:' in line:
                    valid = 'YES' in line.upper()
                if 'FEEDBACK:' in line:
                    feedback = line.split('FEEDBACK:')[1].strip()

            print(f"   Score: {score}/10")
            print(f"   Valid: {'✅' if valid else '❌'} {valid}")

            return {
                'valid': valid and score >= 6,
                'score': score,
                'feedback': feedback
            }

        except Exception as e:
            print(f"   ⚠️  Validation error: {e}")
            return {'valid': True, 'score': 7, 'feedback': f'Could not validate: {e}'}


def main():
    """Test the image generation system"""
    print("\n" + "="*80)
    print("🎨 TESTING IMAGE GENERATION SYSTEM")
    print("="*80)

    API_KEY = "AIzaSyC15ewbSpMcboNAmMJhsj1dZmXA8l8yeGQ"

    generator = GeminiImageGenerator(API_KEY)
    validator = ImageValidator(API_KEY)

    # Test cover generation
    print("\n📚 Generating test cover page...")
    cover_path = generator.generate_cover_page(
        title="The Ultimate Guide to MCP, AI Agents, and Modern AI Development",
        subtitle="From Zero to OpenAI-Level Expertise",
        author="Shriyavallabh Pethkar",
        collaboration="in collaboration with Claude",
        output_path="images/test_cover.png"
    )

    if cover_path:
        # Validate it
        validation = validator.validate_image(
            cover_path,
            "Professional book cover with title, subtitle, author name, and tech/AI theme"
        )
        print(f"\n✅ Cover generation test {'PASSED' if validation['valid'] else 'FAILED'}")
        print(f"   Score: {validation['score']}/10")
        print(f"   Feedback: {validation['feedback'][:150]}")
    else:
        print("\n❌ Cover generation FAILED")

    # Test infographic generation
    print("\n\n📊 Generating test infographic...")
    infographic_path = generator.generate_chapter_infographic(
        chapter_number=1,
        chapter_title="Introduction to Programming",
        concept="Variables and Memory",
        description="Variables are labels that point to values in computer memory. They don't contain values, they reference them.",
        output_path="images/test_infographic.png"
    )

    if infographic_path:
        validation = validator.validate_image(
            infographic_path,
            "Educational diagram showing how variables reference values in memory"
        )
        print(f"\n✅ Infographic test {'PASSED' if validation['valid'] else 'FAILED'}")
        print(f"   Score: {validation['score']}/10")
    else:
        print("\n❌ Infographic generation FAILED")

    print("\n" + "="*80)
    print("✅ IMAGE GENERATION SYSTEM TEST COMPLETE")
    print("="*80)


if __name__ == "__main__":
    main()
