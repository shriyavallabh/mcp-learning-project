# Agentic Foundry - Quick Reference Summary

**Full detailed notes:** `AGENTIC_FOUNDRY_COMPLETE_NOTES.md` (4,318 lines)

---

## What is Agentic Foundry?

Enterprise platform by Infosys for building, testing, deploying, and monitoring AI agents at scale.

**Think of it as:** "WordPress for AI Agents"

---

## Core Components

### 1. Agent = LLM + Tools + System Prompt
- **LLM:** The brain (GPT-4, Claude, Llama - switchable)
- **Tools:** Python functions, MCP servers, APIs
- **System Prompt:** Auto-generated instructions

### 2. The Four Pillars
1. **Tool Onboarding:** Create reusable skills
2. **Agent Creation:** Combine tools into agents
3. **Evaluation:** Test before production (score thresholds)
4. **Prompt Optimization:** Auto-improve system prompts

### 3. MCP Platform (Standalone)
Three types of MCP servers:
- **CODE:** Write Python, platform hosts it
- **ACTIVE:** External URL, you connect to it
- **MODULE:** Install packages (npm/pip)

---

## Key Features

✅ **Low-code/no-code** (GUI-based agent creation)
✅ **Built-in evaluation** (Ground truth + LLM as judge)
✅ **Episodic memory** (Learns from user feedback)
✅ **Human-in-the-loop** (Approval workflows)
✅ **Canvas AI** (Interactive dashboards)
✅ **Export agents** (Docker/Kubernetes)
✅ **Governance** (QA approval, access control)
✅ **Model-agnostic** (Switch models anytime)

---

## Real-World Use Cases from Presentation

1. **Project Audit Automation** (Infosys internal)
   - Before: 2-4 hours per audit
   - After: 45 seconds
   - Impact: 99% faster, 90% fewer errors

2. **Supply Chain Risk Assessment**
   - Before: 2-3 days
   - After: 2 minutes
   - Checks: SAP, Salesforce, credit scores, news

3. **Sales Dashboard Creation**
   - Before: 3-4 hours by analyst
   - After: 30 seconds self-service
   - Impact: Managers create own dashboards

4. **Test Data Generation**
   - Before: 2-3 hours for 100 records
   - After: 20 seconds for 1000+ records
   - Quality: Schema-compliant, realistic

5. **Customer Support Automation**
   - Before: 45 min avg response
   - After: 5 seconds (agent) / 5 min (human for complex)
   - Impact: 60% of tickets auto-handled

---

## MCP Integration (Critical Feature!)

### Three Server Types

**CODE Servers:**
```
You → Write Python code in UI
Platform → Packages as HTTP MCP server
Result → https://mcp.company.com/your-server
```

**ACTIVE Servers:**
```
External MCP already running (GitHub, Microsoft)
You → Provide URL
Platform → Connects to it
```

**MODULE Servers:**
```
npm/pip package
Platform → Installs and runs
Example → Time zone helper, weather API
```

### Visibility Levels
- **Private:** Only you (draft mode)
- **Team:** Your team members
- **Common:** Everyone in company

---

## Deployment Options

| Option | Who Manages | Best For |
|--------|-------------|----------|
| **Hosted** | Infosys | POC, no infra team |
| **Docker Export** | You | Custom infra, full control |
| **Kubernetes** | You | High traffic, HA required |

### Sizing Guide
- **Low (<100 queries/day):** 1 container, $50/mo
- **Medium (100-1000/day):** 2-3 containers, $200-300/mo
- **High (1000+/day):** K8s 5-10 pods, $1000-2000/mo

---

## Evaluation Framework

### Ground Truth Testing
1. Upload Excel with test cases (Q&A pairs)
2. Agent processes each test case
3. Compare actual vs expected
4. Calculate scores: TF-IDF, SBERT, JAKAD
5. Pass/fail based on thresholds

### Score Thresholds
```
High-stakes (Financial): 95%+ required
Medium-stakes (Support): 75-90%
Low-stakes (Internal): 60-70%
```

If agent fails → ❌ Blocked from production

### LLM as Judge
- Use GPT-5 to evaluate GPT-4 agent
- Analyzes tool selection, efficiency, quality
- Runs on production data (periodic audits)

---

## Episodic Memory

**How it works:**
```
User: "Show sales" → Agent: "2500000" → User: 👎 "Format it!"
↓
Stored in memory: "Always format currency"
↓
Next query → Agent: "$2,500,000" → User: 👍
↓
Learning reinforced
```

**Benefits:**
- Agents improve over time
- No code changes needed
- Applies across all users

---

## Agent Templates

1. **React:** Reason → Act → Observe → Repeat (most common)
2. **Plan-Verify:** Create plan → User approves → Execute
3. **Meta Planner:** Plans how other agents should work
4. **Hybrid:** Mix of templates
5. **Agents of Agents:** Multiple specialized agents working together

---

## Comparison: Agentic Foundry vs Alternatives

| Feature | Agentic Foundry | LangSmith | OpenAI Assistants | Agent SDK (DIY) |
|---------|----------------|-----------|-------------------|-----------------|
| **GUI Builder** | ✅ Full | ⚠️ Limited | ✅ Yes | ❌ No |
| **MCP Support** | ✅ Native (3 types) | ✅ Via integration | ❌ No | ✅ Native (DIY) |
| **Evaluation** | ✅ Built-in | ✅ Yes | ⚠️ Basic | ❌ Build yourself |
| **Deployment** | ✅ Export anywhere | ⚠️ Limited | ☁️ Cloud only | ✅ Full control |
| **Model Flexibility** | ✅ Any | ✅ Any | ❌ OpenAI only | ✅ Any |
| **Governance** | ✅ Built-in | ⚠️ Basic | ⚠️ Basic | ❌ Build yourself |
| **Time to Prod** | ⏱️ Hours | ⏱️ Days | ⏱️ Hours | ⏱️ Weeks |
| **Vendor Lock-in** | ⚠️ Medium | ⚠️ Medium | ❌ High | ✅ None |

---

## When to Choose Agentic Foundry

✅ **Choose Agentic Foundry if:**
- Need enterprise features (governance, approvals)
- Want low-code/no-code agent creation
- Need built-in evaluation
- Want fast time-to-market (hours/days)
- Team has limited AI/ML expertise
- Have budget for platform license

❌ **Don't choose if:**
- Need complete control over architecture
- Have experienced AI/ML eng team
- Want zero vendor lock-in
- Custom requirements not met by platform
- Budget for eng time > platform cost

---

## Implementation Roadmap (Your Office)

### Phase 1: POC (Weeks 1-2)
- Create 1 simple agent
- Test with 10-20 queries
- Measure time/cost/quality

### Phase 2: Pilot (Weeks 3-6)
- Deploy 2-3 production agents
- 5-10 pilot users per agent
- Build first MCP servers

### Phase 3: Scale (Weeks 7-12)
- Export to K8s (5-10 pods)
- 10+ production agents
- 5+ shared MCP servers
- Full monitoring setup

### Phase 4: Advanced (Weeks 13+)
- Agents of agents
- Cross-system workflows
- 20+ agents, 10+ MCP servers

---

## Key Metrics to Track

| Metric | Target (6 months) |
|--------|-------------------|
| Agents in production | 15-20 |
| Time savings | 500+ hrs/month |
| Cost per query | <$0.50 |
| User satisfaction | >85% 👍 |
| Evaluation scores | >90% SBERT |
| Teams using platform | 5+ |
| MCP servers (shared) | 10+ |

---

## Top 10 Questions to Ask Infosys

1. Can you share Claude SDK integration analysis? **(They offered!)**
2. What's licensing cost for 10-20 agents?
3. Can Agentic Foundry MCP servers be consumed by external clients (Claude Code)?
4. Case studies for similar companies?
5. Support/training included?
6. 30-day trial with full features?
7. Typical onboarding timeline?
8. Industry-specific templates for [your industry]?
9. How does agent-to-agent communication work (A2A protocol)?
10. What vault backend is used (HashiCorp, Azure KV)?

---

## Important Concepts (Quick Reference)

**Agent:** LLM + Tools + System Prompt

**MCP:** Model Context Protocol (open standard for AI tools)

**CODE Server:** You write Python, platform hosts as MCP server

**ACTIVE Server:** External MCP server, you connect via URL

**MODULE Server:** Install via npm/pip, platform runs it

**Episodic Memory:** Learns from user feedback (👍/👎)

**Ground Truth:** Test agent against known correct answers

**Score Threshold:** Minimum score to deploy (e.g., 85% TF-IDF)

**Canvas AI:** Interactive visual output (charts, dashboards)

**Human-in-Loop:** Agent pauses for approval before action

**React Template:** Reason → Act → Observe → Repeat

**Plan-Verify:** Create plan → Approve → Execute

**Vault:** Secure storage for secrets (never hardcode!)

---

## Critical Success Factors

### Do This ✅
1. Start with POC (1-2 agents)
2. Focus on high-value use cases
3. Build MCP server library early
4. Involve users from day 1
5. Set up monitoring from start
6. Document everything

### Avoid This ❌
1. Don't build too many agents too fast
2. Don't skip evaluation
3. Don't ignore cost tracking
4. Don't deploy without QA approval
5. Don't forget prompt optimization
6. Don't neglect episodic memory

---

## Final Recommendation

**Start with proof-of-concept:**
- 1 agent, 1 use case
- 2 weeks, small team
- Measure ROI (time/cost/quality)
- Present findings

**If ROI positive:**
- Agentic Foundry = Fast time-to-market, managed service
- DIY (Agent SDK) = Full control, no lock-in

**The killer feature:**
- **MCP integration** (three server types)
- Standardized tool ecosystem
- Reusability across teams
- Future-proof (open standard)

---

## Contact Info

**For detailed information:**
- Read full notes: `AGENTIC_FOUNDRY_COMPLETE_NOTES.md`
- Contact Infosys team (presenter from demo)
- Request demo/trial access

**Next Steps:**
1. Schedule follow-up with Infosys
2. Identify 2-3 pilot use cases
3. Form pilot team (dev + QA + business user)
4. Get trial access and start POC

---

**Document Created:** 2025-10-10
**Summary of:** 4,318-line comprehensive notes
**Source:** Infosys Agentic Foundry Presentation & Demo
