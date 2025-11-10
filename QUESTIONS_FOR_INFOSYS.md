# Questions for Infosys - Agentic Foundry

**Prepared:** October 10, 2025
**Source:** Analysis of Agentic Foundry presentation
**Status:** Ready for follow-up meeting

---

## 🔥 TOP PRIORITY QUESTIONS (Must Ask!)

### 1. Claude SDK Integration
**Question:** "You mentioned analyzing Claude Agent SDK integration. Can you share that analysis report?"
**Why important:** Need to understand if/how Claude integration will work
**Context:** They explicitly offered to share this during demo

### 2. MCP Interoperability
**Question:** "Can MCP servers created in Agentic Foundry be consumed by external MCP clients like Claude Code?"
**Why important:** Critical for avoiding vendor lock-in and ecosystem interoperability
**Follow-up:** "Are they fully MCP-spec compliant for external use?"

### 3. Pricing Model
**Question:** "What's the licensing cost for 10-20 agents in production?"
**Why important:** Need for budget planning
**Follow-ups:**
- Is it per-agent, per-user, per-query, or flat fee?
- What's included (hosting, support, training)?
- Any volume discounts?

### 4. Trial Access
**Question:** "Can we get a 30-day trial with full features to run a POC?"
**Why important:** Need hands-on experience before committing
**Follow-up:** "What limitations, if any, on trial?"

### 5. Agent-to-Agent Communication
**Question:** "How exactly do agents communicate in the 'Agents of Agents' template? Are you following the A2A protocol standard?"
**Why important:** Mentioned but not explained in detail
**Follow-up:** "Show example configuration for multi-agent workflow"

---

## 💼 BUSINESS & ROI QUESTIONS

### 6. Case Studies
**Question:** "Do you have case studies for companies similar to ours (size, industry)?"
**Why important:** Validate ROI and success patterns
**Follow-up:** "Can you share metrics (time savings, cost reduction)?"

### 7. Support & Training
**Question:** "What support and training is included?"
**Why important:** Assess total cost of ownership
**Details needed:**
- Onboarding support (how many hours?)
- Ongoing support (SLA, response times?)
- Training materials (videos, docs, workshops?)
- Dedicated account manager?

### 8. Timeline
**Question:** "What's the typical timeline from contract to first agent in production?"
**Why important:** Project planning
**Breakdown needed:**
- Onboarding: X weeks
- Training: X weeks
- First agent: X weeks
- Scaling: X weeks

### 9. Industry Templates
**Question:** "Are there pre-built templates specific to [your industry]?"
**Why important:** Faster time-to-value
**Example:** If finance → "Do you have compliance/audit templates?"

---

## 🔧 TECHNICAL QUESTIONS

### 10. CODE Server Deployment
**Question:** "After a CODE server is approved, what exact HTTP endpoint is generated? Can you show a curl command example?"
**Why important:** Need to understand deployment mechanics
**Follow-up:** "How do you version CODE servers (v1, v2) and rollback?"

### 11. Vault Implementation
**Question:** "What vault backend does Agentic Foundry use - HashiCorp Vault, Azure Key Vault, or custom?"
**Why important:** Integration with existing secrets management
**Follow-ups:**
- How are secrets rotated without downtime?
- Are secrets scoped per-team or org-wide?
- Can MODULE and ACTIVE servers access vault?

### 12. API Documentation
**Question:** "Can you share complete API documentation with example requests/responses?"
**Why important:** Need for integration planning
**Specific needs:**
- Authentication flow
- Invoke agent endpoint
- Human-in-the-loop API workflow
- Session management

### 13. Episodic Memory Architecture
**Question:** "How is episodic memory stored and managed in multi-pod Kubernetes deployments?"
**Why important:** Understanding scalability and state management
**Follow-ups:**
- Database schema for episodic memory?
- How long is memory retained (TTL)?
- Can you view/edit memories via UI?

### 14. Export Agent Details
**Question:** "When you export an agent that uses MCP servers, what happens? Are MCP configs bundled or do we need to redeploy MCP servers separately?"
**Why important:** Understanding deployment independence
**Follow-up:** "Show the complete exported directory structure"

### 15. Tool Selection Logic
**Question:** "When an agent has 20+ tools, what algorithm decides which to use - pure LLM reasoning or separate selection model?"
**Why important:** Understanding how to optimize tool sets
**Follow-up:** "Can you force/bias tool selection or see selection reasoning logs?"

---

## 🎯 EVALUATION & QUALITY QUESTIONS

### 16. Prompt Optimization Details
**Question:** "How does Pareto sampling work in prompt optimization? What's typical improvement range?"
**Why important:** Setting expectations for optimization ROI
**Follow-ups:**
- How many iterations recommended?
- Can you intervene manually during optimization?
- Show before/after examples?

### 17. Evaluation Best Practices
**Question:** "What's the recommended number of test cases for ground truth evaluation?"
**Why important:** Resource planning for QA
**Follow-ups:**
- Can you test multi-turn conversations?
- How do you create test cases for complex agents?
- Show example evaluation report?

### 18. Score Thresholds
**Question:** "Can score thresholds be different per agent type, or are they org-wide?"
**Why important:** Flexibility in quality standards
**Follow-up:** "Who has authority to lower thresholds and is it audited?"

---

## 🚀 DEPLOYMENT & INFRASTRUCTURE QUESTIONS

### 19. Kubernetes Configuration
**Question:** "Can you share an example deployment.yaml for a production agent on AKS?"
**Why important:** Infrastructure planning
**Follow-ups:**
- How does autoscaling work (triggers, limits)?
- How is episodic memory shared across pods?
- Resource requirements per pod?

### 20. Monitoring Integration
**Question:** "What monitoring tools integrate with Agentic Foundry (Prometheus, Grafana, Azure Monitor)?"
**Why important:** Observability requirements
**Follow-ups:**
- What metrics are exposed?
- Can you see tool call traces?
- Show example dashboard?

### 21. Canvas AI Technical Details
**Question:** "Is Canvas AI OpenAI's native implementation or custom? What's the API response format?"
**Why important:** Understanding output capabilities
**Follow-ups:**
- Can external clients render Canvas visualizations?
- What chart types supported?
- Show API response example with Canvas data?

---

## 🔐 SECURITY & COMPLIANCE QUESTIONS

### 22. Security Architecture
**Question:** "How does Agentic Foundry handle data security and compliance (GDPR, SOX, HIPAA)?"
**Why important:** Regulatory requirements
**Follow-ups:**
- Data encryption (at rest, in transit)?
- Audit logging capabilities?
- Data residency options?

### 23. Access Control
**Question:** "What are the role-based access control capabilities?"
**Why important:** Governance requirements
**Details needed:**
- Built-in roles (Developer, QA, Admin, User)?
- Custom role creation?
- Team-based isolation?

---

## 📊 COST & LICENSING QUESTIONS

### 24. Cost Breakdown
**Question:** "Break down total cost of ownership: platform license + LLM API costs + infrastructure + support?"
**Why important:** Budget planning
**Example scenario:** "For 20 agents, 1000 queries/day, what's monthly cost?"

### 25. On-Premise vs Cloud
**Question:** "Can Agentic Foundry be deployed fully on-premise, or is there always a cloud component?"
**Why important:** Data residency requirements
**Follow-up:** "What changes with on-premise deployment (features, cost)?"

---

## 🔄 MIGRATION & INTEGRATION QUESTIONS

### 26. Existing System Integration
**Question:** "We have existing [X system]. How easy is it to integrate via CODE servers or MCP?"
**Why important:** Understanding integration effort
**Example:** "Existing internal APIs, legacy databases, SAP, etc."

### 27. Migration from Other Platforms
**Question:** "If we're currently using [LangChain/OpenAI Assistants], how hard is migration to Agentic Foundry?"
**Why important:** Assessing switching costs
**Follow-up:** "Any migration tools or services available?"

---

## 📈 SCALABILITY QUESTIONS

### 28. Scale Limits
**Question:** "What are the practical limits - max agents, max queries/sec, max MCP servers?"
**Why important:** Long-term scalability planning
**Follow-up:** "What happens when you hit limits?"

### 29. Multi-Region Deployment
**Question:** "Can agents be deployed in multiple regions (US, EU, APAC)?"
**Why important:** Global operations
**Follow-up:** "How is episodic memory synchronized across regions?"

---

## 🛠️ DEVELOPER EXPERIENCE QUESTIONS

### 30. Local Development
**Question:** "Can developers run Agentic Foundry locally for development/testing?"
**Why important:** Developer productivity
**Follow-up:** "What are hardware requirements (16GB RAM mentioned)?"

### 31. CI/CD Integration
**Question:** "How does Agentic Foundry integrate with CI/CD pipelines?"
**Why important:** DevOps workflows
**Details needed:**
- API for automated agent deployment?
- Testing in CI pipeline?
- Automated evaluation runs?

### 32. Version Control
**Question:** "How are agents, tools, and prompts version-controlled?"
**Why important:** Change management
**Follow-ups:**
- Git integration?
- Rollback capabilities?
- Diff views for changes?

---

## 🎓 TRAINING & ADOPTION QUESTIONS

### 33. Learning Curve
**Question:** "What's realistic timeline for a team to become proficient?"
**Why important:** Resource planning
**Breakdown:**
- Business analysts: X weeks
- Developers: X weeks
- QA engineers: X weeks

### 34. Community & Documentation
**Question:** "Is there a user community, forum, or knowledge base?"
**Why important:** Self-service support
**Follow-up:** "How active is the community?"

---

## 🔮 FUTURE ROADMAP QUESTIONS

### 35. OpenAI Agent Framework
**Question:** "You mentioned analyzing OpenAI Agent Framework. What's the integration plan and timeline?"
**Why important:** Future capabilities
**Follow-up:** "Which is being prioritized - Claude SDK or OpenAI Framework?"

### 36. Product Roadmap
**Question:** "What new features are planned for next 6-12 months?"
**Why important:** Long-term investment decision
**Follow-up:** "Can we influence roadmap based on our needs?"

---

## 📋 QUESTIONS BY PRIORITY

### 🔴 Must Ask (Critical for Decision)
1. Claude SDK integration analysis report
2. MCP interoperability with external clients
3. Pricing model details
4. Trial access (30 days)
5. Case studies for similar companies

### 🟡 Should Ask (Important for Planning)
6. Support & training included
7. Timeline (contract to production)
8. API documentation
9. Export agent details with MCP
10. Kubernetes deployment examples

### 🟢 Nice to Ask (If Time Permits)
11. Prompt optimization details
12. Canvas AI technical specs
13. Multi-region deployment
14. CI/CD integration
15. Product roadmap

---

## 💡 FOLLOW-UP STRATEGY

### Before Meeting
- [ ] Prioritize questions based on your needs
- [ ] Prepare context for each question
- [ ] Assign questions to team members
- [ ] Prepare to take detailed notes

### During Meeting
- [ ] Record answers (with permission)
- [ ] Ask follow-ups for clarity
- [ ] Request documents/resources
- [ ] Schedule technical deep-dive if needed

### After Meeting
- [ ] Document answers in this file
- [ ] Share with team
- [ ] Identify remaining gaps
- [ ] Schedule follow-up if needed

---

## 📝 ANSWER TEMPLATE

When you get answers, document them like this:

```
Q: [Question]
A: [Answer from Infosys]
Answered by: [Name, date]
Follow-up needed: [Yes/No]
Notes: [Additional context]
```

---

## 🎯 DECISION CRITERIA

Based on answers to these questions, evaluate:

### Go/No-Go Decision Factors
- [ ] Pricing fits budget
- [ ] Timeline acceptable
- [ ] MCP interoperability confirmed
- [ ] Trial successful
- [ ] ROI case clear
- [ ] Technical requirements met
- [ ] Support adequate

### If "Go" - Next Steps
1. Request trial access
2. Form pilot team
3. Identify 2-3 use cases
4. Start POC
5. Measure results
6. Make final decision

### If "No-Go" - Alternatives
1. Explore DIY with Agent SDK
2. Consider LangSmith/LangChain
3. Evaluate OpenAI Assistants
4. Re-assess in 6 months

---

**Prepared by:** Your team
**Date:** October 10, 2025
**Status:** Ready for Infosys meeting
**Total Questions:** 36 organized by priority and category

---

*Use this document as your meeting guide. Print it, share it with your team, and check off questions as they're answered. Good luck!* 🚀
