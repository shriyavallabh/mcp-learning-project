# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Repository Overview

This is a **personal MCP (Model Context Protocol) learning repository** containing:
- **8 comprehensive MCP tutorial chapters** (beginner to advanced)
- **IntelligentScan** - Production-ready MCP server for code analysis
- **BMad Method** - AI-driven agile development framework
- **Python automation scripts** - Image generation and PDF creation tools
- **Enterprise learning materials** - Notes from Infosys Agentic Foundry

**Learning Context**: The repository owner is learning Python, MCP, and AI agent development with limited Python experience. ALL code explanations must be extremely detailed, explaining every line, every syntax element, and every concept.

---

## Key Projects

### 1. IntelligentScan (`intelligentscan/`)

A production-grade MCP server for AI-powered code intelligence.

**Architecture**:
- FastMCP server exposing 5 MCP tools
- Multi-modal scanning (vulnerabilities, ARB compliance, AI-readiness)
- Knowledge graph generation with NetworkX
- Designed for Claude Desktop, VS Code, and CI/CD integration

**Tech Stack**:
- FastMCP for MCP server
- LangGraph for multi-agent orchestration
- Qdrant (vector DB), Redis (cache), PostgreSQL (persistence)
- Python AST + tree-sitter for code analysis

**Development Commands**:

```bash
# Local development with Docker Compose
cd intelligentscan
docker-compose up -d

# Install dependencies
pip install -r requirements.txt

# Run MCP server directly
python -m intelligentscan.server.main

# Test individual scanners
python -m intelligentscan.scanners.vulnerability_scanner
```

**Deployment**:

```bash
# Docker build
docker build -t intelligentscan:latest .

# Deploy to Azure AKS
az acr build --registry <your-registry> --image intelligentscan:latest .
kubectl apply -f deployment.yml

# Verify deployment
kubectl get pods -n intelligentscan
kubectl get hpa -n intelligentscan
```

**Key Files**:
- `server/main.py` - FastMCP server with tool definitions (lines 58-385 define MCP tools)
- `docker-compose.yml` - Local dev environment (Redis, PostgreSQL, Qdrant)
- `deployment.yml` - Kubernetes manifests for AKS (auto-scales 3-20 replicas)
- `requirements.txt` - Python dependencies

### 2. BMad Method (`.bmad-core/`, `.claude/commands/BMad/`)

An AI-driven agile development framework with predefined agents and workflows.

**Components**:
- **Agents**: Analyst, Architect, PM, PO, QA, Dev, SM, UX Expert (10 agents)
- **Workflows**: Greenfield/brownfield, fullstack/service/UI variants
- **Templates**: PRD, architecture, story, QA gate, etc.
- **Checklists**: Quality gates for each development phase

**Configuration**: `.bmad-core/core-config.yaml`
- PRD location: `docs/prd.md`
- Architecture: `docs/architecture.md`
- Stories: `docs/stories/`
- Slash command prefix: `BMad`

**Usage**:
- BMad commands are available as Claude Code slash commands (e.g., `/BMad/agents/dev`)
- Follows structured planning workflow (see `.bmad-core/user-guide.md`)
- Supports both greenfield and brownfield projects

### 3. Python Automation Scripts (root directory)

**Image Generation**:
- `image_generator.py` - Gemini API image generator class
- `generate_all_book_images.py` - Batch image generation
- Uses Google Gemini 2.5 Flash Image model

**PDF Generation**:
- `generate_premium_final_pdf.py` - PDF book creation
- `complete_book_automation.py` - End-to-end book pipeline
- Multiple variants for different book formats

**Common Pattern**:
```python
# Most scripts follow this pattern:
from google import genai  # Gemini API
from PIL import Image     # Image processing

# Initialize Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Generate content...
```

---

## Development Workflows

### Working with IntelligentScan

1. **Adding a new MCP tool**:
   - Add `@mcp.tool()` decorated function in `server/main.py`
   - Tools are automatically exposed via MCP protocol
   - Example: `scan_vulnerabilities()` at line 58

2. **Adding a new scanner**:
   - Create new scanner in `scanners/` directory
   - Follow pattern from `vulnerability_scanner.py`
   - Scanner must have async `scan()` method
   - Import and use in MCP tool functions

3. **Testing MCP server**:
   - Configure Claude Desktop MCP settings:
     ```json
     {
       "mcpServers": {
         "intelligentscan": {
           "command": "python",
           "args": ["-m", "intelligentscan.server.main"],
           "cwd": "/Users/shriyavallabhvidyadharpethkar/Desktop/mcp/intelligentscan"
         }
       }
     }
     ```

### Working with Python Scripts

**Environment Setup**:
```bash
# Virtual environment (if pdf_env/ exists)
source pdf_env/bin/activate

# Install dependencies for image generation
pip install google-genai pillow

# Set API key
export GEMINI_API_KEY="your-key-here"
```

**Running Scripts**:
```bash
# Image generation
python image_generator.py

# PDF generation
python generate_premium_final_pdf.py
```

### Git Workflow

```bash
# Update repository
git add .
git commit -m "Your detailed message"
git push

# Pull latest changes
git pull
```

---

## Important Python Explanation Requirements

**CRITICAL**: When explaining Python code to the user, you MUST:

1. **Explain EVERY line in extreme detail**
2. **Identify what each element is**:
   - Variable (storing data)
   - Class (blueprint for objects)
   - Object (instance of a class)
   - Function (reusable code block)
   - Method (function inside a class)
   - Decorator (@ symbol - modifies functions)
   - Loop (repeating code)
   - Module import (bringing in external code)

3. **For variable names**: Explain they're just labels
   - `client = MCP_Client()` means "client" is our chosen name to store the MCP_Client object
   - Could have been `my_connection` or `mcp` or `x`

4. **Be EXTREMELY verbose about**:
   - Parentheses meaning
   - Dot notation (object.method)
   - Brackets
   - Quotes (string vs variable)
   - Indentation (code blocks)

**Example Explanation Format**:
```python
client = MCP_Client("localhost:5000")
```
Explain as:
- `client` = VARIABLE NAME (just a label, like naming a pet)
- `=` = Assignment operator (puts something into the variable)
- `MCP_Client` = CLASS (blueprint/template)
- `()` = Parentheses mean we're CREATING an object from the class
- `"localhost:5000"` = String parameter - quotes make it text, not code
- **Whole line**: Creates new MCP_Client object and stores it in variable named "client"

---

## MCP (Model Context Protocol) Concepts

### Key Concepts to Explain

1. **Complete MCP interaction cycle** with detailed diagrams
2. **Tool discovery**: How client discovers which of 20 tools to use
3. **Resource definitions vs tool definitions**
4. **FastMCP library usage**
5. **MCP-O**: OpenAPI to MCP proxy converter
6. **Streamable MCP server** on AKS
7. **Agent-to-agent protocol**
8. **MCP server invoking agents**

### Critical Clarifications

- **MCP servers do NOT contain LLMs** (usually)
- **LLM is typically the CLIENT**, not part of server
- **Non-deterministic responses** come from LLM client, not MCP server
- **MCP server responses are deterministic** (same input = same output)
- **Dockerfile vs Docker image**: Dockerfile is blueprint (recipe), Docker image is built artifact (cake)

### IntelligentScan MCP Tools

The server exposes these tools (defined in `server/main.py`):

1. `scan_vulnerabilities(repo_path, vulnerability_types)` - Security scanning
2. `check_arb_compliance(repo_path, arb_rules)` - ARB compliance checking
3. `scan_ai_readiness(repo_path, include_suggestions)` - AI-readiness analysis
4. `generate_report(scan_id, format)` - Report generation
5. `scan_by_prompt(prompt)` - Natural language scanning interface

**Resources** (read-only data):
- `scan://sessions` - Active scan sessions
- `report://latest` - Latest scan report
- `graph://knowledge-graph/{scan_id}` - Knowledge graph visualization

---

## File Structure

```
mcp/
├── intelligentscan/           # MCP server project
│   ├── server/main.py        # FastMCP server (MCP tool definitions)
│   ├── scanners/             # Code analysis scanners
│   ├── config/rules.yaml     # Scanning rules configuration
│   ├── requirements.txt      # Python dependencies
│   ├── Dockerfile            # Container blueprint
│   ├── docker-compose.yml    # Local dev environment
│   └── deployment.yml        # Kubernetes manifests for AKS
│
├── .bmad-core/               # BMad Method framework
│   ├── agents/               # Agent definitions (10 agents)
│   ├── workflows/            # Development workflows (6 workflows)
│   ├── templates/            # Document templates
│   ├── tasks/                # Agent task definitions
│   └── core-config.yaml      # BMad configuration
│
├── .claude/commands/BMad/    # Claude Code slash commands
│   ├── agents/               # Mirrored agent definitions
│   └── tasks/                # Mirrored task definitions
│
├── MCP_Complete_Tutorial_Chapter_*.md  # 8 tutorial chapters
│
├── *.py                      # Python automation scripts
│   ├── image_generator.py    # Gemini image generation
│   ├── generate_*_pdf.py     # PDF generation scripts
│   └── *_book_*.py          # Book creation automation
│
└── CLAUDE.md                 # This file
```

---

## Common Tasks

### Test IntelligentScan MCP Server

```bash
cd intelligentscan
python -m intelligentscan.server.main
```

### Run Docker Environment

```bash
cd intelligentscan
docker-compose up -d          # Start all services
docker-compose logs -f        # View logs
docker-compose down           # Stop services
```

### Deploy to Azure AKS

```bash
# Build and push to ACR
cd intelligentscan
az acr build --registry <registry-name> \
  --image intelligentscan:latest \
  --file Dockerfile .

# Update deployment.yml with ACR image path
# Then deploy:
kubectl apply -f deployment.yml

# Monitor deployment
kubectl get pods -n intelligentscan -w
kubectl logs -f deployment/intelligentscan-server -n intelligentscan
```

### Generate Images with Gemini

```bash
# Set API key
export GEMINI_API_KEY="your-api-key"

# Run generator
python image_generator.py
```

---

## Learning Resources

**Tutorial Chapters** (Read in order):
1. `MCP_Complete_Tutorial_Chapter_1.md` - Introduction to MCP
2. `MCP_Complete_Tutorial_Chapter_2.md` - Client-Server Architecture
3. `MCP_Complete_Tutorial_Chapter_3.md` - Python Basics
4. `MCP_Complete_Tutorial_Chapter_4.md` - MCP Interaction Cycle
5. `MCP_Complete_Tutorial_Chapter_5.md` - Infrastructure Concepts
6. `MCP_Complete_Tutorial_Chapter_6.md` - FastAPI and Pydantic
7. `MCP_Complete_Tutorial_Chapter_7.md` - JSON-RPC Protocol
8. `MCP_Complete_Tutorial_Chapter_8.md` - Ace Studio Tutorial

**Enterprise Learning**:
- `AGENTIC_FOUNDRY_COMPLETE_NOTES.md` - Infosys platform notes
- `AGENTIC_FOUNDRY_SUMMARY.md` - Platform summary
- `ACE_STUDIO_COMPLETE_TUTORIAL.md` - Ace Studio guide

**Access Guides**:
- `MOBILE_ACCESS_GUIDE.md` - How to access repo from phone
- `QUICK_START_MOBILE_ACCESS.md` - 5-minute setup
- `CRASH_FIX_GUIDE.md` - Troubleshooting

---

## Technical Preferences

### Infrastructure
- **Container Platform**: Docker + Kubernetes (AKS)
- **Orchestration**: Kubernetes with HPA (3-20 replicas)
- **Caching**: Redis
- **Database**: PostgreSQL
- **Vector DB**: Qdrant

### Python
- **Python Version**: 3.13
- **MCP Framework**: FastMCP
- **Agent Framework**: LangGraph
- **Code Analysis**: Python AST + tree-sitter
- **API Framework**: FastAPI
- **Async**: async/await patterns throughout

### API Keys (Environment Variables)
- `GEMINI_API_KEY` - For image generation
- `OPENAI_API_KEY` - For LLM integration
- `ANTHROPIC_API_KEY` - For Claude integration

---

## Repository Status

**Last Updated**: 2025-10-13
**Current Branch**: main
**Status**: Active Learning Journey

**Progress**:
- ✅ 8 MCP tutorial chapters completed
- ✅ IntelligentScan MVP (MCP server, Docker, Kubernetes)
- ✅ BMad Method framework integrated
- 🔄 Building real MCP servers
- 🔄 Deploying to Azure AKS
- 🔄 Enterprise AI agent implementation

**Next Goals**:
1. Deploy first MCP server to production
2. Build enterprise AI agent
3. Implement at office (Infosys project)
4. Create advanced AI systems

---

## Notes for AI Assistants

- **User has limited Python knowledge** - Explain everything in extreme detail
- **User learns best with diagrams** - Use visual representations when possible
- **User needs to understand WHY, not just HOW** - Explain reasoning and concepts
- **User wants to implement at office** - Focus on production-ready, enterprise patterns
- **User is actively learning** - Be patient, thorough, and educational

When explaining code:
1. Start with high-level "what this code does"
2. Break down line-by-line with extreme detail
3. Explain every syntax element (dots, parentheses, brackets, quotes)
4. Clarify variable names are just labels
5. Show practical examples and diagrams
6. Connect to real-world use cases
