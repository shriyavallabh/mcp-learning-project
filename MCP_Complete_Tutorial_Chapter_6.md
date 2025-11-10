# Chapter 6: FastAPI and Pydantic - Modern Python for MCP

## 🔥 FastAPI & Pydantic (Modern Python Web Framework)

These are ESSENTIAL for building MCP servers!

## Pydantic = Data Validation

```python
# PYDANTIC = Makes sure data is correct type/format

# WITHOUT Pydantic (dangerous!):
def process_user(data):
    name = data["name"]  # What if "name" missing? CRASH!
    age = data["age"]    # What if age is "twenty"? CRASH!

# WITH Pydantic (safe!):
from pydantic import BaseModel

class User(BaseModel):  # BaseModel = Pydantic's magic class
    name: str           # MUST be string
    age: int           # MUST be integer
    email: str         # MUST be string

# Using it:
user_data = {"name": "John", "age": 25, "email": "john@example.com"}
user = User(**user_data)  # ** = unpack dictionary
# If data wrong type → Nice error message!

# For MCP:
class MCPRequest(BaseModel):
    method: str  # "tools/call"
    params: dict  # {"tool": "read_file", "path": "/home/file.txt"}

    # Pydantic validates AUTOMATICALLY!
```

## FastAPI = Modern Web Framework

```python
# FASTAPI = Easy way to build web APIs

from fastapi import FastAPI
from pydantic import BaseModel

# Create app instance
app = FastAPI()  # This is your web server!

# Define data model
class FileRequest(BaseModel):
    path: str

class FileResponse(BaseModel):
    content: str
    size: int

# Define endpoint (URL handler)
@app.post("/read-file")  # @ = decorator (modifies function)
async def read_file(request: FileRequest) -> FileResponse:
    # FastAPI automatically:
    # 1. Validates input using Pydantic
    # 2. Converts JSON to Python objects
    # 3. Generates documentation
    # 4. Handles errors

    with open(request.path, 'r') as f:
        content = f.read()

    return FileResponse(
        content=content,
        size=len(content)
    )

# Run with: uvicorn main:app --reload
# Now you have a web API at http://localhost:8000/read-file
```

## 🎯 How It All Connects for MCP

```python
"""
Your MCP Deployment Options:

1. LOCAL DEVELOPMENT:
   Python script → Your laptop

2. CONTAINER:
   Python script → Docker container → Your laptop

3. KUBERNETES:
   Python script → Docker container → Pod → Node → Cluster

4. SERVERLESS:
   Python script → Function → Cloud provider manages everything

5. TRADITIONAL SERVER:
   Python script → VM → Physical server
"""

# Example MCP Server with FastAPI:
from fastapi import FastAPI
from pydantic import BaseModel
import mcp

app = FastAPI()

class MCPToolRequest(BaseModel):
    tool: str
    arguments: dict

@app.post("/mcp/tool")
async def handle_tool(request: MCPToolRequest):
    if request.tool == "read_file":
        with open(request.arguments["path"]) as f:
            return {"content": f.read()}
```

## 🧩 Related Concepts You Should Know

1. **Microservices**: Breaking app into small pieces
2. **REST API**: How web services talk (GET, POST, PUT, DELETE)
3. **WebSockets**: Real-time communication
4. **gRPC**: Fast binary protocol (alternative to REST)
5. **Service Mesh**: Managing service-to-service communication
6. **CI/CD**: Automated testing and deployment
7. **Load Balancer**: Distributes traffic across servers
8. **API Gateway**: Single entry point for all APIs

## ✍️ Assignment:

Create a simple FastAPI server with Pydantic:

```python
# assignment_fastapi.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# TODO: Create a Pydantic model for Calculator request
# Should have: operation (str), a (float), b (float)

# TODO: Create endpoint /calculate that:
# - Takes Calculator request
# - Returns result based on operation (+, -, *, /)
```

## 🔄 FastMCP vs MCP-O - COMPLETELY Different Tools!

These solve DIFFERENT problems:

```python
"""
FastMCP = BUILDING tool (create NEW MCP servers)
MCP-O = CONVERTING tool (wrap EXISTING APIs)
"""
```

### **FastMCP - For Building New MCP Servers**

```python
# FastMCP = Python library to BUILD MCP servers from scratch
# Like: "I want to create a NEW MCP server"

# Option 1: Official MCP SDK (includes FastMCP 1.0) - RECOMMENDED
from mcp.server.fastmcp import FastMCP

# Option 2: FastMCP 2.0 (separate package with extra features)
# from fastmcp import FastMCP

# You're CREATING a new server
mcp = FastMCP("MyNewServer")

@mcp.tool()  # Decorator that says "this is an MCP tool"
def read_database(query: str):
    # YOUR custom code here
    conn = connect_to_database()
    results = conn.execute(query)
    return results

# FastMCP handles all the MCP protocol stuff
# You just write your business logic
```

### **MCP-O - For Converting Existing APIs**

```bash
# MCP-O = Command-line tool to CONVERT existing OpenAPI/REST APIs
# Like: "I already have an API, make it MCP-compatible"

# You have an EXISTING API:
# https://api.weather.com/v1/
#   GET /current/{city}
#   GET /forecast/{city}

# MCP-O creates a PROXY (translator):
mcpo proxy --url https://api.weather.com/swagger.json

# Now Claude can use it as MCP tools:
# - get_current_weather
# - get_forecast
```

### **Visual Comparison**

```
FastMCP (Building):
┌─────────────┐
│  Your Code  │ → FastMCP → MCP Server (NEW)
└─────────────┘

MCP-O (Converting):
┌─────────────┐           ┌─────────────┐
│ Existing API│ → MCP-O → │ MCP Wrapper │
└─────────────┘  (proxy)  └─────────────┘
```

### **When to Use Which?**

```python
# Use FastMCP when:
"""
- Building NEW functionality
- Need custom logic
- Want full control
- Creating from scratch
"""

# Use MCP-O when:
"""
- You ALREADY have a REST API
- Don't want to rewrite code
- Need quick MCP compatibility
- Working with third-party APIs
"""

# Real Example:
# Company has 50 REST APIs
# Option 1: Rewrite all with FastMCP (months of work)
# Option 2: Use MCP-O proxy (5 minutes per API)
```

## 🤔 Why Kubernetes Uses VMs as Nodes

### **Why Containers Still Need an OS Somewhere**

```python
# Container says: "I don't have an OS"
# But it needs OS SERVICES:

class Container:
    def __init__(self):
        self.app = "my_app.py"
        # But wait! Who handles:
        # - File system? (reading/writing files)
        # - Networking? (sending packets)
        # - Memory management?
        # - Process scheduling?

# Answer: The HOST OS (Node's OS)!

"""
Container: "Hey, I need to read a file"
     ↓
Node's Linux OS: "I'll handle that for you"
     ↓
Container: "Thanks! Here's the data"
"""
```

### **Why K8s Uses VMs as Nodes**

```python
# REASON 1: Isolation & Security
"""
Node 1 (VM): Customer A's containers
Node 2 (VM): Customer B's containers
→ Complete isolation between customers
"""

# REASON 2: Resource Management
"""
Node (VM): 16 CPU, 64GB RAM
├── Pod 1: 2 CPU, 8GB RAM
├── Pod 2: 4 CPU, 16GB RAM
└── Pod 3: 2 CPU, 8GB RAM
→ VM provides resource boundaries
"""

# REASON 3: Flexibility
"""
Node 1: Windows VM (for .NET containers)
Node 2: Linux VM (for Python containers)
Node 3: GPU VM (for AI workloads)
→ Different OS/hardware per node
"""
```

## 💡 Mental Models

```python
# FastMCP vs MCP-O
"FastMCP is like cooking from scratch"
"MCP-O is like putting takeout on nice plates"

# Why Nodes are VMs
"Containers are apps without an OS"
"But they still need OS services"
"Node VM provides those services"

# Container vs Pod
"Container = One program"
"Pod = Container(s) + networking + storage wrapper"
```