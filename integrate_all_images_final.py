#!/usr/bin/env python3
"""
FINAL IMAGE INTEGRATION SCRIPT
Integrates ALL generated anime images into the book with proper placement
"""

import re
from pathlib import Path

def integrate_all_anime_images(input_file: str, output_file: str):
    """Integrate all 41 anime images into appropriate locations"""

    print("📚 Reading enhanced book...")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    print("🎨 Integrating ALL anime images...")

    # Image placements mapped to book sections
    image_integrations = [
        # Cover
        ("![Book Cover](images/anime_book/00_cover.png)", 0, "# 🚀 The Ultimate Guide"),

        # Chapter 1
        ("![What is Programming?](images/anime_book/01_what_is_programming.png)\n\n", "## 1.1 What is Programming?"),
        ("![Program Execution Flow](images/anime_book/02_program_execution.png)\n\n", "### Components of a Program"),
        ("![Why Python?](images/anime_book/03_why_python.png)\n\n", "## 1.2 What is Python?"),
        ("![Python Ecosystem](images/anime_book/04_python_ecosystem.png)\n\n", "### Python Characteristics"),

        # Chapter 2
        ("![Variables are References](images/anime_book/05_variables_references.png)\n\n", "# Chapter 2: Variables and Data Types"),
        ("![Memory References](images/anime_book/06_memory_references.png)\n\n", "## 2.1 Variables: References, Not Containers"),
        ("![Data Types](images/anime_book/07_data_types.png)\n\n", "## 2.2 Data Types"),
        ("![Dynamic Typing](images/anime_book/08_dynamic_typing.png)\n\n", "### Dynamic Typing"),
        ("![Type Conversion](images/anime_book/09_type_conversion.png)\n\n", "## 2.3 Type Conversion"),

        # Chapter 3
        ("![Collections Overview](images/anime_book/10_collections_overview.png)\n\n", "# Chapter 3: Data Structures"),
        ("![List vs Tuple](images/anime_book/11_list_vs_tuple.png)\n\n", "## 3.2 Tuples"),
        ("![List Operations](images/anime_book/12_list_operations.png)\n\n", "## 3.1 Lists"),
        ("![Dictionaries](images/anime_book/13_dictionaries.png)\n\n", "## 3.3 Dictionaries"),

        # MCP Protocol (Part II)
        ("![MCP Introduction](images/anime_book/14_mcp_intro.png)\n\n", "# PART II: MCP PROTOCOL"),
        ("![What is MCP?](images/anime_book/15_what_is_mcp.png)\n\n", "# Chapter 9: Understanding MCP Protocol"),
        ("![MCP Architecture](images/anime_book/16_mcp_architecture.png)\n\n", "## 9.1 MCP Architecture"),
        ("![MCP Components](images/anime_book/17_mcp_components.png)\n\n", "## 9.2 Core Concepts"),
        ("![MCP vs REST](images/anime_book/18_mcp_vs_rest.png)\n\n", "## 9.3 Why MCP?"),
        ("![Building MCP Server](images/anime_book/19_building_mcp_server.png)\n\n", "# Chapter 10: Building MCP Servers"),
        ("![MCP Tools](images/anime_book/20_mcp_tools.png)\n\n", "## 10.1 Defining Tools"),
        ("![MCP Resources](images/anime_book/21_mcp_resources.png)\n\n", "## 10.2 Resources"),
        ("![MCP Transports](images/anime_book/22_mcp_transports.png)\n\n", "## 10.3 Transports"),

        # AI Agents (Part III)
        ("![AI Agents Introduction](images/anime_book/23_agents_intro.png)\n\n", "# PART III: AI AGENTS"),
        ("![What are AI Agents?](images/anime_book/24_what_are_agents.png)\n\n", "# Chapter 17: Introduction to AI Agents"),
        ("![Agent Loop](images/anime_book/25_agent_loop.png)\n\n", "## 17.1 Agent Architecture"),
        ("![LangChain Overview](images/anime_book/26_langchain_overview.png)\n\n", "# Chapter 18: LangChain Framework"),
        ("![ReAct Pattern](images/anime_book/27_react_pattern.png)\n\n", "## 18.2 ReAct Pattern"),
        ("![LangGraph](images/anime_book/28_langgraph.png)\n\n", "# Chapter 19: LangGraph"),
        ("![Agent Architectures](images/anime_book/29_agent_architectures.png)\n\n", "## 19.2 Multi-Agent Systems"),

        # MLflow (Part IV)
        ("![MLflow Introduction](images/anime_book/30_mlflow_intro.png)\n\n", "# PART IV: MLFLOW"),
        ("![Why MLflow?](images/anime_book/31_why_mlflow.png)\n\n", "# Chapter 25: Experiment Tracking"),
        ("![MLflow Components](images/anime_book/32_mlflow_components.png)\n\n", "## 25.1 MLflow Platform"),
        ("![Experiment Tracking](images/anime_book/33_experiment_tracking.png)\n\n", "## 25.2 Tracking Experiments"),
        ("![Model Registry](images/anime_book/34_model_registry.png)\n\n", "## 25.3 Model Registry"),

        # A.A.Studio (Part V)
        ("![A.A.Studio Introduction](images/anime_book/35_aastudio_intro.png)\n\n", "# PART V: A.A.STUDIO"),
        ("![What is A.A.Studio?](images/anime_book/36_what_is_aastudio.png)\n\n", "# Chapter 31: A.A.Studio Platform"),
        ("![A.A.Studio Features](images/anime_book/37_aastudio_features.png)\n\n", "## 31.1 Platform Overview"),
        ("![A.A.Studio Architecture](images/anime_book/38_aastudio_architecture.png)\n\n", "## 31.2 Architecture"),

        # Conclusion
        ("![Learning Summary](images/anime_book/39_learning_summary.png)\n\n", "# Conclusion"),
        ("![Thank You](images/anime_book/40_thank_you.png)\n\n", "## Congratulations!"),
    ]

    # Process each image integration
    integrated_count = 0
    for img_info in image_integrations:
        if len(img_info) == 2:
            image_md, section_heading = img_info
        else:
            image_md, position, section_heading = img_info

        # Find the section and add image after it
        if section_heading in content:
            # Add image right after the heading
            content = content.replace(
                section_heading,
                section_heading + "\n\n" + image_md,
                1  # Only replace first occurrence
            )
            integrated_count += 1
            print(f"   ✅ Integrated image for: {section_heading}")
        else:
            print(f"   ⚠️  Section not found: {section_heading}")

    print(f"\n✨ Integrated {integrated_count} images")

    print("💾 Saving final book...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ Final book saved: {output_file}")

    # Statistics
    lines = len(content.split('\n'))
    words = len(content.split())
    images = content.count('![')

    print(f"\n📊 Final Statistics:")
    print(f"   Lines: {lines:,}")
    print(f"   Words: {words:,}")
    print(f"   Characters: {len(content):,}")
    print(f"   Images: {images}")

    return output_file

if __name__ == "__main__":
    integrate_all_anime_images(
        "THE_ULTIMATE_AI_DEVELOPMENT_GUIDE_ANIME_FINAL.md",
        "THE_ULTIMATE_AI_DEVELOPMENT_GUIDE_WITH_ANIME_COMPLETE.md"
    )
