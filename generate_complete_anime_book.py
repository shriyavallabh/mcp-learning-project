#!/usr/bin/env python3
"""
COMPLETE ANIME-STYLE BOOK REGENERATION SCRIPT
Generates ALL images for the entire book with anime/manga style
DO NOT STOP until all images are generated
"""

import sys
import time
from pathlib import Path
from anime_book_generator import AnimeEducationalImageGenerator

API_KEY = "AIzaSyC15ewbSpMcboNAmMJhsj1dZmXA8l8yeGQ"
AUTHOR_NAME = "Shriyavallabh Pethkar"

def wait_between_images(seconds=7):
    """Wait between API calls to avoid rate limiting"""
    print(f"   ⏳ Waiting {seconds} seconds before next image...")
    time.sleep(seconds)

def generate_with_retry(func, max_retries=3, **kwargs):
    """Execute generation function with retry logic"""
    for attempt in range(max_retries):
        try:
            print(f"      Attempt {attempt + 1}/{max_retries}...")
            result = func(**kwargs)
            if result:
                print(f"      ✅ SUCCESS!")
                return result
            else:
                print(f"      ⚠️  No result returned")
        except Exception as e:
            print(f"      ❌ Error: {e}")

        if attempt < max_retries - 1:
            wait_time = (attempt + 1) * 5
            print(f"      ⏳ Retrying in {wait_time} seconds...")
            time.sleep(wait_time)

    print(f"      ❌ FAILED after {max_retries} attempts")
    return None

def main():
    print("\n" + "="*100)
    print("🎨 COMPLETE ANIME-STYLE BOOK IMAGE GENERATION")
    print("   Generating comprehensive visual guide for the entire book")
    print("   DO NOT STOP UNTIL COMPLETE!")
    print("="*100)

    generator = AnimeEducationalImageGenerator(API_KEY, AUTHOR_NAME)

    # Create anime images directory
    Path("images/anime_book").mkdir(parents=True, exist_ok=True)

    successful = []
    failed = []

    # =============================================================================
    # COMPREHENSIVE IMAGE LIST FOR ENTIRE BOOK
    # =============================================================================

    all_images = [
        # -------------------------------------------------------------------------
        # 1. BOOK COVER (Anime Style)
        # -------------------------------------------------------------------------
        {
            "num": 1,
            "type": "cover",
            "title": "Anime Book Cover",
            "generator": lambda: generator.generate_anime_cover(
                title="The Ultimate Guide to MCP, AI Agents, and Modern AI Development",
                subtitle="From Zero to OpenAI-Level Expertise",
                output_path="images/anime_book/00_cover.png"
            )
        },

        # -------------------------------------------------------------------------
        # PART I: PYTHON MASTERY
        # -------------------------------------------------------------------------

        # Chapter 1: Introduction to Programming
        {
            "num": 2,
            "type": "comic",
            "title": "Ch1: What is Programming?",
            "generator": lambda: generator.generate_comic_panel_image(
                concept="What is Programming?",
                dialogue_exchange=[
                    {"speaker": "Student", "text": "What exactly is programming?", "expression": "curious"},
                    {"speaker": "Teacher", "text": "It's giving step-by-step instructions to a computer!", "expression": "enthusiastic"},
                    {"speaker": "Student", "text": "Like a recipe?", "expression": "thinking"},
                    {"speaker": "Teacher", "text": "Exactly! A recipe for the computer to follow!", "expression": "happy"}
                ],
                output_path="images/anime_book/01_what_is_programming.png",
                panel_count=4
            )
        },
        {
            "num": 3,
            "type": "concept",
            "title": "Ch1: How Programs Execute",
            "generator": lambda: generator.generate_concept_visualization(
                concept_title="Program Execution Flow",
                concept_description="Code → Interpreter → Execution → Output",
                visual_metaphor="Show the journey from writing code to seeing results on screen",
                output_path="images/anime_book/02_program_execution.png",
                include_character=True
            )
        },
        {
            "num": 4,
            "type": "comic",
            "title": "Ch1: Why Python?",
            "generator": lambda: generator.generate_comic_panel_image(
                concept="Why Choose Python for AI Development?",
                dialogue_exchange=[
                    {"speaker": "Student", "text": "Why should I learn Python instead of other languages?", "expression": "confused"},
                    {"speaker": "Teacher", "text": "Python is the #1 language for AI and Machine Learning!", "expression": "confident"},
                    {"speaker": "Student", "text": "What makes it special?", "expression": "interested"},
                    {"speaker": "Teacher", "text": "Easy to learn, powerful libraries, and used by Google, OpenAI, Netflix!", "expression": "excited"}
                ],
                output_path="images/anime_book/03_why_python.png",
                panel_count=4
            )
        },
        {
            "num": 5,
            "type": "infographic",
            "title": "Ch1: Python Ecosystem",
            "generator": lambda: generator.generate_infographic_with_characters(
                topic="Python's AI/ML Ecosystem",
                key_points=[
                    "TensorFlow & PyTorch - Deep Learning",
                    "scikit-learn - Machine Learning",
                    "LangChain - AI Agents",
                    "Pandas & NumPy - Data Science",
                    "FastAPI - Modern APIs"
                ],
                output_path="images/anime_book/04_python_ecosystem.png"
            )
        },

        # Chapter 2: Variables and Data Types
        {
            "num": 6,
            "type": "comic",
            "title": "Ch2: Variables are References",
            "generator": lambda: generator.generate_comic_panel_image(
                concept="Variables are References, NOT Containers",
                dialogue_exchange=[
                    {"speaker": "Student", "text": "So variables store values like boxes?", "expression": "thinking"},
                    {"speaker": "Teacher", "text": "Common mistake! Variables are LABELS pointing to values!", "expression": "correcting"},
                    {"speaker": "Student", "text": "Wait, they don't CONTAIN the value?", "expression": "surprised"},
                    {"speaker": "Teacher", "text": "Nope! They're like name tags pointing to where the value lives in memory!", "expression": "teaching"}
                ],
                output_path="images/anime_book/05_variables_references.png",
                panel_count=4
            )
        },
        {
            "num": 7,
            "type": "concept",
            "title": "Ch2: Memory Visualization",
            "generator": lambda: generator.generate_concept_visualization(
                concept_title="How Variables Reference Memory",
                concept_description="Variable name → Memory address → Value object",
                visual_metaphor="Show variable as arrow/pointer to memory location containing value",
                output_path="images/anime_book/06_memory_references.png",
                include_character=True
            )
        },
        {
            "num": 8,
            "type": "infographic",
            "title": "Ch2: Python Data Types",
            "generator": lambda: generator.generate_infographic_with_characters(
                topic="Python's 5 Basic Data Types",
                key_points=[
                    "int - Whole numbers (42, -7, 0)",
                    "float - Decimals (3.14, -0.5)",
                    "str - Text ('hello', \"world\")",
                    "bool - True or False",
                    "None - Absence of value"
                ],
                output_path="images/anime_book/07_data_types.png"
            )
        },
        {
            "num": 9,
            "type": "comic",
            "title": "Ch2: Dynamic Typing",
            "generator": lambda: generator.generate_comic_panel_image(
                concept="Python's Dynamic Typing System",
                dialogue_exchange=[
                    {"speaker": "Student", "text": "Do I need to declare types like 'int x = 5'?", "expression": "questioning"},
                    {"speaker": "Teacher", "text": "Nope! Python figures it out automatically!", "expression": "cheerful"},
                    {"speaker": "Student", "text": "So I can just write x = 5?", "expression": "amazed"},
                    {"speaker": "Teacher", "text": "Exactly! That's dynamic typing - Python is smart!", "expression": "proud"}
                ],
                output_path="images/anime_book/08_dynamic_typing.png",
                panel_count=4
            )
        },
        {
            "num": 10,
            "type": "concept",
            "title": "Ch2: Type Conversion",
            "generator": lambda: generator.generate_concept_visualization(
                concept_title="Type Conversion Flow",
                concept_description="Converting between data types: str ↔ int ↔ float",
                visual_metaphor="Show transformation pipeline with int(), str(), float() functions",
                output_path="images/anime_book/09_type_conversion.png",
                include_character=True
            )
        },

        # Chapter 3: Data Structures
        {
            "num": 11,
            "type": "infographic",
            "title": "Ch3: Collections Overview",
            "generator": lambda: generator.generate_infographic_with_characters(
                topic="Python's 4 Collection Types",
                key_points=[
                    "LIST [1,2,3] - Ordered, mutable, allows duplicates",
                    "TUPLE (1,2,3) - Ordered, immutable, allows duplicates",
                    "DICT {'k':'v'} - Key-value pairs, mutable, unique keys",
                    "SET {1,2,3} - Unordered, mutable, unique values only"
                ],
                output_path="images/anime_book/10_collections_overview.png"
            )
        },
        {
            "num": 12,
            "type": "comic",
            "title": "Ch3: Lists vs Tuples",
            "generator": lambda: generator.generate_comparison_diagram(
                concept_a="LIST",
                concept_b="TUPLE",
                differences=[
                    {"aspect": "Syntax", "a": "[1, 2, 3]", "b": "(1, 2, 3)"},
                    {"aspect": "Mutability", "a": "Mutable (can change)", "b": "Immutable (fixed)"},
                    {"aspect": "Use Case", "a": "Dynamic data", "b": "Fixed data"},
                    {"aspect": "Performance", "a": "Slower", "b": "Faster"}
                ],
                output_path="images/anime_book/11_list_vs_tuple.png"
            )
        },
        {
            "num": 13,
            "type": "concept",
            "title": "Ch3: List Operations",
            "generator": lambda: generator.generate_concept_visualization(
                concept_title="Common List Operations",
                concept_description="append, insert, remove, index, slice operations",
                visual_metaphor="Show list transformations with before/after states",
                output_path="images/anime_book/12_list_operations.png",
                include_character=True
            )
        },
        {
            "num": 14,
            "type": "comic",
            "title": "Ch3: Dictionaries Explained",
            "generator": lambda: generator.generate_comic_panel_image(
                concept="Understanding Python Dictionaries",
                dialogue_exchange=[
                    {"speaker": "Student", "text": "What's a dictionary in Python?", "expression": "curious"},
                    {"speaker": "Teacher", "text": "It's like a real dictionary - word (key) to definition (value)!", "expression": "explaining"},
                    {"speaker": "Student", "text": "So {'name': 'Alice'} maps 'name' to 'Alice'?", "expression": "understanding"},
                    {"speaker": "Teacher", "text": "Perfect! Keys are unique, values can be anything!", "expression": "impressed"}
                ],
                output_path="images/anime_book/13_dictionaries.png",
                panel_count=4
            )
        },

        # -------------------------------------------------------------------------
        # PART II: MCP PROTOCOL
        # -------------------------------------------------------------------------

        {
            "num": 15,
            "type": "chapter_opener",
            "title": "Part II: MCP Protocol",
            "generator": lambda: generator.generate_chapter_opener(
                chapter_number=9,
                chapter_title="Introduction to MCP Protocol",
                chapter_description="Learn the revolutionary Model Context Protocol for AI integration",
                output_path="images/anime_book/14_mcp_intro.png"
            )
        },
        {
            "num": 16,
            "type": "comic",
            "title": "Ch9: What is MCP?",
            "generator": lambda: generator.generate_comic_panel_image(
                concept="Model Context Protocol (MCP) Explained",
                dialogue_exchange=[
                    {"speaker": "Student", "text": "What is this MCP everyone's talking about?", "expression": "confused"},
                    {"speaker": "Teacher", "text": "MCP is Anthropic's protocol for AI to talk to tools and data!", "expression": "enthusiastic"},
                    {"speaker": "Student", "text": "Like an API for AI models?", "expression": "thinking"},
                    {"speaker": "Teacher", "text": "Yes! It's the universal standard for AI integration!", "expression": "excited"}
                ],
                output_path="images/anime_book/15_what_is_mcp.png",
                panel_count=4
            )
        },
        {
            "num": 17,
            "type": "concept",
            "title": "Ch9: MCP Architecture",
            "generator": lambda: generator.generate_concept_visualization(
                concept_title="MCP Architecture: Client-Server Model",
                concept_description="AI Client ↔ MCP Protocol ↔ MCP Server ↔ Tools/Data Sources",
                visual_metaphor="Show communication flow between AI, MCP server, and various tools",
                output_path="images/anime_book/16_mcp_architecture.png",
                include_character=True
            )
        },
        {
            "num": 18,
            "type": "infographic",
            "title": "Ch9: MCP Core Concepts",
            "generator": lambda: generator.generate_infographic_with_characters(
                topic="MCP Protocol Core Components",
                key_points=[
                    "Tools - Actions AI can perform",
                    "Resources - Data AI can access",
                    "Prompts - Templates for AI interaction",
                    "Sampling - AI decision-making flow",
                    "Transports - Communication channels (stdio, HTTP)"
                ],
                output_path="images/anime_book/17_mcp_components.png"
            )
        },
        {
            "num": 19,
            "type": "comic",
            "title": "Ch10: MCP vs REST API",
            "generator": lambda: generator.generate_comparison_diagram(
                concept_a="Traditional REST API",
                concept_b="MCP Protocol",
                differences=[
                    {"aspect": "Purpose", "a": "General data exchange", "b": "AI-optimized integration"},
                    {"aspect": "Discovery", "a": "Manual docs", "b": "Automatic tool discovery"},
                    {"aspect": "Context", "a": "Stateless requests", "b": "Context-aware communication"},
                    {"aspect": "Complexity", "a": "Multiple endpoints", "b": "Unified protocol"}
                ],
                output_path="images/anime_book/18_mcp_vs_rest.png"
            )
        },
        {
            "num": 20,
            "type": "comic",
            "title": "Ch10: Building MCP Server",
            "generator": lambda: generator.generate_comic_panel_image(
                concept="Creating Your First MCP Server",
                dialogue_exchange=[
                    {"speaker": "Student", "text": "How do I build an MCP server?", "expression": "eager"},
                    {"speaker": "Teacher", "text": "We'll use FastMCP - it makes it super easy!", "expression": "confident"},
                    {"speaker": "Student", "text": "What's FastMCP?", "expression": "curious"},
                    {"speaker": "Teacher", "text": "A Python library that handles all the MCP complexity for you!", "expression": "teaching"}
                ],
                output_path="images/anime_book/19_building_mcp_server.png",
                panel_count=4
            )
        },
        {
            "num": 21,
            "type": "concept",
            "title": "Ch11: MCP Tools",
            "generator": lambda: generator.generate_concept_visualization(
                concept_title="Defining MCP Tools",
                concept_description="Tools are functions AI can call to perform actions",
                visual_metaphor="Show tool definition with @tool decorator, parameters, return values",
                output_path="images/anime_book/20_mcp_tools.png",
                include_character=True
            )
        },
        {
            "num": 22,
            "type": "comic",
            "title": "Ch12: MCP Resources",
            "generator": lambda: generator.generate_comic_panel_image(
                concept="MCP Resources: Providing Data to AI",
                dialogue_exchange=[
                    {"speaker": "Student", "text": "What's the difference between tools and resources?", "expression": "confused"},
                    {"speaker": "Teacher", "text": "Tools are ACTIONS, resources are DATA!", "expression": "clarifying"},
                    {"speaker": "Student", "text": "So resources are like files or databases?", "expression": "understanding"},
                    {"speaker": "Teacher", "text": "Exactly! Resources give AI access to information!", "expression": "pleased"}
                ],
                output_path="images/anime_book/21_mcp_resources.png",
                panel_count=4
            )
        },
        {
            "num": 23,
            "type": "infographic",
            "title": "Ch13: MCP Transports",
            "generator": lambda: generator.generate_infographic_with_characters(
                topic="MCP Transport Mechanisms",
                key_points=[
                    "stdio - Standard input/output (local)",
                    "HTTP/SSE - Server-Sent Events (remote)",
                    "WebSocket - Real-time bidirectional",
                    "Each transport has different use cases",
                    "FastMCP handles transport complexity"
                ],
                output_path="images/anime_book/22_mcp_transports.png"
            )
        },

        # -------------------------------------------------------------------------
        # PART III: AI AGENTS
        # -------------------------------------------------------------------------

        {
            "num": 24,
            "type": "chapter_opener",
            "title": "Part III: AI Agents",
            "generator": lambda: generator.generate_chapter_opener(
                chapter_number=17,
                chapter_title="Introduction to AI Agents",
                chapter_description="Build intelligent autonomous agents with LangChain and LangGraph",
                output_path="images/anime_book/23_agents_intro.png"
            )
        },
        {
            "num": 25,
            "type": "comic",
            "title": "Ch17: What are AI Agents?",
            "generator": lambda: generator.generate_comic_panel_image(
                concept="Understanding AI Agents",
                dialogue_exchange=[
                    {"speaker": "Student", "text": "What's an AI agent?", "expression": "curious"},
                    {"speaker": "Teacher", "text": "An AI that can THINK and ACT autonomously!", "expression": "excited"},
                    {"speaker": "Student", "text": "Like a robot assistant?", "expression": "amazed"},
                    {"speaker": "Teacher", "text": "Yes! It can use tools, make decisions, and complete tasks!", "expression": "proud"}
                ],
                output_path="images/anime_book/24_what_are_agents.png",
                panel_count=4
            )
        },
        {
            "num": 26,
            "type": "concept",
            "title": "Ch17: Agent Loop",
            "generator": lambda: generator.generate_concept_visualization(
                concept_title="The Agent Decision Loop",
                concept_description="Observe → Think → Act → Repeat",
                visual_metaphor="Show circular flow: perception → reasoning → action → feedback",
                output_path="images/anime_book/25_agent_loop.png",
                include_character=True
            )
        },
        {
            "num": 27,
            "type": "infographic",
            "title": "Ch18: LangChain Overview",
            "generator": lambda: generator.generate_infographic_with_characters(
                topic="LangChain Framework Components",
                key_points=[
                    "LLMs - Language models (GPT, Claude, etc.)",
                    "Chains - Sequences of operations",
                    "Agents - Autonomous decision makers",
                    "Tools - Functions agents can use",
                    "Memory - Context persistence"
                ],
                output_path="images/anime_book/26_langchain_overview.png"
            )
        },
        {
            "num": 28,
            "type": "comic",
            "title": "Ch19: ReAct Pattern",
            "generator": lambda: generator.generate_comic_panel_image(
                concept="ReAct: Reasoning + Acting",
                dialogue_exchange=[
                    {"speaker": "Student", "text": "How does an agent decide what to do?", "expression": "questioning"},
                    {"speaker": "Teacher", "text": "It uses ReAct - Reasoning AND Acting together!", "expression": "teaching"},
                    {"speaker": "Student", "text": "So it thinks out loud before acting?", "expression": "realizing"},
                    {"speaker": "Teacher", "text": "Perfect! It explains its reasoning, then acts!", "expression": "impressed"}
                ],
                output_path="images/anime_book/27_react_pattern.png",
                panel_count=4
            )
        },
        {
            "num": 29,
            "type": "concept",
            "title": "Ch20: LangGraph",
            "generator": lambda: generator.generate_concept_visualization(
                concept_title="LangGraph State Machines",
                concept_description="Build complex agent workflows as graphs",
                visual_metaphor="Show nodes (states) and edges (transitions) in agent workflow",
                output_path="images/anime_book/28_langgraph.png",
                include_character=True
            )
        },
        {
            "num": 30,
            "type": "comparison",
            "title": "Ch20: Agent Architectures",
            "generator": lambda: generator.generate_comparison_diagram(
                concept_a="Single Agent",
                concept_b="Multi-Agent System",
                differences=[
                    {"aspect": "Complexity", "a": "Simple, one decision maker", "b": "Complex, multiple agents"},
                    {"aspect": "Capabilities", "a": "Limited to one perspective", "b": "Diverse perspectives"},
                    {"aspect": "Scalability", "a": "Limited scope", "b": "Highly scalable"},
                    {"aspect": "Use Case", "a": "Focused tasks", "b": "Complex workflows"}
                ],
                output_path="images/anime_book/29_agent_architectures.png"
            )
        },

        # -------------------------------------------------------------------------
        # PART IV: MLFLOW
        # -------------------------------------------------------------------------

        {
            "num": 31,
            "type": "chapter_opener",
            "title": "Part IV: MLflow",
            "generator": lambda: generator.generate_chapter_opener(
                chapter_number=25,
                chapter_title="Experiment Tracking with MLflow",
                chapter_description="Track, manage, and deploy machine learning experiments",
                output_path="images/anime_book/30_mlflow_intro.png"
            )
        },
        {
            "num": 32,
            "type": "comic",
            "title": "Ch25: Why MLflow?",
            "generator": lambda: generator.generate_comic_panel_image(
                concept="The Need for Experiment Tracking",
                dialogue_exchange=[
                    {"speaker": "Student", "text": "Why do I need MLflow? Can't I just train models?", "expression": "questioning"},
                    {"speaker": "Teacher", "text": "Without tracking, you'll lose your best models!", "expression": "warning"},
                    {"speaker": "Student", "text": "Really? Even with good code?", "expression": "worried"},
                    {"speaker": "Teacher", "text": "Yes! MLflow tracks EVERYTHING - params, metrics, models!", "expression": "reassuring"}
                ],
                output_path="images/anime_book/31_why_mlflow.png",
                panel_count=4
            )
        },
        {
            "num": 33,
            "type": "infographic",
            "title": "Ch25: MLflow Components",
            "generator": lambda: generator.generate_infographic_with_characters(
                topic="MLflow Platform Components",
                key_points=[
                    "Tracking - Log parameters, metrics, artifacts",
                    "Projects - Package code reproducibly",
                    "Models - Standardize model format",
                    "Registry - Manage model lifecycle",
                    "UI - Visual experiment comparison"
                ],
                output_path="images/anime_book/32_mlflow_components.png"
            )
        },
        {
            "num": 34,
            "type": "concept",
            "title": "Ch26: Experiment Tracking",
            "generator": lambda: generator.generate_concept_visualization(
                concept_title="MLflow Experiment Tracking Flow",
                concept_description="Log params → Train model → Log metrics → Save artifacts",
                visual_metaphor="Show flow from experiment setup to model registry",
                output_path="images/anime_book/33_experiment_tracking.png",
                include_character=True
            )
        },
        {
            "num": 35,
            "type": "comic",
            "title": "Ch27: Model Registry",
            "generator": lambda: generator.generate_comic_panel_image(
                concept="MLflow Model Registry Lifecycle",
                dialogue_exchange=[
                    {"speaker": "Student", "text": "How do I manage different versions of my model?", "expression": "overwhelmed"},
                    {"speaker": "Teacher", "text": "Use MLflow Model Registry - it's like Git for models!", "expression": "helpful"},
                    {"speaker": "Student", "text": "Can I stage models for testing?", "expression": "interested"},
                    {"speaker": "Teacher", "text": "Yes! Staging, Production, Archived - full lifecycle!", "expression": "enthusiastic"}
                ],
                output_path="images/anime_book/34_model_registry.png",
                panel_count=4
            )
        },

        # -------------------------------------------------------------------------
        # PART V: A.A.STUDIO
        # -------------------------------------------------------------------------

        {
            "num": 36,
            "type": "chapter_opener",
            "title": "Part V: A.A.Studio Platform",
            "generator": lambda: generator.generate_chapter_opener(
                chapter_number=31,
                chapter_title="A.A.Studio Enterprise Platform",
                chapter_description="Enterprise-grade AI development and deployment platform",
                output_path="images/anime_book/35_aastudio_intro.png"
            )
        },
        {
            "num": 37,
            "type": "comic",
            "title": "Ch31: What is A.A.Studio?",
            "generator": lambda: generator.generate_comic_panel_image(
                concept="Introduction to A.A.Studio Platform",
                dialogue_exchange=[
                    {"speaker": "Student", "text": "What is A.A.Studio?", "expression": "curious"},
                    {"speaker": "Teacher", "text": "It's an enterprise platform for building AI agents at scale!", "expression": "excited"},
                    {"speaker": "Student", "text": "Like a complete AI development environment?", "expression": "understanding"},
                    {"speaker": "Teacher", "text": "Exactly! Build, deploy, monitor - everything in one place!", "expression": "proud"}
                ],
                output_path="images/anime_book/36_what_is_aastudio.png",
                panel_count=4
            )
        },
        {
            "num": 38,
            "type": "infographic",
            "title": "Ch31: A.A.Studio Features",
            "generator": lambda: generator.generate_infographic_with_characters(
                topic="A.A.Studio Platform Capabilities",
                key_points=[
                    "Visual Agent Builder - No-code interface",
                    "Multi-Agent Orchestration - Complex workflows",
                    "Enterprise Security - SOC2, HIPAA compliance",
                    "Monitoring & Analytics - Real-time insights",
                    "Integration Hub - Connect any tool or API"
                ],
                output_path="images/anime_book/37_aastudio_features.png"
            )
        },
        {
            "num": 39,
            "type": "concept",
            "title": "Ch32: A.A.Studio Architecture",
            "generator": lambda: generator.generate_concept_visualization(
                concept_title="A.A.Studio Platform Architecture",
                concept_description="UI Layer → API Gateway → Agent Runtime → Tool Integrations",
                visual_metaphor="Show layered architecture from user interface to backend services",
                output_path="images/anime_book/38_aastudio_architecture.png",
                include_character=True
            )
        },

        # -------------------------------------------------------------------------
        # FINAL PAGES
        # -------------------------------------------------------------------------

        {
            "num": 40,
            "type": "infographic",
            "title": "Learning Path Summary",
            "generator": lambda: generator.generate_infographic_with_characters(
                topic="Your Complete AI Engineering Journey",
                key_points=[
                    "✅ Python fundamentals mastered",
                    "✅ MCP protocol expertise gained",
                    "✅ AI agents built and deployed",
                    "✅ MLflow experiment tracking learned",
                    "✅ A.A.Studio platform proficiency",
                    "🎉 Ready for OpenAI/Anthropic interviews!"
                ],
                output_path="images/anime_book/39_learning_summary.png"
            )
        },
        {
            "num": 41,
            "type": "end_page",
            "title": "Thank You Page",
            "generator": lambda: generator.generate_concept_visualization(
                concept_title="Thank You for Learning with Us!",
                concept_description="You've completed the ultimate AI development journey",
                visual_metaphor="Anime characters celebrating completion with confetti",
                output_path="images/anime_book/40_thank_you.png",
                include_character=True
            )
        }
    ]

    # =============================================================================
    # GENERATION LOOP - DO NOT STOP!
    # =============================================================================

    total = len(all_images)

    for img_spec in all_images:
        num = img_spec['num']
        title = img_spec['title']
        img_type = img_spec['type']

        print(f"\n{'='*100}")
        print(f"🎨 IMAGE {num}/{total}: {title} [{img_type.upper()}]")
        print(f"{'='*100}")

        # Check if exists
        # We regenerate anyway for consistency

        result = generate_with_retry(img_spec['generator'], max_retries=3)

        if result:
            print(f"   ✅ COMPLETED: {title}")
            successful.append((num, title, result))
        else:
            print(f"   ❌ FAILED: {title}")
            failed.append((num, title))

        # Wait between images to avoid rate limits
        if num < total:
            wait_between_images(7)

    # =============================================================================
    # FINAL REPORT
    # =============================================================================

    print("\n\n" + "="*100)
    print("📊 FINAL GENERATION REPORT")
    print("="*100)

    print(f"\n✅ SUCCESSFUL: {len(successful)}/{total} images")
    for num, title, path in successful:
        print(f"   {num:3d}. {title}")
        print(f"        → {path}")

    if failed:
        print(f"\n❌ FAILED: {len(failed)}/{total} images")
        for num, title in failed:
            print(f"   {num:3d}. {title}")
        print("\n⚠️  You may need to regenerate failed images manually")
    else:
        print(f"\n🎉 🎉 🎉  100% COMPLETE!  🎉 🎉 🎉")
        print("All anime-style educational images generated successfully!")

    print("\n" + "="*100)

    return len(successful) == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
