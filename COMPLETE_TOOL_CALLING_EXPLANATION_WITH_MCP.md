# Complete Tool Calling Explanation - WITH MCP

**A line-by-line breakdown of how tool calling works with MCP (Model Context Protocol)**

---

## Table of Contents
1. [The Complete MCP Program](#the-complete-mcp-program)
2. [Line-by-Line Explanation](#line-by-line-explanation)
3. [Client Configuration](#client-configuration)
4. [Complete Execution Flow](#complete-execution-flow)
5. [Visual Diagrams](#visual-diagrams)
6. [Comparison with Before MCP](#comparison-with-before-mcp)
7. [Key Concepts Summary](#key-concepts-summary)

---

## The Complete MCP Program

### The MCP Server (weather_server.py)

```python
# weather_server.py - MCP Server Implementation
from mcp.server import Server
from mcp.server.stdio import stdio_server
import requests
import asyncio

# Create MCP server instance
app = Server("weather-server")

@app.tool()
async def get_weather(city: str) -> str:
    """Get current weather for a city"""
    api_key = "your-openweathermap-key"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    # Make the API call
    response = requests.get(url)
    data = response.json()

    # Extract data
    temp = data['main']['temp']
    description = data['weather'][0]['description']

    return f"Weather in {city}: {temp}°C, {description}"

# Run the server
if __name__ == "__main__":
    asyncio.run(stdio_server(app))
```

**That's it!** Just 27 lines vs 112 lines in the pre-MCP version!

---

## Line-by-Line Explanation

### Lines 1-4: Imports

```python
# weather_server.py - MCP Server Implementation
from mcp.server import Server
from mcp.server.stdio import stdio_server
import requests
import asyncio
```

**Line 1:**
- `#` = Comment
- **Purpose:** Explains this is an MCP server implementation

**Line 2: `from mcp.server import Server`**
- `from` = Import keyword
- `mcp.server` = Module path
  - **What is mcp?** The Model Context Protocol Python SDK
  - **What is mcp.server?** A submodule containing server components
- `import Server` = Bring in the Server class
- **What is Server?** A class (blueprint) for creating MCP servers
- **Installation:** `pip install mcp`
- **What does this do?** Imports the Server class so we can create our own MCP server

**Breaking down what "Server" is:**
- **Server** = A CLASS (a blueprint)
- It's like a template/recipe for creating an MCP server
- You use it to create your own server instance
- It handles all the MCP protocol details for you

**Line 3: `from mcp.server.stdio import stdio_server`**
- `from mcp.server.stdio` = Module path
  - **What is stdio?** Standard Input/Output
  - **Why stdio?** MCP servers communicate via stdin/stdout (like typing in terminal)
- `import stdio_server` = Bring in the stdio_server function
- **What is stdio_server?** A function that runs an MCP server using stdin/stdout communication
- **What does this do?** Imports the function that will start our server and handle communication

**Why stdin/stdout?**
- **stdin** = Standard Input (reading messages)
- **stdout** = Standard Output (sending messages)
- MCP clients (like Claude) launch your server as a subprocess
- They send JSON-RPC messages to your stdin
- Your server sends responses to stdout
- It's like a conversation through a pipe!

**Line 4: `import requests`**
- `requests` = HTTP library (same as in Part 1)
- **Why?** To call the weather API
- **Installation:** `pip install requests`

**Line 5: `import asyncio`**
- `asyncio` = Python's built-in async/await library
- **What is async?** Asynchronous programming - run code without blocking
- **Why do we need this?** MCP uses async/await pattern for efficient I/O
- **What does it do?** Allows the server to handle multiple requests efficiently
- **Built-in:** Comes with Python 3.7+

**What is async/await?**
- **Regular code:** Do one thing → wait → do next thing
- **Async code:** Start task → don't wait → do other things → come back when ready
- **Example:**
  ```python
  # Regular (synchronous)
  result1 = call_api()  # Wait 2 seconds
  result2 = call_api()  # Wait 2 seconds
  # Total: 4 seconds

  # Async (asynchronous)
  result1 = await call_api()  # Start, but can do other work
  result2 = await call_api()  # Can be done in parallel
  # Total: 2 seconds (if parallel)
  ```

---

### Lines 7-8: Create MCP Server Instance

```python
# Create MCP server instance
app = Server("weather-server")
```

**Line 7:**
- Comment explaining what we're doing

**Line 8: `app = Server("weather-server")`**

Let me break this down EXTREMELY carefully:

- `app` = Variable name
  - **What is "app"?** Just a variable name we chose
  - Could be called: `server`, `my_server`, `weather_srv`, anything!
  - It's like naming your restaurant "app"
- `=` = Assignment operator
- `Server()` = Calling the Server class (creating an instance)
  - **What is Server?** The class we imported from mcp.server
  - **What happens when you call it?** Creates a new MCP server object
  - **Think of it as:** Using the blueprint to build an actual restaurant
- `"weather-server"` = Argument (the server name)
  - **What is this?** The name/identifier for your server
  - **Why name it?** For logging, debugging, identification
  - **You choose this name** - could be anything

**What does this line do?**
- Creates a new MCP server object
- Stores it in the variable `app`
- Names the server "weather-server"
- The server is now ready to have tools added to it

**Think of it as:**
- `Server` = Restaurant blueprint
- `Server("weather-server")` = Building a restaurant using that blueprint and naming it "weather-server"
- `app` = Your variable pointing to that restaurant

**After this line:**
- `app` contains an MCP server instance
- The server has built-in functionality:
  - Can register tools
  - Can handle JSON-RPC messages
  - Can manage communication with clients
  - Handles all the protocol details automatically

---

### Lines 10-24: Define the Weather Tool

```python
@app.tool()
async def get_weather(city: str) -> str:
    """Get current weather for a city"""
    api_key = "your-openweathermap-key"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    # Make the API call
    response = requests.get(url)
    data = response.json()

    # Extract data
    temp = data['main']['temp']
    description = data['weather'][0]['description']

    return f"Weather in {city}: {temp}°C, {description}"
```

**Line 10: `@app.tool()`**

This is CRITICAL! Let me explain decorators in extreme detail:

- `@` = Decorator symbol
- **What is a decorator?** A special Python syntax that modifies the function below it
- `app` = Our server variable from line 8
- `.tool()` = A method on the server object
- `()` = Calling the method

**What does `@app.tool()` do?**
1. Tells the MCP server: "the function below is a TOOL"
2. Automatically registers this function as an available tool
3. MCP will create the tool definition automatically from the function signature
4. When clients ask "what tools do you have?", this will be listed
5. When clients call this tool, MCP routes the request to this function

**Without the decorator:**
```python
# Without decorator - just a regular function
def get_weather(city: str) -> str:
    ...

# The MCP server doesn't know about it!
# It's just a normal Python function
```

**With the decorator:**
```python
# With decorator - registered as an MCP tool
@app.tool()
def get_weather(city: str) -> str:
    ...

# The MCP server knows about it!
# It will be advertised to clients
# Clients can call it via JSON-RPC
```

**How decorators work (simplified):**
```python
# This:
@app.tool()
def get_weather(city: str) -> str:
    ...

# Is equivalent to:
def get_weather(city: str) -> str:
    ...
get_weather = app.tool()(get_weather)  # Wraps the function

# The decorator registers the function with the MCP server
```

**Line 11: `async def get_weather(city: str) -> str:`**

Let me break down EVERY part:

- `async` = Keyword marking this as an asynchronous function
  - **What does async mean?** This function can pause and resume
  - **Why async?** MCP uses async for efficient I/O operations
  - **How is it different?** You can use `await` inside it
- `def` = Define a function
- `get_weather` = Function name (you choose this)
  - **This becomes the tool name!** Clients will call "get_weather"
- `(city: str)` = Parameter with type hint
  - `city` = Parameter name
  - `: str` = Type hint (expects a string)
  - **Type hints are IMPORTANT in MCP!** They define the tool's input schema
- `->` = Return type annotation arrow
- `str` = Return type (this function returns a string)
- `:` = Function body starts next

**What MCP does with this signature:**
```python
# MCP automatically generates this tool definition:
{
    "name": "get_weather",  # From function name
    "description": "Get current weather for a city",  # From docstring
    "inputSchema": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string"  # From type hint ": str"
            }
        },
        "required": ["city"]  # From the parameter being non-optional
    }
}
```

**Compare to Before MCP:**
```python
# Before MCP - you had to write this MANUALLY:
weather_function_definition = {
    "name": "get_weather",
    "description": "Get current weather for a city",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city name, e.g., London, Tokyo"
            }
        },
        "required": ["city"]
    }
}

# With MCP - it's AUTOMATIC from your function signature!
```

**Line 12: `"""Get current weather for a city"""`**
- `"""..."""` = Docstring (documentation)
- **What is this for?** MCP uses this as the tool description
- **Why important?** Clients (like Claude) read this to understand what the tool does
- **This appears in:** The tool definition sent to clients

**Lines 13-24: Function Body**

These lines are IDENTICAL to the pre-MCP version:

**Line 13: `api_key = "your-openweathermap-key"`**
- Same as before - stores your API key

**Line 14: Building the URL**
```python
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
```
- Same as before - builds the weather API URL
- Uses f-string to insert `city` and `api_key`

**Line 17: `response = requests.get(url)`**
- **THIS IS THE KITCHEN!** The actual API call happens here
- Makes HTTP GET request to openweathermap.org
- Waits for response
- Stores result in `response` variable

**Line 18: `data = response.json()`**
- Parses JSON response into Python dictionary
- Same as before

**Line 21: `temp = data['main']['temp']`**
- Extracts temperature from nested dictionary
- Same as before

**Line 22: `description = data['weather'][0]['description']`**
- Extracts weather description from nested list and dictionary
- Same as before

**Line 24: `return f"Weather in {city}: {temp}°C, {description}"`**
- Formats and returns the result
- Same as before

**The KEY difference:**
- The function logic is IDENTICAL
- But it's wrapped with `@app.tool()` decorator
- And it's `async` (for MCP compatibility)
- MCP handles all the rest automatically!

---

### Lines 26-28: Run the Server

```python
# Run the server
if __name__ == "__main__":
    asyncio.run(stdio_server(app))
```

**Line 26:**
- Comment

**Line 27: `if __name__ == "__main__":`**
- Special Python check
- **What is `__name__`?** A special variable Python sets automatically
- **When does this run?** Only when you run this file directly
- **When does it NOT run?** If you import this file from another file
- **Why?** Prevents the server from starting if you import this file elsewhere

**Example:**
```bash
# Running directly:
$ python weather_server.py
# __name__ is "__main__" → code runs

# Importing:
>>> import weather_server
# __name__ is "weather_server" → code doesn't run
```

**Line 28: `asyncio.run(stdio_server(app))`**

This is THE LINE that starts everything! Let me break it down:

- `asyncio.run()` = Function that runs an async function
  - **What does it do?** Creates an event loop and runs async code
  - **Why needed?** async functions need an event loop to run
  - **Think of it as:** Starting the engine that makes async code work
- `stdio_server()` = Function we imported from mcp.server.stdio
  - **What does it do?** Runs an MCP server using stdin/stdout
  - **How?** Listens for JSON-RPC messages on stdin
  - **How?** Sends responses on stdout
- `(app)` = Our server instance from line 8
  - **What's being passed?** The server with our registered tools

**What happens when this line runs:**

1. **`stdio_server(app)` is called**
   - MCP sets up stdin/stdout communication
   - MCP prepares to handle JSON-RPC messages
   - MCP has access to all registered tools (our get_weather function)

2. **`asyncio.run()` starts the event loop**
   - Creates an async event loop
   - Runs the stdio_server coroutine
   - Keeps the server running

3. **Server starts listening**
   - Waits for messages on stdin
   - Ready to respond to JSON-RPC requests
   - Will run until killed or stdin closes

**The server is now running and waiting for requests!**

---

## Client Configuration

Now that we have an MCP server, how does a client (like Claude) use it?

### Claude Desktop Configuration

**File: `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS)**

```json
{
  "mcpServers": {
    "weather": {
      "command": "python",
      "args": ["/path/to/weather_server.py"]
    }
  }
}
```

**Line-by-line explanation:**

```json
{
```
- `{` = Start of JSON object

```json
  "mcpServers": {
```
- `"mcpServers"` = Key (tells Claude "here are your MCP servers")
- `{` = Value is an object containing server definitions

```json
    "weather": {
```
- `"weather"` = Server nickname (you choose this)
  - Could be: "my-weather-server", "weather-api", anything!
  - This is how you identify the server in logs
- `{` = Configuration for this server

```json
      "command": "python",
```
- `"command"` = Key
- `"python"` = Value (the executable to run)
  - **What is this?** The command to start your server
  - **Could be:** `"python"`, `"python3"`, `"/usr/bin/python"`, `"node"`, etc.
  - **This runs:** The Python interpreter

```json
      "args": ["/path/to/weather_server.py"]
```
- `"args"` = Key (arguments to pass to the command)
- `[...]` = Value is a list/array
- `"/path/to/weather_server.py"` = The path to your server file
  - **Replace this** with the actual path!
  - Example: `"/Users/shriya/mcp/weather_server.py"`

```json
    }
  }
}
```
- Closing braces

**What does this configuration do?**

When Claude Desktop starts:
```bash
# Claude runs this command:
python /path/to/weather_server.py

# This starts your MCP server
# Claude connects to it via stdin/stdout
# Your server is now available to Claude!
```

**Full command equivalent:**
```bash
$ python /path/to/weather_server.py
# Server starts
# Waits for JSON-RPC messages on stdin
# Sends responses on stdout
```

---

## Complete Execution Flow

### Startup Phase

```
┌─────────────────────────────────────────────────────────────┐
│ STEP 1: User starts Claude Desktop                          │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 2: Claude reads config file                            │
│ - Finds "weather" server configuration                      │
│ - Command: python /path/to/weather_server.py                │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 3: Claude launches your MCP server                     │
│                                                             │
│ $ python /path/to/weather_server.py                         │
│                                                             │
│ Your server starts:                                         │
│ - Line 8: app = Server("weather-server")                   │
│ - Line 10-24: @app.tool() registers get_weather            │
│ - Line 28: asyncio.run(stdio_server(app))                  │
│ - Server now listening on stdin/stdout                      │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 4: Claude discovers available tools                    │
│                                                             │
│ Claude sends JSON-RPC message to your server's stdin:       │
│ {                                                           │
│   "jsonrpc": "2.0",                                         │
│   "id": 1,                                                  │
│   "method": "tools/list"                                    │
│ }                                                           │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 5: Your MCP server responds                            │
│                                                             │
│ MCP framework automatically sends to stdout:                │
│ {                                                           │
│   "jsonrpc": "2.0",                                         │
│   "id": 1,                                                  │
│   "result": {                                               │
│     "tools": [                                              │
│       {                                                     │
│         "name": "get_weather",                              │
│         "description": "Get current weather for a city",    │
│         "inputSchema": {                                    │
│           "type": "object",                                 │
│           "properties": {                                   │
│             "city": {"type": "string"}                      │
│           },                                                │
│           "required": ["city"]                              │
│         }                                                   │
│       }                                                     │
│     ]                                                       │
│   }                                                         │
│ }                                                           │
│                                                             │
│ NOTE: This was AUTO-GENERATED from your function!          │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 6: Claude stores the tool information                  │
│                                                             │
│ Claude now knows:                                           │
│ - Server "weather" has tool "get_weather"                   │
│ - Tool gets current weather for a city                      │
│ - Tool needs parameter "city" (string)                      │
│                                                             │
│ Persistent connection established!                          │
│ Claude ←→ (stdin/stdout) ←→ Your MCP Server                │
└─────────────────────────────────────────────────────────────┘
```

### User Interaction Phase

**Scenario: User asks "What's the weather in Tokyo?"**

```
┌─────────────────────────────────────────────────────────────┐
│ STEP 1: User types in Claude                                │
│ "What's the weather in Tokyo?"                              │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 2: Claude's LLM analyzes the message                   │
│                                                             │
│ Claude thinks:                                              │
│ 1. "User wants weather information"                         │
│ 2. "I have a tool called 'get_weather'"                     │
│ 3. "That tool needs parameter 'city'"                       │
│ 4. "The city is 'Tokyo'"                                    │
│ 5. "I should call the tool!"                                │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 3: Claude sends tool call to your server               │
│                                                             │
│ Via stdin → Your MCP server:                                │
│ {                                                           │
│   "jsonrpc": "2.0",                                         │
│   "id": 2,                                                  │
│   "method": "tools/call",                                   │
│   "params": {                                               │
│     "name": "get_weather",                                  │
│     "arguments": {                                          │
│       "city": "Tokyo"                                       │
│     }                                                       │
│   }                                                         │
│ }                                                           │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 4: MCP framework receives and parses                   │
│                                                             │
│ MCP framework:                                              │
│ 1. Receives JSON-RPC message from stdin                     │
│ 2. Parses it                                                │
│ 3. Sees method: "tools/call"                                │
│ 4. Sees tool name: "get_weather"                            │
│ 5. Looks up registered tools                                │
│ 6. Finds your @app.tool() decorated function                │
│ 7. Extracts arguments: {"city": "Tokyo"}                    │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 5: MCP calls your function                             │
│                                                             │
│ result = await get_weather(city="Tokyo")                    │
│                                                             │
│ Inside your get_weather function:                           │
│                                                             │
│ Line 13: api_key = "your-openweathermap-key"               │
│ Line 14: url = "https://api...?q=Tokyo&appid=..."          │
│ Line 17: response = requests.get(url)                       │
│          ↓                                                  │
│          HTTP GET → openweathermap.org                      │
│          ← Response (JSON)                                  │
│          THIS IS THE KITCHEN!                               │
│                                                             │
│ Line 18: data = response.json()                             │
│          {                                                  │
│            "main": {"temp": 15, ...},                       │
│            "weather": [{"description": "cloudy"}]           │
│          }                                                  │
│                                                             │
│ Line 21: temp = 15                                          │
│ Line 22: description = "cloudy"                             │
│ Line 24: return "Weather in Tokyo: 15°C, cloudy"           │
│                                                             │
│ result = "Weather in Tokyo: 15°C, cloudy"                  │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 6: MCP framework packages the result                   │
│                                                             │
│ MCP automatically creates JSON-RPC response:                │
│ {                                                           │
│   "jsonrpc": "2.0",                                         │
│   "id": 2,                                                  │
│   "result": {                                               │
│     "content": [                                            │
│       {                                                     │
│         "type": "text",                                     │
│         "text": "Weather in Tokyo: 15°C, cloudy"           │
│       }                                                     │
│     ]                                                       │
│   }                                                         │
│ }                                                           │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 7: MCP sends response to Claude                        │
│                                                             │
│ Via stdout → Claude                                         │
│ (JSON-RPC response from above)                              │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 8: Claude receives the result                          │
│                                                             │
│ Claude's LLM now has:                                       │
│ - User question: "What's the weather in Tokyo?"             │
│ - Tool result: "Weather in Tokyo: 15°C, cloudy"            │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 9: Claude generates natural language response          │
│                                                             │
│ Claude formats a friendly response:                         │
│ "The weather in Tokyo is currently 15°C and cloudy."        │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 10: User sees the response                             │
│                                                             │
│ Displayed in Claude:                                        │
│ "The weather in Tokyo is currently 15°C and cloudy."        │
└─────────────────────────────────────────────────────────────┘
```

**KEY POINTS:**
1. **Only ONE interaction with the server** (not two API calls like before!)
2. **MCP handles all the orchestration** (you don't manage the loop)
3. **Persistent connection** (stdin/stdout stays open)
4. **Standardized JSON-RPC** (works with any MCP client)

---

## Visual Diagrams

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                        CLAUDE DESKTOP                        │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  Claude's LLM (Sonnet, Opus, etc.)                     │ │
│  │  - Analyzes user messages                              │ │
│  │  - Decides when to use tools                           │ │
│  │  - Generates responses                                 │ │
│  └─────────────────────┬──────────────────────────────────┘ │
│                        │                                     │
│  ┌─────────────────────▼──────────────────────────────────┐ │
│  │  MCP Client (Built into Claude)                        │ │
│  │  - Manages server connections                          │ │
│  │  - Sends JSON-RPC requests                             │ │
│  │  - Receives JSON-RPC responses                         │ │
│  └─────────────────────┬──────────────────────────────────┘ │
└────────────────────────┼────────────────────────────────────┘
                         │
                         │ stdin/stdout
                         │ (Persistent Connection)
                         │
┌────────────────────────▼────────────────────────────────────┐
│                   YOUR MCP SERVER                            │
│                  (weather_server.py)                         │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  MCP Framework (from mcp.server)                       │ │
│  │  - Listens on stdin for JSON-RPC messages              │ │
│  │  - Routes requests to your tools                       │ │
│  │  - Packages responses as JSON-RPC                      │ │
│  │  - Sends responses to stdout                           │ │
│  └─────────────────────┬──────────────────────────────────┘ │
│                        │                                     │
│  ┌─────────────────────▼──────────────────────────────────┐ │
│  │  Your Tool Function                                    │ │
│  │  @app.tool()                                           │ │
│  │  async def get_weather(city: str) -> str:              │ │
│  │      # Your actual business logic                      │ │
│  │      response = requests.get(weather_api_url)          │ │
│  │      return result                                     │ │
│  └─────────────────────┬──────────────────────────────────┘ │
└────────────────────────┼────────────────────────────────────┘
                         │
                         │ HTTP Request
                         │
┌────────────────────────▼────────────────────────────────────┐
│              WEATHER API (openweathermap.org)                │
│  - Receives HTTP GET request                                │
│  - Looks up weather data                                    │
│  - Returns JSON response                                    │
└─────────────────────────────────────────────────────────────┘
```

### Message Flow Diagram

```
User asks: "What's the weather in Tokyo?"
         │
         ↓
┌────────────────────┐
│  Claude's LLM      │
│  Decides to call   │
│  get_weather tool  │
└─────────┬──────────┘
          │
          │ JSON-RPC Request
          ↓
{
  "method": "tools/call",
  "params": {
    "name": "get_weather",
    "arguments": {"city": "Tokyo"}
  }
}
          │
          │ (via stdin)
          ↓
┌────────────────────┐
│  MCP Framework     │
│  - Receives msg    │
│  - Parses JSON     │
│  - Finds tool      │
└─────────┬──────────┘
          │
          │ Function Call
          ↓
result = await get_weather(city="Tokyo")
          │
          │ Inside your function:
          ↓
┌────────────────────┐
│  requests.get()    │──── HTTP GET ───→ ┌──────────────────┐
│                    │                   │  Weather API     │
│                    │←─── JSON data ──── │  (external)      │
└─────────┬──────────┘                   └──────────────────┘
          │
          │ return "Weather in Tokyo: 15°C, cloudy"
          ↓
┌────────────────────┐
│  MCP Framework     │
│  - Packages result │
│  - Creates JSON    │
└─────────┬──────────┘
          │
          │ JSON-RPC Response
          ↓
{
  "result": {
    "content": [
      {"type": "text", "text": "Weather in Tokyo: 15°C, cloudy"}
    ]
  }
}
          │
          │ (via stdout)
          ↓
┌────────────────────┐
│  Claude's LLM      │
│  Generates         │
│  friendly response │
└─────────┬──────────┘
          │
          ↓
User sees: "The weather in Tokyo is currently 15°C and cloudy."
```

### Comparison: Before vs After MCP

```
BEFORE MCP (OpenAI Function Calling)
=====================================

User Message
    ↓
YOU send to OpenAI (HTTP)
    ↓
OpenAI responds: "call function X"
    ↓
YOU execute function
    ↓
YOU send result back to OpenAI (HTTP)
    ↓
OpenAI responds: "here's the answer"
    ↓
YOU display to user

- 2 HTTP requests
- YOU manage orchestration
- Different format per vendor


AFTER MCP
=========

User Message
    ↓
Claude (MCP Client) → Your Server (JSON-RPC via stdin)
    ↓
MCP Framework calls your function
    ↓
Your Server → Claude (JSON-RPC via stdout)
    ↓
Claude displays to user

- 1 request/response cycle
- MCP manages orchestration
- Standard format (JSON-RPC 2.0)
- Persistent connection
```

---

## Comparison with Before MCP

### Code Comparison

#### Before MCP (112 lines)

```python
import openai
import requests
import json

openai.api_key = "..."

def get_weather(city):
    # ... weather logic ...
    return result

weather_function_definition = {
    "name": "get_weather",
    "description": "Get current weather for a city",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "..."
            }
        },
        "required": ["city"]
    }
}

def chat():
    messages = []

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == 'quit':
            break

        messages.append({"role": "user", "content": user_input})

        # FIRST API CALL
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            functions=[weather_function_definition],
            function_call="auto"
        )

        assistant_message = response['choices'][0]['message']

        if assistant_message.get('function_call'):
            function_name = assistant_message['function_call']['name']
            function_args = json.loads(assistant_message['function_call']['arguments'])

            # YOU EXECUTE THE FUNCTION
            if function_name == "get_weather":
                function_result = get_weather(city=function_args['city'])

            messages.append(assistant_message)
            messages.append({
                "role": "function",
                "name": function_name,
                "content": function_result
            })

            # SECOND API CALL
            second_response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=messages
            )

            final_message = second_response['choices'][0]['message']
            print(f"\nAssistant: {final_message['content']}")
            messages.append(final_message)

        else:
            print(f"\nAssistant: {assistant_message['content']}")
            messages.append(assistant_message)

if __name__ == "__main__":
    chat()
```

**Issues:**
- ❌ Manual function definition (20+ lines)
- ❌ Manual orchestration loop
- ❌ Manage conversation history yourself
- ❌ Check for function calls manually
- ❌ Execute functions manually
- ❌ Two API calls per function use
- ❌ OpenAI-specific format
- ❌ HTTP request/response (not persistent)

#### After MCP (27 lines)

```python
from mcp.server import Server
from mcp.server.stdio import stdio_server
import requests
import asyncio

app = Server("weather-server")

@app.tool()
async def get_weather(city: str) -> str:
    """Get current weather for a city"""
    api_key = "your-openweathermap-key"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    temp = data['main']['temp']
    description = data['weather'][0]['description']

    return f"Weather in {city}: {temp}°C, {description}"

if __name__ == "__main__":
    asyncio.run(stdio_server(app))
```

**Advantages:**
- ✅ Function definition AUTO-GENERATED from signature
- ✅ NO orchestration code needed
- ✅ NO conversation history management
- ✅ NO manual function checking
- ✅ MCP calls your function automatically
- ✅ ONE request/response cycle
- ✅ Standard JSON-RPC format (works with ANY MCP client)
- ✅ Persistent stdin/stdout connection

**Lines of code:**
- Before: **112 lines**
- After: **27 lines**
- **Reduction: 76%!**

---

### What You DON'T Have to Do Anymore

| Task | Before MCP | After MCP |
|------|-----------|----------|
| **Write function definitions** | ✋ Manual (20+ lines) | ✅ Auto-generated |
| **Manage orchestration loop** | ✋ Manual (while loop, if/else) | ✅ MCP handles it |
| **Conversation history** | ✋ Manual (messages array) | ✅ Client handles it |
| **Parse function calls** | ✋ Manual (json.loads, checking) | ✅ MCP parses it |
| **Execute functions** | ✋ Manual (if function_name == ...) | ✅ MCP routes it |
| **Package results** | ✋ Manual (dict building) | ✅ MCP packages it |
| **Two API calls** | ✋ Required | ✅ One request/response |
| **Vendor-specific code** | ✋ Different per AI | ✅ Standard format |

---

### Feature Comparison

| Feature | Before MCP | After MCP |
|---------|-----------|----------|
| **Lines of code** | 112 | 27 |
| **Function definition** | Manual dictionary | Decorator + type hints |
| **Tool discovery** | Send definitions every call | Automatic on connection |
| **Orchestration** | YOU write it | MCP handles it |
| **Connection type** | HTTP (stateless) | stdin/stdout (persistent) |
| **API calls per tool** | 2 (request + result) | 1 (single cycle) |
| **Format** | Vendor-specific | JSON-RPC 2.0 (standard) |
| **Works with** | One AI (OpenAI or Claude) | Any MCP client |
| **Add new tool** | 30+ lines | 5 lines (@app.tool + function) |
| **Error handling** | Manual | Built into MCP |
| **Type validation** | Manual | Automatic from type hints |

---

## Key Concepts Summary

### 1. The MCP Server Pattern

**Three simple parts:**

```python
# 1. Create server
app = Server("server-name")

# 2. Define tools with decorator
@app.tool()
async def my_tool(param: str) -> str:
    return result

# 3. Run server
asyncio.run(stdio_server(app))
```

**That's it!** MCP handles everything else.

---

### 2. Tool Registration with Decorators

**The `@app.tool()` decorator:**

```python
@app.tool()
async def get_weather(city: str) -> str:
    """Get current weather for a city"""
    ...
```

**Automatically generates:**
```json
{
  "name": "get_weather",
  "description": "Get current weather for a city",
  "inputSchema": {
    "type": "object",
    "properties": {
      "city": {"type": "string"}
    },
    "required": ["city"]
  }
}
```

**Magic ingredients:**
- Function name → tool name
- Docstring → tool description
- Type hints → input schema
- Parameters → required fields

---

### 3. stdin/stdout Communication

**How it works:**

```
┌──────────────┐                           ┌──────────────┐
│    Claude    │                           │  Your Server │
│              │                           │              │
│  sends JSON  │───── stdin ────────────→  │  receives    │
│              │                           │  on stdin    │
│              │                           │              │
│  receives    │←──── stdout ───────────── │  sends JSON  │
│  from stdout │                           │              │
└──────────────┘                           └──────────────┘
```

**Like a conversation through pipes:**
- Claude writes JSON to your server's stdin
- Your server reads from stdin
- Your server writes JSON to stdout
- Claude reads from your server's stdout

**Persistent connection:** Stays open for the entire session!

---

### 4. JSON-RPC 2.0 Protocol

**Every message is JSON-RPC:**

**Request:**
```json
{
  "jsonrpc": "2.0",
  "id": 123,
  "method": "tools/call",
  "params": {...}
}
```

**Response:**
```json
{
  "jsonrpc": "2.0",
  "id": 123,
  "result": {...}
}
```

**Standard format for:**
- Tool discovery: `method: "tools/list"`
- Tool execution: `method: "tools/call"`
- Resource access: `method: "resources/read"`

---

### 5. Automatic Tool Discovery

**Discovery happens once at startup:**

```
Claude starts
    ↓
Launches your server
    ↓
Sends: {"method": "tools/list"}
    ↓
Receives: {"result": {"tools": [...]}}
    ↓
Claude now knows all your tools!
```

**Never sent again!** Claude caches the tool list.

**Compare to before:**
- Before: Send function definitions with EVERY API call
- After: Discover once, use forever (until restart)

---

### 6. Where the "Kitchen" Is

**Still in YOUR code!**

```python
@app.tool()
async def get_weather(city: str) -> str:
    # THIS is still the kitchen:
    response = requests.get(url)  # ← Your computer calls API
    data = response.json()         # ← Your computer processes
    return result                  # ← Your computer returns
```

**MCP doesn't change WHERE work happens:**
- Still runs on YOUR computer
- Still accesses YOUR resources
- Still calls YOUR APIs

**MCP only changes HOW tools are:**
- Defined (decorator vs manual dict)
- Discovered (automatic vs manual)
- Called (JSON-RPC vs HTTP)
- Managed (MCP framework vs your code)

---

### 7. Works with ANY MCP Client

**Same server, different clients:**

```python
# Your server (weather_server.py)
# No changes needed!

@app.tool()
async def get_weather(city: str) -> str:
    ...
```

**Can be used by:**
- ✅ Claude Desktop
- ✅ Claude Web (when MCP support added)
- ✅ OpenAI ChatGPT (when MCP support added)
- ✅ VS Code with MCP extension
- ✅ Custom MCP clients
- ✅ Any future MCP-compatible AI

**One server, many clients!**

---

## Adding More Tools

**How easy is it to add more tools?**

### Before MCP: 30+ lines per tool

```python
# Need to define the function
def get_stock_price(symbol):
    ...

# Need to define the schema (20+ lines)
stock_function_definition = {
    "name": "get_stock_price",
    "description": "...",
    "parameters": {
        "type": "object",
        "properties": {
            "symbol": {
                "type": "string",
                "description": "..."
            }
        },
        "required": ["symbol"]
    }
}

# Need to add to function list
functions=[weather_function_definition, stock_function_definition]

# Need to add execution logic
if function_name == "get_weather":
    result = get_weather(...)
elif function_name == "get_stock_price":
    result = get_stock_price(...)
```

### After MCP: 5 lines per tool

```python
@app.tool()
async def get_stock_price(symbol: str) -> str:
    """Get current stock price"""
    # ... logic ...
    return result

# That's it! Done! Tool is automatically available!
```

**Adding 5 tools:**
- Before MCP: ~150 lines of boilerplate
- After MCP: ~25 lines total

---

## Error Handling

### Before MCP

```python
# YOU handle all errors manually
try:
    response = openai.ChatCompletion.create(...)
except openai.error.APIError as e:
    print(f"OpenAI API error: {e}")
except openai.error.Timeout as e:
    print(f"Timeout: {e}")
except Exception as e:
    print(f"Error: {e}")

# And handle function execution errors
try:
    result = get_weather(city)
except Exception as e:
    # What do you send back to OpenAI?
    # How do you format the error?
    ...
```

### After MCP

```python
@app.tool()
async def get_weather(city: str) -> str:
    # MCP automatically catches exceptions
    # and sends proper JSON-RPC error responses

    if city == "":
        raise ValueError("City cannot be empty")

    # MCP will automatically send:
    # {
    #   "jsonrpc": "2.0",
    #   "id": 123,
    #   "error": {
    #     "code": -32000,
    #     "message": "City cannot be empty"
    #   }
    # }
```

**MCP handles:**
- Exception catching
- Error formatting
- JSON-RPC error responses
- Proper error codes
- Stack traces (in debug mode)

---

## Real-World Example: Multiple Tools

**A complete MCP server with 3 tools:**

```python
from mcp.server import Server
from mcp.server.stdio import stdio_server
import requests
import asyncio

app = Server("multi-tool-server")

@app.tool()
async def get_weather(city: str) -> str:
    """Get current weather for a city"""
    # ... weather logic ...
    return f"Weather in {city}: ..."

@app.tool()
async def get_stock_price(symbol: str) -> str:
    """Get current stock price"""
    url = f"https://api.example.com/stock/{symbol}"
    response = requests.get(url)
    price = response.json()['price']
    return f"{symbol}: ${price}"

@app.tool()
async def search_database(query: str) -> str:
    """Search the local database"""
    import sqlite3
    conn = sqlite3.connect('mydata.db')
    results = conn.execute("SELECT * FROM items WHERE name LIKE ?", (f"%{query}%",))
    return str(results.fetchall())

if __name__ == "__main__":
    asyncio.run(stdio_server(app))
```

**37 lines total for 3 tools!**

**Compare to before MCP:** Would be ~300 lines!

**All three tools automatically:**
- Discovered by clients
- Properly typed
- Error handled
- Work with any MCP client

---

## Summary: Why MCP is Better

### Code Simplicity
- **Before:** 112 lines → **After:** 27 lines
- **76% reduction** in code
- **90% less boilerplate**

### Development Speed
- **Before:** 30 minutes to add a tool
- **After:** 2 minutes to add a tool
- **15x faster** development

### Maintainability
- **Before:** Change one tool, update 5 places
- **After:** Change function, done
- **Easy refactoring**

### Portability
- **Before:** Rewrite for each AI vendor
- **After:** Write once, works everywhere
- **Future-proof**

### Reliability
- **Before:** You handle errors, parsing, formatting
- **After:** MCP handles it all
- **Fewer bugs**

### Scalability
- **Before:** 10 tools = 1000+ lines
- **After:** 10 tools = 100 lines
- **Linear growth**

---

## What You Learned

### Core Concepts

1. **MCP Server Creation**
   ```python
   app = Server("name")
   ```

2. **Tool Registration**
   ```python
   @app.tool()
   async def my_tool(...):
   ```

3. **Type Hints for Schema**
   ```python
   async def tool(param: str) -> str:
   ```

4. **Server Execution**
   ```python
   asyncio.run(stdio_server(app))
   ```

5. **JSON-RPC Communication**
   - Standardized message format
   - Works over stdin/stdout
   - Persistent connection

6. **Automatic Discovery**
   - Tools discovered at startup
   - No repeated definitions
   - Cached by clients

### Key Differences from Before

| Aspect | Your Responsibility Before | Your Responsibility After |
|--------|--------------------------|-------------------------|
| Tool definition | ✋ Write JSON schema | ✅ Just type hints |
| Discovery | ✋ Send every time | ✅ Automatic |
| Orchestration | ✋ Write loop | ✅ MCP handles |
| Parsing | ✋ Manual JSON | ✅ MCP parses |
| Execution | ✋ Route manually | ✅ MCP routes |
| Errors | ✋ Handle everything | ✅ MCP handles |
| Format | ✋ Vendor-specific | ✅ Standard |

---

## Next Steps

Now that you understand MCP, you can:

1. **Create your own MCP servers**
   - File operations
   - Database queries
   - API integrations
   - System commands

2. **Use with Claude Desktop**
   - Add to config
   - Start using immediately
   - Combine multiple servers

3. **Deploy to production**
   - Docker containers
   - Kubernetes
   - Azure AKS
   - Cloud services

4. **Build complex workflows**
   - Multi-step processes
   - Agent interactions
   - Resource management

---

## Conclusion

**MCP transforms tool calling from:**
- Complex, manual, vendor-specific code
- **Into:** Simple, automatic, universal servers

**You write business logic, MCP handles:**
- Protocol details
- Tool discovery
- Request routing
- Response formatting
- Error handling
- Type validation

**Result:**
- Less code
- Faster development
- More reliable
- Future-proof
- Works everywhere

**That's the power of MCP!** 🚀

---

**End of Part 2: Tool Calling With MCP**

You now understand the complete picture! Ready to build your own MCP servers? 😊
