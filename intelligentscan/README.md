# IntelligentScan

**AI-Powered Code Intelligence Platform**

IntelligentScan is a comprehensive code analysis platform that scans codebases for:
- 🔒 **Security Vulnerabilities** (Log4j, hardcoded secrets, SQL injection, etc.)
- 📋 **ARB Compliance** (Architectural Review Board guidelines)
- 🤖 **AI-Readiness** (How well AI tools can understand your code)

Built on the **MCP (Model Context Protocol)** for maximum flexibility and scalability.

---

## 🌟 Key Features

### Multi-Modal Scanning
- **Vulnerability Detection**: Pattern matching + AST analysis + LLM verification
- **ARB Compliance**: Automated checking against organizational guidelines
- **AI-Readiness Analysis**: Identifies code that's hard for AI tools to understand

### Knowledge Graph Visualization
- Red/green color-coded nodes show problem areas
- Interactive graph showing file relationships and violations
- Export to JSON, GraphML, or GEXF formats

### Multi-Interface Support
- **MCP Server**: Works with Claude Desktop, VS Code, CI/CD pipelines
- **Web Dashboard**: Management interface (coming soon)
- **CLI Tool**: Command-line interface
- **Prompt-Driven**: Natural language scanning requests

### Enterprise-Ready
- Kubernetes deployment on Azure AKS
- Horizontal auto-scaling (3-20 pods)
- Redis caching for performance
- PostgreSQL for scan history
- Vector database (Qdrant) for RAG

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Docker & Docker Compose (for local development)
- Azure AKS (for production deployment)

### Local Development Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd intelligentscan
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run with Docker Compose**
```bash
docker-compose up -d
```

This starts:
- IntelligentScan MCP Server (port 8000)
- Redis (port 6379)
- PostgreSQL (port 5432)
- Qdrant vector database (port 6333)

4. **Test the server**
```bash
# Run a simple vulnerability scan
python -m intelligentscan.scanners.vulnerability_scanner
```

---

## 📖 Usage

### Using as MCP Server with Claude Desktop

1. **Configure Claude Desktop**

Add to your Claude Desktop MCP settings:
```json
{
  "mcpServers": {
    "intelligentscan": {
      "command": "python",
      "args": ["-m", "intelligentscan.server.main"],
      "cwd": "/path/to/intelligentscan"
    }
  }
}
```

2. **Use in Claude Desktop**

```
You: Scan ./my-project for vulnerabilities

Claude: *Uses scan_vulnerabilities tool*
Found 3 critical vulnerabilities:
1. Hardcoded API key in auth/login.py:42
2. SQL injection risk in db/queries.py:89
3. Log4j vulnerability in pom.xml
```

### Using the API Directly

```python
from intelligentscan.scanners.vulnerability_scanner import VulnerabilityScanner

scanner = VulnerabilityScanner("/path/to/repository")
results = await scanner.scan()

print(f"Found {len(results['vulnerabilities_found'])} vulnerabilities")
for vuln in results['vulnerabilities_found']:
    print(f"[{vuln['severity']}] {vuln['description']} at {vuln['file']}:{vuln['line']}")
```

### Natural Language Interface

```python
# Prompt-driven scanning
result = await scan_by_prompt("Check if my auth module has log4j vulnerability")
```

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────┐
│          IntelligentScan MCP Server         │
├─────────────────────────────────────────────┤
│ Tools:                                      │
│  - scan_vulnerabilities()                   │
│  - check_arb_compliance()                   │
│  - scan_ai_readiness()                      │
│  - generate_report()                        │
│  - scan_by_prompt()                         │
├─────────────────────────────────────────────┤
│ Scanners:                                   │
│  - VulnerabilityScanner (regex + AST)       │
│  - ARBScanner (rule engine)                 │
│  - AIReadinessScanner (confidence analysis) │
└─────────────────────────────────────────────┘
         ↕️ MCP Protocol
┌─────────────────────────────────────────────┐
│      Clients:                               │
│  • Claude Desktop                           │
│  • VS Code (via MCP extension)              │
│  • Custom Web UI                            │
│  • CI/CD Pipeline                           │
└─────────────────────────────────────────────┘
```

### Technology Stack
- **MCP Server**: FastMCP
- **Agent Framework**: LangGraph (coming soon)
- **Vector DB**: Qdrant
- **Cache**: Redis
- **Database**: PostgreSQL
- **Code Analysis**: Python AST, tree-sitter
- **Graph**: NetworkX

---

## 📁 Project Structure

```
intelligentscan/
├── server/
│   └── main.py                 # FastMCP server with tools
├── scanners/
│   ├── vulnerability_scanner.py   # Security vulnerability detection
│   ├── arb_scanner.py            # ARB compliance checking
│   ├── ai_readiness_scanner.py   # AI-readiness analysis
│   └── ast_analyzer.py           # Deep AST-based analysis
├── agents/
│   ├── planning_agent.py         # Determines scan strategy
│   ├── execution_agent.py        # Performs scans
│   ├── verification_agent.py     # LLM-based verification
│   └── reflection_agent.py       # Self-correction
├── utils/
│   ├── knowledge_graph.py        # Graph builder
│   └── report_generator.py       # Report generation
├── config/
│   └── rules.yaml                # Scanning rules configuration
├── tests/
│   └── test_scanners.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── deployment.yml                # Kubernetes deployment
└── README.md
```

---

## 🔧 Configuration

### Rules Configuration

Edit `config/rules.yaml` to customize scanning rules:

```yaml
vulnerability_rules:
  log4j:
    enabled: true
    severity: critical
    patterns:
      - "org\\.apache\\.logging\\.log4j"

arb_rules:
  ARB-SEC-001:
    title: "No hardcoded credentials"
    severity: critical
    applicable_languages: [python, java]
```

### Environment Variables

```bash
# LLM API Keys
export OPENAI_API_KEY="your-key"
export ANTHROPIC_API_KEY="your-key"

# Database
export POSTGRES_HOST="localhost"
export POSTGRES_DB="intelligentscan"
export POSTGRES_PASSWORD="password"

# Redis
export REDIS_HOST="localhost"
export REDIS_PORT=6379

# Logging
export LOG_LEVEL="INFO"
```

---

## 🚢 Deployment

### Docker

```bash
# Build image
docker build -t intelligentscan:latest .

# Run container
docker run -p 8000:8000 \
  -e OPENAI_API_KEY=$OPENAI_API_KEY \
  intelligentscan:latest
```

### Azure AKS (Production)

1. **Build and push to Azure Container Registry**
```bash
az acr build --registry <your-registry> \
  --image intelligentscan:latest \
  --file Dockerfile .
```

2. **Update deployment.yml**
```yaml
image: <your-registry>.azurecr.io/intelligentscan:latest
```

3. **Deploy to AKS**
```bash
kubectl apply -f deployment.yml
```

4. **Verify deployment**
```bash
kubectl get pods -n intelligentscan
kubectl get hpa -n intelligentscan
```

### Auto-Scaling

The deployment automatically scales based on:
- CPU usage (target: 70%)
- Memory usage (target: 80%)
- Min replicas: 3
- Max replicas: 20

---

## 📊 MCP Tools Reference

### scan_vulnerabilities
Scans repository for security vulnerabilities.

**Arguments:**
- `repo_path` (str): Path to repository
- `vulnerability_types` (list, optional): Specific types to check

**Returns:**
```json
{
  "scan_id": "vuln_20250110_143022",
  "status": "completed",
  "summary": {
    "total_vulnerabilities": 5,
    "critical": 2,
    "high": 2,
    "medium": 1
  },
  "vulnerabilities": [...]
}
```

### check_arb_compliance
Checks code against ARB guidelines.

**Arguments:**
- `repo_path` (str): Path to repository
- `arb_rules` (list, optional): Specific rule IDs

**Returns:**
```json
{
  "scan_id": "arb_20250110_143030",
  "compliance_score": 67,
  "violations": [...],
  "violations_by_category": {...}
}
```

### scan_ai_readiness
Analyzes AI-readiness of codebase.

**Arguments:**
- `repo_path` (str): Path to repository
- `include_suggestions` (bool): Include fix suggestions

**Returns:**
```json
{
  "ai_readiness_score": 75,
  "low_confidence_areas": [...],
  "knowledge_graph": {...}
}
```

### generate_report
Generates formatted report.

**Arguments:**
- `scan_id` (str): Scan session ID
- `format` (str): "json", "html", or "markdown"

### scan_by_prompt
Natural language scanning interface.

**Arguments:**
- `prompt` (str): Natural language request

**Examples:**
- "Check log4j vulnerability in ./myproject"
- "Is my codebase following ARB security guidelines?"

---

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=intelligentscan --cov-report=html

# Run specific test
pytest tests/test_vulnerability_scanner.py
```

---

## 🛣️ Roadmap

### Phase 1: MVP (Current)
- ✅ Core MCP server with vulnerability scanning
- ✅ AST-based code analysis
- ✅ Knowledge graph visualization
- ✅ Docker deployment

### Phase 2: Enterprise Features (Next 3 months)
- ⏳ Full ARB compliance engine
- ⏳ LangGraph multi-agent orchestration
- ⏳ RAG-based rule matching
- ⏳ Web dashboard UI
- ⏳ VS Code extension
- ⏳ CI/CD integration (GitHub Actions, Azure DevOps)

### Phase 3: Platform (Next 6 months)
- ⏳ Plugin marketplace
- ⏳ Custom rule builder UI
- ⏳ Advanced analytics
- ⏳ Multi-tenant SaaS
- ⏳ GitHub/GitLab native apps

---

## 🤝 Contributing

We welcome contributions! Areas where you can help:

1. **Add language support**: Java, C#, Go, Rust analyzers
2. **New vulnerability patterns**: Add to `config/rules.yaml`
3. **ARB rules**: Contribute common architectural guidelines
4. **Documentation**: Improve guides and examples
5. **Testing**: Add test cases

---

## 📄 License

[Add your license here]

---

## 🆘 Support

- **Documentation**: See `IntelligentScan.md` for detailed architecture
- **Issues**: Report bugs on GitHub Issues
- **Discussions**: Join our community discussions

---

## 🙏 Acknowledgments

Built with:
- [FastMCP](https://github.com/jlowin/fastmcp) - MCP server framework
- [LangGraph](https://github.com/langchain-ai/langgraph) - Agent orchestration
- [Qdrant](https://qdrant.tech/) - Vector database
- [NetworkX](https://networkx.org/) - Graph algorithms

---

**IntelligentScan** - Making codebases AI-ready, secure, and compliant.
