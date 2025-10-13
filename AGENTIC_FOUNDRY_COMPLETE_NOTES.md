# Agentic Foundry & MCP Platform - Complete Study Notes

**Date:** 2025-10-10
**Author:** Shriyavallabh Pethkar
**Source:** Infosys Agentic Foundry Presentation & Demo
**Purpose:** Comprehensive reference document for understanding Agentic Foundry, MCP integration, and enterprise AI agent deployment

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [What is Agentic Foundry?](#what-is-agentic-foundry)
3. [Core Concepts & Architecture](#core-concepts--architecture)
4. [The Four Pillars of Agentic Foundry](#the-four-pillars-of-agentic-foundry)
5. [MCP Platform Deep Dive](#mcp-platform-deep-dive)
6. [Real-World Use Cases](#real-world-use-cases)
7. [Technical Implementation Details](#technical-implementation-details)
8. [Evaluation & Monitoring](#evaluation--monitoring)
9. [Deployment & Infrastructure](#deployment--infrastructure)
10. [Comparison with Other Platforms](#comparison-with-other-platforms)
11. [Questions & Answers](#questions--answers)
12. [Implementation Roadmap for Office](#implementation-roadmap-for-office)

---

## Executive Summary

### What Problem Does Agentic Foundry Solve?

**The Challenge:**
Building production-ready AI agents requires:
- Writing complex Python code for tools
- Crafting effective system prompts
- Configuring LLM connections
- Building evaluation frameworks
- Deploying to production infrastructure
- Monitoring and debugging in production
- Managing secrets and credentials
- Ensuring governance and compliance

**The Solution:**
Agentic Foundry is an **enterprise platform** that provides:
- GUI-based agent creation (low-code/no-code)
- Built-in tool templates and MCP server integration
- Auto-generated system prompts with optimization
- Comprehensive evaluation dashboards
- One-click export to Docker/Kubernetes
- Built-in monitoring, traceability, and governance

### Key Value Propositions

1. **Speed:** Build agents in hours instead of weeks
2. **Accessibility:** Non-developers can create agents via GUI
3. **Enterprise-Ready:** Built-in governance, approval workflows, audit trails
4. **Integration:** Connect to any API, database, or MCP server
5. **Quality Assurance:** Built-in testing and evaluation frameworks
6. **Flexibility:** Export to any infrastructure or use hosted platform
7. **Templates:** Pre-built agents for common enterprise use cases

### Platform Components

**Agentic Foundry = Complete Agent Lifecycle Platform:**
- Tool creation & management
- Agent configuration & templates
- Evaluation & benchmarking
- Deployment & export
- Monitoring & optimization

**MCP Platform = Standalone MCP Server Management:**
- Can be used independently (without Agentic Foundry)
- Three MCP server types: CODE, ACTIVE, MODULE
- Team-based collaboration & sharing
- Governance & approval workflows
- Built-in testing & validation

---

## What is Agentic Foundry?

### Definition

**Agentic Foundry** is a comprehensive enterprise platform developed by Infosys for building, testing, evaluating, deploying, and monitoring AI agents at scale.

Think of it as **"WordPress for AI Agents"**:
- WordPress makes website creation accessible to non-developers
- Agentic Foundry makes AI agent creation accessible to non-AI-experts

### Core Philosophy

**Traditional Approach (Code-First):**
```
Developer writes everything in code
→ Manually configure infrastructure
→ Build custom evaluation tools
→ Deploy and hope it works
→ Debug in production
→ Hard to maintain/update
```

**Agentic Foundry Approach (Platform-First):**
```
Use GUI to create agent
→ Platform auto-generates code
→ Built-in evaluation & testing
→ Export or use hosted deployment
→ Monitor with built-in dashboards
→ Easy updates and versioning
```

### Target Users

| User Type | Use Case | Benefit |
|-----------|----------|---------|
| **Developers** | Build custom tools, integrate systems | Faster development with templates |
| **Data Scientists** | Optimize prompts, evaluate metrics | Built-in benchmarking tools |
| **Business Analysts** | Create agents via GUI | No coding required |
| **QA Teams** | Test agents before production | Comprehensive testing framework |
| **DevOps** | Deploy and monitor agents | One-click deployment to K8s |
| **Admins** | Manage governance & approvals | Centralized control & audit trails |

---

## Core Concepts & Architecture

### What is an Agent?

An **agent** in Agentic Foundry is composed of three core components:

```
┌─────────────────────────────────────────┐
│              AGENT                      │
├─────────────────────────────────────────┤
│                                         │
│  1. LLM (Language Model)                │
│     - GPT-4, GPT-5, Claude, Llama       │
│     - Switchable at runtime             │
│                                         │
│  2. Tools (Skills/Capabilities)         │
│     - Python functions                  │
│     - MCP servers                       │
│     - External APIs                     │
│                                         │
│  3. System Prompt (Instructions)        │
│     - Auto-generated                    │
│     - Optimizable                       │
│     - Includes tool descriptions        │
│                                         │
└─────────────────────────────────────────┘
```

#### 1. LLM (The Brain)

**What it is:**
- The language model that powers the agent
- Does the "thinking" and decision-making

**In Agentic Foundry:**
- ✅ Model-agnostic (not locked to one provider)
- ✅ Switchable at query time (GPT-4 → GPT-5 → Llama)
- ✅ Supports: OpenAI, Claude, Llama, open-source models

**Example:**
```python
# You can switch models without recreating the agent
agent_response = agent.run(
    query="Analyze Q1 sales",
    model="gpt-4"  # Or "gpt-5", "claude-3.5", "llama-3"
)
```

#### 2. Tools (The Hands)

**What they are:**
- Python functions that give agents capabilities
- Connect to databases, APIs, file systems, etc.

**Types of tools:**

**A. Built-in Python Tools (CODE):**
```python
def get_customer_info(customer_id: str) -> dict:
    """Fetch customer data from database"""
    # Connect to database
    # Query customer info
    # Return data
    return customer_data
```

**B. MCP Server Tools (ACTIVE/MODULE):**
```python
# Agent can use tools from MCP servers:
# - GitHub MCP: create_issue(), list_repos()
# - Salesforce MCP: get_opportunities(), create_lead()
# - Custom MCP: Your team's tools
```

**C. External API Integrations:**
```python
# Tools can call any API:
# - Microsoft Graph API (SharePoint, Outlook)
# - Slack API
# - Jira API
# - Your internal microservices
```

#### 3. System Prompt (The Instructions)

**What it is:**
- Instructions that define the agent's identity and behavior
- Tells the agent what tools it has and how to use them

**Auto-generated example:**
```
You are a Sales Dashboard Agent.

Your purpose: Help sales managers analyze sales data and create reports.

Available tools:
1. get_sales_data(region, start_date, end_date) - Query sales database
2. create_chart(data, chart_type) - Generate visualizations
3. send_email(recipient, subject, body) - Email reports

Guidelines:
- Always validate date ranges before querying
- Use bar charts for regional comparisons
- Use line charts for time series
- Ask for confirmation before sending emails

When a user asks for sales analysis:
1. Determine what data is needed
2. Call get_sales_data() with appropriate parameters
3. Analyze the results
4. Create visualizations using create_chart()
5. Present findings clearly
```

**This prompt is generated automatically based on:**
- Agent name and description
- Available tools and their docstrings
- Agent template (React, Plan-Verify, etc.)
- Best practices from Infosys's experience

---

### Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                   USER INTERFACE LAYER                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   Web UI     │  │   Chatbot    │  │  Canvas AI   │     │
│  │  (Tool/Agent │  │  Interface   │  │  (Visual     │     │
│  │   Builder)   │  │              │  │   Output)    │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                             │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              AGENTIC FOUNDRY CORE PLATFORM                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  TOOL ONBOARDING                                    │   │
│  │  - Code editor with PEP-8 linting                   │   │
│  │  - Auto-generate docstrings                         │   │
│  │  - Vault integration for secrets                    │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  AGENT CREATION                                     │   │
│  │  - Select template (React, Plan-Verify, etc.)       │   │
│  │  - Add tools & MCP servers                          │   │
│  │  - Auto-generate system prompt                      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  EVALUATION FRAMEWORK                               │   │
│  │  - Ground truth testing (Excel test cases)          │   │
│  │  - LLM as judge (GPT-5 evaluates GPT-4)             │   │
│  │  - Tool efficiency metrics                          │   │
│  │  - Score thresholds (block poor agents)             │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  PROMPT OPTIMIZER                                   │   │
│  │  - Iterative prompt improvement                     │   │
│  │  - Pareto sampling                                  │   │
│  │  - Reasoning chain guidance                         │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  EPISODIC MEMORY                                    │   │
│  │  - Thumbs up/down feedback                          │   │
│  │  - Persistent learning across sessions              │   │
│  │  - Cache for user interactions                      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                  MCP PLATFORM (Standalone)                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐             │
│  │   CODE    │  │  ACTIVE   │  │  MODULE   │             │
│  │  Servers  │  │  Servers  │  │  Servers  │             │
│  │  (Custom  │  │ (External │  │  (NPM/Pip │             │
│  │   Python) │  │    URLs)  │  │  Packages)│             │
│  └───────────┘  └───────────┘  └───────────┘             │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  GOVERNANCE & APPROVAL WORKFLOWS                    │   │
│  │  - Developer → QA → Admin approval                  │   │
│  │  - Visibility levels (Private/Team/Common)          │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                  DEPLOYMENT LAYER                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   Hosted     │  │   Export     │  │  Kubernetes  │     │
│  │   API        │  │   Docker     │  │     (AKS)    │     │
│  │   Gateway    │  │  Container   │  │   Multi-Pod  │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                             │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                 INFRASTRUCTURE LAYER                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │    Vault     │  │   Database   │  │File Storage  │     │
│  │  (Secrets)   │  │  (Episodic   │  │   (Agent     │     │
│  │              │  │   Memory)    │  │    Files)    │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  MONITORING & OBSERVABILITY                          │  │
│  │  - Metrics (latency, cost, accuracy)                 │  │
│  │  - Traceability (tool call logs)                     │  │
│  │  - Alerting                                          │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## The Four Pillars of Agentic Foundry

### Pillar 1: Tool Onboarding

**Purpose:** Create reusable skills/capabilities for agents

#### Features

1. **Web-Based Code Editor**
   - Write Python code directly in browser
   - Syntax highlighting
   - Auto-completion
   - Import suggestions

2. **PEP-8 Linting & Validation**
   - Real-time code quality checks
   - Style compliance (PEP-8 standards)
   - Error detection
   - "Script looks good" confirmation before submission

3. **Auto-Generated Docstrings**
   - LLM analyzes your code
   - Generates comprehensive docstrings
   - Describes parameters, return types, purpose
   - Makes tools discoverable by agents

4. **Vault Integration**
   - Never hardcode secrets in tools
   - Reference secrets by variable name: `{{vault:api_key}}`
   - Secrets injected at runtime
   - Centralized secret management

#### Example: Creating a Tool

**Scenario:** Create a tool to fetch data from Salesforce

**Step 1: Write Code**
```python
from fastmcp import FastMCP
import requests

mcp = FastMCP("Salesforce Opportunities Tool")

@mcp.tool()
def get_opportunities(region: str, min_amount: int) -> list:
    # Vault reference (not actual password!)
    token = "{{vault:salesforce_api_token}}"

    # API endpoint
    url = "https://api.salesforce.com/v2/opportunities"

    # Headers with authentication
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # Query parameters
    params = {
        "region": region,
        "amount__gte": min_amount
    }

    # Make request
    response = requests.get(url, headers=headers, params=params)

    # Return data
    return response.json()["opportunities"]
```

**Step 2: Platform Analysis**

Platform automatically:
- ✅ Validates syntax
- ✅ Checks PEP-8 compliance
- ✅ Verifies vault reference exists
- ✅ Generates docstring:

```python
"""
Get sales opportunities from Salesforce based on region and minimum amount.

This tool queries the Salesforce API to retrieve opportunity records
filtered by geographic region and minimum deal size.

Args:
    region (str): Geographic region to filter by (e.g., "Northeast", "West")
    min_amount (int): Minimum opportunity value in dollars

Returns:
    list: List of opportunity dictionaries containing:
        - id: Opportunity ID
        - name: Opportunity name
        - amount: Deal value
        - stage: Current sales stage
        - owner: Assigned sales representative

Example:
    >>> get_opportunities("Northeast", 100000)
    [
        {
            "id": "006...",
            "name": "Acme Corp Deal",
            "amount": 250000,
            "stage": "Negotiation",
            "owner": "John Smith"
        }
    ]

Raises:
    requests.HTTPError: If Salesforce API returns error
    KeyError: If API response format is unexpected
"""
```

**Step 3: Submit**

Tool is now available in tool library for any agent to use!

---

### Pillar 2: Agent Creation

**Purpose:** Combine tools, MCP servers, and LLM into a functional agent

#### Agent Templates

Agentic Foundry provides multiple templates for different use cases:

##### 1. **React Template**

**What it is:**
- ReAct = Reasoning + Acting
- Agent reasons about what to do, then acts (calls tools)
- Iterative: Observe → Reason → Act → Repeat

**When to use:**
- General-purpose agents
- Tasks requiring step-by-step reasoning
- When you need agent to "think out loud"

**Example workflow:**
```
User: "Get Q1 sales for Northeast region"

Agent thinks:
Step 1 (Reason): I need sales data for Q1 in Northeast
Step 2 (Act): Call get_sales_data(region="Northeast", quarter="Q1")
Step 3 (Observe): Received data showing $2.5M in sales
Step 4 (Reason): User asked for Q1 sales, I have the answer
Step 5 (Act): Return "Q1 sales for Northeast: $2.5M"
```

##### 2. **Plan-Verify Template**

**What it is:**
- Agent creates a plan BEFORE executing
- User can approve/reject plan (thumbs up/down)
- Only executes after approval

**When to use:**
- High-stakes operations (financial transactions, data deletion)
- When you want human oversight
- Complex multi-step workflows

**Example workflow:**
```
User: "Do risk assessment for supplier ID 42"

Agent creates plan:
┌─────────────────────────────────────────┐
│ PLAN                                    │
├─────────────────────────────────────────┤
│ Step 1: Fetch supplier data from SAP    │
│ Step 2: Get contract details from SFDC  │
│ Step 3: Check credit score from DB      │
│ Step 4: Calculate risk score            │
│ Step 5: Generate report                 │
│                                         │
│ [👍 Approve] [👎 Reject]                │
└─────────────────────────────────────────┘

User clicks 👍 Approve

Agent executes plan step-by-step...
```

##### 3. **Meta Planner Template**

**What it is:**
- Agent that plans how OTHER agents should work
- Creates strategies for complex tasks
- Delegates to specialized sub-agents

**When to use:**
- Very complex workflows
- Need coordination between multiple specialized agents
- Strategic planning tasks

##### 4. **Hybrid Agents**

**What it is:**
- Combination of multiple templates
- Mix React + Plan-Verify + custom logic

**When to use:**
- Unique requirements not covered by single template

##### 5. **Agents of Agents**

**What it is:**
- Multiple specialized agents working together
- Coordinator agent orchestrates sub-agents
- Each sub-agent has specific expertise

**When to use:**
- Complex enterprise workflows
- Tasks requiring diverse skill sets
- Large-scale automation

**Example:**
```
Main Agent: "Project Management Coordinator"
├─ Sub-Agent 1: "Jira Integration Agent"
│  └─ Tools: Jira MCP (create tickets, update status)
│
├─ Sub-Agent 2: "Code Analysis Agent"
│  └─ Tools: GitHub MCP, code quality tools
│
├─ Sub-Agent 3: "Documentation Agent"
│  └─ Tools: Confluence MCP, markdown generator
│
└─ Sub-Agent 4: "Notification Agent"
   └─ Tools: Slack MCP, email sender

User: "Set up new sprint"

Coordinator delegates:
1. Jira Agent → Creates sprint, adds stories
2. Code Agent → Creates feature branches
3. Docs Agent → Generates sprint docs
4. Notification Agent → Alerts team
```

#### Creating an Agent (Step-by-Step)

**Step 1: Basic Configuration**
```
┌─────────────────────────────────────────┐
│  Create New Agent                       │
├─────────────────────────────────────────┤
│ Agent Name: Sales Dashboard Agent      │
│                                         │
│ Description:                            │
│ Helps sales managers analyze sales     │
│ data and create interactive dashboards │
│                                         │
│ Template: ⦿ React                      │
│            ○ Plan-Verify               │
│            ○ Agents of Agents          │
└─────────────────────────────────────────┘
```

**Step 2: Add Tools**
```
┌─────────────────────────────────────────┐
│  Select Tools                           │
├─────────────────────────────────────────┤
│ Available Tools:                        │
│  ☑ get_sales_data (SQL database)       │
│  ☑ create_chart (visualization)        │
│  ☑ generate_excel (report generator)   │
│  ☐ send_email (notifications)          │
│  ☐ get_customer_info (CRM)             │
└─────────────────────────────────────────┘
```

**Step 3: Add MCP Servers**
```
┌─────────────────────────────────────────┐
│  List of Servers (MCP)                  │
├─────────────────────────────────────────┤
│ Available MCP Servers:                  │
│  ☑ Salesforce MCP                       │
│     Tools: get_opportunities, create... │
│                                         │
│  ☐ GitHub MCP                           │
│     Tools: create_issue, list_repos     │
│                                         │
│  ☐ Jira MCP                             │
│     Tools: create_ticket, get_sprints   │
└─────────────────────────────────────────┘
```

**Step 4: Review Auto-Generated System Prompt**
```
System Prompt (Auto-Generated):

You are a Sales Dashboard Agent designed to help sales managers
analyze sales data and create interactive dashboards.

Available Tools:
1. get_sales_data(region, start_date, end_date, metrics)
   - Queries the sales database
   - Returns: Sales figures, trends, comparisons

2. create_chart(data, chart_type, title)
   - Generates visualizations
   - Supported types: bar, line, pie, scatter

3. generate_excel(data, filename)
   - Creates downloadable Excel reports

MCP Servers:
1. Salesforce MCP
   - get_opportunities(): Fetch opportunity pipeline
   - create_lead(): Add new leads to CRM

Guidelines:
- Always validate date ranges before queries
- Use appropriate chart types for data
- Provide clear explanations of insights
- Ask for clarification if query is ambiguous

[Edit System Prompt] [Continue]
```

**Step 5: Agent Created!**

Agent is now ready for testing and evaluation.

---

### Pillar 3: Evaluation Framework

**Purpose:** Validate agent quality before production deployment

Agentic Foundry provides multiple evaluation methods:

#### 3.1 Ground Truth Evaluation

**Concept:** Test agent against known correct answers

**How it works:**

**Step 1: Create Test Cases (Excel file)**
```
test_cases.xlsx:

┌─────────────────────────┬──────────────┬────────────────────┐
│ Question (Column A)     │ Expected     │ Reasoning (Col C)  │
│                         │ (Column B)   │                    │
├─────────────────────────┼──────────────┼────────────────────┤
│ Q1 sales for Northeast? │ $2,500,000   │ Query sales DB for │
│                         │              │ Q1 + Northeast     │
├─────────────────────────┼──────────────┼────────────────────┤
│ Top 3 customers by      │ Acme Corp,   │ Sort customers by  │
│ revenue?                │ TechCo,      │ total revenue DESC │
│                         │ GlobalInc    │ LIMIT 3            │
├─────────────────────────┼──────────────┼────────────────────┤
│ Create bar chart of     │ [Image of    │ get_sales_data() → │
│ regional sales          │ bar chart]   │ create_chart()     │
└─────────────────────────┴──────────────┴────────────────────┘
```

**Step 2: Upload to Platform**
```
┌─────────────────────────────────────────┐
│  Ground Truth Evaluation                │
├─────────────────────────────────────────┤
│ Agent: Sales Dashboard Agent            │
│                                         │
│ Test Cases: [Upload Excel]              │
│ ✓ test_cases.xlsx (10 test cases)      │
│                                         │
│ Score Threshold:                        │
│  TF-IDF: ≥ 85%                          │
│  SBERT: ≥ 90%                           │
│  JAKAD: ≥ 80%                           │
│                                         │
│ [Run Evaluation]                        │
└─────────────────────────────────────────┘
```

**Step 3: Platform Tests Agent**

For each test case:
1. Send question to agent
2. Agent generates response
3. Compare to expected answer
4. Calculate similarity scores

**Step 4: Review Results**
```
┌─────────────────────────────────────────────────────────┐
│  Evaluation Results                                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Overall Scores:                                        │
│  ┌───────────┬────────┬───────────┬────────┐           │
│  │ Metric    │ Score  │ Threshold │ Status │           │
│  ├───────────┼────────┼───────────┼────────┤           │
│  │ TF-IDF    │ 92%    │ ≥ 85%     │ ✅ PASS│           │
│  │ SBERT     │ 96%    │ ≥ 90%     │ ✅ PASS│           │
│  │ JAKAD     │ 88%    │ ≥ 80%     │ ✅ PASS│           │
│  │ LLM Judge │ 4.5/5  │ ≥ 4.0     │ ✅ PASS│           │
│  └───────────┴────────┴───────────┴────────┘           │
│                                                         │
│  ✅ Agent Ready for Production                         │
│                                                         │
│  Test Case Details:                                    │
│  Case 1: Q1 sales for Northeast?                      │
│    Expected: $2,500,000                               │
│    Got:      $2,500,000                               │
│    ✅ Exact match                                      │
│                                                         │
│  Case 2: Top 3 customers                              │
│    Expected: Acme Corp, TechCo, GlobalInc             │
│    Got:      Acme Corporation, TechCo, Global Inc.    │
│    ⚠️  Different formatting (semantically correct)     │
│                                                         │
│  [Download Full Report] [Approve for Production]       │
└─────────────────────────────────────────────────────────┘
```

**Understanding Similarity Metrics:**

| Metric | What It Measures | When It Matters |
|--------|------------------|-----------------|
| **TF-IDF** | Word-by-word matching | Legal docs, financial reports (exact wording matters) |
| **SBERT** | Semantic meaning | Customer support (meaning > exact words) |
| **JAKAD** | Character-level similarity | Data validation (typos, formatting) |
| **LLM Judge** | Overall quality (subjective) | Creative tasks (writing, summarization) |

**Example of Score Threshold in Action:**

```
Scenario: Financial Audit Agent

Test Case:
  Question: "Is budget compliant?"
  Expected: "Yes, budget is $500,000, within limit of $750,000"
  Agent Said: "Budget okay. Current: 500K, Max: 750K"

Scores:
  TF-IDF: 65% ❌ (Below 85% threshold - different wording)
  SBERT: 98% ✅ (Above 90% - same meaning)

Result: BLOCKED from production

Reason:
  For financial audit reports, EXACT wording matters (compliance, legal)
  "500K" vs "$500,000" could confuse stakeholders
  Agent needs to use formal language

Action: Improve system prompt to enforce formal language
```

#### 3.2 LLM as Judge Evaluation

**Concept:** Use a better/different LLM to evaluate agent performance

**When to use:**
- After agent has run for some time in production
- Periodic audits
- Evaluate based on real user interactions

**How it works:**

**Step 1: Collect Session Data**

Platform automatically stores all agent interactions:
```
Session ID: abc123
User: "Show me Q1 sales"
Agent: "Q1 sales were $2.5M, up 20% from Q4"
Tools Called: get_sales_data(quarter="Q1")
Timestamp: 2025-10-01 09:15:32
User Feedback: 👍 (thumbs up)
```

**Step 2: Select Judge LLM**
```
┌─────────────────────────────────────────┐
│  LLM as Judge Evaluation                │
├─────────────────────────────────────────┤
│ Agent Being Evaluated:                  │
│  Sales Dashboard Agent (GPT-4)          │
│                                         │
│ Judge LLM:                              │
│  ⦿ GPT-5 (newer, better model)         │
│  ○ Claude 3.5                           │
│  ○ Custom evaluator                    │
│                                         │
│ Session History: Last 50 interactions   │
│                                         │
│ [Run Evaluation]                        │
└─────────────────────────────────────────┘
```

**Step 3: Judge Evaluates**

Judge LLM analyzes each interaction and rates:

1. **Tool Selection Accuracy**
   - Did agent pick the right tools?
   - Were unnecessary tools called?

   Example:
   ```
   User: "Get Q1 sales"

   Agent called:
     1. get_sales_data(quarter="Q1") ✅
     2. create_chart() ❌ (user didn't ask for chart)
     3. get_customer_info() ❌ (not needed)

   Judge: "Tool selection inefficient. Agent should only call
          get_sales_data(). Score: 6/10"
   ```

2. **Tool Usage Efficiency**
   - How many times was each tool called?
   - Were there unnecessary retries?

   Example:
   ```
   User: "Get customer list"

   Agent called:
     1. nl_to_sql_query() → Error (syntax issue)
     2. nl_to_sql_query() → Error (still wrong)
     3. nl_to_sql_query() → Success

   Judge: "Tool called 3 times when should be 1.
          Agent struggles with SQL generation. Score: 4/10"
   ```

3. **Response Quality**
   - Was the answer correct?
   - Was it clear and helpful?
   - Appropriate tone?

   Example:
   ```
   User: "What were Q1 sales?"
   Agent: "2500000"

   Judge: "Answer is correct but poorly formatted.
          Should be '$2,500,000' or '$2.5M'. Score: 7/10"
   ```

4. **Reasoning Correctness**
   - Did agent think logically?
   - Were assumptions valid?

   Example:
   ```
   User: "Show me top products"
   Agent reasoning: "User wants top products. I'll sort by price."

   Judge: "Incorrect reasoning. 'Top products' likely means
          best-selling (by quantity/revenue), not highest price.
          Score: 3/10"
   ```

**Step 4: Review Judge's Report**
```
┌─────────────────────────────────────────────────────────┐
│  LLM Judge Evaluation Report                            │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Sessions Analyzed: 50                                  │
│  Time Period: Last 7 days                               │
│                                                         │
│  Overall Scores:                                        │
│  ┌────────────────────────┬───────┬──────────┐         │
│  │ Metric                 │ Score │ Trend    │         │
│  ├────────────────────────┼───────┼──────────┤         │
│  │ Tool Selection         │ 8.2/10│ ↗️ +0.5  │         │
│  │ Tool Efficiency        │ 6.5/10│ ↘️ -0.3  │         │
│  │ Response Quality       │ 9.1/10│ → Stable │         │
│  │ Reasoning Correctness  │ 7.8/10│ ↗️ +0.2  │         │
│  └────────────────────────┴───────┴──────────┘         │
│                                                         │
│  ⚠️  Issues Found:                                      │
│                                                         │
│  1. Tool Efficiency Declining                          │
│     - nl_to_sql_query() called avg 2.3 times per query │
│     - Recommendation: Improve SQL generation prompt    │
│                                                         │
│  2. Unnecessary Chart Generation                       │
│     - create_chart() called even when not requested    │
│     - Recommendation: Update system prompt to only     │
│       create charts when explicitly asked              │
│                                                         │
│  ✅ Strengths:                                          │
│                                                         │
│  1. Response quality excellent (9.1/10)                │
│  2. Users happy (78% thumbs up rate)                   │
│                                                         │
│  [Download Full Report] [Implement Recommendations]    │
└─────────────────────────────────────────────────────────┘
```

#### 3.3 Score Thresholds

**What they are:**
- Minimum passing grades for agents
- Organizational quality standards
- Gates before production deployment

**How they work:**

```python
# Conceptual logic
def can_deploy_agent(evaluation_results, org_thresholds):
    """
    Determine if agent meets quality standards

    evaluation_results = Dictionary containing scores
    org_thresholds = Organization's minimum requirements
    Returns True if agent can deploy, False if blocked
    """

    # Check each metric
    if evaluation_results["tf_idf"] < org_thresholds["tf_idf"]:
        return False  # BLOCKED

    if evaluation_results["sbert"] < org_thresholds["sbert"]:
        return False  # BLOCKED

    if evaluation_results["jakad"] < org_thresholds["jakad"]:
        return False  # BLOCKED

    if evaluation_results["llm_judge"] < org_thresholds["llm_judge"]:
        return False  # BLOCKED

    # All thresholds passed
    return True  # ✅ DEPLOY ALLOWED
```

**Example Threshold Policies:**

```
High-Stakes Agent (Financial Advisor):
┌────────────┬───────────┐
│ Metric     │ Threshold │
├────────────┼───────────┤
│ TF-IDF     │ ≥ 95%     │ Very strict (exact wording critical)
│ SBERT      │ ≥ 98%     │ Very strict (meaning must be precise)
│ JAKAD      │ ≥ 90%     │ Very strict (no typos/formatting errors)
│ LLM Judge  │ ≥ 4.5/5   │ Very strict (high quality only)
└────────────┴───────────┘

Medium-Stakes Agent (Customer Support):
┌────────────┬───────────┐
│ Metric     │ Threshold │
├────────────┼───────────┤
│ TF-IDF     │ ≥ 75%     │ Moderate (wording can vary)
│ SBERT      │ ≥ 90%     │ Strict (meaning important)
│ JAKAD      │ ≥ 70%     │ Lenient (some flexibility)
│ LLM Judge  │ ≥ 4.0/5   │ Moderate
└────────────┴───────────┘

Low-Stakes Agent (Test Data Generator):
┌────────────┬───────────┐
│ Metric     │ Threshold │
├────────────┼───────────┤
│ TF-IDF     │ ≥ 60%     │ Lenient (exact words don't matter)
│ SBERT      │ ≥ 85%     │ Moderate (general meaning ok)
│ JAKAD      │ ≥ 60%     │ Very lenient
│ LLM Judge  │ ≥ 3.5/5   │ Lenient (acceptable quality)
└────────────┴───────────┘
```

---

### Pillar 4: Prompt Optimization

**Purpose:** Automatically improve system prompts to enhance agent performance

**The Problem:**
- Initial system prompt is auto-generated
- Might not be optimally phrased
- Could be missing important instructions
- May not emphasize critical behaviors

**The Solution:**
- Use LLM to iteratively improve the prompt
- Provide examples of desired behavior
- Test multiple prompt variations
- Select best-performing prompt

#### How Prompt Optimization Works

**Step 1: Provide Training Examples**

Instead of just question + expected answer, provide:
- Question
- Expected answer
- **Reasoning chain** (how to get there)

```
Example:

Question: "Calculate Q1 revenue"

Expected Answer: "$2,500,000"

Reasoning Chain:
  1. Use tool: get_sales_data(quarter="Q1")
  2. Sum all sales transactions
  3. Format as currency with $ and commas
  4. Return formatted result
```

**Step 2: Set Optimization Goal**
```
┌─────────────────────────────────────────┐
│  Prompt Optimization                    │
├─────────────────────────────────────────┤
│ Current Agent: Sales Dashboard Agent    │
│                                         │
│ Evaluation LLM: GPT-5                   │
│                                         │
│ Score Threshold: 0.75                   │
│ (Only accept prompts scoring ≥75%)     │
│                                         │
│ Optimization Strategy:                  │
│  ⦿ Pareto Sampling (multiple variants) │
│  ○ Gradient-based                      │
│  ○ Evolutionary                        │
│                                         │
│ Max Iterations: 10                      │
│                                         │
│ Training Examples: [Upload Excel]       │
│ ✓ training_data.xlsx (20 examples)     │
│                                         │
│ [Start Optimization]                    │
└─────────────────────────────────────────┘
```

**Step 3: Optimization Process**

Platform runs multiple iterations:

```
Iteration 1:
  Original Prompt: "You are a sales dashboard agent..."
  Test Score: 72% (below 75% threshold)

  Optimizer suggests changes:
    - Add: "Always format currency with $ and commas"
    - Add: "Validate date ranges before querying"
    - Remove: Redundant instruction about data sources

  New Prompt Generated
  Test Score: 76% ✅ (above threshold!)

Iteration 2:
  Previous Prompt (76%)
  Test Score: 76%

  Optimizer suggests changes:
    - Add: "If data is ambiguous, ask for clarification"
    - Rephrase: Tool usage section for clarity

  New Prompt Generated
  Test Score: 79% ✅ (improvement!)

Iteration 3:
  Previous Prompt (79%)
  Test Score: 79%

  Optimizer suggests changes:
    - Add: "Provide data insights, not just raw numbers"

  New Prompt Generated
  Test Score: 78% (worse - discard this change)

...continues for 10 iterations...

Final Result:
  Best Prompt: Iteration 5 (82%)
  Improvement: +10% from original
```

**Step 4: Review Changes**
```
┌─────────────────────────────────────────────────────────┐
│  Prompt Optimization Results                            │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Original Score: 72%                                    │
│  Optimized Score: 82% (+10%)                            │
│                                                         │
│  Summary of Changes:                                    │
│                                                         │
│  ✅ Added:                                              │
│    - Currency formatting guidelines                    │
│    - Date validation instructions                      │
│    - Clarification protocol                            │
│    - Data insights requirement                         │
│                                                         │
│  ❌ Removed:                                            │
│    - Redundant data source descriptions                │
│    - Overly verbose tool explanations                  │
│                                                         │
│  ✏️  Modified:                                          │
│    - Tool usage section (clearer phrasing)             │
│    - Error handling instructions (more specific)       │
│                                                         │
│  [View Side-by-Side Comparison]                        │
│  [Accept Optimized Prompt] [Keep Original]             │
└─────────────────────────────────────────────────────────┘
```

**Side-by-Side Example:**

```
BEFORE (Original):                 AFTER (Optimized):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

You are a sales dashboard agent.    You are a Sales Dashboard Agent
                                     designed to help sales managers
                                     analyze data and make decisions.

Available tools:                     Available Tools & Usage:
- get_sales_data
- create_chart                       1. get_sales_data(region, dates)
- generate_excel                        - ALWAYS validate date ranges
                                        - Format: YYYY-MM-DD
                                        - Return: Sales figures + trends

Use these tools to help users.       2. create_chart(data, type)
                                        - Types: bar, line, pie
                                        - Choose appropriate type:
                                          • Regional data → bar chart
                                          • Time series → line chart
                                          • Proportions → pie chart

                                     3. generate_excel(data, name)
                                        - Include summary statistics
                                        - Format currency: $X,XXX,XXX

                                     Critical Guidelines:
                                     • Format ALL currency with $ and commas
                                     • Provide insights, not just numbers
                                     • If query is ambiguous, ask for clarification
                                     • Explain significant trends (>10% change)

When users ask questions, answer     Response Strategy:
them using the tools.                1. Understand user's intent
                                     2. Validate inputs
                                     3. Call appropriate tools
                                     4. Analyze results
                                     5. Provide actionable insights
                                     6. Offer to create visualizations
```

**Key Insight:**
The optimized prompt is more:
- **Specific** (exact formatting requirements)
- **Structured** (clear sections)
- **Actionable** (step-by-step guidance)
- **Smart** (when to ask for clarification)

---

## MCP Platform Deep Dive

The MCP Platform is a **standalone product** that can be used independently of Agentic Foundry. It focuses specifically on creating, managing, and deploying MCP (Model Context Protocol) servers.

### What is MCP?

**MCP (Model Context Protocol)** is an open standard created by Anthropic that allows:
- LLMs to discover and use external tools
- Standardized way to expose tools/resources
- Interoperability between different AI systems

Think of it like **HTTP for AI tools**:
- HTTP is the standard for web communication
- MCP is the standard for AI-tool communication

### The Three MCP Server Types

Agentic Foundry's MCP Platform supports three ways to create/use MCP servers:

---

#### Type 1: CODE Servers

**What it is:**
- You write Python code directly in the platform
- Platform packages it as an MCP server
- Deploys it as a hosted HTTP endpoint

**When to use:**
- Custom business logic unique to your company
- Integration with internal systems
- You're comfortable writing Python

**Complete Workflow Example:**

**Scenario:** Create MCP server for internal employee database

**Step 1: Write Code in Platform**
```python
from fastmcp import FastMCP
import psycopg2

mcp = FastMCP("Employee Database MCP")

@mcp.tool()
def get_employee_info(employee_id: str) -> dict:
    """
    Retrieve employee information from internal HR database

    Args:
        employee_id: Unique employee identifier (e.g., "EMP001")

    Returns:
        Dictionary with employee details (name, dept, hire_date, etc.)
    """

    # Vault references (secrets not hardcoded!)
    db_host = "{{vault:hr_db_host}}"
    db_password = "{{vault:hr_db_password}}"

    # Connect to database
    conn = psycopg2.connect(
        host=db_host,
        database="hr_system",
        user="readonly_user",
        password=db_password
    )

    # Safe query (prevents SQL injection)
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT name, department, hire_date, manager_id
        FROM employees
        WHERE employee_id = %s
        """,
        (employee_id,)
    )

    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if result:
        return {
            "name": result[0],
            "department": result[1],
            "hire_date": str(result[2]),
            "manager_id": result[3]
        }
    else:
        return {"error": "Employee not found"}

@mcp.tool()
def list_team_members(manager_id: str) -> list:
    """Get all employees reporting to a manager"""
    # Similar database query logic...
    pass
```

**Step 2: Configure in UI**
```
┌─────────────────────────────────────────┐
│  Create CODE Server                     │
├─────────────────────────────────────────┤
│ Server Name: Employee Database MCP      │
│                                         │
│ Code: [Already entered above]           │
│                                         │
│ Vault References:                       │
│  ✓ hr_db_host (found)                  │
│  ✓ hr_db_password (found)              │
│                                         │
│ Visibility:                             │
│  ○ Keep it private (draft)             │
│  ⦿ Publish to team: HR Team            │
│  ○ Publish to common (all users)       │
│                                         │
│ [Test Code] [Submit for Approval]       │
└─────────────────────────────────────────┘
```

**Step 3: Test Before Submitting**
```
Click [Test Code]

Running PEP-8 validation...
✓ No style issues found

Checking vault references...
✓ All vault keys exist

Running basic validation...
✓ Valid FastMCP structure
✓ Tool decorators correctly applied
✓ Type hints present

Simulating tool execution...
✓ get_employee_info("EMP001") → Success
✓ list_team_members("MGR042") → Success

✅ Script looks good! Ready to submit.
```

**Step 4: Submit for Approval**

After clicking [Submit for Approval]:
```
Status: Pending Review
Assigned to: QA Team

Workflow:
  ✓ Developer (You) → Submitted
  ⏳ QA Team → Testing
  ⏳ Admin → Final Approval
  ⏳ Auto-Deploy → HTTP endpoint
```

**Step 5: QA Tests It**

QA team sees:
```
┌─────────────────────────────────────────┐
│  Pending Approval: Employee DB MCP      │
├─────────────────────────────────────────┤
│ Submitted by: You                       │
│ Team: HR Team                           │
│ Date: 2025-10-10                        │
│                                         │
│ Tools:                                  │
│  - get_employee_info(employee_id)       │
│  - list_team_members(manager_id)        │
│                                         │
│ [View Code] [Test Tools] [Approve/Reject]│
└─────────────────────────────────────────┘
```

QA clicks [Test Tools]:
```
Test get_employee_info("EMP001"):
  Result: {
    "name": "John Doe",
    "department": "Engineering",
    "hire_date": "2020-01-15",
    "manager_id": "MGR042"
  }
  ✅ Test passed

Test with invalid ID ("INVALID"):
  Result: {"error": "Employee not found"}
  ✅ Error handling works

Test list_team_members("MGR042"):
  Result: [...]
  ✅ Returns list of employees

QA Decision: ✅ Approve
```

**Step 6: Admin Final Approval**
```
Admin reviews and clicks: ✅ Approve for Production

Platform automatically:
  1. Creates Docker container
  2. Injects vault secrets as env vars
  3. Deploys to internal infrastructure
  4. Exposes HTTP endpoint
  5. Generates authentication tokens
```

**Step 7: MCP Server is Live!**
```
Employee Database MCP

Status: ✅ Active
Endpoint: https://mcp.company.internal/employee-db
Port: 8080
Authentication: Bearer token required

Tools Available:
  - get_employee_info
  - list_team_members

Usage (from any MCP client):
  curl https://mcp.company.internal/employee-db/tools/get_employee_info \
    -H "Authorization: Bearer YOUR_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{"employee_id": "EMP001"}'

Available to: HR Team members
```

**Step 8: Use in Agents**

Now HR team can add this MCP server to their agents:
```
Agent: "HR Assistant Agent"
MCP Servers:
  ✓ Employee Database MCP

System Prompt: (auto-includes)
  "You have access to Employee Database MCP with tools:
   - get_employee_info: Look up employee details
   - list_team_members: Get team rosters"
```

**User asks agent:**
> "Who reports to manager MGR042?"

**Agent automatically:**
```
1. Recognizes need for team member data
2. Calls MCP server: list_team_members("MGR042")
3. Receives list of employees
4. Formats response:
   "Manager MGR042 (Jane Smith) has 5 direct reports:
    - John Doe (Engineering)
    - Sarah Lee (Engineering)
    - Mike Chen (Engineering)
    - Lisa Park (QA)
    - Tom Wilson (QA)"
```

---

#### Type 2: ACTIVE Servers

**What it is:**
- MCP server already running somewhere else
- You just provide the URL
- Platform connects to it

**When to use:**
- Third-party MCP servers (GitHub, Microsoft, etc.)
- MCP servers from other teams
- External services you don't control

**Complete Workflow Example:**

**Scenario:** Use GitHub's official MCP server

**Step 1: Find External MCP Server**

GitHub provides official MCP server at:
```
https://mcp.github.com
```

**Step 2: Add to Platform**
```
┌─────────────────────────────────────────┐
│  Add ACTIVE Server                      │
├─────────────────────────────────────────┤
│ Server Name: GitHub MCP                 │
│                                         │
│ Endpoint URL:                           │
│ https://mcp.github.com                  │
│                                         │
│ Authentication:                         │
│  ⦿ API Key                             │
│  ○ OAuth                               │
│  ○ None (public)                       │
│                                         │
│ API Key (from vault):                   │
│ {{vault:github_personal_access_token}}  │
│                                         │
│ [Ping Server]                           │
└─────────────────────────────────────────┘
```

**Step 3: Test Connection**
```
Click [Ping Server]

Connecting to https://mcp.github.com...
✓ Server reachable

Authenticating with API key...
✓ Authentication successful

Discovering tools...
✓ Found 12 tools:
  - create_issue(repo, title, body)
  - create_pr(repo, branch, title)
  - list_repos(org)
  - search_code(query, repo)
  - get_commits(repo, branch)
  - ...and 7 more

✅ Server is healthy and ready to use
```

**Step 4: Configure Visibility**
```
Visibility:
  ○ Keep it private
  ⦿ Publish to team: Engineering Team
  ○ Publish to common

[Add to Workspace]
```

**Step 5: Use in Agents**

Engineering team creates an agent:
```
Agent: "DevOps Helper"
MCP Servers:
  ✓ GitHub MCP (external)
  ✓ Jira MCP (external)
  ✓ Internal Build System MCP (CODE server from other team)
```

**Agent can now:**
- Create GitHub issues from Jira tickets
- Search code across repositories
- Trigger builds and monitor commits

---

#### Type 3: MODULE Servers

**What it is:**
- MCP server distributed as a package (npm, pip, Docker)
- Platform installs and runs it for you
- Like installing an app from an app store

**When to use:**
- Community-built MCP servers
- Open-source tools
- Standardized functionality (time, weather, etc.)

**Complete Workflow Example:**

**Scenario:** Use open-source Time MCP server

**Step 1: Find Module**

Browse npm registry:
```
Package: @modelcontextprotocol/server-time
Version: 1.0.0
Downloads: 50K
Description: MCP server for time zone operations
```

**Step 2: Add to Platform**
```
┌─────────────────────────────────────────┐
│  Add MODULE Server                      │
├─────────────────────────────────────────┤
│ Server Name: Time Zone Helper           │
│                                         │
│ Installation Method:                    │
│  ⦿ NPM Package                         │
│  ○ Python Package (pip)                │
│  ○ Docker Image                        │
│                                         │
│ Package Name:                           │
│ @modelcontextprotocol/server-time      │
│                                         │
│ Version:                                │
│  ⦿ Latest                              │
│  ○ Specific: [____]                    │
│                                         │
│ Run Command:                            │
│ npx @modelcontextprotocol/server-time  │
│                                         │
│ Port: 8081                              │
│                                         │
│ [Install & Test]                        │
└─────────────────────────────────────────┘
```

**Step 3: Platform Installs It**
```
Click [Install & Test]

Installing package...
  npm install @modelcontextprotocol/server-time
  ✓ Dependencies resolved
  ✓ Package installed (2.3 MB)

Starting server...
  npx @modelcontextprotocol/server-time --port 8081
  ✓ Server started on port 8081

Discovering tools...
  ✓ get_current_time(timezone)
  ✓ convert_time(from_tz, to_tz, time)
  ✓ get_time_difference(tz1, tz2)
  ✓ list_timezones()

Running test queries...
  Test: get_current_time("America/New_York")
  Result: "2025-10-10 14:30:00 EDT"
  ✓ Success

✅ Module installed and running successfully
```

**Step 4: Configure & Publish**
```
Visibility:
  ○ Keep it private
  ○ Publish to team
  ⦿ Publish to common (everyone needs this!)

[Add to Workspace]
```

**Step 5: Company-Wide Access**

Now ANY agent in the company can use time operations:
```
Sales Agent: "What time is it in Tokyo?"
→ Calls Time MCP: get_current_time("Asia/Tokyo")
→ Response: "11:30 PM JST"

Support Agent: "Customer in London wants call at 9am their time. What time for me (NYC)?"
→ Calls Time MCP: convert_time("Europe/London", "America/New_York", "09:00")
→ Response: "4:00 AM EDT"
```

---

### MCP Server Visibility & Permissions

**Three visibility levels control who can see and use MCP servers:**

#### 1. Keep it Private (Draft Mode)

**Who can see:**
- ✅ Only you (the creator)
- ❌ Your team
- ❌ Other teams
- ❌ Company-wide

**Use cases:**
- 🔬 Experimental/testing
- 🚧 Work in progress
- 🐛 Debugging issues
- 📝 Not ready for others

**Example:**
```
You're testing a new Slack notification MCP:

Server: "Slack Notifier MCP"
Visibility: Private
Status: Works 80% of time, needs fixes

You can test it in your own agents,
but don't want others using it yet.
```

#### 2. Publish to Team

**Who can see:**
- ✅ You
- ✅ Everyone on your team
- ❌ Other teams (unless approved)
- ❌ Company-wide

**Use cases:**
- 👥 Team-specific tools
- 🔐 Sensitive data (only team should access)
- 🎯 Department-specific functionality
- ✅ Ready for team, not company

**Example:**
```
Sales team needs Salesforce access:

Server: "Salesforce Opportunities MCP"
Visibility: Team (Sales Team)
Data: Sales pipeline (confidential)

✓ Sales team members can use it
✗ Engineering can't see sales data
✗ Finance can't access it
```

**Team structure:**
```
Company
├─ Sales Team
│  └─ Members: Bill, Sarah, Mike
│     Can access: Salesforce MCP, CRM MCP
│
├─ Engineering Team
│  └─ Members: Alice, Bob, Carol
│     Can access: GitHub MCP, Build System MCP
│
└─ Finance Team
   └─ Members: Dan, Emma
      Can access: ERP MCP, Invoice MCP
```

#### 3. Publish to Common (Enterprise-Wide)

**Who can see:**
- ✅ Everyone in the company
- ✅ All teams
- ✅ All agents

**Use cases:**
- 🌍 Utility functions (time, weather, etc.)
- 📊 Company-wide services (employee directory)
- 🔓 Public/non-sensitive tools
- ✨ Approved for general use

**Example:**
```
Everyone needs time zone conversions:

Server: "Time Zone Helper MCP"
Visibility: Common
Users: All 5000 employees

Available to:
  ✓ Sales agents (schedule calls)
  ✓ Support agents (global customers)
  ✓ HR agents (international hiring)
  ✓ Everyone else
```

**Approval workflow for "Common":**
```
Developer creates MCP → Submit
  ↓
QA Team tests → Approve
  ↓
Security Review → Approve
  ↓
Admin approves → Common visibility
  ↓
All employees can now use it
```

---

### MCP Workspace

**Workspace = Your MCP Control Center**

Think of it like an app store, but for MCP servers:
- Browse available servers
- Test before using
- Add to your agents
- Manage subscriptions

**Example Workspace View:**

```
┌─────────────────────────────────────────────────────────────┐
│  Bill's MCP Workspace (Sales Team)                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  🔧 MY SERVERS (Created by me)                              │
│  ┌───────────────────────────────────────────────────┐     │
│  │ Salesforce Opportunities MCP                      │     │
│  │ Type: CODE  Status: ✅ Active                     │     │
│  │ Created: 2 days ago                               │     │
│  │ Tools: get_opportunities, create_lead             │     │
│  │ Visibility: Team (Sales)                          │     │
│  │ [Edit Code] [Test] [View Logs] [Deprecate]       │     │
│  └───────────────────────────────────────────────────┘     │
│                                                             │
│  👥 TEAM SERVERS (Available to Sales Team)                  │
│  ┌───────────────────────────────────────────────────┐     │
│  │ CRM Data Sync MCP                                 │     │
│  │ Type: CODE  Status: ✅ Active                     │     │
│  │ Created by: Sarah (Sales Team)                    │     │
│  │ Tools: sync_customer_data, update_notes           │     │
│  │ [Add to My Agents] [Test] [View Docs]            │     │
│  └───────────────────────────────────────────────────┘     │
│                                                             │
│  🌍 COMMON SERVERS (Available to everyone)                  │
│  ┌───────────────────────────────────────────────────┐     │
│  │ Time Zone Helper                                  │     │
│  │ Type: MODULE  Status: ✅ Active                   │     │
│  │ Maintained by: IT Team                            │     │
│  │ Tools: get_current_time, convert_time             │     │
│  │ [Add to My Agents] [Test]                         │     │
│  ├───────────────────────────────────────────────────┤     │
│  │ GitHub MCP                                        │     │
│  │ Type: ACTIVE  Status: ✅ Active                   │     │
│  │ External: https://mcp.github.com                  │     │
│  │ Tools: create_issue, create_pr, search_code       │     │
│  │ [Add to My Agents] [View API Docs]                │     │
│  ├───────────────────────────────────────────────────┤     │
│  │ Microsoft Graph API MCP                           │     │
│  │ Type: CODE  Status: ✅ Active                     │     │
│  │ Created by: IT Team                               │     │
│  │ Tools: get_sharepoint_file, send_email            │     │
│  │ [Add to My Agents] [Request Access]               │     │
│  └───────────────────────────────────────────────────┘     │
│                                                             │
│  🔍 [Search Servers]  [+ Create New Server]                 │
└─────────────────────────────────────────────────────────────┘
```

**What you can do in workspace:**

1. **Test servers before using:**
```
Click [Test] on Time Zone Helper

┌─────────────────────────────────────┐
│  Test Time Zone Helper MCP          │
├─────────────────────────────────────┤
│ Tool: get_current_time              │
│                                     │
│ Parameters:                         │
│  timezone: America/Los_Angeles      │
│                                     │
│ [Run Test]                          │
└─────────────────────────────────────┘

Result:
{
  "time": "11:30 AM PDT",
  "date": "2025-10-10",
  "timestamp": 1728574200
}

✅ Test successful
```

2. **Add to your agents:**
```
Click [Add to My Agents] on GitHub MCP

┌─────────────────────────────────────┐
│  Add GitHub MCP to Agent            │
├─────────────────────────────────────┤
│ Select agent:                       │
│  ⦿ Sales Dashboard Agent           │
│  ○ Customer Support Agent          │
│  ○ Create New Agent                │
│                                     │
│ [Confirm]                           │
└─────────────────────────────────────┘

✅ GitHub MCP added to Sales Dashboard Agent
   Agent can now use GitHub tools
```

3. **View usage statistics:**
```
Click [View Logs] on your Salesforce MCP

┌──────────────────────────────────────────────┐
│  Salesforce MCP Usage (Last 7 days)         │
├──────────────────────────────────────────────┤
│ Total Calls: 1,247                           │
│ Success Rate: 98.3%                          │
│ Avg Response Time: 324ms                     │
│                                              │
│ Most Used Tool:                              │
│  get_opportunities (892 calls)               │
│                                              │
│ Errors (21):                                 │
│  - 15x Authentication timeout                │
│  - 6x Invalid region parameter               │
│                                              │
│ Top Users:                                   │
│  1. Sarah (453 calls)                        │
│  2. Mike (398 calls)                         │
│  3. You (396 calls)                          │
└──────────────────────────────────────────────┘
```

4. **Request access to restricted servers:**
```
Microsoft Graph MCP requires permission

[Request Access]

Email sent to: admin@company.com
Status: Pending approval
Justification: "Need SharePoint access for sales reports"
```

---

### MCP Governance & Approval Workflow

**Problem:** Can't let everyone deploy MCP servers without review
- Security risks (malicious code, data leaks)
- Quality issues (broken tools)
- Compliance (regulatory requirements)

**Solution:** Multi-stage approval workflow

#### Roles in MCP Platform

| Role | Permissions | Responsibilities |
|------|-------------|------------------|
| **Developer** | Create, edit, test servers | Write MCP server code, submit for review |
| **QA** | Test, approve/reject | Validate functionality, security checks |
| **Admin** | Final approval, deploy | Production deployment, access control |
| **User** | Use approved servers | Add servers to agents, provide feedback |

#### Complete Approval Flow

```
┌─────────────────────────────────────────────────────────┐
│  STAGE 1: DEVELOPMENT                                   │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Developer (Bill) writes CODE server                    │
│    ↓                                                    │
│  Tests locally in platform                              │
│    ↓                                                    │
│  Platform validates:                                    │
│    ✓ PEP-8 compliance                                   │
│    ✓ Vault references valid                            │
│    ✓ No syntax errors                                  │
│    ↓                                                    │
│  Developer clicks [Submit for Approval]                 │
│                                                         │
│  Status: Draft → Pending QA                             │
│                                                         │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│  STAGE 2: QA TESTING                                    │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  QA Team receives notification                          │
│    ↓                                                    │
│  QA reviews code:                                       │
│    • Security scan (no hardcoded secrets?)             │
│    • Code quality (follows standards?)                 │
│    • Performance (efficient queries?)                  │
│    ↓                                                    │
│  QA tests tools:                                        │
│    • Unit tests (each tool works?)                     │
│    • Integration tests (connects to systems?)          │
│    • Error handling (fails gracefully?)                │
│    ↓                                                    │
│  QA Decision:                                           │
│    ✅ Approve → Forward to Admin                       │
│    ❌ Reject → Back to Developer with feedback         │
│                                                         │
│  Status: Pending QA → Pending Admin                     │
│                                                         │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│  STAGE 3: ADMIN APPROVAL                                │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Admin receives approval request                        │
│    ↓                                                    │
│  Admin reviews:                                         │
│    • Business justification (why needed?)              │
│    • Visibility level (who should access?)             │
│    • Compliance (meets regulations?)                   │
│    • Resource usage (compute/cost impact?)             │
│    ↓                                                    │
│  Admin Decision:                                        │
│    ✅ Approve → Auto-deploy                            │
│    ❌ Reject → Back to Developer                       │
│    ⏸️  Hold → Request more information                 │
│                                                         │
│  Status: Pending Admin → Deploying                      │
│                                                         │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│  STAGE 4: AUTOMATIC DEPLOYMENT                          │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Platform automatically:                                │
│    1. Creates Docker container                          │
│    2. Injects vault secrets                            │
│    3. Deploys to infrastructure                        │
│    4. Exposes HTTP endpoint                            │
│    5. Generates auth tokens                            │
│    6. Updates workspace (makes visible)                │
│                                                         │
│  Status: Deploying → Active ✅                          │
│                                                         │
│  Notifications sent to:                                 │
│    • Developer (Bill): "Your MCP is live!"             │
│    • Team members: "New MCP available"                 │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**Example with rejection:**

```
Bill creates "Salesforce MCP"
  ↓ Submit
QA Team tests
  ↓
QA finds issue:
  ❌ Hardcoded API endpoint (should use vault)
  ❌ No error handling for network failures

QA clicks [Reject]:
┌─────────────────────────────────────┐
│  Rejection Reason                   │
├─────────────────────────────────────┤
│ Issues Found:                       │
│  1. API endpoint hardcoded on line 23│
│     → Store in vault instead        │
│                                     │
│  2. Missing try/except for network  │
│     errors in get_opportunities()   │
│     → Add error handling            │
│                                     │
│  Estimated Fix Time: 30 mins        │
│  [Send to Developer]                │
└─────────────────────────────────────┘

Bill receives notification with feedback
  ↓
Bill fixes issues
  ↓
Bill resubmits
  ↓
QA re-tests → ✅ Approve
  ↓
Admin approves → ✅ Deploy
  ↓
MCP is live!
```

---


## Real-World Use Cases

### Use Case 1: Project Audit Automation (Infosys Internal)

**Business Context:**
- Infosys manages thousands of client projects simultaneously
- Each project requires regular audits for compliance
- Manual audit process takes 2-4 hours per project
- Human auditors prone to fatigue and inconsistency
- Audit backlog of weeks

**Manual Process (Before Agentic Foundry):**
```
1. Auditor opens SharePoint
2. Downloads project plan Excel file
3. Manually checks:
   - Budget within approved limits?
   - Milestones on track?
   - Escalations properly documented?
   - Resource allocation correct?
   - Compliance requirements met?
4. Cross-references with:
   - Historical project data (SQL database)
   - Client contracts (separate system)
   - Resource availability (HR system)
5. Writes audit report (Word document)
6. Submits for review
7. Uploads back to SharePoint

Total Time: 2-4 hours per project
Error Rate: ~5% (manual data entry errors)
```

**Automated Solution with Agentic Foundry:**

**Agent Configuration:**
```
Agent Name: "Project Validation Agent"
Template: Plan-Verify (requires human approval for critical decisions)

Tools:
1. SharePoint Connector (CODE server)
   - get_project_file(project_id)
   - update_audit_comments(project_id, comments)

2. SQL Database Tool (CODE server)
   - get_historical_data(project_id)
   - get_budget_thresholds()

3. Validation Engine (Python tool)
   - validate_budget(current, approved, variance_threshold)
   - validate_milestones(planned_dates, actual_dates)
   - check_escalations(escalation_log, requirements)

MCP Servers:
1. Jira MCP (ACTIVE)
   - If critical issues found → create Jira ticket

System Prompt: (auto-generated)
"You are a Project Audit Agent. Your purpose is to validate 
project compliance and flag issues requiring human review.

Audit Checklist:
1. Budget Compliance
   - Current spend vs approved budget
   - Variance threshold: ±10%
   - Flag if exceeded

2. Milestone Tracking
   - Compare planned vs actual dates
   - Flag delays > 2 weeks

3. Escalation Documentation
   - All escalations logged in system?
   - Resolution status updated?

4. Resource Allocation
   - Staffing matches approved plan?

Human-in-Loop Requirements:
- Budget overage > 15% → Request approval
- Critical milestone missed → Request decision
- Compliance violation detected → Escalate immediately"
```

**Agent Workflow:**

**Step 1: User Initiates Audit**
```
User (Audit Manager): "Audit project ID PR-2024-1234"

Agent creates plan:
┌─────────────────────────────────────────┐
│ AUDIT PLAN for PR-2024-1234             │
├─────────────────────────────────────────┤
│ Step 1: Fetch project file from         │
│         SharePoint                      │
│                                         │
│ Step 2: Retrieve historical data from   │
│         database for comparison         │
│                                         │
│ Step 3: Validate budget compliance      │
│         (±10% variance threshold)       │
│                                         │
│ Step 4: Check milestone status          │
│         (flag delays > 2 weeks)         │
│                                         │
│ Step 5: Verify escalation documentation │
│                                         │
│ Step 6: Generate audit report           │
│                                         │
│ Step 7: Upload to SharePoint with       │
│         audit comments                  │
│                                         │
│ [👍 Approve Plan] [👎 Modify]           │
└─────────────────────────────────────────┘

User clicks 👍 Approve
```

**Step 2: Agent Executes (Normal Case)**
```
Agent executes plan:

✓ Step 1: Downloaded project_PR-2024-1234.xlsx
✓ Step 2: Retrieved historical data
✓ Step 3: Budget check
    Current: $450,000
    Approved: $500,000
    Variance: -10% (within limits) ✅
✓ Step 4: Milestones
    Planned: Phase 1 complete by Oct 1
    Actual: Completed Sep 28
    Status: On time ✅
✓ Step 5: Escalations
    Total: 3 escalations
    All documented ✅
    All resolved ✅
✓ Step 6: Report generated
✓ Step 7: Uploaded to SharePoint

AUDIT RESULT: ✅ COMPLIANT
No issues found.

Time taken: 45 seconds (was 2 hours manually)
```

**Step 3: Human-in-Loop (Issue Detected)**
```
Different project: PR-2024-5678

Agent executes plan:
✓ Step 1-2: Data retrieved
⚠️  Step 3: Budget check FAILED
    Current: $580,000
    Approved: $500,000
    Variance: +16% (OVER THRESHOLD!)

Agent pauses and asks human:
┌─────────────────────────────────────────┐
│ ⚠️  HUMAN INPUT REQUIRED                │
├─────────────────────────────────────────┤
│ Issue: Budget Overage Detected          │
│                                         │
│ Project: PR-2024-5678                   │
│ Approved Budget: $500,000               │
│ Current Spend: $580,000                 │
│ Overage: +$80,000 (+16%)                │
│                                         │
│ Reason (from project notes):            │
│ "Additional resources needed for        │
│  unexpected technical complexity"       │
│                                         │
│ Historical Context:                     │
│ - Similar projects avg 12% overage     │
│ - Client has approved scope changes    │
│                                         │
│ Approve overage and continue audit?     │
│ [✅ Approve] [❌ Escalate] [📝 Comment] │
└─────────────────────────────────────────┘

Audit Manager reviews:
- Checks client approval documentation
- Verifies scope change requests
- Decides: ✅ Approve

Agent continues:
✓ Step 4-7: Complete
✅ AUDIT RESULT: COMPLIANT (with approved exception)
```

**Results:**

| Metric | Before (Manual) | After (Agent) | Improvement |
|--------|----------------|---------------|-------------|
| **Time per audit** | 2-4 hours | 45 seconds | **99% faster** |
| **Error rate** | ~5% | <0.5% | **90% reduction** |
| **Audits per day** | 2-3 per person | 50+ automated | **20x increase** |
| **Backlog** | 3 weeks | 0 (real-time) | **Eliminated** |
| **Cost per audit** | $50-80 (labor) | $0.10 (compute) | **99% cost reduction** |

**Additional Benefits:**
- ✅ Consistent audit criteria (no human bias)
- ✅ Complete audit trail (all decisions logged)
- ✅24/7 operation (no waiting for auditor availability)
- ✅ Automatic Jira ticket creation for issues
- ✅ Episodic memory (learns from past exceptions)

---

### Use Case 2: Supply Chain Risk Assessment

**Business Context:**
- Manufacturing company with 500+ suppliers
- Need to assess supplier risk regularly
- Data scattered across multiple systems:
  - SAP (supplier master data)
  - Salesforce (contract details)
  - Financial database (credit scores)
  - External APIs (news, compliance)
- Manual assessment takes days
- Risk changes rapidly (need real-time updates)

**Agent Configuration:**
```
Agent Name: "Supplier Risk Analyzer"
Template: React (iterative reasoning)

Tools:
1. SAP Connector (CODE server)
   - get_supplier_data(supplier_id)
   - get_order_history(supplier_id, months)

2. Financial Database (CODE server)
   - get_credit_score(supplier_id)
   - get_payment_history(supplier_id)

3. Risk Calculation Engine (Python tool)
   - calculate_risk_score(supplier_data)
   - identify_risk_factors(supplier_data)

MCP Servers:
1. Salesforce MCP (ACTIVE)
   - get_contract_details(supplier_id)

2. News API MCP (MODULE - from npm)
   - search_news(company_name, days=30)

3. Jira MCP (ACTIVE)
   - create_ticket(title, description, priority)

Canvas AI: Enabled
- Generate interactive risk dashboard
- Bar charts for risk scores
- Timeline of risk changes
```

**Agent Workflow:**

**User Request:**
```
Risk Manager: "Do risk assessment for supplier ID SUP-4821"
```

**Agent Reasoning (React Template):**
```
Agent thinks (Reason):
"I need to assess risk for SUP-4821. Risk assessment requires:
 1. Supplier profile (from SAP)
 2. Contract status (from Salesforce)
 3. Financial health (credit score)
 4. Recent news (potential issues)
 5. Order history (performance)"

Agent acts (Action 1):
Call SAP: get_supplier_data("SUP-4821")

Agent observes (Observation 1):
Received: {
  "name": "TechParts Inc",
  "location": "Vietnam",
  "established": "2015",
  "category": "Electronics Components"
}

Agent thinks (Reason):
"Got basic info. Now need contract details."

Agent acts (Action 2):
Call Salesforce MCP: get_contract_details("SUP-4821")

Agent observes (Observation 2):
Received: {
  "contract_value": "$2.5M/year",
  "renewal_date": "2025-12-31",
  "payment_terms": "Net 60",
  "status": "Active"
}

Agent thinks (Reason):
"Contract is significant ($2.5M). Need to check financial health."

Agent acts (Action 3):
Call Financial DB: get_credit_score("SUP-4821")

Agent observes (Observation 3):
Received: {
  "credit_score": 650,
  "rating": "B",
  "trend": "declining",
  "last_payment_delay": "15 days"
}

Agent thinks (Reason):
"⚠️  Credit score declining + payment delay = potential risk.
 Need to check recent news for issues."

Agent acts (Action 4):
Call News API MCP: search_news("TechParts Inc", days=30)

Agent observes (Observation 4):
Received: [
  {
    "date": "2025-10-05",
    "headline": "TechParts Inc expands factory in Vietnam",
    "sentiment": "positive"
  },
  {
    "date": "2025-09-28",
    "headline": "Vietnam electronics sector faces export challenges",
    "sentiment": "negative"
  }
]

Agent thinks (Reason):
"Mixed signals:
 + Expansion (good)
 - Regional export challenges (risk)
 - Declining credit (risk)
 - Payment delays (risk)
 
 Need to check order performance."

Agent acts (Action 5):
Call SAP: get_order_history("SUP-4821", months=6)

Agent observes (Observation 5):
Received: {
  "total_orders": 24,
  "on_time_delivery": "87%",
  "quality_issues": 2,
  "average_delay": "3 days"
}

Agent thinks (Reason):
"On-time delivery 87% is below our 95% threshold.
 Quality issues present.
 
 Calculate overall risk score."

Agent acts (Action 6):
Call risk engine: calculate_risk_score({all collected data})

Agent observes (Observation 6):
Risk Score: 68/100 (Medium-High Risk)

Risk Factors:
1. Declining credit score (Weight: High)
2. Payment delays (Weight: Medium)
3. Below-target delivery performance (Weight: Medium)
4. Regional export challenges (Weight: Low)

Agent thinks (Reason):
"Risk score is 68 = Medium-High.
 This is concerning for a $2.5M contract.
 Should create Jira ticket for procurement review."

Agent acts (Action 7):
Call Jira MCP: create_ticket(
  title="Review Supplier SUP-4821 (Medium-High Risk)",
  description="Risk assessment flagged concerns...",
  priority="High"
)

Agent observes (Observation 7):
Ticket created: PROC-8472

Agent thinks (Reason):
"All data collected and analyzed.
 Jira ticket created.
 Now generate dashboard for risk manager."

Agent acts (Action 8):
Use Canvas AI to generate interactive dashboard
```

**Canvas AI Output:**
```
┌─────────────────────────────────────────────────────────┐
│  Supplier Risk Assessment - SUP-4821                    │
│  TechParts Inc                                          │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Overall Risk Score: 68/100 ⚠️  MEDIUM-HIGH            │
│                                                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │ Risk Score Breakdown (Bar Chart)                │   │
│  ├─────────────────────────────────────────────────┤   │
│  │ Financial Health    ████████░░ 45/100 (Red)    │   │
│  │ Delivery Performance █████████░ 87/100 (Yellow)│   │
│  │ Contract Status     ██████████ 95/100 (Green)  │   │
│  │ Market Conditions   ███████░░░ 70/100 (Yellow) │   │
│  └─────────────────────────────────────────────────┘   │
│                                                         │
│  🔴 Critical Risk Factors:                              │
│    • Credit score declining (650, was 720 6mo ago)     │
│    • Payment delays averaging 15 days                  │
│    • On-time delivery 87% (target: 95%)                │
│                                                         │
│  📊 Key Metrics:                                        │
│    Contract Value: $2.5M/year                          │
│    Orders (6mo): 24                                    │
│    Quality Issues: 2                                   │
│    Average Delay: 3 days                               │
│                                                         │
│  📰 Recent News:                                        │
│    ✓ Factory expansion (positive)                      │
│    ⚠️  Regional export challenges                       │
│                                                         │
│  ✅ Actions Taken:                                      │
│    • Jira ticket created: PROC-8472                    │
│    • Assigned to: Procurement Team                     │
│    • Priority: High                                    │
│                                                         │
│  💡 Recommendations:                                    │
│    1. Request financial statements (verify health)     │
│    2. Review alternative suppliers                     │
│    3. Negotiate stricter delivery SLAs                 │
│    4. Consider contract renegotiation                  │
│                                                         │
│  [Download Full Report] [Schedule Review] [View History]│
└─────────────────────────────────────────────────────────┘
```

**Results:**

| Aspect | Before (Manual) | After (Agent) |
|--------|----------------|---------------|
| **Time** | 2-3 days | 2 minutes |
| **Data sources** | 2-3 (too time-consuming to check all) | 5+ (checks everything) |
| **Frequency** | Quarterly | On-demand / Real-time |
| **Coverage** | 50 suppliers/year | All 500+ suppliers |
| **Consistency** | Subjective (varies by analyst) | Objective (same criteria) |
| **Cost** | $200-300 per assessment | $0.50 per assessment |

---

### Use Case 3: Sales Dashboard Creation

**Business Context:**
- Sales managers need weekly performance dashboards
- Data in multiple systems:
  - SQL database (sales transactions)
  - Salesforce (opportunity pipeline)
  - Excel files (sales targets)
- Analysts spend 3-4 hours per dashboard
- Managers want self-service (no waiting for analysts)

**Agent Configuration:**
```
Agent Name: "Sales Dashboard Agent"
Template: React

Tools:
1. SQL Database Connector (CODE server)
   - query_sales_data(region, date_range, metrics)
   
2. Excel Generator (Python tool)
   - create_excel_report(data, template)

3. Chart Creator (Python tool with Canvas AI)
   - create_bar_chart(data, title)
   - create_line_chart(data, title)
   - create_pie_chart(data, title)

MCP Servers:
1. Salesforce MCP (ACTIVE)
   - get_opportunities(region, stage)
   - get_pipeline_value(region)

Canvas AI: Enabled (interactive dashboards)
```

**Interaction Example:**

**User Request:**
```
Sales Manager (Northeast): "Create Q3 sales dashboard for Northeast region"
```

**Agent Response:**
```
Agent: "I'll create your Q3 Northeast dashboard. Gathering data..."

[Agent calls tools in background:]
1. query_sales_data(region="Northeast", quarter="Q3")
2. get_opportunities(region="Northeast", stage="all")
3. get_pipeline_value(region="Northeast")

Agent: "Dashboard ready! Here's your Q3 performance:"

[Canvas AI displays interactive dashboard:]

┌─────────────────────────────────────────────────────────┐
│  Northeast Region - Q3 2025 Sales Dashboard             │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  📊 KEY METRICS                                         │
│  ┌──────────────┬──────────────┬──────────────┐        │
│  │ Closed Sales │ Pipeline     │ Target       │        │
│  ├──────────────┼──────────────┼──────────────┤        │
│  │ $8.2M        │ $12.5M       │ $10M         │        │
│  │ ✅ +18%      │ ⚠️  -5% vs Q2 │ ✅ 82% achieved│       │
│  └──────────────┴──────────────┴──────────────┘        │
│                                                         │
│  📈 Revenue Trend (Line Chart)                          │
│  ┌─────────────────────────────────────────────────┐   │
│  │ 10M ┤              ●                           │   │
│  │  8M ┤        ●           ●                     │   │
│  │  6M ┤   ●                                      │   │
│  │  4M ┤                                          │   │
│  │  2M ┤                                          │   │
│  │     └──────────────────────────────────────   │   │
│  │      Jul    Aug    Sep    Q3 Total            │   │
│  └─────────────────────────────────────────────────┘   │
│                                                         │
│  🏆 Top 5 Sales Reps (Bar Chart)                        │
│  ┌─────────────────────────────────────────────────┐   │
│  │ John D.  ████████████████████ $2.1M            │   │
│  │ Sarah M. ███████████████░░░░░ $1.8M            │   │
│  │ Mike P.  ██████████████░░░░░░ $1.5M            │   │
│  │ Lisa K.  ████████████░░░░░░░░ $1.3M            │   │
│  │ Tom W.   ███████████░░░░░░░░░ $1.2M            │   │
│  └─────────────────────────────────────────────────┘   │
│                                                         │
│  🎯 Performance by Product (Pie Chart)                  │
│  ┌─────────────────────────────────────────────────┐   │
│  │          Product A (42%)                        │   │
│  │              Product B (28%)                    │   │
│  │                  Product C (18%)                │   │
│  │                      Other (12%)                │   │
│  └─────────────────────────────────────────────────┘   │
│                                                         │
│  💡 Insights:                                           │
│    ✅ Exceeded Q3 target by 18% ($8.2M vs $10M goal)   │
│    ⚠️  Pipeline down 5% - need to boost prospecting    │
│    🏆 John D. leading team (26% of total sales)        │
│    📈 Product A growth accelerating (+35% vs Q2)       │
│                                                         │
│  [Download Excel] [Email Report] [Drill Down]          │
└─────────────────────────────────────────────────────────┘

Agent: "Would you like me to:
• Break down by customer segment?
• Compare to other regions?
• Create forecast for Q4?
• Send this report to your team?"
```

**User:** "Yes, compare to other regions"

**Agent:**
```
[Calls query_sales_data for all regions]

Updated view with regional comparison:

┌─────────────────────────────────────────────────────────┐
│  Regional Performance Comparison - Q3 2025              │
├─────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────────┐  │
│  │ Northeast  ███████████████████ $8.2M (✅ +18%)  │  │
│  │ West       ████████████████░░░ $7.5M (✅ +12%)  │  │
│  │ South      █████████████████░░ $7.8M (✅ +15%)  │  │
│  │ Midwest    ████████████░░░░░░░ $5.2M (⚠️  -3%)  │  │
│  └──────────────────────────────────────────────────┘  │
│                                                         │
│  🏆 Northeast is #1 performer                           │
│  ⚠️  Midwest underperforming - needs attention          │
└─────────────────────────────────────────────────────────┘
```

**Results:**

| Metric | Before (Manual) | After (Agent) |
|--------|----------------|---------------|
| **Creation time** | 3-4 hours | 30 seconds |
| **Manager wait time** | 1-2 days | Instant |
| **Update frequency** | Weekly (scheduled) | On-demand |
| **Data freshness** | Day-old data | Real-time |
| **Cost per dashboard** | $75-100 (analyst time) | $0.20 (compute) |
| **Self-service** | No (needs analyst) | Yes (managers do it) |

---

### Use Case 4: Test Data Generation

**Business Context:**
- QA team needs realistic test data for new features
- Data must match production schema exactly
- Manual creation is tedious and error-prone
- Need thousands of records quickly
- Must avoid using real customer data (GDPR/privacy)

**Agent Configuration:**
```
Agent Name: "Test Data Generator"
Template: React

Tools:
1. Schema Reader (CODE server)
   - read_database_schema(table_name)
   - get_column_constraints(table_name, column_name)

2. Faker Integration (Python tool)
   - generate_realistic_name()
   - generate_realistic_email()
   - generate_realistic_address()
   - generate_realistic_phone()

3. Data Validator (Python tool)
   - validate_against_schema(data, schema)
   - check_referential_integrity(data)

4. SQL Executor (CODE server)
   - bulk_insert(table_name, data)
```

**Interaction Example:**

**User Request:**
```
QA Engineer: "Generate 1000 customer records with orders for testing checkout flow"
```

**Agent Reasoning:**
```
Agent thinks:
"Need to generate:
 1. 1000 customers (with realistic data)
 2. Associated orders (need referential integrity)
 3. Match production schema exactly"

Agent acts (Action 1):
Call schema_reader: read_database_schema("customers")

Agent observes:
Schema: {
  "id": "UUID (primary key)",
  "name": "VARCHAR(100) NOT NULL",
  "email": "VARCHAR(255) UNIQUE NOT NULL",
  "phone": "VARCHAR(20)",
  "address": "TEXT",
  "created_at": "TIMESTAMP DEFAULT NOW()",
  "tier": "ENUM('bronze','silver','gold')"
}

Agent thinks:
"Schema has constraints:
 - Email must be unique
 - Name required
 - Tier must be bronze/silver/gold
 
 Use Faker to generate realistic data."

Agent acts (Action 2):
Generate 1000 customer records using Faker

Generated sample:
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "name": "John Smith",
  "email": "john.smith.550e8400@testdata.com",
  "phone": "+1-555-0123",
  "address": "123 Main St, New York, NY 10001",
  "tier": "silver"  # Random distribution: 60% bronze, 30% silver, 10% gold
}

Agent acts (Action 3):
Validate data against schema

Agent observes:
✅ All emails unique
✅ All names present
✅ All tiers valid (bronze/silver/gold)
✅ Phone numbers formatted correctly

Agent thinks:
"Customer data valid. Now generate orders."

Agent acts (Action 4):
Read orders schema, generate 2500 orders (avg 2.5 per customer)

Agent acts (Action 5):
Bulk insert:
  INSERT INTO test_customers VALUES (...)
  INSERT INTO test_orders VALUES (...)

Agent observes:
✅ Inserted 1000 customers
✅ Inserted 2500 orders
✅ Referential integrity maintained
```

**Agent Response:**
```
✅ Test data generated successfully!

Summary:
  Customers: 1,000
  Orders: 2,500
  Products in orders: 8,732

Distribution:
  Bronze tier: 615 customers (61.5%)
  Silver tier: 289 customers (28.9%)
  Gold tier: 96 customers (9.6%)

Order values:
  Min: $12.50
  Max: $3,245.00
  Avg: $487.32

Sample records:
┌────────────┬─────────────────┬─────────────────────────┬──────┐
│ Customer ID│ Name            │ Email                   │ Tier │
├────────────┼─────────────────┼─────────────────────────┼──────┤
│ 550e8400...│ John Smith      │ john.smith.550@test.com │silver│
│ 660f9511...│ Sarah Johnson   │ sarah.j.660@test.com    │gold  │
│ 770a1622...│ Mike Williams   │ mike.w.770@test.com     │bronze│
└────────────┴─────────────────┴─────────────────────────┴──────┘

All data inserted into test database.
Ready for QA testing!

[Download SQL Dump] [Generate More] [Clear Test Data]
```

**Results:**

| Aspect | Before (Manual) | After (Agent) |
|--------|----------------|---------------|
| **Time** | 2-3 hours | 20 seconds |
| **Records** | 50-100 (tedious) | 1000+ (easy) |
| **Quality** | Variable (human error) | Consistent (schema-compliant) |
| **Realism** | Low (generic data) | High (Faker library) |
| **Privacy** | Risk (might copy production) | Safe (100% synthetic) |

---

### Use Case 5: Customer Support Automation

**Business Context:**
- Support team handles 500+ tickets/day
- Common questions repeated frequently
- Need to look up data from multiple systems
- Response time target: <15 minutes
- Want to reduce agent workload (focus on complex issues)

**Agent Configuration:**
```
Agent Name: "Customer Support Agent"
Template: Plan-Verify (show plan before taking action)

Tools:
1. Customer Database (CODE server)
   - get_customer_info(customer_id)
   - get_order_history(customer_id)

2. Inventory System (CODE server)
   - check_product_availability(product_id)
   - get_shipping_status(order_id)

3. Email Sender (Python tool)
   - send_template_email(customer_email, template, data)

MCP Servers:
1. Zendesk MCP (ACTIVE)
   - create_ticket(customer, subject, priority)
   - update_ticket(ticket_id, status, comment)

2. Slack MCP (MODULE)
   - notify_channel(channel, message) # For escalations

Human-in-Loop:
- Auto-handle common queries
- Escalate complex issues to human agent
- Get approval before refunds/credits
```

**Example 1: Simple Query (Auto-handled)**

**Customer via chatbot:**
> "Where is my order #12345?"

**Agent:**
```
[Thinks: Simple order tracking query - I can handle this]

[Calls: get_shipping_status("12345")]

Agent responds:
"Hi! I checked your order #12345:

📦 Order Status: In Transit
🚚 Carrier: FedEx
📍 Current Location: Memphis, TN
🗓️  Estimated Delivery: October 12, 2025 (2 days)

Tracking link: https://fedex.com/track/...

Is there anything else I can help with?"

[No human involvement needed - resolved in 3 seconds]
```

**Example 2: Requires Approval**

**Customer:**
> "My order #67890 arrived damaged. I want a refund."

**Agent:**
```
[Thinks: Refund request - need approval]

Agent creates plan:
┌─────────────────────────────────────────┐
│ SUPPORT PLAN: Damaged Order Refund     │
├─────────────────────────────────────────┤
│ Customer: Jane Doe (ID: C-9876)         │
│ Order: #67890 ($245.00)                 │
│ Issue: Damaged product                  │
│                                         │
│ Proposed Actions:                       │
│ 1. Verify order details                 │
│ 2. Check return policy eligibility      │
│ 3. Create Zendesk ticket                │
│ 4. Process refund ($245.00)             │
│ 5. Send confirmation email              │
│                                         │
│ ⚠️  Requires Manager Approval           │
│ Reason: Refund >$200                    │
│                                         │
│ [Notify Manager] [Show to Customer]     │
└─────────────────────────────────────────┘

[Agent notifies manager via Slack]
Slack message: "@manager Refund approval needed: $245
Customer C-9876, damaged order #67890. Review in dashboard."

[Manager approves in 2 minutes]

Agent to customer:
"I've reviewed your case. You're eligible for a full refund.

✅ Refund approved: $245.00
💳 Processing time: 3-5 business days
📧 Confirmation sent to jane.doe@email.com

I've also created ticket #SUPP-1234 for tracking.

We're sorry about the damaged item. Is there anything else I can help with?"

Total resolution time: 3 minutes (including manager approval)
```

**Example 3: Escalation to Human**

**Customer:**
> "I'm extremely frustrated. This is my 3rd issue this month and I'm considering canceling my account. The product doesn't work as advertised."

**Agent:**
```
[Thinks: Complex situation:
 - Emotional customer (frustrated)
 - Account retention risk
 - Product quality complaint
 → Escalate to human agent immediately]

Agent responds:
"I understand your frustration, and I sincerely apologize for 
these repeated issues. This is clearly unacceptable.

Given the complexity of your situation, I'm connecting you with 
Sarah, our senior support specialist, who can provide dedicated 
attention to resolve this properly.

[Creating high-priority ticket...]
[Notifying Sarah via Slack...]

Sarah will reach out within 5 minutes. She has full context 
of your history and will work to make this right.

Again, I apologize for these issues."

[Slack to Sarah: "🚨 URGENT: Account retention risk. Customer C-9876
has had 3 issues this month, considering cancellation. Full history
attached. Please call within 5 minutes."]

[Human agent Sarah takes over]

Total time to escalation: 15 seconds
```

**Results:**

| Metric | Before (Human Only) | After (Agent + Human) |
|--------|---------------------|----------------------|
| **Simple queries** | 10 min avg | 5 seconds (99% faster) |
| **Tickets/day** | 500 (overwhelmed) | 200 (agent handles 300) |
| **Response time** | 45 min avg | 30 seconds (agent) / 5 min (human for complex) |
| **Agent workload** | 8 hours/day tickets | 5 hours/day (complex only) |
| **Cost per ticket** | $8 (15 min @ $32/hr) | $0.10 (agent) + $8 (human for 40% only) = ~$3.30 avg |
| **Customer satisfaction** | 78% | 89% (faster + consistent) |

---

## Technical Implementation Details

### Agent Execution Flow (Under the Hood)

**When a user sends a query to an agent, here's what happens:**

```
┌─────────────────────────────────────────────────────────┐
│  STEP 1: REQUEST RECEIVED                               │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  User: "Get Q1 sales for Northeast"                    │
│    ↓                                                    │
│  API Endpoint: POST /api/v1/agents/{agent-id}/invoke   │
│    ↓                                                    │
│  Request Body:                                          │
│  {                                                      │
│    "session_id": "sess_abc123",                        │
│    "query": "Get Q1 sales for Northeast",              │
│    "user_id": "user_xyz",                              │
│    "model": "gpt-4"  // Optional override              │
│  }                                                      │
│                                                         │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│  STEP 2: LOAD AGENT CONFIGURATION                      │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Platform loads from database:                          │
│    • System prompt                                      │
│    • Available tools (list + descriptions)             │
│    • MCP servers (endpoints + auth)                    │
│    • Agent template (React/Plan-Verify/etc.)           │
│    • Episodic memory (past feedback for this agent)    │
│    • Model configuration (GPT-4 or user override)      │
│                                                         │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│  STEP 3: BUILD CONTEXT                                  │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Construct LLM context:                                 │
│                                                         │
│  messages = [                                           │
│    {                                                    │
│      "role": "system",                                  │
│      "content": system_prompt +                        │
│                 tool_descriptions +                     │
│                 episodic_memory_relevant               │
│    },                                                   │
│    {                                                    │
│      "role": "user",                                    │
│      "content": "Get Q1 sales for Northeast"           │
│    }                                                    │
│  ]                                                      │
│                                                         │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│  STEP 4: LLM REASONING (First Turn)                    │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Call LLM API:                                          │
│    openai.ChatCompletion.create(                       │
│      model="gpt-4",                                    │
│      messages=messages,                                │
│      tools=tool_definitions  # Function calling        │
│    )                                                    │
│                                                         │
│  LLM Response:                                          │
│  {                                                      │
│    "reasoning": "User wants Q1 sales for Northeast.    │
│                  I need to use get_sales_data tool.",  │
│    "tool_calls": [                                     │
│      {                                                  │
│        "tool": "get_sales_data",                       │
│        "arguments": {                                  │
│          "region": "Northeast",                        │
│          "quarter": "Q1",                              │
│          "metrics": ["revenue", "orders"]              │
│        }                                               │
│      }                                                  │
│    ]                                                    │
│  }                                                      │
│                                                         │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│  STEP 5: EXECUTE TOOL CALLS                            │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Platform executes tool:                                │
│                                                         │
│  IF tool is Python function:                            │
│    result = get_sales_data(                            │
│      region="Northeast",                               │
│      quarter="Q1",                                     │
│      metrics=["revenue", "orders"]                     │
│    )                                                    │
│                                                         │
│  IF tool is MCP server:                                 │
│    POST https://mcp.company.com/salesforce/tools/...   │
│    with authentication                                 │
│                                                         │
│  Tool returns:                                          │
│  {                                                      │
│    "revenue": 2500000,                                 │
│    "orders": 847,                                      │
│    "growth": "+18%"                                    │
│  }                                                      │
│                                                         │
│  Log to tracing system:                                 │
│    tool_name: get_sales_data                           │
│    execution_time: 234ms                               │
│    status: success                                     │
│                                                         │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│  STEP 6: LLM REASONING (Second Turn)                   │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Add tool result to context:                            │
│                                                         │
│  messages.append({                                      │
│    "role": "tool",                                     │
│    "name": "get_sales_data",                           │
│    "content": '{"revenue": 2500000, ...}'             │
│  })                                                     │
│                                                         │
│  Call LLM again:                                        │
│                                                         │
│  LLM Response:                                          │
│  {                                                      │
│    "reasoning": "Tool returned revenue of $2.5M.       │
│                  User wants this information. I'll     │
│                  format it clearly with growth %.",    │
│    "response": "Q1 sales for Northeast region:        │
│                                                         │
│                 Revenue: $2,500,000                    │
│                 Orders: 847                            │
│                 Growth: +18% vs Q1 last year           │
│                                                         │
│                 Strong performance! Revenue exceeded    │
│                 target by 18%."                        │
│  }                                                      │
│                                                         │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│  STEP 7: STORE SESSION DATA                            │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Save to database:                                      │
│                                                         │
│  session_log = {                                        │
│    "session_id": "sess_abc123",                        │
│    "agent_id": "sales_dashboard_agent",                │
│    "timestamp": "2025-10-10T14:30:00Z",                │
│    "query": "Get Q1 sales for Northeast",              │
│    "response": "Q1 sales for Northeast...",            │
│    "tools_called": [                                   │
│      {                                                  │
│        "tool": "get_sales_data",                       │
│        "args": {...},                                  │
│        "result": {...},                                │
│        "duration_ms": 234                              │
│      }                                                  │
│    ],                                                   │
│    "model": "gpt-4",                                   │
│    "tokens_used": 487,                                 │
│    "latency_ms": 1250,                                 │
│    "cost_usd": 0.0082                                  │
│  }                                                      │
│                                                         │
│  (Used later for evaluation, tracing, cost tracking)   │
│                                                         │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│  STEP 8: RETURN RESPONSE TO USER                       │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  API Response:                                          │
│  {                                                      │
│    "session_id": "sess_abc123",                        │
│    "response": "Q1 sales for Northeast region: ...",  │
│    "status": "completed",                              │
│    "metadata": {                                       │
│      "tools_used": ["get_sales_data"],                │
│      "latency_ms": 1250,                               │
│      "model": "gpt-4"                                  │
│    },                                                   │
│    "canvas": null  // Or Canvas AI data if enabled     │
│  }                                                      │
│                                                         │
│  User sees: "Q1 sales for Northeast region: ..."      │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Tool Calling Mechanics

**How agents discover and call tools:**

**1. Tool Registration**

When you create a tool, platform stores:
```json
{
  "tool_id": "get_sales_data_v1",
  "name": "get_sales_data",
  "description": "Query sales database for revenue, orders, and growth metrics",
  "parameters": {
    "type": "object",
    "properties": {
      "region": {
        "type": "string",
        "enum": ["Northeast", "West", "South", "Midwest"],
        "description": "Geographic region to query"
      },
      "quarter": {
        "type": "string",
        "pattern": "Q[1-4]",
        "description": "Fiscal quarter (Q1, Q2, Q3, Q4)"
      },
      "metrics": {
        "type": "array",
        "items": {"type": "string"},
        "description": "Metrics to return (revenue, orders, growth, etc.)"
      }
    },
    "required": ["region", "quarter"]
  },
  "returns": {
    "type": "object",
    "description": "Sales data with requested metrics"
  }
}
```

**2. Tool Discovery (LLM Perspective)**

When LLM receives query, it sees:
```
System: You are a Sales Dashboard Agent.

Available tools:

1. get_sales_data(region, quarter, metrics)
   Query sales database for revenue, orders, and growth metrics
   
   Parameters:
   - region (required): Geographic region (Northeast/West/South/Midwest)
   - quarter (required): Fiscal quarter (Q1/Q2/Q3/Q4)
   - metrics (optional): Array of metrics to return
   
   Returns: Object with sales data

2. create_chart(data, chart_type, title)
   Generate visualization from data
   ...

3. [MCP] Salesforce.get_opportunities(region, stage)
   From Salesforce MCP server
   Fetch sales opportunities from CRM
   ...

User query: "Get Q1 sales for Northeast"
```

**3. Tool Selection (LLM Reasoning)**

LLM thinks:
```
"User wants: Q1 sales + Northeast region

Available tools:
- get_sales_data: ✅ Has 'region' and 'quarter' params - MATCH!
- create_chart: ❌ Not needed yet (no visualization requested)
- Salesforce.get_opportunities: ❌ User wants closed sales, not pipeline

Decision: Call get_sales_data(region='Northeast', quarter='Q1')"
```

**4. Tool Execution (Platform)**

```python
# Pseudo-code of what platform does

def execute_tool_call(tool_name, arguments):
    """Execute a tool call from the agent"""
    
    # Look up tool in registry
    tool = tool_registry.get(tool_name)
    
    if tool.type == "python":
        # Execute Python function directly
        result = tool.function(**arguments)
    
    elif tool.type == "mcp":
        # Call MCP server via HTTP
        result = requests.post(
            f"{tool.mcp_url}/tools/{tool_name}",
            json=arguments,
            headers={"Authorization": f"Bearer {tool.auth_token}"}
        ).json()
    
    # Log for tracing
    log_tool_call(
        tool_name=tool_name,
        arguments=arguments,
        result=result,
        timestamp=now(),
        duration=elapsed_time
    )
    
    return result
```

---

### Episodic Memory Implementation

**How agents "learn" from user feedback:**

**Scenario:** User gives thumbs down

```
┌─────────────────────────────────────────┐
│  User Query: "Show Q1 sales"            │
│  Agent Response: "Q1: 2500000"          │
│  User Feedback: 👎 (thumbs down)        │
│  User Comment: "Format with commas!"    │
└─────────────────────────────────────────┘
```

**What happens:**

**1. Feedback Stored**
```python
# Saved to episodic_memory table

episodic_memory.insert({
  "agent_id": "sales_dashboard_agent",
  "session_id": "sess_abc123",
  "query": "Show Q1 sales",
  "response": "Q1: 2500000",
  "feedback": "negative",  # thumbs down
  "user_comment": "Format with commas!",
  "timestamp": "2025-10-10T14:30:00Z",
  "context": {
    "tools_used": ["get_sales_data"],
    "model": "gpt-4"
  }
})
```

**2. Memory Retrieval (Next Query)**

When same or similar query comes in:
```python
# Before calling LLM, retrieve relevant memories

relevant_memories = episodic_memory.search(
  agent_id="sales_dashboard_agent",
  query_similarity="Show Q1 sales",  # Semantic search
  limit=5
)

# Returns:
[
  {
    "query": "Show Q1 sales",
    "response": "Q1: 2500000",
    "feedback": "negative",
    "lesson": "Format numbers with commas and currency symbol"
  }
]
```

**3. Memory Injected into Context**

```python
# Add to system prompt dynamically

system_prompt_with_memory = f"""
{original_system_prompt}

IMPORTANT LESSONS FROM PAST INTERACTIONS:
- When displaying sales figures, always format with commas and $ symbol
  (e.g., "$2,500,000" not "2500000")
  [Learned from negative feedback on 2025-10-10]
"""

# Now send to LLM with enhanced context
```

**4. Improved Response**

Next time user asks "Show Q1 sales":
```
Agent: "Q1 sales: $2,500,000"
      (Correctly formatted now!)

User: 👍 (thumbs up)
```

**5. Positive Feedback Stored**

```python
episodic_memory.insert({
  "query": "Show Q1 sales",
  "response": "$2,500,000",
  "feedback": "positive",  # thumbs up
  "improvement": "Applied lesson from previous feedback"
})

# Updates confidence score for this pattern
memory_confidence["currency_formatting"] += 1
```

**Memory Pruning:**

To prevent memory from growing indefinitely:
```python
# Periodic cleanup job

def prune_episodic_memory():
    """Keep memory manageable"""
    
    # Keep high-value memories
    keep_if:
      - Explicit user feedback (thumbs up/down)
      - Led to behavior change
      - Recurring patterns (seen >3 times)
      - Recent (last 30 days)
    
    # Discard low-value memories
    discard_if:
      - No user feedback
      - One-off interactions
      - Old (>90 days) and no pattern
      - Superseded by newer learnings
```

---

### Vault & Secret Management

**How secrets flow from vault to tools:**

**1. Secret Storage**

```
┌─────────────────────────────────────────┐
│  VAULT (HashiCorp Vault / Azure KV)     │
├─────────────────────────────────────────┤
│                                         │
│  secrets/salesforce/                    │
│    api_token: "sfdx_abc123..."         │
│    instance_url: "company.salesforce..."│
│                                         │
│  secrets/database/                      │
│    hr_db_host: "db.company.internal"   │
│    hr_db_password: "secure_pass_xyz"   │
│                                         │
│  secrets/apis/                          │
│    github_token: "ghp_xyz123..."       │
│                                         │
└─────────────────────────────────────────┘
```

**2. Tool Code References Vault**

```python
# Tool code (stored in platform)

@mcp.tool()
def get_salesforce_opportunities(region: str):
    # REFERENCE to vault (not actual secret!)
    token = "{{vault:salesforce/api_token}}"
    url = "{{vault:salesforce/instance_url}}"
    
    # Use secrets
    response = requests.get(
        f"{url}/api/opportunities",
        headers={"Authorization": f"Bearer {token}"}
    )
    return response.json()
```

**3. Runtime Secret Injection**

```python
# Platform execution engine

def execute_tool_with_secrets(tool_code, vault_refs):
    """Replace vault references with actual secrets"""
    
    # Parse code for vault references
    vault_refs = find_vault_references(tool_code)
    # Returns: ["{{vault:salesforce/api_token}}", ...]
    
    # Fetch secrets from vault
    secrets = {}
    for ref in vault_refs:
        secret_path = extract_path(ref)  # "salesforce/api_token"
        secrets[ref] = vault.get_secret(secret_path)
    
    # Replace in code
    # "{{vault:salesforce/api_token}}" → "sfdx_abc123..."
    executable_code = tool_code
    for ref, actual_secret in secrets.items():
        executable_code = executable_code.replace(ref, actual_secret)
    
    # Execute with secrets injected
    exec(executable_code)
```

**4. Security Measures**

- ✅ Secrets never stored in tool code (only references)
- ✅ Secrets never logged (redacted in traces)
- ✅ Secrets injected only at runtime
- ✅ Short-lived: Secrets fetched fresh for each execution
- ✅ Access control: Tools only access secrets they're authorized for
- ✅ Audit trail: All vault accesses logged

**Example: Secret Rotation**

```
Day 1: Salesforce token = "sfdx_old123"
       Tool code: "{{vault:salesforce/api_token}}"
       Runtime: Fetches "sfdx_old123"

Day 30: Admin rotates token in vault
        New token = "sfdx_new456"
        Tool code: UNCHANGED (still "{{vault:...}}")
        Runtime: Automatically fetches "sfdx_new456"

✅ Zero code changes needed!
✅ All tools automatically use new token
```

---

# Agentic Foundry Complete Notes - Part 3

## Deployment & Infrastructure (Continued)

### When to Choose Each Platform

**CHOOSE AGENTIC FOUNDRY WHEN:**
- ✅ Need enterprise features (governance, approvals)
- ✅ Want low-code/no-code agent creation
- ✅ Need built-in evaluation framework
- ✅ Want MCP + Python tools in one platform
- ✅ Have budget for platform license
- ✅ Need pre-built industry templates
- ✅ Want fast time-to-production (hours/days)
- ✅ Team has limited AI/ML expertise

**CHOOSE LANGSMITH/LANGCHAIN WHEN:**
- ✅ Already using LangChain ecosystem
- ✅ Need detailed prompt tracking
- ✅ Want community-driven tools/integrations
- ✅ Comfortable with code-first approach
- ✅ Need complex agent chains (LangGraph)

**CHOOSE OPENAI ASSISTANTS WHEN:**
- ✅ Simple use case (single-purpose agent)
- ✅ OpenAI models sufficient (no need for others)
- ✅ Want managed service (no infrastructure)
- ✅ Don't need MCP integration
- ✅ Low query volume

**CHOOSE AGENT SDK + FASTMCP (DIY) WHEN:**
- ✅ Need complete control over architecture
- ✅ Have experienced AI/ML engineering team
- ✅ Want zero vendor lock-in
- ✅ Custom requirements not met by platforms
- ✅ Want to integrate with existing systems deeply
- ✅ Have time for development (weeks/months)
- ✅ Budget for engineering time > platform cost

---

## Complete Questions & Answers

### Answered Questions

#### Q1: What is score threshold?
**Answer:**
Score threshold is the minimum passing grade an agent must achieve on evaluation metrics before being allowed to deploy to production.

**How it works:**
- Organization sets thresholds (e.g., TF-IDF ≥85%, SBERT ≥90%)
- Agent is evaluated against test cases
- If ALL metrics pass thresholds → ✅ Deploy allowed
- If ANY metric fails → ❌ Deployment blocked

**Example:**
```
Financial agent: Very strict (95%+ required)
Customer support: Moderate (75-90%)
Internal tools: Lenient (60-70%)
```

---

#### Q2: What are the three MCP server types?
**Answer:**

**1. CODE Servers**
- You write Python code in platform
- Platform packages and hosts it
- Use for: Custom business logic, internal systems

**2. ACTIVE Servers**
- External MCP server already running
- You provide URL and connect
- Use for: Third-party services (GitHub, Microsoft), other team's servers

**3. MODULE Servers**
- Distributed as packages (npm, pip, Docker)
- Platform installs and runs it
- Use for: Open-source tools, community MCP servers

---

#### Q3: How does episodic memory work?
**Answer:**

**Storage:**
```
User gives feedback (👍/👎) → Stored in database
  Fields:
  - query
  - response
  - feedback (positive/negative)
  - user comment
  - timestamp
```

**Retrieval:**
```
Next similar query → Platform searches episodic memory
  Finds relevant past feedback
  Injects learnings into system prompt
  Agent applies lessons
```

**Example:**
```
First time: Agent says "2500000" → User 👎 "Format with commas!"
Stored: "Always format currency with commas"

Next time: Agent says "$2,500,000" → User 👍
Memory confirmed and reinforced
```

---

#### Q4: Can Agentic Foundry MCP servers be used by other MCP clients (like Claude Code)?
**Answer:**
**Likely YES, but not explicitly confirmed in presentation.**

**Reasoning:**
- CODE servers are packaged as HTTP MCP servers
- They follow MCP protocol standard
- If exposed with proper authentication, any MCP client should be able to consume them

**What we know:**
- ✅ Can expose as HTTP endpoints
- ✅ Use bearer token authentication
- ⚠️ Need to confirm: Are they fully MCP-spec compliant for external clients?

**Question to ask Infosys:**
"Can MCP servers created in Agentic Foundry be consumed by external MCP clients like Claude Code, or are they only for internal use within Agentic Foundry agents?"

---

### Open Questions (Still Need Answers)

#### High Priority

**Q5: Agent-to-Agent Communication (A2A Protocol)**
- How do multiple agents communicate in "Agents of Agents" template?
- Is there a coordinator agent?
- What protocol is used (A2A standard or custom)?
- How is state shared between agents?

**Q6: CODE Server Deployment Details**
- After approval, what exact HTTP endpoint format is generated?
- Show example curl command to call a deployed CODE server
- Can you version CODE servers (v1, v2, etc.)?
- How do you roll back to previous version?

**Q7: Vault Implementation**
- What vault backend is used (HashiCorp, Azure Key Vault, custom)?
- How are secrets rotated without downtime?
- Are secrets scoped per-team or organization-wide?
- Can MODULE and ACTIVE servers access vault?

**Q8: Claude Agent SDK Integration Timeline**
- When will Claude SDK be integrated?
- Will it support sub-agent orchestration?
- **Can you share the Claude SDK analysis report?** (They offered!)
- How will Claude agents use existing Agentic Foundry tools?

**Q9: Complete API Documentation**
- What's the exact API endpoint format?
- Share example API request/response with authentication
- How does human-in-the-loop work via API?
- What's the API response when agent pauses for input?

**Q10: Export Agent with MCP Servers**
- When you export an agent that uses MCP servers, what happens?
- Are MCP server configs bundled?
- Do you need to redeploy MCP servers separately?
- How do you configure MCP endpoints for different environments (dev/prod)?

#### Medium Priority

**Q11: Prompt Optimization Algorithm**
- How does Pareto sampling work for prompt optimization?
- What's the typical improvement range (5%? 20%?)?
- How many iterations are recommended?
- Can you manually intervene during optimization?

**Q12: Canvas AI Technical Details**
- Is this OpenAI's native Canvas or custom implementation?
- When calling via API, what's the response format for Canvas output?
- Can external clients render Canvas visualizations?
- What chart types are supported?

**Q13: Tool Selection Logic**
- When agent has 20+ tools, what algorithm decides which to use?
- Is it pure LLM reasoning or is there a separate selection model?
- Can you force/bias tool selection (prefer tool A over tool B)?
- How do you debug wrong tool selection?

**Q14: Evaluation Metrics Deep Dive**
- What's the recommended number of test cases for ground truth evaluation?
- Can you test multi-turn conversations (not just single Q&A)?
- How does the LLM judge get context about what's "correct"?
- Show example of tool efficiency report with retry patterns

**Q15: Pre-built Template Agents**
- How many template agents are available?
- Can you show code/config for one template (e.g., SQL agent)?
- Are templates open-source or proprietary?
- Can you customize templates or only use as-is?

---

## Implementation Roadmap for Your Office

### Phase 1: Proof of Concept (Weeks 1-2)

**Goal:** Validate Agentic Foundry + MCP for one simple use case

**Steps:**

1. **Set up environment**
   - Get Agentic Foundry access (trial/demo)
   - Provision Azure/AWS infrastructure
   - Set up vault for secrets

2. **Create first agent**
   - Use case: Simple data query agent
   - Tool: SQL database connector (CODE server)
   - Test with 10-20 queries
   - Evaluate with ground truth testing

3. **Add one MCP server**
   - Option A: Use existing MODULE (e.g., Time server)
   - Option B: Create simple CODE server (e.g., internal API wrapper)
   - Connect to agent
   - Test integration

4. **Measure success**
   - Time savings vs manual process
   - Accuracy (evaluation scores)
   - User feedback (thumbs up/down)

**Deliverable:** Working agent + report on feasibility

---

### Phase 2: Pilot Deployment (Weeks 3-6)

**Goal:** Deploy 2-3 production agents for specific business problems

**Recommended Use Cases:**

**Option A: Customer Support Automation**
```
Agent: "Support Ticket Analyzer"
Tools:
  - Customer DB lookup (CODE server)
  - Ticket history (CODE server)
MCP Servers:
  - Zendesk MCP (ACTIVE)
  - Slack MCP (MODULE)
Human-in-Loop: Enabled
Expected Impact: 40% reduction in simple ticket handling time
```

**Option B: Sales Data Analysis**
```
Agent: "Sales Insights Agent"
Tools:
  - SQL query generator (CODE server)
  - Chart creator (Python tool)
MCP Servers:
  - Salesforce MCP (if available, or create CODE server)
Canvas AI: Enabled
Expected Impact: Dashboards in seconds instead of hours
```

**Option C: Document Processing**
```
Agent: "Contract Analyzer"
Tools:
  - PDF reader (CODE server)
  - SharePoint connector (Graph API via CODE server)
MCP Servers:
  - Microsoft Graph MCP (if available)
Expected Impact: 80% faster contract review
```

**Steps:**

1. **Build agents**
   - Create tools and MCP servers
   - Configure agents with appropriate templates
   - Set up governance (QA approval for each)

2. **Evaluate thoroughly**
   - Ground truth testing (50+ test cases per agent)
   - LLM as judge evaluation
   - Set score thresholds (85-90% for production)

3. **Deploy to pilot users**
   - 5-10 users per agent
   - Collect feedback daily
   - Monitor metrics (latency, cost, satisfaction)

4. **Iterate based on feedback**
   - Use episodic memory to improve
   - Optimize prompts if needed
   - Add missing tools

**Deliverables:**
- 3 production agents
- Evaluation reports
- User feedback summary
- Cost analysis

---

### Phase 3: Scale & Optimize (Weeks 7-12)

**Goal:** Roll out to wider organization, add more agents

**Steps:**

1. **Export agents for production infrastructure**
   - Export to Docker containers
   - Deploy to Kubernetes (AKS)
   - Set up autoscaling (5-10 pods)
   - Configure monitoring (Prometheus, Grafana)

2. **Build MCP server library**
   - Identify common needs across teams
   - Create reusable CODE servers
   - Publish to "common" (enterprise-wide)
   - Examples:
     - SharePoint MCP (Graph API)
     - Internal database MCP
     - HR system MCP
     - ERP system MCP

3. **Create team-specific agents**
   - Finance team: Budget analysis agent
   - HR team: Employee onboarding agent
   - Engineering team: Code review agent
   - Each team uses shared MCP servers + custom tools

4. **Implement governance**
   - QA team reviews all agents
   - Admin approval required for production
   - Regular evaluation (monthly LLM-as-judge reviews)
   - Cost tracking and alerts

**Deliverables:**
- 10+ production agents
- 5+ shared MCP servers
- Monitoring dashboard
- Governance documentation

---

### Phase 4: Advanced Features (Weeks 13+)

**Goal:** Implement advanced workflows and optimizations

**Advanced Use Cases:**

1. **Agents of Agents**
   ```
   Main Agent: "Project Kickoff Coordinator"
   Sub-agents:
     - Jira Agent (creates epics, stories)
     - Code Agent (sets up repos, branches)
     - Docs Agent (generates project docs)
     - Notification Agent (alerts team)

   User: "Start new project: Mobile App Redesign"
   Coordinator delegates to all sub-agents in parallel
   ```

2. **Cross-System Workflows**
   ```
   Agent: "Order Fulfillment Orchestrator"
   Workflow:
     1. Check inventory (ERP MCP)
     2. Create sales order (CRM MCP)
     3. Generate invoice (Billing CODE server)
     4. Send confirmation (Email tool)
     5. Update dashboard (Canvas AI)
   Human approval: Required for orders > $10K
   ```

3. **Proactive Agents**
   ```
   Agent: "Anomaly Detector"
   Runs on schedule: Every hour
   Checks:
     - Sales data for unusual patterns
     - System metrics for anomalies
     - Budget variances
   Actions:
     - Creates Jira tickets for issues
     - Notifies relevant teams via Slack
     - Generates investigation reports
   ```

**Steps:**

1. **Optimize costs**
   - Switch to smaller models where possible (GPT-3.5 for simple tasks)
   - Cache common queries
   - Batch processing where applicable

2. **Improve agent quality**
   - Periodic prompt optimization
   - Episodic memory analysis (what are users teaching agents?)
   - A/B testing different agent versions

3. **Build internal MCP ecosystem**
   - Encourage teams to publish MCP servers
   - Cross-team collaboration via shared servers
   - Reusability reduces duplicate work

4. **Knowledge sharing**
   - Document best practices
   - Train more teams on platform
   - Share success stories

**Deliverables:**
- 20+ production agents
- 10+ MCP servers (CODE + ACTIVE + MODULE)
- Cost optimization report (show savings)
- Training materials for new teams

---

### Success Metrics

**Track these KPIs:**

| Metric | Target (6 months) |
|--------|-------------------|
| **Agents in production** | 15-20 agents |
| **Time savings** | 500+ hours/month |
| **Cost per agent query** | <$0.50 avg |
| **User satisfaction** | >85% thumbs up |
| **Evaluation scores** | >90% SBERT avg |
| **Teams using platform** | 5+ teams |
| **MCP servers (shared)** | 10+ common servers |
| **Queries/day** | 1000+ |

---

## Key Takeaways & Recommendations

### What Makes Agentic Foundry Unique

1. **Enterprise-First Design**
   - Governance and approval workflows built-in
   - Not an afterthought like other platforms
   - Critical for large organizations

2. **MCP Native Integration**
   - Three server types (CODE, ACTIVE, MODULE)
   - Governance for MCP servers
   - Can work independently of Agentic Foundry

3. **Low-Code/No-Code**
   - Business analysts can create agents
   - Reduces dependency on AI/ML team
   - Faster time-to-production

4. **Built-in Evaluation**
   - Ground truth testing
   - LLM as judge
   - Score thresholds prevent bad agents from going live
   - Most platforms lack this

5. **Episodic Memory**
   - Agents learn from user feedback
   - Gets better over time automatically
   - Unique feature not common in other platforms

6. **Flexibility**
   - Use hosted or export to your infrastructure
   - Model-agnostic (not locked to OpenAI)
   - Can switch models at runtime

---

### Potential Concerns & Mitigations

**Concern 1: Vendor Lock-in**
- **Risk:** Platform proprietary to Infosys
- **Mitigation:** Export agents to Docker (can run independently)
- **Mitigation:** MCP servers follow open standard
- **Strategy:** Start with small pilot, evaluate alternatives

**Concern 2: Cost**
- **Risk:** Platform licensing + LLM API costs
- **Mitigation:** Calculate ROI (time savings vs cost)
- **Mitigation:** Start small, scale based on value
- **Comparison:** vs hiring developers for custom build

**Concern 3: Learning Curve**
- **Risk:** Team needs to learn platform
- **Mitigation:** GUI makes it easier than code-first
- **Mitigation:** Infosys provides training/support
- **Timeline:** 1-2 weeks for basic proficiency

**Concern 4: Integration Complexity**
- **Risk:** Connecting to existing systems
- **Mitigation:** MCP standard makes it easier
- **Mitigation:** CODE servers for custom integrations
- **Support:** Leverage pre-built templates

---

### Recommendations for Your Office

**Do This:**
1. ✅ Start with proof-of-concept (1-2 agents)
2. ✅ Focus on high-value use cases (big time savings)
3. ✅ Build MCP server library early (reusability)
4. ✅ Involve users from day 1 (feedback crucial)
5. ✅ Set up monitoring from the start
6. ✅ Document everything (knowledge sharing)

**Avoid This:**
1. ❌ Don't build too many agents too fast (quality > quantity)
2. ❌ Don't skip evaluation (score thresholds critical)
3. ❌ Don't ignore cost tracking (can get expensive)
4. ❌ Don't deploy without QA approval (governance matters)
5. ❌ Don't forget to optimize prompts (iteration improves results)
6. ❌ Don't neglect episodic memory (user feedback gold mine)

---

### Next Steps

**Immediate (This Week):**
1. Contact Infosys for demo/trial access
2. Identify 2-3 pilot use cases
3. Form pilot team (1-2 developers + 1 QA + business user)
4. Set up evaluation criteria (what metrics matter?)

**Short Term (Next Month):**
1. Complete POC with 1 agent
2. Measure results (time, cost, quality)
3. Present findings to stakeholders
4. Decide: Go forward or explore alternatives?

**Long Term (Next Quarter):**
1. If approved: Roll out to 3-5 use cases
2. Build MCP server library
3. Train additional teams
4. Share success stories

---

## Glossary of Terms

**Agent:**
An AI assistant composed of LLM + tools + system prompt. Can perform tasks autonomously.

**Agent Template:**
Pre-configured agent pattern (React, Plan-Verify, etc.). Determines how agent reasons and acts.

**Agents of Agents:**
Multiple specialized agents working together, coordinated by a main agent.

**ACTIVE Server (MCP):**
External MCP server already running. You connect to it via URL.

**Canvas AI:**
Interactive visual output (charts, tables, dashboards) instead of plain text.

**CODE Server (MCP):**
MCP server you create by writing Python code in platform. Platform hosts it for you.

**Episodic Memory:**
System that stores user feedback and applies learnings to future interactions.

**Ground Truth Evaluation:**
Testing agent against known correct answers to measure accuracy.

**Human-in-the-Loop:**
Workflow where agent pauses for human approval before taking action.

**JAKAD Similarity:**
Character-level similarity metric used in evaluation.

**LLM:**
Large Language Model (GPT-4, Claude, Llama, etc.). The "brain" of the agent.

**LLM as Judge:**
Using a better/different LLM to evaluate another agent's performance.

**MCP (Model Context Protocol):**
Open standard for exposing tools to AI systems. Like HTTP for AI tools.

**MODULE Server (MCP):**
MCP server distributed as package (npm, pip). Platform installs and runs it.

**Pareto Sampling:**
Optimization technique used in prompt optimization to generate variations.

**Plan-Verify Template:**
Agent template where agent creates plan, user approves, then agent executes.

**React Template:**
Agent template: Reason → Act → Observe → Repeat. Most common pattern.

**SBERT:**
Semantic similarity metric (compares meaning, not exact words).

**Score Threshold:**
Minimum evaluation score required to deploy agent to production.

**Session:**
Single conversation between user and agent. Has unique session_id.

**System Prompt:**
Instructions that define agent's identity, capabilities, and behavior.

**TF-IDF:**
Text similarity metric (compares word-by-word matching).

**Tool:**
Function that gives agent capabilities (database query, API call, etc.).

**Tool Selection:**
Process by which agent decides which tool(s) to use for a query.

**Vault:**
Secure storage for secrets (API keys, passwords, tokens).

**Visibility Levels:**
Permission settings for MCP servers (Private, Team, Common).

---

## Additional Resources

### Documentation (Ask Infosys for):
- Platform user guide
- API documentation
- MCP server creation guide
- Agent template reference
- Evaluation framework guide
- Deployment best practices

### Internal Reports (Ask Infosys for):
- Claude Agent SDK integration analysis (they offered to share!)
- OpenAI Agent Framework comparison
- Cost optimization case studies
- Client success stories

### Training:
- Request hands-on training session
- Ask for sandbox environment
- Request sample agents to study
- Ask for video tutorials

---

## Contact & Follow-up

**Questions to Ask Infosys:**

1. "Can you share the Claude SDK integration analysis report?"
2. "What's the typical licensing cost for 10-20 agents?"
3. "Can Agentic Foundry MCP servers be consumed by external clients like Claude Code?"
4. "Do you have case studies for similar-sized companies?"
5. "What support/training is included?"
6. "Can we get a 30-day trial with full features?"
7. "What's the typical onboarding timeline?"
8. "Are there any industry-specific templates for [your industry]?"

**Information to Provide Them:**

1. Your use cases (be specific)
2. Current pain points (what takes too long?)
3. Expected query volume (queries/day estimate)
4. Team size (how many people will use it?)
5. Infrastructure (cloud provider, existing tech stack)
6. Timeline (when do you need this in production?)
7. Budget constraints (if any)

---

## Conclusion

**Agentic Foundry is a comprehensive enterprise platform for building, deploying, and managing AI agents at scale.**

**Key Strengths:**
- ✅ Enterprise features (governance, evaluation, templates)
- ✅ MCP native integration (three server types)
- ✅ Low-code/no-code (accessible to non-experts)
- ✅ Flexible deployment (hosted or self-hosted)
- ✅ Episodic memory (continuous learning)

**Comparison to DIY (Agent SDK + FastMCP):**
- **Agentic Foundry:** Faster time-to-market, less dev work, higher platform cost
- **DIY:** Full control, no vendor lock-in, more dev work, lower platform cost

**Recommendation:**
- Start with POC to validate value
- If ROI positive and team prefers managed platform → Choose Agentic Foundry
- If need full control and have strong eng team → Consider DIY with Agent SDK

**The MCP integration is the killer feature:**
- Standardized tool ecosystem
- Reusability across teams
- Can work independently of Agentic Foundry
- Future-proof (MCP is open standard)

**Final Thought:**
The combination of Agentic Foundry's enterprise features + MCP's open standard creates a powerful platform for scaling AI agents across your organization. The key is starting small, proving value, and scaling based on results.

---

**END OF NOTES**

*These notes represent a comprehensive summary of the Infosys Agentic Foundry presentation and demo, supplemented with detailed explanations, real-world examples, technical implementation details, and recommendations for office implementation.*

*Created: 2025-10-10*
*Last Updated: 2025-10-10*
*Version: 1.0*
