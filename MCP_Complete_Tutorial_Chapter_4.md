# Chapter 4: The Complete MCP Interaction Cycle

## 🎯 The COMPLETE Interaction Cycle - How It REALLY Works

Let me show you EXACTLY what happens when you type something to Claude:

```
┌──────────────────────────────────────────────────────────────┐
│                     COMPLETE MCP FLOW                         │
├──────────────────────────────────────────────────────────────┤
│                                                                │
│  STEP 1: You type to Claude                                   │
│  ┌─────────────┐                                             │
│  │    YOU      │ "Read my sales report and summarize it"     │
│  └──────┬──────┘                                             │
│         ↓                                                     │
│                                                                │
│  STEP 2: Claude (LLM Client) thinks                          │
│  ┌─────────────────────────────────────┐                    │
│  │         CLAUDE (CLIENT)              │                    │
│  │  "Hmm, user wants to read a file.    │                    │
│  │   Let me check what tools I have..." │                    │
│  └──────┬───────────────────────────────┘                    │
│         ↓                                                     │
│                                                                │
│  STEP 3: Claude asks MCP Server "What can you do?"          │
│  ┌─────────────────────────────────────┐                    │
│  │    REQUEST: List Available Tools     │                    │
│  │    Method: "tools/list"              │                    │
│  └──────┬───────────────────────────────┘                    │
│         ↓                                                     │
│                                                                │
│  STEP 4: MCP Server responds with tool list                  │
│  ┌─────────────────────────────────────┐                    │
│  │        MCP SERVER RESPONSE           │                    │
│  │  Tools available:                    │                    │
│  │  1. read_file                        │                    │
│  │  2. write_file                       │                    │
│  │  3. search_files                     │                    │
│  │  4. delete_file                      │                    │
│  │  ... (16 more tools)                 │                    │
│  └──────┬───────────────────────────────┘                    │
│         ↓                                                     │
│                                                                │
│  STEP 5: Claude picks the right tool                         │
│  ┌─────────────────────────────────────┐                    │
│  │         CLAUDE'S THINKING            │                    │
│  │  "User wants to 'read' a 'report'    │                    │
│  │   Best tool: read_file               │                    │
│  │   I'll use that!"                    │                    │
│  └──────┬───────────────────────────────┘                    │
│         ↓                                                     │
│                                                                │
│  STEP 6: Claude calls the specific tool                      │
│  ┌─────────────────────────────────────┐                    │
│  │    REQUEST: Use Tool                 │                    │
│  │    Method: "tools/call"              │                    │
│  │    Tool: "read_file"                 │                    │
│  │    Args: {path: "sales_report.txt"}  │                    │
│  └──────┬───────────────────────────────┘                    │
│         ↓                                                     │
│                                                                │
│  STEP 7: MCP Server executes the tool                        │
│  ┌─────────────────────────────────────┐                    │
│  │      MCP SERVER EXECUTION            │                    │
│  │  Opening file: sales_report.txt      │                    │
│  │  Reading contents...                  │                    │
│  │  Returning data...                   │                    │
│  └──────┬───────────────────────────────┘                    │
│         ↓                                                     │
│                                                                │
│  STEP 8: Server returns the result                           │
│  ┌─────────────────────────────────────┐                    │
│  │        RESPONSE TO CLAUDE            │                    │
│  │  "Sales Report Q4 2024:              │                    │
│  │   Revenue: $1.2M                     │                    │
│  │   Growth: 15%..."                    │                    │
│  └──────┬───────────────────────────────┘                    │
│         ↓                                                     │
│                                                                │
│  STEP 9: Claude processes and responds to you                │
│  ┌─────────────────────────────────────┐                    │
│  │         CLAUDE TO YOU                │                    │
│  │  "Your Q4 sales report shows:        │                    │
│  │   • Revenue of $1.2M (15% growth)    │                    │
│  │   • Top product: Widget X..."        │                    │
│  └─────────────────────────────────────┘                    │
│                                                                │
└──────────────────────────────────────────────────────────────┘
```

## 🔍 Understanding Tools, Resources, and Prompts

### **1. "Client will invoke tools, resources, prompts"**

Let me explain EACH term with Python code:

```python
# This is what Claude (CLIENT) does internally:

class ClaudeClient:
    def __init__(self):
        # 'self' means "this object's own data"
        # '__init__' is the constructor (runs when object is created)
        self.mcp_connection = None  # Variable to store MCP connection

    def connect_to_mcp(self, server_address):
        # 'def' means we're defining a function
        # 'self' is always first parameter in class methods
        # 'server_address' is a parameter (like "localhost:5000")

        # Creating connection object and storing in variable
        self.mcp_connection = MCPConnection(server_address)
        # The dot (.) means "belonging to" - mcp_connection belongs to self

    def invoke_tool(self, tool_name, parameters):
        # INVOKING A TOOL means calling/using it
        # 'tool_name' is a string like "read_file"
        # 'parameters' is a dictionary like {"path": "/home/file.txt"}

        request = {  # Creating a dictionary (key-value pairs)
            "method": "tools/call",  # The key is "method", value is "tools/call"
            "params": {  # Nested dictionary
                "name": tool_name,  # Using the parameter passed in
                "arguments": parameters
            }
        }
        # Send request and get response
        return self.mcp_connection.send(request)

    def invoke_resource(self, resource_uri):
        # RESOURCES are like bookmarks to data
        # Example: "file:///home/documents/"

        request = {
            "method": "resources/read",
            "params": {"uri": resource_uri}
        }
        return self.mcp_connection.send(request)

    def interpolate_prompt(self, prompt_name, variables):
        # PROMPTS are templates with placeholders
        # Example: "Summarize this: {content}"
        # We fill in the {content} with actual data

        request = {
            "method": "prompts/get",
            "params": {
                "name": prompt_name,
                "arguments": variables  # Fill in the blanks
            }
        }
        return self.mcp_connection.send(request)
```

### **2. "Server will expose tools, resources, prompts"**

```python
class MCPServer:
    def __init__(self):
        # EXPOSE means "make available" or "offer"
        # Like a restaurant menu - showing what's available

        # Dictionary of available tools
        self.tools = {
            "read_file": self.handle_read_file,  # Function reference
            "write_file": self.handle_write_file,
            "search": self.handle_search
        }

        # Dictionary of available resources
        self.resources = {
            "file:///documents/": "/home/user/documents/",
            "database://users": "SELECT * FROM users"
        }

        # Dictionary of prompt templates
        self.prompts = {
            "summarize": "Please summarize the following: {text}",
            "translate": "Translate this to {language}: {text}"
        }

    def expose_capabilities(self):
        # This tells the client what we can do
        return {
            "tools": list(self.tools.keys()),  # ["read_file", "write_file", "search"]
            "resources": list(self.resources.keys()),
            "prompts": list(self.prompts.keys())
        }
```

## 📦 Key Libraries & Terms Explained

### **FastMCP Library**
```python
# FastMCP is a Python library that makes MCP servers EASY to build
# IMPORTANT: FastMCP 1.0 is now part of the official MCP SDK
# FastMCP 2.0 is a separate enhanced version with additional features

# WITHOUT FastMCP (hard way):
class ManualMCPServer:
    def handle_json_rpc(self, message):
        # Parse JSON
        # Route to handler
        # Format response
        # ... lots of code

# WITH FastMCP (using official SDK - recommended):
from mcp.server.fastmcp import FastMCP  # Official SDK version

app = FastMCP("MyServer")  # One line!

@app.tool()  # Decorator - modifies the function below
def read_file(path: str):  # Type hint - 'str' means text
    return open(path).read()  # That's it!

# Alternative: FastMCP 2.0 (separate package with extra features)
# from fastmcp import FastMCP  # Enhanced standalone version
```

### **MCP-O (MCP OpenAPI Bridge)**
```bash
# MCP-O converts existing REST APIs to MCP format
# It's a TRANSLATOR!

# Your existing API (OpenAPI/Swagger format):
# GET /api/users
# POST /api/users
# DELETE /api/users/{id}

# MCP-O command converts it:
mcpo proxy --api-url https://yourapi.com/swagger.json

# Now Claude can use your API as MCP tools!
# - get_users
# - create_user
# - delete_user
```

## 🤖 Agent-to-Agent Protocol

This is ADVANCED - one MCP server calling another!

```python
# MCP Server A (Finance)
class FinanceServer:
    def calculate_tax(self, income):
        # Sometimes needs exchange rates
        # Calls another MCP server!

        currency_server = MCPClient("currency-server:5001")
        rate = currency_server.call_tool("get_exchange_rate", {
            "from": "USD",
            "to": "EUR"
        })
        return income * 0.3 * rate

# MCP Server B (Currency)
class CurrencyServer:
    def get_exchange_rate(self, from_currency, to_currency):
        return 0.85  # USD to EUR
```

## ❓ Key Clarifications:

1. **`client` variable name**:
   - YES, it's just a variable name!
   - Could be `connection`, `mcp`, `c`, `banana` - doesn't matter!
   - Convention is to use meaningful names

2. **LLM inside MCP Server?**
   - Technically POSSIBLE but UNUSUAL
   - Would be for special cases (like content moderation)
   - Generally kept separate for clarity

3. **Non-LLM clients exist!**
   - Your Python scripts
   - Web applications
   - Mobile apps
   - Testing tools

4. **Deterministic vs Non-deterministic**:
   - MCP Server responses: DETERMINISTIC (same input = same output)
   - LLM responses: NON-DETERMINISTIC (can vary each time)
   - MCP servers typically don't contain LLMs