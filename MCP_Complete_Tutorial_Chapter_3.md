# Chapter 3: Python Basics for MCP (Only What You Need!)

## 🎯 What Python Concepts Do You ACTUALLY Need for MCP?

Think of Python like learning to drive - you don't need to know how to build an engine, just how to use the car!

**For MCP, you need:**
1. Variables (storing information)
2. Functions (doing tasks)
3. Dictionaries (organizing data)
4. Classes (creating servers)
5. Async/Await (handling multiple requests)

Let's learn each one!

## 📦 Concept 1: Variables (Storage Boxes)

Variables are like labeled boxes where you store things:

```python
# Basic Variables - Like sticky notes with information
name = "John"           # Text (string)
age = 20               # Number (integer)
height = 5.9           # Decimal (float)
is_student = True      # Yes/No (boolean)

# Using them
print(f"Hi, I'm {name} and I'm {age} years old")
# Output: Hi, I'm John and I'm 20 years old
```

### **MCP Example:**
```python
# In your MCP server
server_name = "MyFileReader"
server_version = "1.0"
is_running = True
```

## 📋 Concept 2: Lists & Dictionaries (Organizing Data)

### **Lists = Numbered Shopping List**
```python
# List - Order matters, like a queue
tools = ["read_file", "write_file", "delete_file"]
print(tools[0])  # First item: "read_file"
print(tools[1])  # Second item: "write_file"

# Adding items
tools.append("copy_file")  # Adds to end
```

### **Dictionaries = Labeled Drawers**
```python
# Dictionary - Labels (keys) with values
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

print(student["name"])  # Gets "Alice"
student["age"] = 21    # Updates age
```

### **MCP Example:**
```python
# This is what MCP messages look like!
mcp_message = {
    "method": "tools/call",
    "params": {
        "name": "read_file",
        "arguments": {
            "path": "/home/user/document.txt"
        }
    }
}
```

## 🔧 Concept 3: Functions (Reusable Tasks)

Functions are like recipes - write once, use many times:

```python
# Simple function
def greet(name):
    return f"Hello, {name}!"

# Using it
message = greet("Alice")
print(message)  # "Hello, Alice!"

# Function with multiple inputs
def add_numbers(a, b):
    result = a + b
    return result

total = add_numbers(5, 3)  # Returns 8
```

### **MCP Function Example:**
```python
# This is what you'll write for MCP!
def read_file_tool(file_path):
    """This tool reads a file"""
    with open(file_path, 'r') as f:
        content = f.read()
    return content

# When Claude asks to read a file:
result = read_file_tool("/home/user/notes.txt")
```

## 🏗️ Concept 4: Classes (Building Servers)

Classes are like blueprints for creating things:

```python
# Think of a class like a template
class Student:
    def __init__(self, name, age):
        self.name = name  # Store name
        self.age = age    # Store age

    def introduce(self):
        return f"I'm {self.name}, {self.age} years old"

# Creating an actual student
john = Student("John", 20)
print(john.introduce())  # "I'm John, 20 years old"
```

### **MCP Server Class (Simplified):**
```python
class MyMCPServer:
    def __init__(self):
        self.name = "FileHelper"
        self.tools = ["read", "write"]

    def handle_request(self, request):
        if request["method"] == "read":
            return "File content here"
```

## ⚡ Concept 5: Async/Await (Handling Multiple Things)

This is like a waiter serving multiple tables:

```python
# Regular way (one at a time)
def make_coffee():
    print("Making coffee...")  # Takes 3 seconds
    return "☕ Coffee ready"

def make_toast():
    print("Making toast...")   # Takes 2 seconds
    return "🍞 Toast ready"

# Async way (both at once!)
async def make_breakfast():
    coffee = await make_coffee_async()  # Start coffee
    toast = await make_toast_async()    # While waiting, start toast
    return f"{coffee} and {toast}"
```

### **Why MCP Needs This:**
```python
# MCP Server can handle multiple requests
async def handle_mcp_request(request):
    if request["method"] == "read_file":
        content = await read_file_async(request["path"])
        return content
    # Can handle other requests while reading!
```

## 📝 Practical Exercise: Build a Mini Tool

Let's combine everything into a simple tool:

```python
# mini_server.py - Your first MCP-style code!

class SimpleServer:
    def __init__(self):
        self.name = "Calculator"
        self.tools = {
            "add": self.add_numbers,
            "subtract": self.subtract_numbers
        }

    def add_numbers(self, a, b):
        """Adds two numbers"""
        return a + b

    def subtract_numbers(self, a, b):
        """Subtracts b from a"""
        return a - b

    def handle_request(self, request):
        """Process incoming request"""
        tool_name = request["tool"]
        arguments = request["args"]

        if tool_name in self.tools:
            result = self.tools[tool_name](**arguments)
            return {"success": True, "result": result}
        else:
            return {"success": False, "error": "Tool not found"}

# Using your server
server = SimpleServer()

# Simulate a request
request1 = {
    "tool": "add",
    "args": {"a": 5, "b": 3}
}

response = server.handle_request(request1)
print(response)  # {"success": True, "result": 8}
```

## 🎯 Quick Reference - Only What You Need:

| Python Concept | MCP Usage |
|---------------|-----------|
| Variables | Store server settings |
| Dictionaries | Handle JSON messages |
| Functions | Create tools |
| Classes | Build servers |
| Async/Await | Handle multiple requests |
| Try/Except | Error handling |

## ✍️ Assignment #3: Your Turn!

Create a simple class with one tool:

```python
# assignment3.py
class MyFirstTool:
    def __init__(self):
        self.name = "Greeter"

    def greet_user(self, user_name):
        # YOUR CODE HERE: Return greeting message
        pass  # Replace this

    def handle_request(self, request):
        # YOUR CODE HERE: Call greet_user with the name from request
        pass  # Replace this

# Test it
tool = MyFirstTool()
request = {"action": "greet", "name": "Alice"}
# Should print something like "Hello, Alice!"
```

## 🚀 You Now Know Enough Python for MCP!

Seriously! With just these concepts, you can build:
- File readers
- Database connectors
- API bridges
- Custom tools

**The MCP library handles all the complex stuff!**