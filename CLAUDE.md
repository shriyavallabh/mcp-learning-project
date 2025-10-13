# IMPORTANT TEACHING INSTRUCTIONS FOR MCP TUTORIAL

## Python Code Explanation Requirements
When explaining Python code to the user, ALWAYS:

1. **Explain EVERY line in extreme detail**
2. **Identify what each element is:**
   - Is it a variable? (storing data)
   - Is it a class? (blueprint for objects)
   - Is it an object? (instance of a class)
   - Is it a function? (reusable code block)
   - Is it a method? (function inside a class)
   - Is it a decorator? (@ symbol - modifies functions)
   - Is it a for loop? (repeating code)
   - Is it a module import? (bringing in code from elsewhere)

3. **For variable names like `client`:**
   - Explain it's just a variable NAME (could be anything)
   - `client = MCP_Client()` means: "client" is just our chosen name to store the MCP_Client object
   - Could have been `my_connection` or `mcp` or `x` - it's just a label

4. **Be EXTREMELY verbose about:**
   - What each parenthesis means
   - What each dot notation means (object.method)
   - What each bracket means
   - What quotes mean (string vs variable)
   - What indentation means (code blocks)

5. **Example format:**
```python
client = MCP_Client("localhost:5000")
```
Explain as:
- `client` = This is a VARIABLE NAME (just a label we chose, like naming a pet)
- `=` = Assignment operator (puts something into the variable)
- `MCP_Client` = This is a CLASS (blueprint/template)
- `()` = Parentheses mean we're CREATING an object from the class
- `"localhost:5000"` = String (text) parameter - the quotes make it text, not code
- This whole line: Creates a new MCP_Client object and stores it in a variable we decided to call "client"

## Topics to Cover Based on Demo Discussion

### Must Explain:
1. Complete MCP interaction cycle with detailed diagrams
2. How client discovers which of 20 tools to use
3. Resource definitions vs tool definitions
4. FastMCP library usage
5. MCP-O (OpenAPI to MCP proxy converter)
6. Streamable MCP server on AKS
7. Agent-to-agent protocol
8. MCP server invoking agents
9. LLM as part of MCP server (is it possible?)
10. Docker file vs Docker image (clear difference)
11. deployment.yml for AKS
12. Deterministic vs non-deterministic responses
13. Guardrails in MCP

### Clarify Misconceptions:
- MCP servers do NOT contain LLMs (usually)
- LLM is typically the CLIENT, not part of server
- Non-deterministic responses come from LLM client, not MCP server
- MCP server responses are deterministic (same input = same output)

### Always Remember:
- User has limited Python knowledge
- User needs EXTREME detail on every concept
- User learns best with diagrams and real examples
- User wants to implement this at office
- User needs to understand WHY, not just HOW