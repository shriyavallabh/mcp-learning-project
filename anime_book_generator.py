#!/usr/bin/env python3
"""
ANIME/MANGA STYLE EDUCATIONAL BOOK IMAGE GENERATOR
Generates comic-style dialogue panels with anime characters explaining concepts
Using Google Gemini API for image generation
"""

import os
from pathlib import Path
from typing import Optional, Dict, List
from google import genai
from google.genai import types
from PIL import Image, ImageDraw, ImageFont
import io
import time

class AnimeEducationalImageGenerator:
    """Generates anime/manga style educational images with dialogue panels"""

    def __init__(self, api_key: str, author_name: str = "Shriyavallabh Pethkar"):
        """Initialize with API key and author name for attribution"""
        self.api_key = api_key
        self.client = genai.Client(api_key=api_key)
        self.model = "gemini-2.5-flash-image"
        self.author_name = author_name

    def generate_comic_panel_image(
        self,
        concept: str,
        dialogue_exchange: List[Dict[str, str]],
        output_path: str,
        panel_count: int = 4,
        aspect_ratio: str = "16:9"
    ) -> Optional[str]:
        """
        Generate anime-style comic panels with characters explaining a concept

        Args:
            concept: The programming/AI concept to explain
            dialogue_exchange: List of dicts with 'speaker', 'text', 'expression' keys
            output_path: Where to save the image
            panel_count: Number of panels (2-6)
            aspect_ratio: Image ratio

        Returns:
            Path to saved image or None
        """

        # Build the detailed prompt for manga-style educational comic
        dialogue_text = "\n".join([
            f"Panel {i+1}: {d['speaker']} ({d.get('expression', 'friendly')}): \"{d['text']}\""
            for i, d in enumerate(dialogue_exchange[:panel_count])
        ])

        prompt = f"""Create a PROFESSIONAL educational manga/anime-style comic panel layout explaining a programming concept.

CONCEPT TO EXPLAIN: {concept}

COMIC LAYOUT:
- {panel_count} panels arranged horizontally or in 2x2 grid
- Each panel shows anime/manga style characters having a dialogue
- Clean panel borders (black lines)
- Speech bubbles with clear text
- Professional manga art style (similar to educational manga like "The Manga Guide to" series)

DIALOGUE SEQUENCE:
{dialogue_text}

CHARACTER DESIGN:
- Two main characters:
  1. Student character (curious, eager to learn, younger appearance, big expressive eyes)
  2. Teacher/Mentor character (knowledgeable, friendly, slightly older, confident)
- Both should be diverse, professional, and appealing
- Anime/manga art style but NOT childish - suitable for college students/professionals
- Clean line art, expressive faces, professional quality

VISUAL ELEMENTS:
- Speech bubbles with dialogue text (MUST be readable)
- Thought bubbles or visual metaphors where helpful
- Background elements related to programming (computers, code snippets, tech elements)
- Professional manga panel composition
- Clean, organized layout

QUALITY STANDARDS:
- Similar to "The Manga Guide to Statistics" or "The Manga Guide to Databases" series
- Professional educational manga quality
- Clear, readable text in speech bubbles
- Engaging but educational
- Suitable for a professional textbook

COLOR SCHEME:
- Can be full color or manga-style (black/white with accent colors)
- Clean, professional appearance
- Good contrast for readability

AUTHOR ATTRIBUTION:
- Small text at bottom: "Author: {self.author_name}"

Make it engaging, professional, and educational. The goal is to make learning fun through manga-style storytelling while maintaining academic credibility."""

        return self._generate_and_save(prompt, output_path, aspect_ratio, "educational-manga")

    def generate_anime_cover(
        self,
        title: str,
        subtitle: str,
        output_path: str
    ) -> Optional[str]:
        """Generate anime-style book cover with characters"""

        prompt = f"""Create a STUNNING anime-style book cover for a technical programming/AI textbook.

TITLE: "{title}"
SUBTITLE: "{subtitle}"
AUTHOR: {self.author_name} (bottom of cover)

DESIGN CONCEPT:
- Professional anime/manga art style cover (think light novel or educational manga quality)
- Feature 2-3 appealing anime characters who will be the "guides" throughout the book
- Characters should look intelligent, tech-savvy, friendly
- One character pointing at holographic AI/code elements
- Background: Futuristic tech environment with floating code, neural networks, digital interfaces
- Professional light novel cover quality

CHARACTERS:
- Main character: Enthusiastic young professional/student (protagonist learner)
- Supporting: Wise mentor figure (teacher/guide)
- Both should be diverse, professional-looking, appealing anime style
- Modern clothing with tech elements

VISUAL ELEMENTS:
- Holographic displays showing code, AI symbols, neural networks
- Floating digital particles/data streams
- Modern tech aesthetic meets anime art
- Professional lighting and composition

TYPOGRAPHY:
- Bold, modern title text at top
- Clear, readable subtitle
- Author name at bottom in smaller text
- Professional font choices that work with anime aesthetic

COLOR PALETTE:
- Vibrant but professional colors
- Tech blues, cyans, purples with warm accent colors
- Eye-catching gradient background
- Good contrast for text readability

QUALITY STANDARD:
- Professional light novel / educational manga cover quality
- Would look good in a bookstore next to "The Manga Guide to" series
- Appealing to college students and young professionals
- Both fun AND professional

Make it striking, professional, and make people WANT to pick up this book!"""

        return self._generate_and_save(prompt, output_path, "3:4", "anime-cover")

    def generate_concept_visualization(
        self,
        concept_title: str,
        concept_description: str,
        visual_metaphor: str,
        output_path: str,
        include_character: bool = True
    ) -> Optional[str]:
        """Generate anime-style concept visualization with optional character guide"""

        character_prompt = ""
        if include_character:
            character_prompt = """
- Include an anime character (your friendly guide) pointing at or interacting with the diagram
- Character should be explaining/gesturing towards key elements
- Speech bubble with brief explanation or tip
- Character: professional, friendly, anime style"""

        prompt = f"""Create a professional educational diagram with anime/manga aesthetic.

CONCEPT: {concept_title}
EXPLANATION: {concept_description}
VISUAL METAPHOR: {visual_metaphor}

DESIGN APPROACH:
- Clean technical diagram showing the concept
- Anime/manga art style for any human elements
- Professional educational quality (think "The Manga Guide" series)
- Clear labels and annotations
- Flow arrows showing process/relationships
- Color-coded elements for clarity{character_prompt}

VISUAL ELEMENTS:
- Main diagram in center (flowchart, architecture, process flow, etc.)
- Clear labels with professional typography
- Arrows showing relationships/flow
- Color coding for different element types
- Clean, organized layout
- Professional quality suitable for textbook

STYLE:
- Blend of technical diagram + anime aesthetic
- Professional but engaging
- Clear and educational
- Suitable for college-level textbook

ATTRIBUTION:
- Small text at bottom right: "Author: {self.author_name}"

Make it clear, professional, and visually engaging. Balance technical accuracy with visual appeal."""

        return self._generate_and_save(prompt, output_path, "16:9", "technical-anime")

    def generate_chapter_opener(
        self,
        chapter_number: int,
        chapter_title: str,
        chapter_description: str,
        output_path: str
    ) -> Optional[str]:
        """Generate anime-style chapter opening page with character introduction"""

        prompt = f"""Create an engaging anime-style chapter opening page for a technical textbook.

CHAPTER {chapter_number}: {chapter_title}
DESCRIPTION: {chapter_description}

DESIGN:
- Feature your anime guide characters excited about this chapter
- Characters in dynamic, welcoming poses
- One character holding a sign or holographic display with chapter title
- Background: Tech-themed environment relevant to chapter topic
- Professional light novel / educational manga quality

LAYOUT:
- "CHAPTER {chapter_number}" prominently displayed at top
- Chapter title in bold, clear typography
- Brief chapter description or teaser
- Characters looking excited and inviting reader to learn

VISUAL ELEMENTS:
- Anime characters (your friendly teaching guides)
- Tech background elements related to chapter content
- Floating icons or symbols representing key topics
- Professional composition and lighting
- Vibrant but professional colors

MOOD:
- Exciting, "let's learn this!" energy
- Welcoming and encouraging
- Professional but fun
- Makes reader eager to start chapter

ATTRIBUTION:
- Small text at bottom: "Author: {self.author_name}"

Quality: Professional educational manga chapter opener quality."""

        return self._generate_and_save(prompt, output_path, "16:9", "chapter-opener")

    def generate_infographic_with_characters(
        self,
        topic: str,
        key_points: List[str],
        output_path: str
    ) -> Optional[str]:
        """Generate infographic with anime characters presenting information"""

        points_text = "\n".join([f"{i+1}. {point}" for i, point in enumerate(key_points)])

        prompt = f"""Create a professional educational infographic with anime characters presenting information.

TOPIC: {topic}

KEY POINTS TO VISUALIZE:
{points_text}

DESIGN:
- Central infographic layout (organized, clean structure)
- Anime characters positioned around the infographic, pointing to different sections
- Characters explaining or highlighting key points
- Professional educational manga quality
- Clear visual hierarchy

INFOGRAPHIC ELEMENTS:
- Clean boxes/sections for each key point
- Icons or symbols for each concept
- Clear typography for all text
- Numbered or organized flow
- Color-coded sections
- Connecting lines/arrows showing relationships

CHARACTER INTEGRATION:
- 1-2 anime characters interacting with the infographic
- Characters pointing, gesturing, or holding elements
- Speech bubbles with brief explanations or tips
- Professional, friendly anime style
- Makes the information feel more personal and engaging

STYLE:
- Blend of professional infographic + anime elements
- Clean, modern design
- Educational but engaging
- Suitable for professional textbook

COLORS:
- Professional color scheme (blues, teals, purples with accents)
- Good contrast and readability
- Consistent with tech/education theme

ATTRIBUTION:
- Bottom: "Author: {self.author_name}"

Make it informative, visually appealing, and engaging through character integration."""

        return self._generate_and_save(prompt, output_path, "16:9", "infographic-anime")

    def generate_comparison_diagram(
        self,
        concept_a: str,
        concept_b: str,
        differences: List[Dict[str, str]],
        output_path: str
    ) -> Optional[str]:
        """Generate side-by-side comparison with anime characters"""

        diff_text = "\n".join([
            f"- {d['aspect']}: {d['a']} vs {d['b']}"
            for d in differences
        ])

        prompt = f"""Create a professional comparison diagram with anime-style characters.

COMPARING: {concept_a} VS {concept_b}

DIFFERENCES:
{diff_text}

LAYOUT:
- Split screen design: {concept_a} on left, {concept_b} on right
- Vertical dividing line in center
- Each side has a character representative/mascot
- Characters should visually represent their concept
- Professional educational manga quality

CHARACTERS:
- Left character representing {concept_a}
- Right character representing {concept_b}
- Both in anime/manga style
- Characters can be "competing" in friendly way or explaining their side
- Professional, appealing design

COMPARISON ELEMENTS:
- Clear bullet points or sections showing differences
- Visual symbols or icons for each aspect
- Color coding (e.g., blue for A, green for B)
- Clear labels and typography
- Easy to scan and understand

STYLE:
- Professional comparison infographic with anime elements
- Clean, organized layout
- Educational but engaging
- Suitable for textbook use

VISUAL APPEAL:
- Balanced composition
- Professional colors
- Clear readability
- Engaging through character design

ATTRIBUTION:
- Bottom: "Author: {self.author_name}"

Make it clear, professional, and make the comparison easy to understand at a glance."""

        return self._generate_and_save(prompt, output_path, "16:9", "comparison-anime")

    def _generate_and_save(
        self,
        prompt: str,
        output_path: str,
        aspect_ratio: str,
        style_tag: str
    ) -> Optional[str]:
        """Internal method to generate and save image"""

        print(f"\n🎨 Generating {style_tag}: {Path(output_path).name}")
        print(f"📝 Concept: {prompt.split('CONCEPT')[1].split('\\n')[0] if 'CONCEPT' in prompt else 'Cover/Chapter page'}")

        try:
            print(f"   📡 Calling Gemini API...")

            response = self.client.models.generate_content(
                model=self.model,
                contents=[prompt],
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

    def generate_image_with_retry(
        self,
        generator_method,
        max_retries: int = 3,
        wait_time: int = 5,
        **kwargs
    ) -> Optional[str]:
        """Wrapper to retry image generation on failure"""

        for attempt in range(max_retries):
            try:
                result = generator_method(**kwargs)
                if result:
                    return result
                print(f"   ⚠️  Attempt {attempt + 1}/{max_retries} failed, retrying...")
            except Exception as e:
                print(f"   ❌ Error on attempt {attempt + 1}: {e}")

            if attempt < max_retries - 1:
                print(f"   ⏳ Waiting {wait_time} seconds...")
                time.sleep(wait_time)

        print(f"   ❌ Failed after {max_retries} attempts")
        return None


def main():
    """Test the anime educational image generator"""
    print("\n" + "="*80)
    print("🎨 ANIME EDUCATIONAL IMAGE GENERATOR - TEST")
    print("="*80)

    API_KEY = "AIzaSyC15ewbSpMcboNAmMJhsj1dZmXA8l8yeGQ"
    generator = AnimeEducationalImageGenerator(API_KEY, "Shriyavallabh Pethkar")

    # Create test directory
    Path("images/anime_test").mkdir(parents=True, exist_ok=True)

    # Test 1: Comic panel explaining variables
    print("\n📘 TEST 1: Comic panel explaining Python variables")
    dialogue = [
        {
            "speaker": "Student (Alex)",
            "text": "What exactly is a variable in Python?",
            "expression": "curious"
        },
        {
            "speaker": "Teacher (Maya)",
            "text": "Great question! A variable is like a label that points to a value in memory!",
            "expression": "enthusiastic"
        },
        {
            "speaker": "Student (Alex)",
            "text": "So it's not a box that contains the value?",
            "expression": "surprised"
        },
        {
            "speaker": "Teacher (Maya)",
            "text": "Exactly! Think of it as a name tag pointing to where the value lives in memory!",
            "expression": "proud"
        }
    ]

    generator.generate_comic_panel_image(
        concept="Python Variables are References, Not Containers",
        dialogue_exchange=dialogue,
        output_path="images/anime_test/test_comic_variables.png",
        panel_count=4
    )

    print("\n⏳ Waiting 5 seconds before next generation...")
    time.sleep(5)

    # Test 2: Anime cover
    print("\n📕 TEST 2: Anime-style book cover")
    generator.generate_anime_cover(
        title="The Ultimate Guide to MCP, AI Agents, and Modern AI Development",
        subtitle="From Zero to OpenAI-Level Expertise",
        output_path="images/anime_test/test_anime_cover.png"
    )

    print("\n⏳ Waiting 5 seconds before next generation...")
    time.sleep(5)

    # Test 3: Concept visualization
    print("\n📊 TEST 3: Concept visualization with character")
    generator.generate_concept_visualization(
        concept_title="How Python Code Executes",
        concept_description="Python reads your code line by line, interprets it, and executes the instructions",
        visual_metaphor="Show flow: Code → Interpreter → Execution → Output",
        output_path="images/anime_test/test_concept_execution.png",
        include_character=True
    )

    print("\n" + "="*80)
    print("✅ ANIME GENERATOR TEST COMPLETE!")
    print("   Check images/anime_test/ folder for results")
    print("="*80)


if __name__ == "__main__":
    main()
