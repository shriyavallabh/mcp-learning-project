# Chapter 7: JSON-RPC Protocol - The Language of MCP

## 🎯 What is JSON-RPC?

Think of it like a structured phone conversation:

```python
"""
Regular conversation (messy):
"Hey, can you read that file? The one in documents? Thanks!"

JSON-RPC conversation (structured):
{
  "jsonrpc": "2.0",
  "method": "read_file",
  "params": {"path": "/documents/report.txt"},
  "id": 1
}
"""
```

## 📦 JSON Basics First

```python
# JSON = JavaScript Object Notation
# It's just a TEXT format for data!

# Python Dictionary (in memory):
data = {
    "name": "John",
    "age": 25,
    "hobbies": ["coding", "gaming"]
}

# JSON String (text that can be sent):
json_text = '{"name": "John", "age": 25, "hobbies": ["coding", "gaming"]}'

# Converting:
import json
json_string = json.dumps(data)  # Python → JSON text
python_dict = json.loads(json_string)  # JSON text → Python
```

## 🔄 JSON-RPC Structure - EVERY Message Has These Parts

```python
# REQUEST (Client → Server):
{
    "jsonrpc": "2.0",      # Version (always "2.0")
    "method": "tool_name",  # What to do
    "params": {...},        # Input data
    "id": 1                 # Tracking number
}

# RESPONSE (Server → Client):
{
    "jsonrpc": "2.0",      # Version
    "result": {...},        # Success data
    "id": 1                 # Same tracking number!
}

# ERROR RESPONSE:
{
    "jsonrpc": "2.0",
    "error": {
        "code": -32601,     # Error number
        "message": "Method not found"  # What went wrong
    },
    "id": 1
}
```

## 🎬 Complete MCP Conversation in JSON-RPC

Let me show you an ACTUAL MCP conversation:

```python
# STEP 1: Claude says hello
client_to_server = {
    "jsonrpc": "2.0",
    "method": "initialize",
    "params": {
        "protocolVersion": "0.1.0",
        "capabilities": {
            "tools": True,
            "resources": True
        },
        "clientInfo": {
            "name": "Claude Desktop",
            "version": "1.0"
        }
    },
    "id": 1
}

# STEP 2: Server responds with capabilities
server_to_client = {
    "jsonrpc": "2.0",
    "result": {
        "protocolVersion": "0.1.0",
        "capabilities": {
            "tools": True,
            "resources": True
        },
        "serverInfo": {
            "name": "FileSystemServer",
            "version": "1.0"
        }
    },
    "id": 1  # Matches request ID!
}

# STEP 3: Claude lists available tools
client_to_server = {
    "jsonrpc": "2.0",
    "method": "tools/list",
    "params": {},
    "id": 2
}

# STEP 4: Server lists its tools
server_to_client = {
    "jsonrpc": "2.0",
    "result": {
        "tools": [
            {
                "name": "read_file",
                "description": "Read contents of a file",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string"}
                    },
                    "required": ["path"]
                }
            },
            {
                "name": "write_file",
                "description": "Write content to a file",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string"},
                        "content": {"type": "string"}
                    },
                    "required": ["path", "content"]
                }
            }
        ]
    },
    "id": 2
}

# STEP 5: Claude uses a tool
client_to_server = {
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
        "name": "read_file",
        "arguments": {
            "path": "/home/user/document.txt"
        }
    },
    "id": 3
}

# STEP 6: Server executes and returns
server_to_client = {
    "jsonrpc": "2.0",
    "result": {
        "content": "This is the file content...",
        "isError": false
    },
    "id": 3
}
```

## 🔑 Why the ID Field is CRUCIAL

```python
# IDs match requests to responses!

# Claude sends 3 requests at once:
request_1 = {"jsonrpc": "2.0", "method": "read_file", "id": 1}
request_2 = {"jsonrpc": "2.0", "method": "list_dir", "id": 2}
request_3 = {"jsonrpc": "2.0", "method": "get_time", "id": 3}

# Server might respond OUT OF ORDER:
response_3 = {"jsonrpc": "2.0", "result": "3:30 PM", "id": 3}  # Fast!
response_1 = {"jsonrpc": "2.0", "result": "content", "id": 1}  # Slow file
response_2 = {"jsonrpc": "2.0", "result": ["a.txt"], "id": 2}  # Medium

# Claude uses ID to match: "Oh, id:3 is the time response!"
```

## 🚨 JSON-RPC Error Codes (Standard)

```python
# Standard error codes everyone uses:
ERROR_CODES = {
    -32700: "Parse error",      # Invalid JSON
    -32600: "Invalid Request",  # Missing required fields
    -32601: "Method not found", # Unknown method
    -32602: "Invalid params",   # Wrong parameters
    -32603: "Internal error",   # Server crashed
    -32000: "Server error"      # Custom errors (-32000 to -32099)
}

# Example error:
error_response = {
    "jsonrpc": "2.0",
    "error": {
        "code": -32601,
        "message": "Method not found",
        "data": "No tool named 'read_files' (did you mean 'read_file'?)"
    },
    "id": 4
}
```

## 🔄 Notification (No Response Expected)

```python
# Sometimes you just inform, don't need response
# NO ID = Notification!

notification = {
    "jsonrpc": "2.0",
    "method": "log",
    "params": {
        "level": "info",
        "message": "File operation completed"
    }
    # NO "id" field! Server won't respond
}
```

## 💻 Python Implementation

Let me show you how to handle JSON-RPC in Python:

```python
import json
from typing import Dict, Any, Optional

class JSONRPCHandler:
    """Handles JSON-RPC 2.0 protocol"""

    def __init__(self):
        # Store methods we can handle
        self.methods = {}

    def register_method(self, name: str, handler):
        """Register a function to handle a method"""
        self.methods[name] = handler

    def create_request(self, method: str, params: Dict, id: int) -> str:
        """Create a JSON-RPC request"""
        request = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": id
        }
        return json.dumps(request)  # Convert to JSON string

    def create_response(self, result: Any, id: int) -> str:
        """Create a JSON-RPC response"""
        response = {
            "jsonrpc": "2.0",
            "result": result,
            "id": id
        }
        return json.dumps(response)

    def create_error(self, code: int, message: str, id: Optional[int]) -> str:
        """Create a JSON-RPC error"""
        error = {
            "jsonrpc": "2.0",
            "error": {
                "code": code,
                "message": message
            }
        }
        if id is not None:
            error["id"] = id
        return json.dumps(error)

    def handle_request(self, json_string: str) -> str:
        """Process incoming JSON-RPC request"""
        try:
            # Parse JSON
            request = json.loads(json_string)

            # Validate structure
            if request.get("jsonrpc") != "2.0":
                return self.create_error(-32600, "Invalid Request", None)

            # Get method
            method = request.get("method")
            if method not in self.methods:
                return self.create_error(
                    -32601,
                    f"Method '{method}' not found",
                    request.get("id")
                )

            # Call handler
            params = request.get("params", {})
            result = self.methods[method](**params)

            # Return response
            return self.create_response(result, request.get("id"))

        except json.JSONDecodeError:
            return self.create_error(-32700, "Parse error", None)
        except Exception as e:
            return self.create_error(-32603, str(e), request.get("id"))

# Usage example:
handler = JSONRPCHandler()

# Register a method
def read_file(path: str) -> str:
    with open(path, 'r') as f:
        return f.read()

handler.register_method("read_file", read_file)

# Handle request
request = '{"jsonrpc": "2.0", "method": "read_file", "params": {"path": "test.txt"}, "id": 1}'
response = handler.handle_request(request)
print(response)  # {"jsonrpc": "2.0", "result": "file contents", "id": 1}
```

## 🎯 MCP-Specific JSON-RPC Methods

```python
# MCP defines these standard methods:

MCP_METHODS = {
    # Lifecycle
    "initialize": "Start connection",
    "initialized": "Confirm ready",
    "shutdown": "Close connection",

    # Tools
    "tools/list": "Get available tools",
    "tools/call": "Execute a tool",

    # Resources
    "resources/list": "Get available resources",
    "resources/read": "Read a resource",
    "resources/subscribe": "Watch for changes",

    # Prompts
    "prompts/list": "Get available prompts",
    "prompts/get": "Get prompt with arguments",

    # Completion
    "completion/complete": "Get autocomplete suggestions"
}
```

## 📊 Quick Reference Card

| Component | Purpose | Example |
|-----------|---------|---------|
| `jsonrpc` | Version | Always "2.0" |
| `method` | What to do | "tools/call" |
| `params` | Input data | {"path": "/file"} |
| `id` | Track request | 1, 2, 3... |
| `result` | Success data | {"content": "..."} |
| `error` | Failure info | {"code": -32601} |

## ✍️ Assignment: Build a JSON-RPC Calculator

```python
# assignment_jsonrpc.py
import json

class CalculatorServer:
    def handle_jsonrpc(self, request_string):
        """
        TODO: Parse JSON-RPC request and handle these methods:
        - "add": params {"a": number, "b": number}
        - "subtract": params {"a": number, "b": number}
        - "multiply": params {"a": number, "b": number}
        - "divide": params {"a": number, "b": number}

        Return proper JSON-RPC response or error
        """
        pass  # Your code here

# Test:
server = CalculatorServer()
request = '{"jsonrpc": "2.0", "method": "add", "params": {"a": 5, "b": 3}, "id": 1}'
response = server.handle_jsonrpc(request)
# Should return: {"jsonrpc": "2.0", "result": 8, "id": 1}
```

## 🎬 The Big Picture

```
You type → Claude → JSON-RPC Request → MCP Server
                                           ↓
You see ← Claude ← JSON-RPC Response ← Processes
```

JSON-RPC is just the structured way they talk - like filling out a form instead of writing a letter!

## 📡 Transport Mechanisms (How JSON-RPC Messages Travel)

**Current supported transports:**
1. **stdio (Standard Input/Output)**: For local connections, server runs as subprocess
2. **Streamable HTTP**: For remote connections, can use SSE for streaming responses

**Important Note**: SSE as a standalone transport was deprecated as of protocol version 2024-11-05. Modern MCP uses "Streamable HTTP" which can optionally use SSE for streaming within HTTP responses.

## 📚 Sources
- Official MCP Documentation: https://modelcontextprotocol.io
- MCP GitHub: https://github.com/modelcontextprotocol
- JSON-RPC 2.0 Specification: https://www.jsonrpc.org/specification