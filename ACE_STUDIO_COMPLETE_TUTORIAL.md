# ACE Studio Complete Tutorial
## Comprehensive Guide to AI Development Platform

---

## Table of Contents
1. [Getting Started with ACE Studio](#getting-started)
2. [Workspace Creation and Configuration](#workspace-creation)
3. [Projects and Organization](#projects-organization)
4. [Agent Development Workflow](#agent-development)
5. [MLflow Integration](#mlflow-integration)
6. [MCP Server Deployment](#mcp-server-deployment)
7. [Web Application Deployment](#web-app-deployment)
8. [Jobs and Scheduling](#jobs-scheduling)
9. [Data Management](#data-management)
10. [Benchmarker Tool](#benchmarker-tool)
11. [Access and Permissions](#access-permissions)

---

## 1. Getting Started with ACE Studio {#getting-started}

### What is ACE Studio?
ACE Studio is a comprehensive AI development platform that provides:
- **Workspace management** for development environments
- **Agent deployment** using MLflow
- **MCP (Model Context Protocol) servers** for tool collections
- **Web application hosting** (Streamlit, Dash, FastAPI)
- **Job scheduling** for remote script execution
- **Data storage** with ADFS integration
- **Benchmarking tools** for agent evaluation

### Access Requirements

#### For QRM Users:
- Request access: `RISClab_AI_QRM_developer_user`
- No additional requests needed for Databricks

#### For RISC-Tech Colleagues:
- Request access: `RISClab_AI_others_developer_user` OR
- Request access: `RISClab_AI_IB_developer` (if in IB organization)

#### Important Notes:
- Everything is automatically synchronized once you have the main access
- No separate Databricks access request needed
- Access is organization-dependent

---

## 2. Workspace Creation and Configuration {#workspace-creation}

### Step-by-Step Workspace Creation

#### Step 1: Navigate to Workspace Creation
1. Click the **"Create New Workspace"** button
2. System will load and generate a random workspace name
3. You can customize the name if needed

#### Step 2: Select Docker Image

**Available Docker Images:**
- **Base Image** (recommended for 99% of use cases)
  - Standard Python environment
  - Most common libraries pre-installed

- **CUDA Images** (for GPU workloads)
  - Different CUDA versions available
  - For deep learning and GPU-intensive tasks

- **PVT Image**
  - Specialized environment

**What is a Docker Image?**
- **Docker Image**: A pre-packaged template containing:
  - Operating system
  - Python version
  - Pre-installed libraries
  - System configurations

- **Think of it as**: A blueprint for your workspace environment
- **Analogy**: Like choosing a computer with pre-installed software

#### Step 3: Select IDE Instance

**Two Options Available:**

1. **VS Code**
   - Full-featured code editor
   - Extension support
   - Terminal access
   - Git integration

2. **JupyterLab**
   - Notebook interface
   - Interactive Python cells
   - Great for data exploration
   - Visualization support

#### Step 4: Configure Server Resources

**CPU Configuration:**
- Adjustable CPU requirements
- Higher CPU = higher cost
- Cost estimation shown in real-time

**Memory Configuration:**
- Adjustable RAM allocation
- Impacts performance and cost
- Choose based on workload needs

**Volume (Storage):**
- Persistent storage space
- For saving files and data
- Also impacts cost

**Environmental Variables:**
- Define custom environment variables
- Set API keys, configuration values
- Format: `KEY=VALUE`

#### Step 5: Link GitLab Project (Optional)

**Why Link GitLab?**
- Access your repositories directly in workspace
- Automatic code synchronization
- Version control integration

**Process:**

1. Click **"Link Projects"**
2. Click **"Link A Student"** (or relevant option)
3. You'll be prompted to generate a token

**Token Generation:**
1. Click **"Generate Personal Access Token"**
2. Opens GitLab page with pre-selected scopes:
   - **API scope** - allows API access
   - **Write Repository scope** - allows code pushes
3. Token name pre-filled: "ASUS2D token"
4. Click **"Create Personal Access Token"**
5. **Copy the token** (you won't see it again!)
6. Paste token back in ACE Studio
7. Click **"Verify Personal Access Token"**

**Select Project Details:**
- **Project**: Choose from your accessible DevCloud projects
  - Example: "cookbooks" project
- **Branch**: Select which branch to work on
  - Example: "main", "dev", "add-timeouts"
- **Python Version**: Choose 3.9, 3.10, or 3.11

**Dependency Management:**

ACE Studio supports two dependency managers:

1. **Poetry**
   - Modern Python dependency manager
   - Automatic dependency resolution
   - Lock file for reproducibility

2. **UV**
   - Fast dependency manager
   - Compatible with Poetry

**How it works:**
- Add packages to your project file
- Dependencies resolve automatically
- All packages install when workspace starts
- No manual `pip install` needed

#### Step 6: Create Workspace
1. Click **"Add to project"** (if using GitLab)
2. Click **"Create Workspace"**
3. Wait for provisioning (takes a few seconds to minutes)
4. Workspace appears in your workspace list

---

## 3. Projects and Organization {#projects-organization}

### MR (Model Registry) Projects

**What is an MR Project?**
- **Use case-based organization**
- Central place for team collaboration
- Shared access to models, data, and code

**Creating an MR Project:**
1. Navigate to the MR Project section
2. Click **"Create New MR Product"**
3. Sends email to AMR team for approval
4. Once created, all team members can access

**Benefits:**
- Share work across your project team
- Collaborative development
- Centralized model registry
- Shared data storage

### Execution Tabs

The platform has **three main execution sub-tabs**:

#### 3.1 Modeling Agents Tab
- **Purpose**: Deploy ML models and AI agents
- **What you can do**:
  - Deploy trained models
  - Deploy LangChain agents
  - Test and invoke models
  - Monitor performance

#### 3.2 Apps and MCP Servers Tab
- **Web Applications**:
  - Deploy Streamlit apps
  - Deploy Dash apps
  - Deploy FastAPI applications

- **MCP Marketplace**:
  - Browse available MCP servers
  - Deploy tool collections
  - Connect tools to agents

#### 3.3 Jobs Tab
- **Purpose**: Schedule remote script execution
- **Use cases**:
  - Model training overnight
  - Batch processing
  - Scheduled tasks
  - Data pipeline execution

---

## 4. Agent Development Workflow {#agent-development}

### Understanding the Agent Development Process

This section covers the **complete workflow** from development to deployment.

### Example: Simple Agent with LangGraph

#### What is LangGraph?
- **LangGraph**: A library for building agents with graphs
- **Node**: A step in the agent's workflow
- **Graph**: The complete flow of the agent

**Simple Agent Structure:**
```
START → CHAT → END
```
This is a 3-node graph:
1. **START node** - Entry point
2. **CHAT node** - Main processing
3. **END node** - Exit point

#### Step 1: Write Agent Code

**File: `simple_agent.py`**

This file contains your agent definition. Here's what you need:

**Required Components:**

1. **Agent Definition**
   ```python
   # This is your agent's logic
   # Define nodes, edges, and behavior
   ```

2. **Signature Inference**
   ```python
   # What is a signature?
   # - Defines input/output format
   # - Unique identifier for your model
   # - Required by MLflow

   # Think of it as: A contract describing what your agent accepts and returns
   ```

3. **MLflow Registration Code**
   ```python
   # Code to log your agent to MLflow
   # Makes it available for deployment
   ```

#### Step 2: Understanding MLflow Concepts

**What is MLflow?**
- **MLflow**: A platform for managing machine learning lifecycle
- **Purpose**: Track experiments, package code, deploy models

**Key Concepts Explained:**

1. **Experiment**
   - **What it is**: A collection of related runs
   - **Think of it as**: Your use case or project
   - **Example**: "cookbook-example", "customer-chatbot", "fraud-detection"
   - **Analogy**: Like a folder containing different versions of your work

2. **Run**
   - **What it is**: A single execution/version of your agent
   - **Think of it as**: One version of your agent
   - **Example**: "Entazed-Moth-548" (auto-generated name)
   - **Each run has**:
     - Unique ID
     - Timestamp
     - Parameters used
     - Artifacts (saved files)
     - Metrics

**Relationship:**
```
Experiment (Use Case)
  ├── Run 1 (Version 1 - GPT-4, temp=0.5)
  ├── Run 2 (Version 2 - GPT-4, temp=0.8)
  └── Run 3 (Version 3 - GPT-4o-mini, temp=0.5)
```

#### Step 3: Logging Your Agent

**Code Pattern:**

```python
import mlflow

# STEP 1: Set the experiment
# This creates or uses an existing experiment
mlflow.set_experiment("cookbook-example")

# What does this mean?
# - mlflow: The MODULE we imported (collection of tools)
# - set_experiment: A FUNCTION inside mlflow module
# - "cookbook-example": A STRING (text in quotes) - the experiment name
# - This line: "Tell MLflow to use/create experiment called 'cookbook-example'"

# STEP 2: Start a run
# This begins tracking a new version
with mlflow.start_run():
    # What is 'with'?
    # - KEYWORD: Creates a context (temporary workspace)
    # - Ensures proper cleanup when done
    # - Everything indented runs inside this context

    # What is mlflow.start_run()?
    # - mlflow: The MODULE
    # - start_run: A FUNCTION
    # - (): PARENTHESES mean we're calling/executing the function
    # - This creates a new run (new version) in our experiment

    # Log the agent (save it)
    mlflow.log_model(...)
    # - log_model: A FUNCTION that saves your model
    # - Stores all files needed to run your agent
```

**Line-by-Line Explanation:**

```python
mlflow.set_experiment("cookbook-example")
```
- `mlflow` - Variable name pointing to the imported module
- `.` - DOT NOTATION: Access something inside mlflow
- `set_experiment` - Function (method) inside mlflow
- `()` - Parentheses: We're CALLING the function
- `"cookbook-example"` - STRING argument (text data)
- FULL MEANING: "Use the mlflow module's set_experiment function with the name 'cookbook-example'"

**What Gets Saved in a Run?**

When you log an agent, MLflow saves:

1. **Artifacts** (files):
   - Agent code
   - Dependencies (requirements.txt)
   - Environment variables
   - Input examples
   - Model weights

2. **Metadata**:
   - Timestamp
   - Parameters used
   - Framework (e.g., "langchain")
   - Python version

3. **Metrics** (if tracked):
   - Accuracy
   - Performance scores
   - Custom metrics

#### Step 4: Viewing Your Experiment in MLflow UI

**Accessing MLflow:**
1. Navigate to the MLflow section in ACE Studio
2. Click on your experiment name (e.g., "cookbook-example")
3. You'll see a login prompt - authenticate
4. View all your runs

**In the MLflow UI:**

**Experiment View:**
- List of all runs
- Run names (e.g., "Entazed-Moth-548")
- Creation dates
- Parameters
- Metrics

**Run Details:**
Click on a run to see:

1. **Overview**
   - Run ID
   - Start time
   - Duration
   - Status

2. **Parameters**
   - Model type
   - Temperature
   - System prompt
   - Other hyperparameters

3. **Artifacts** (files saved)
   - Agent code
   - `requirements.txt` - Python packages needed
   - `conda.yaml` - Environment specification
   - Input examples
   - Model files

#### Step 5: Loading and Testing Your Agent

**From Code:**

```python
import mlflow

# What is import?
# - KEYWORD: Brings in external code/library
# - mlflow: The library name we're importing
# - After import, 'mlflow' becomes a VARIABLE holding the module

# Set the experiment
mlflow.set_experiment("cookbook-example")
# - Tells MLflow which experiment to use
# - Same one we created earlier

# Load the model
model_uri = "runs:/RUN_ID/model"
# - model_uri: A VARIABLE (we chose this name, could be 'x' or 'path')
# - = : ASSIGNMENT OPERATOR (puts value into variable)
# - "runs:/RUN_ID/model": A STRING specifying model location
# - Think of it as: An address/path to your saved agent

loaded_agent = mlflow.pyfunc.load_model(model_uri)
# - loaded_agent: VARIABLE to store the loaded agent
# - mlflow.pyfunc: A SUB-MODULE inside mlflow
# - load_model: FUNCTION to load saved models
# - (model_uri): Pass the URI as ARGUMENT (input to function)
# - FULL MEANING: "Use MLflow's pyfunc module to load model from the URI, store in loaded_agent"

# Chat with it
response = loaded_agent.predict({"question": "What's my name?"})
# - response: VARIABLE to store the answer
# - loaded_agent: OBJECT (instance of the loaded model)
# - .predict: METHOD (function belonging to loaded_agent)
# - {"question": "What's my name?"}: DICTIONARY (key-value pair)
#   - { }: CURLY BRACES define a dictionary
#   - "question": KEY (string)
#   - "What's my name?": VALUE (string)
# - FULL MEANING: "Call the predict method on loaded_agent with this input"
```

**Example Conversation:**
```python
# First message: Introduce yourself
loaded_agent.predict({"message": "My name is Morpheus"})

# Second message: Ask for name
loaded_agent.predict({"message": "What's my name?"})
# Response: "Your name is Morpheus"
```

---

## 5. MLflow Integration {#mlflow-integration}

### Deploying Your Agent Through ACE UI

#### Step 1: Navigate to Models and Agents
1. In ACE Studio, click **"Models and Agents"** tab
2. Click **"Deploy"** button (top left)

#### Step 2: Configure Deployment

**Deployment Form Fields:**

1. **Name**
   - Enter deployment name
   - Example: "test", "customer-chatbot-v1"
   - This is what you'll use to reference it

2. **Select Experiment**
   - Dropdown of all your experiments
   - Choose the one containing your agent
   - Example: "Ace-Agent-Cookbook-Example"
   - System fetches all runs from this experiment

3. **Select Run**
   - Dropdown of all runs in the experiment
   - Shows run names (e.g., "Entazed-Moth-548")
   - Choose the version you want to deploy
   - Tip: Use the latest successful run

4. **Select Framework**
   - **LangChain**: For LangChain-based agents
   - **Scikit-learn**: For traditional ML models
   - **Python**: For custom Python models
   - **Other frameworks**: Based on what you used

**Important:** Select the framework you used when creating your agent!

#### Step 3: Create Deployment
1. Click **"Create"** button
2. Deployment process begins (takes 1-2 minutes)
3. Wait for status to show "Up"

#### Step 4: Deployment Ready

**What You See After Deployment:**

1. **Status Indicator**: Green "Up" badge
2. **Deployment URL**: Endpoint for API calls
3. **Model Card Button**: View details
4. **Configuration**: Server settings

### Using the Model Card Interface

#### Accessing Model Card
1. Click **"Model Card"** button on your deployment
2. Opens detailed view

**Model Card Sections:**

#### 1. Overview Tab
- Deployment name
- Associated run ID
- Framework used
- Creation timestamp
- Server configuration (CPU, memory)

#### 2. Inference Tab

**This is where you test your agent!**

**Three Inference Methods:**

1. **Invoke** (Single Request)
   - Send one input
   - Get one response
   - Synchronous (waits for response)
   - Best for: Testing, single predictions

2. **Batch** (Multiple Requests)
   - Send array of inputs
   - Get array of responses
   - Process multiple items at once
   - Best for: Bulk processing

3. **Stream** (Streaming Response)
   - Send one input
   - Receive response in chunks
   - Real-time streaming
   - Best for: Chat applications, long responses

**Testing Example:**

**Input Format:**
```json
{
  "messages": [
    {"role": "user", "content": "My name is Morpheus"},
    {"role": "user", "content": "What is my name?"}
  ]
}
```

**Breakdown:**
- `{...}`: OBJECT (container for data)
- `"messages"`: KEY (field name)
- `[...]`: ARRAY (list of items)
- Each item is an OBJECT with:
  - `"role"`: Who's speaking ("user", "assistant", "system")
  - `"content"`: The actual message text

**Click "Send":**
- Request goes to your deployed agent
- Agent processes the messages
- Response appears below

**Example Response:**
```json
{
  "response": "Your name is Morpheus."
}
```

### Using the Deployment URL

**API Endpoint:**
After deployment, you get a URL like:
```
https://ace-studio.example.com/api/v1/agents/test/invoke
```

**Using from Code:**

```python
import requests  # Library for HTTP requests

# What is import?
# - KEYWORD to bring in external library
# - requests: Library name (for making web requests)

url = "https://ace-studio.example.com/api/v1/agents/test/invoke"
# - url: VARIABLE (we chose this name)
# - = : Assignment
# - "https://...": STRING containing the endpoint address

payload = {
    "messages": [
        {"role": "user", "content": "Hello"}
    ]
}
# - payload: VARIABLE containing request data
# - {...}: DICTIONARY (key-value container)
# - "messages": KEY
# - [...]: LIST (array) as VALUE
# - Nested structure: Dict containing list of dicts

response = requests.post(url, json=payload)
# - response: VARIABLE to store result
# - requests: MODULE we imported
# - .post: METHOD (function for POST requests)
# - url: ARGUMENT 1 - where to send request
# - json=payload: ARGUMENT 2 - data to send
#   - json=: PARAMETER NAME
#   - payload: PARAMETER VALUE
# - MEANING: "Send POST request to URL with payload as JSON"

result = response.json()
# - result: VARIABLE to store parsed response
# - response: OBJECT from previous line
# - .json(): METHOD that parses JSON response
# - (): PARENTHESES mean we're calling the method
# - MEANING: "Convert response to Python dictionary"

print(result)
# - print: BUILT-IN FUNCTION (displays output)
# - result: ARGUMENT (what to print)
# - MEANING: "Show the result on screen"
```

---

## 6. MCP Server Deployment {#mcp-server-deployment}

### What is MCP (Model Context Protocol)?

**MCP Explained:**

- **MCP Server**: A collection of tools that an agent can use
- **Purpose**: Provide specialized capabilities to agents
- **Example**: Weather API, database queries, file operations

**Think of it as:**
- A toolbox for your agent
- Each tool performs a specific function
- Agent decides which tool to use

**Real Example: Canteen MCP Server**
- **Purpose**: Get cafeteria menu information
- **Tools Available**:
  - Get today's menu
  - Get weekly menu
  - Get menu by date
  - Check availability

### MCP Marketplace

#### Registering Your MCP Server

**Step 1: Access Marketplace**
1. Navigate to **"Apps and MCP Servers"** tab
2. Click **"MCP Marketplace"**
3. Click **"Register a Project"**

**Step 2: Select GitLab Project**
- Search for your MCP server repository
- Must be a GitLab project
- Example: "asp-mcp-server"

**Step 3: Add Description**
- Brief description of what tools are available
- Helps others understand server purpose
- Example: "Provides canteen menu information for Zurich office"

**Step 4: Register**
- Click **"Register Project"**
- Server appears in marketplace
- Available for deployment

### Deploying an MCP Server

#### Step 1: Select Server
1. Browse marketplace
2. Click on desired server
3. Example: "ASP MCP Server"

**Server Information Display:**
- README content shown
- Tools description
- Usage examples
- Configuration requirements

#### Step 2: Configure Deployment

**Click "Deploy"**

**Configuration Options:**

1. **Deployment Name**
   - Choose unique name
   - Example: "test", "canteen-menu-prod"
   - Used to reference this deployment

2. **MCP Transport Type**

   **Two Options:**

   - **HTTP**
     - Standard HTTP protocol
     - Request-response pattern
     - Good for most use cases

   - **SSE (Server-Sent Events)**
     - Real-time streaming
     - Server pushes updates
     - Good for live data

   **Which to choose?**
   - Either works fine
   - No significant difference for most cases
   - Personal preference

3. **Entry Point Script**
   - Auto-generated shell script
   - Defines how MCP server starts
   - Usually don't need to modify

**Example Entry Point:**
```bash
#!/bin/bash
# What is this?
# - #!/bin/bash: SHEBANG (tells system to use bash shell)
# - This is a SHELL SCRIPT (list of commands to run)

python mcp_server.py
# - python: COMMAND to run Python interpreter
# - mcp_server.py: ARGUMENT (file to run)
# - MEANING: "Run the Python file mcp_server.py"
```

#### Step 3: Deploy
- Click **"Close"** (confirms configuration)
- Click **"Deploy"**
- Wait for deployment (1-2 minutes)
- Status shows "Up" when ready

### Connecting MCP Server to Continue Extension

**What is Continue Extension?**
- **Continue**: VS Code/JetBrains extension
- **Purpose**: AI coding assistant
- **Integration**: Works with your deployed agents and MCP servers

#### Step 1: Copy Configuration

After deployment:
1. Click **"Copy Container Configuration"** button
2. Configuration copied to clipboard

**What's in the configuration?**
```yaml
# This is YAML format (key: value pairs)
mcpServers:
  canteen-menu:
    url: "https://..."
    transport: "sse"
```

- `mcpServers`: KEY (section header)
- Indentation matters in YAML!
- `canteen-menu`: SERVER NAME
- `url`: ENDPOINT address
- `transport`: CONNECTION type

#### Step 2: Navigate to Workspace
1. Go back to your running workspace
2. Open VS Code or JupyterLab instance
3. Look for **Continue extension** icon

#### Step 3: Configure Continue

1. Click **MCP Server icon** in Continue
2. Click **"Add MCP Server"**
3. Creates/opens YAML configuration file
4. Paste copied configuration (Ctrl+V)
5. Save file

**Configuration File Location:**
- Usually: `.continue/config.yaml`
- Hidden folder (starts with `.`)

#### Step 4: Verify Connection

**Continue Extension Interface:**
- Should show your MCP server connected
- Green indicator = working
- Red/yellow = configuration issue

**Common Errors:**
- Indentation wrong in YAML
- URL incorrect
- Authentication missing

### Using MCP Server with Agent

#### Example Conversation

**You can now ask:**
```
User: "What food is available in the canteen in Zurich?"
```

**What happens behind the scenes:**

1. **Agent receives question**
   - Analyzes what you're asking
   - Determines it needs canteen information

2. **Agent discovers available tools**
   - Sees MCP server connected
   - Reads tool descriptions
   - Finds "get menu" tool

3. **Agent invokes tool**
   - Calls MCP server
   - Passes parameters (location: Zurich)
   - Waits for response

4. **MCP server executes**
   - Fetches canteen data
   - Returns menu information

5. **Agent formulates response**
   - Receives tool output
   - Formats nicely for user
   - Sends back answer

**Example Response:**
```
Assistant: "Today's menu at the Zurich canteen includes:
- Soup: Tomato basil
- Main 1: Chicken curry with rice
- Main 2: Vegetarian pasta
- Dessert: Fruit salad"
```

### Understanding Tool Selection

**How does agent know which tool to use?**

**Tool Definition Example:**
```json
{
  "name": "get_menu",
  "description": "Retrieves cafeteria menu for specified date and location",
  "parameters": {
    "location": "string",
    "date": "string (YYYY-MM-DD)"
  }
}
```

**Agent's Decision Process:**
1. Reads all available tool descriptions
2. Matches user intent to tool purpose
3. Extracts parameters from user query
4. Calls appropriate tool
5. Uses response to answer

**This is called: Function Calling or Tool Use**

---

## 7. Web Application Deployment {#web-app-deployment}

### Supported Frameworks

ACE Studio supports **three web frameworks**:

1. **Streamlit**
   - Python-based
   - Quick UI creation
   - Great for data apps
   - Minimal code required

2. **Dash**
   - Python-based
   - Plotly integration
   - Interactive dashboards
   - More control than Streamlit

3. **FastAPI**
   - REST API framework
   - Multiple endpoints
   - Full backend capability
   - Production-ready

### Deploying a Streamlit App

#### Step 1: Create New App
1. Navigate to **"Apps and MCP Servers"** tab
2. Click **"Create New App"**

#### Step 2: Configure App

**Configuration Options:**

1. **Docker Image**
   - Select **"Base"** for most apps
   - Choose Python version (3.9, 3.10, 3.11)
   - Base image has common libraries

2. **Link GitLab Project**
   - Click **"Add Project"**
   - Select your project (e.g., "base-cookbooks")
   - Choose branch
   - App code pulled from repository

3. **Entry Point Selection**

   **This is critical!**

   - Entry point = file that starts your app
   - Example: `app.py` or `main.py`
   - Select from dropdown or browse

   **Example: Streamlit App**
   ```python
   # File: app.py

   import streamlit as st
   # - import: KEYWORD to load library
   # - streamlit: LIBRARY name (web framework)
   # - as st: ALIAS (short name to use instead)
   # - Now we can use 'st' instead of typing 'streamlit'

   st.title("My App")
   # - st: The module we imported (alias for streamlit)
   # - .title: METHOD (function) to create title
   # - "My App": STRING argument (the title text)
   # - MEANING: "Create a title saying 'My App'"

   st.write("Hello World")
   # - st.write: FUNCTION to display content
   # - Can show text, dataframes, charts, etc.
   ```

4. **Framework Selection**

   - Select **"Streamlit"** from dropdown
   - System auto-generates entry script

**Auto-Generated Entry Script:**
```bash
#!/bin/bash
streamlit run app.py --server.port=8888 --server.address=0.0.0.0
```

**Line-by-Line Explanation:**

```bash
#!/bin/bash
```
- `#!`: SHEBANG (special marker)
- `/bin/bash`: Path to bash interpreter
- MEANING: "This is a bash script"

```bash
streamlit run app.py --server.port=8888 --server.address=0.0.0.0
```
- `streamlit`: COMMAND (the Streamlit CLI)
- `run`: SUB-COMMAND (tells Streamlit to run app)
- `app.py`: ARGUMENT (which file to run)
- `--server.port=8888`: FLAG (configuration option)
  - `--`: Indicates a flag
  - `server.port`: FLAG NAME
  - `=8888`: FLAG VALUE (port number)
  - MEANING: "Listen on port 8888"
- `--server.address=0.0.0.0`: FLAG
  - `0.0.0.0`: Special IP (means "all network interfaces")
  - MEANING: "Accept connections from anywhere"

**Why these specific values?**
- Port 8888: ACE Studio requirement
- Address 0.0.0.0: Allows external access
- **Don't change these unless you know what you're doing!**

#### Custom Entry Points

**For Other Frameworks:**

**Dash Example:**
```bash
#!/bin/bash
python app.py
# Make sure app.py has:
# app.run_server(host='0.0.0.0', port=8888)
```

**FastAPI Example:**
```bash
#!/bin/bash
uvicorn main:app --host 0.0.0.0 --port 8888
```
- `uvicorn`: COMMAND (ASGI server for FastAPI)
- `main:app`: MODULE:OBJECT format
  - `main`: Python file name (main.py)
  - `:`: SEPARATOR
  - `app`: Variable name in main.py
- `--host 0.0.0.0`: Listen on all interfaces
- `--port 8888`: Port number

**Critical Requirements:**
- **Port must be 8888**
- **Host must be 0.0.0.0** (or localhost)
- These are required by ACE platform

#### Step 3: Deploy

1. Click **"Create and Deploy"**
2. Deployment starts (1-2 minutes)
3. Progress shown in UI

#### Step 4: Access Your App

**After Deployment:**

1. **Status**: Shows "Running" with green indicator
2. **URL**: Unique URL for your app
   - Example: `https://ace.example.com/apps/username/my-app`
3. **Open Button**: Click to view app

**URL Sharing:**
- Share URL with team members
- Only accessible to those in your AMR project
- If using personal namespace, only you can access

**Example App: Uber Pickups NYC**
- Streamlit demo application
- Shows Uber pickup locations on map
- Interactive slider for time selection
- Demonstrates Streamlit capabilities

### Web App Features

#### Available Capabilities

**Streamlit Apps Can:**
- Display dataframes and tables
- Create charts (line, bar, scatter)
- Show maps
- Accept user input (text, sliders, buttons)
- Upload files
- Download data
- Real-time updates

**Dash Apps Can:**
- Complex dashboards
- Plotly charts
- Multiple pages
- Custom callbacks
- Advanced interactivity

**FastAPI Apps Can:**
- REST API endpoints
- Database connections
- Authentication
- Background tasks
- WebSocket support

---

## 8. Jobs and Scheduling {#jobs-scheduling}

### What are Jobs?

**Job Definition:**
- **Job**: Remote execution of a script or file
- **Purpose**: Run tasks without tying up your workspace
- **Use Cases**:
  - Model training (long-running)
  - Batch processing
  - Data pipeline execution
  - Scheduled tasks

**Think of it as:**
- Submitting a task to run in the background
- Like cron jobs or scheduled tasks
- Runs on separate resources

### Creating a Job

#### Step 1: Navigate to Jobs
1. Click **"Jobs"** tab in ACE Studio
2. Click **"Create Job"** button

#### Step 2: Configure Job

**Configuration Options:**

1. **Docker Image**
   - Select environment for job
   - Same options as workspace
   - Choose based on requirements

2. **Select GitLab Project**
   - Choose project containing your code
   - Select branch
   - Code pulled automatically

3. **Select File to Run**
   - Browse project files
   - Choose Python script
   - Example: `train_model.py`

**Example: Training Job**
```python
# File: train_model.py

# This script trains a model and saves results

import pandas as pd
import mlflow

# Load data
data = pd.read_csv('data.csv')

# Train model
model = train_my_model(data)

# Log to MLflow
with mlflow.start_run():
    mlflow.log_model(model, "model")
    mlflow.log_metric("accuracy", 0.95)

print("Training complete!")
```

4. **Resource Configuration**
   - CPU requirements
   - Memory requirements
   - GPU (if needed)

5. **Create Schedule (Optional)**

**Scheduling Options:**

- **One-time**: Run once, now or at specific time
- **Recurring**: Run on schedule

**Cron Schedule Examples:**

```
0 2 * * *    # Every day at 2 AM
0 9 * * 1    # Every Monday at 9 AM
*/30 * * * * # Every 30 minutes
```

**What is Cron Format?**
```
* * * * *
│ │ │ │ │
│ │ │ │ └── Day of week (0-7, 0 and 7 = Sunday)
│ │ │ └──── Month (1-12)
│ │ └────── Day of month (1-31)
│ └──────── Hour (0-23)
└────────── Minute (0-59)
```

**Use Case Example:**
```
# Schedule training every night at 2 AM
0 2 * * *

# Why?
# - Training takes 4 hours
# - Runs overnight
# - Results ready in morning
# - Doesn't block development work
```

#### Step 3: Submit Job
1. Review configuration
2. Click **"Create Job"**
3. Job queued for execution

### Monitoring Jobs

**Job Status:**
- **Queued**: Waiting to start
- **Running**: Currently executing
- **Completed**: Finished successfully
- **Failed**: Error occurred

**Viewing Results:**
1. Click on job in list
2. View logs and output
3. Check execution time
4. Download artifacts

### Job Output Storage

**Where Output Goes:**
- **Jobs folder**: In Data section
- **Path**: `/data/jobs/JOB_ID/`
- **Contents**:
  - Logs (stdout, stderr)
  - Generated files
  - Model artifacts

**Accessing Output:**
```python
# In your workspace or another job
import os

job_output = "/data/jobs/12345/output.csv"
df = pd.read_csv(job_output)
```

### Comparison to Domino

**For Domino Users:**

| Feature | Domino | ACE Jobs |
|---------|--------|----------|
| Submit job | ✓ | ✓ |
| Schedule | ✓ | ✓ |
| View logs | ✓ | ✓ |
| Artifacts | ✓ | ✓ |
| Resource config | ✓ | ✓ |

**Key Similarity:**
- Same workflow concept
- Remote execution
- Scheduled runs
- Output persistence

---

## 9. Data Management {#data-management}

### Data Tab Overview

The **Data** section has three main areas:

1. **Files**
2. **Indexes** (Vector Stores)
3. **Shared Storage**

### File Storage Structure

#### Three Main Folders:

1. **Jobs Folder**
   - **Purpose**: Stores job output
   - **Path**: `/data/jobs/`
   - **Auto-created**: When jobs complete
   - **Contents**:
     - Job logs
     - Generated files
     - Model outputs

2. **Private Folder**
   - **Purpose**: Your personal storage
   - **Path**: `/data/private/USERNAME/`
   - **Access**: Only you
   - **Use for**:
     - Personal datasets
     - Experimental files
     - Temporary storage

3. **Projects Folder**
   - **Purpose**: Team-shared storage
   - **Path**: `/data/projects/PROJECT_NAME/`
   - **Access**: All project members
   - **Use for**:
     - Shared datasets
     - Team resources
     - Collaboration

### Uploading Files

#### Via Web Interface:

1. Navigate to **Data** tab
2. Choose folder (Private or Projects)
3. Click **"Upload"** button
4. Select files from computer
5. Files upload to ACE storage

#### From Workspace:

**Python Example:**
```python
import shutil

# Copy file to shared storage
source = "local_file.csv"
destination = "/data/projects/my-project/dataset.csv"

shutil.copy(source, destination)
# - shutil: MODULE (shell utilities)
# - .copy: FUNCTION to copy files
# - source: SOURCE file path
# - destination: DESTINATION file path
```

**Bash Example:**
```bash
cp local_file.csv /data/projects/my-project/dataset.csv
# - cp: COMMAND (copy)
# - First arg: source
# - Second arg: destination
```

### Understanding ADFS Storage

**What is ADFS?**
- **ADFS**: Azure Data Lake File System
- **Type**: Cloud-based distributed file system
- **Benefits**:
  - Already in cloud
  - High availability
  - Scalable
  - Shared across workspaces

**How it works:**
```
Your Workspace <---> ADFS Storage <---> Teammate's Workspace
     (read/write)                          (read/write)
```

**Key Points:**
- Files persist when workspace stops
- Accessible from any workspace
- Team members see same files
- No manual syncing needed

### Accessing Files in Workspace

**File paths are consistent:**

```python
# These paths work in any workspace
private_file = "/data/private/username/my_data.csv"
shared_file = "/data/projects/my-project/dataset.csv"
job_output = "/data/jobs/12345/results.csv"

# Read data
import pandas as pd
df = pd.read_csv(shared_file)
```

**Why this matters:**
- Predictable paths
- No configuration needed
- Works across all workspaces
- Team collaboration easy

### Vector Stores (Indexes)

**What are Vector Stores?**
- **Vector Store**: Database for embeddings
- **Purpose**: Semantic search for RAG applications
- **Use case**: Agent retrieval systems

**Available Vector Stores:**

1. **Qdrant** (Currently available)
   - Open-source vector database
   - High performance
   - Filtering capabilities

2. **Azure AI Search** (Coming soon)
   - Microsoft's vector search
   - Enterprise features
   - Integration with Azure

### Creating a Vector Store Collection

**Purpose: RAG (Retrieval-Augmented Generation)**

**What is RAG?**
1. User asks question
2. System searches documents (using vector store)
3. Relevant documents retrieved
4. Agent uses docs to answer

**Creating Collection:**
1. Navigate to **Indexes** section
2. Click **"Create Collection"**
3. Configure:
   - **Name**: Collection identifier
   - **Dimension**: Embedding size (e.g., 1536 for OpenAI)
   - **Distance**: Similarity metric (cosine, euclidean)

**Adding Documents:**
```python
from qdrant_client import QdrantClient

# Connect to vector store
client = QdrantClient(url="...")
# - QdrantClient: CLASS (blueprint for client objects)
# - (...): Calling class creates OBJECT (instance)
# - client: VARIABLE storing the object

# Add documents
client.upsert(
    collection_name="my-docs",
    points=[
        {
            "id": 1,
            "vector": [0.1, 0.2, ...],  # Embedding
            "payload": {"text": "Document content"}
        }
    ]
)
```

**Connecting to Agent:**
```python
# Agent can now search this collection
retriever = vector_store.as_retriever()
agent = create_retrieval_agent(llm, retriever)
```

---

## 10. Benchmarker Tool {#benchmarker-tool}

### What is Benchmarker?

**Benchmarker** is a library for evaluating agent performance.

**Purpose:**
- Test agent with different configurations
- Measure performance with metrics
- Find optimal hyperparameters
- Compare versions

**Library Location:**
- Part of RISClab ecosystem
- Available in ACE Studio
- Documentation in cookbooks

### Core Concepts

#### 1. Hyperparameter Space

**What are Hyperparameters?**
- **Hyperparameter**: Configuration setting for model/agent
- **Examples**:
  - Temperature (0-1)
  - System prompt
  - Model version
  - Max tokens

**Hyperparameter Space:**
- **Space**: All possible combinations to test
- **Example**:
  ```
  Temperature: [0, 0.4, 0.8]
  Model: [GPT-4, GPT-4o-mini]

  Total combinations: 3 × 2 = 6
  ```

#### 2. Evaluation Metrics

**What is a Metric?**
- **Metric**: Measurement of performance
- **Purpose**: Quantify agent quality
- **Output**: Numerical score

**Predefined Metrics:**

1. **Answer Correctness**
   - Compares answer to ground truth
   - Score: 0-5
   - Uses LLM as judge

2. **Answer Relevance**
   - Is answer on-topic?
   - Checks if addresses question
   - Score: 0-5

3. **Faithfulness**
   - Does answer match retrieved docs?
   - For RAG systems
   - Prevents hallucination

4. **Factuality**
   - Factual accuracy
   - Compares to known facts
   - Score: 0-5

5. **Contextual Precision**
   - Relevance of retrieved context
   - RAG evaluation
   - Higher = better retrieval

6. **Contextual Recall**
   - Did retrieval get all relevant docs?
   - RAG evaluation
   - Higher = better coverage

7. **Conciseness**
   - Is answer concise?
   - Penalizes verbosity
   - Score: 0-5

**Note:** There are 7-8 predefined metrics in total.

### Setting Up an Evaluation

#### Step 1: Define Hyperparameter Space

**Code Example:**

```python
from benchmarker import EvaluationRun

# What is 'from...import'?
# - from benchmarker: Look in benchmarker MODULE
# - import EvaluationRun: Bring in EvaluationRun CLASS
# - Now can use EvaluationRun directly

# Define hyperparameters to test
hyperparameters = {
    "temperature": [0, 0.4, 0.8],
    "system_prompt": [
        "You are an MLflow agent.",
        "You are an MLflow agent with expertise in experiment operations."
    ],
    "deployment_name": ["gpt-4o", "gpt-4o-mini"]
}
# - hyperparameters: VARIABLE (dictionary)
# - {...}: DICTIONARY (key-value pairs)
# - "temperature": KEY
# - [0, 0.4, 0.8]: VALUE (list of numbers to test)
# - Each key maps to LIST of values to try

# What is a dictionary?
# - DICTIONARY: Collection of key: value pairs
# - {...}: CURLY BRACES define dictionary
# - "key": value: Each entry
# - Access: hyperparameters["temperature"] gives [0, 0.4, 0.8]
```

**Calculation of Search Space:**
```
3 temperatures × 2 prompts × 2 models = 12 combinations
```

**All Combinations:**
1. temp=0, prompt1, gpt-4o
2. temp=0, prompt1, gpt-4o-mini
3. temp=0, prompt2, gpt-4o
4. temp=0, prompt2, gpt-4o-mini
5. temp=0.4, prompt1, gpt-4o
6. temp=0.4, prompt1, gpt-4o-mini
... (12 total)

#### Step 2: Create Evaluation Run

```python
eval_run = EvaluationRun(
    agent_path="path/to/agent.py",
    hyperparameters=hyperparameters,
    metrics=["answer_correctness", "faithfulness"],
    test_data=test_dataset,
    top_k=3
)
# - eval_run: VARIABLE storing evaluation object
# - EvaluationRun: CLASS we imported
# - (...): PARENTHESES mean calling/instantiating class
# - agent_path: PARAMETER NAME
# - "path/to/agent.py": ARGUMENT (parameter value)
# - This creates an OBJECT (instance of EvaluationRun)

# Parameters explained:
# - agent_path: Where to find your agent code
# - hyperparameters: Dictionary we defined above
# - metrics: LIST of metric names to calculate
# - test_data: Dataset to evaluate against
# - top_k: Return top 3 best configurations
```

**What is top_k?**
- **k**: Number of best results to return
- **top_k=3**: Return 3 best configurations
- Sorted by performance score
- Helpful for finding winners

#### Step 3: Run Evaluation

```python
results = eval_run.run()
# - results: VARIABLE to store results
# - eval_run: OBJECT from previous step
# - .run(): METHOD (function) to execute evaluation
# - (): Call the method
# - This starts the evaluation process
```

**What happens:**
1. For each of 12 combinations:
   - Create agent with those parameters
   - Log to MLflow (creates run)
   - Test against test dataset
   - Calculate metrics
   - Store results
2. Compare all results
3. Rank by performance
4. Return top 3

### Custom Metrics

**When to create custom metric:**
- Predefined metrics don't fit your use case
- Need domain-specific evaluation
- Want different scoring criteria

#### Creating Custom Metric

**Example: Factuality Metric**

```python
from benchmarker import make_generic_metric

# Define the metric
factuality_metric = make_generic_metric(
    name="factuality",
    definition="Measures factual accuracy of the response",
    grading_prompt="""
    Score the response based on factual accuracy:
    1 = Completely inaccurate
    2 = Mostly inaccurate
    3 = Partially accurate
    4 = Mostly accurate
    5 = Completely accurate
    """,
    examples=[
        {
            "input": "Summarize the Gettysburg Address",
            "output": "It was a speech about freedom in 1863",
            "score": 2,
            "justification": "Correct year but oversimplified and missing key points"
        },
        {
            "input": "Summarize the Gettysburg Address",
            "output": "Lincoln's 1863 speech affirming equality and dedication to Union soldiers",
            "score": 4,
            "justification": "Accurate main points, good detail"
        }
    ],
    parameters=["input", "output"]
)
```

**Line-by-Line Explanation:**

```python
factuality_metric = make_generic_metric(...)
```
- `factuality_metric`: VARIABLE (stores the metric object)
- `=`: ASSIGNMENT
- `make_generic_metric`: FUNCTION (creates metric)
- `(...)`: Arguments passed to function

**Parameters:**

1. **name**: String identifier
   - `"factuality"`: What you'll reference it as

2. **definition**: Description of what it measures
   - Explains the purpose
   - Used by LLM judge to understand goal

3. **grading_prompt**: Instructions for scoring
   - Tells LLM how to evaluate
   - Defines score ranges
   - Clear criteria for each score

4. **examples**: Few-shot examples
   - `[...]`: LIST of example dictionaries
   - Each example has:
     - `input`: The question asked
     - `output`: An answer
     - `score`: Rating for that answer
     - `justification`: Why that score
   - LLM learns from these examples

5. **parameters**: What data to pass
   - `["input", "output"]`: Use question and answer
   - Could add `"retrieved_docs"` for RAG

**How it works:**
1. Benchmarker sends input + output to LLM
2. Includes definition and grading prompt
3. Shows few-shot examples
4. LLM returns score (1-5) and justification
5. Score recorded for this run

#### Using Custom Metric

```python
eval_run = EvaluationRun(
    agent_path="path/to/agent.py",
    hyperparameters=hyperparameters,
    metrics=[
        "answer_correctness",  # Predefined
        factuality_metric       # Custom
    ],
    test_data=test_dataset
)
```

**Mixing predefined and custom:**
- Use predefined for standard evaluation
- Add custom for domain-specific needs
- All metrics calculated for each run

### Weighted Metrics

**Purpose:** Different metrics have different importance

**Example:**
```python
metric_weights = {
    "answer_correctness": 0.5,  # 50% of score
    "factuality": 0.3,           # 30% of score
    "conciseness": 0.2           # 20% of score
}

eval_run = EvaluationRun(
    ...,
    metrics=["answer_correctness", "factuality", "conciseness"],
    metric_weights=metric_weights
)
```

**Score Calculation:**
```
Final Score = (0.5 × correctness) + (0.3 × factuality) + (0.2 × conciseness)

Example:
correctness = 4
factuality = 5
conciseness = 3

Final = (0.5 × 4) + (0.3 × 5) + (0.2 × 3)
      = 2.0 + 1.5 + 0.6
      = 4.1
```

**Why use weights:**
- Prioritize important aspects
- De-emphasize less critical metrics
- Match business requirements

### Deterministic Metrics

**What are deterministic metrics?**
- **Deterministic**: Same input always gives same output
- **Opposite**: LLM-based (non-deterministic)

**Examples:**

1. **Exact Match**
```python
def exact_match(output, expected):
    return 1 if output == expected else 0
```
- Binary: correct or not
- No variability
- Fast computation

2. **Token Count**
```python
def token_count(output):
    return len(output.split())
```
- Counts words
- Always same result
- No LLM needed

3. **Regex Match**
```python
import re

def contains_phone_number(output):
    pattern = r'\d{3}-\d{3}-\d{4}'
    return 1 if re.search(pattern, output) else 0
```
- Pattern matching
- Deterministic
- Useful for format validation

**When to use:**
- Need fast evaluation
- Clear right/wrong answers
- Format requirements
- Exact matching needed

### Viewing Results in Databricks

After evaluation completes:

#### Step 1: Navigate to Databricks
1. From ACE Studio, go to MLflow
2. Click on experiment
3. See all runs from evaluation

#### Step 2: Analyze Results

**Runs View:**
- All 12 runs listed
- Each with different parameters
- Metrics shown in columns

**Example View:**
| Run Name | Temperature | Model | answer_correctness (mean) | factuality (mean) |
|----------|-------------|-------|---------------------------|-------------------|
| Run 1 | 0.0 | gpt-4o | 3.5 | 4.2 |
| Run 2 | 0.0 | gpt-4o-mini | 2.1 | 3.1 |
| Run 3 | 0.4 | gpt-4o | 4.1 | 4.5 |
| ... | ... | ... | ... | ... |

**Sorting:**
- Click column header to sort
- Find highest scoring run
- Compare different configurations

**Detailed Run View:**
Click a run to see:
- All parameters used
- Individual metric scores
- Test case results
- Artifacts

#### Step 3: Select Best Configuration

**Top K Results:**
- If top_k=3, returns top 3
- Based on weighted score
- Programmatic access:

```python
top_runs = results.get_top_k()
# Returns list of top 3 runs

best_run = top_runs[0]
print(f"Best config: {best_run.parameters}")
print(f"Score: {best_run.score}")
```

**Deploy Best Agent:**
1. Note the best run ID
2. Go to Models and Agents
3. Deploy that specific run
4. Now using optimized configuration!

### Complete Benchmarker Example

```python
from benchmarker import EvaluationRun, make_generic_metric
import mlflow

# 1. Define custom metric
factuality = make_generic_metric(
    name="factuality",
    definition="Factual accuracy",
    grading_prompt="Score 1-5 based on facts",
    examples=[...],
    parameters=["input", "output"]
)

# 2. Define hyperparameter space
hyperparams = {
    "temperature": [0, 0.5, 1.0],
    "model": ["gpt-4o", "gpt-4o-mini"],
    "system_prompt": [
        "You are a helpful assistant",
        "You are an expert assistant"
    ]
}

# 3. Create test dataset
test_data = [
    {"input": "What is MLflow?", "expected": "..."},
    {"input": "How do I log a model?", "expected": "..."},
    # ... more test cases
]

# 4. Run evaluation
eval_run = EvaluationRun(
    agent_path="my_agent.py",
    hyperparameters=hyperparams,
    metrics=["answer_correctness", factuality],
    metric_weights={
        "answer_correctness": 0.6,
        "factuality": 0.4
    },
    test_data=test_data,
    top_k=3
)

results = eval_run.run()

# 5. Get best configurations
top_3 = results.get_top_k()

for i, run in enumerate(top_3, 1):
    print(f"\n{i}. Run: {run.run_id}")
    print(f"   Score: {run.score}")
    print(f"   Parameters: {run.parameters}")

# 6. Deploy best
best_run_id = top_3[0].run_id
# Use this run_id to deploy in ACE Studio
```

---

## 11. Access and Permissions {#access-permissions}

### Access Request Process

#### Step 1: Identify Your Organization

**Organization Types:**
1. **QRM** (Quality & Risk Management)
2. **IB** (Investment Banking)
3. **RISC-Tech** (part of "others")
4. **Others** (various departments)

**How to know which you are:**
- Ask your manager
- Check your department code
- Look at existing access groups

#### Step 2: Request Appropriate Access

**For QRM Users:**
```
Access Group: RISClab_AI_QRM_developer_user
```
- Request this in PBS (Permission Business System)
- Or relevant access management system

**For IB Users:**
```
Access Group: RISClab_AI_IB_developer
```

**For RISC-Tech and Others:**
```
Access Group: RISClab_AI_others_developer_user
OR
Access Group: RISClab_AI_others_user
```

**Important Notes:**
- Only need ONE access request
- Don't request Databricks separately
- Everything auto-syncs
- Takes 24-48 hours typically

#### Step 3: Verify Access

After approval:
1. Log into ACE Studio
2. Check you can create workspace
3. Verify MLflow access
4. Test Databricks connection

### Permission Levels

**Developer User:**
- Create workspaces
- Deploy agents
- Access MLflow
- Use Databricks
- Create jobs
- Deploy apps
- Full platform access

**Read-Only User:**
- View deployments
- See experiments
- Cannot create/modify
- Limited access

**Admin:**
- Manage projects
- Add/remove users
- Configure resources
- Platform administration

### Data Access Permissions

**Automatic Access Includes:**

1. **Private Folder**
   - Your personal space
   - Only you can access
   - Path: `/data/private/USERNAME/`

2. **Project Folders**
   - Based on project membership
   - Shared with team
   - Path: `/data/projects/PROJECT_NAME/`

3. **Jobs Output**
   - Your job outputs
   - Jobs you have permission for
   - Path: `/data/jobs/`

**Adding Someone to Project:**
1. Contact AMR team
2. Provide user email/ID
3. Specify project name
4. They get access within 24 hours

### GitLab Integration

**Personal Access Token (PAT):**

**Purpose:**
- Authenticates ACE with GitLab
- Allows repository access
- Enables code synchronization

**Scopes Required:**
1. **API** - Full API access
2. **Write Repository** - Push code changes

**Token Security:**
- Keep token secret
- Don't share with others
- Regenerate if compromised
- Set expiration date

**Token Management:**
1. Generate in GitLab
2. Copy immediately (won't see again)
3. Paste in ACE Studio
4. ACE stores encrypted
5. Used automatically for git operations

### Cost Management and Limits

**Spending Guidelines:**

**Be Judicious:**
- Don't leave workspaces running idle
- Stop when not in use
- Use appropriate resources
- Monitor cost estimates

**Resource Selection:**
- **Development**: Smaller instances
- **Training**: Larger, time-limited
- **Inference**: Based on load

**Cost Estimates:**
- Shown during workspace creation
- Updates as you adjust resources
- Hourly rates displayed

**Best Practices:**
1. Stop workspace when done
2. Use scheduled jobs for training
3. Right-size your resources
4. Share resources within team
5. Archive old deployments

### Common Access Issues

**Issue 1: "Access Denied"**
- **Cause**: Access not yet approved
- **Solution**: Wait for approval, check PBS

**Issue 2: "Cannot See Project"**
- **Cause**: Not added to AMR project
- **Solution**: Contact project admin

**Issue 3: "GitLab Connection Failed"**
- **Cause**: Invalid token or scopes
- **Solution**: Regenerate token with correct scopes

**Issue 4: "Databricks Login Required"**
- **Cause**: Session expired
- **Solution**: Re-authenticate, check access group

**Issue 5: "Cannot Deploy Model"**
- **Cause**: Insufficient permissions
- **Solution**: Verify developer access level

---

## 12. Additional Resources

### Cookbooks

**Location:** Base cookbooks repository in GitLab

**Available Examples:**
1. Simple agent creation
2. LangChain integration
3. RAG (Retrieval-Augmented Generation)
4. Tool use examples
5. MLflow logging
6. Benchmarker usage
7. Custom metrics
8. Streamlit apps
9. FastAPI applications

**How to Use:**
1. Link cookbooks project to workspace
2. Browse examples
3. Run notebooks
4. Modify for your use case
5. Create your own

### Documentation

**Where to Find:**
- ACE Studio documentation portal
- MLflow official docs
- LangChain documentation
- Streamlit documentation
- Qdrant documentation

### Support Channels

**Getting Help:**

**Teams Channel:**
- Early October setup
- Post questions
- Community support
- Share solutions

**Instructor-Led Walkthrough:**
- Scheduled for early October
- Live Q&A session
- Demonstrations
- Troubleshooting help

**Presenters:**
- Daniel (platform expert)
- Natalia (technical support)
- Rohit (infrastructure)
- Jay (architecture)

### Hackathon Preparation

**Before Hackathon:**
1. Request and receive access
2. Create first workspace
3. Try examples from cookbooks
4. Deploy test agent
5. Familiarize with interface
6. Prepare your ideas

**During Hackathon:**
- Use what you've learned
- Ask questions in Teams
- Experiment with features
- Build your solution
- Deploy and demo

**What to Bring:**
- Ideas for agents/apps
- Sample datasets (if applicable)
- Team members (if collaborative)
- Questions

---

## 13. Key Concepts Summary

### Python Fundamentals Review

**Variables:**
```python
x = 5
```
- `x`: VARIABLE NAME (label you choose)
- `=`: ASSIGNMENT OPERATOR
- `5`: VALUE stored in variable

**Functions:**
```python
def my_function(parameter):
    return result
```
- `def`: KEYWORD to define function
- `my_function`: FUNCTION NAME
- `parameter`: INPUT variable
- `return`: Send value back

**Classes:**
```python
class MyClass:
    def method(self):
        pass
```
- `class`: KEYWORD to define class
- `MyClass`: CLASS NAME (blueprint)
- `method`: FUNCTION inside class
- `self`: Reference to instance

**Objects:**
```python
obj = MyClass()
```
- `MyClass()`: Creating OBJECT (instance)
- `obj`: VARIABLE holding the object
- Objects have methods and attributes

**Modules:**
```python
import mlflow
```
- `import`: KEYWORD to load library
- `mlflow`: MODULE name
- Now `mlflow` is available as variable

**Dot Notation:**
```python
mlflow.set_experiment()
```
- `mlflow`: MODULE/OBJECT
- `.`: ACCESSOR (get attribute/method)
- `set_experiment`: METHOD (function)
- `()`: CALL the method

### MLflow Workflow

1. **Set Experiment**
   - Groups related runs
   - Creates if doesn't exist

2. **Start Run**
   - Creates version
   - Tracks this execution

3. **Log Artifacts**
   - Save model
   - Save parameters
   - Save metrics

4. **End Run**
   - Finalize tracking
   - Store in registry

5. **Load Model**
   - Retrieve for inference
   - Deploy to production

### MCP Server Workflow

1. **Register Server**
   - Add to marketplace
   - Provide description

2. **Deploy Server**
   - Configure transport
   - Start service

3. **Connect to Agent**
   - Add to Continue config
   - Agent discovers tools

4. **Agent Uses Tools**
   - Analyzes user request
   - Selects appropriate tool
   - Calls MCP server
   - Returns result

### Deployment Workflow

1. **Develop in Workspace**
   - Write code
   - Test locally

2. **Log to MLflow**
   - Create experiment
   - Start run
   - Save artifacts

3. **Deploy from UI**
   - Select run
   - Configure deployment
   - Create endpoint

4. **Test Deployment**
   - Use Model Card
   - Try API calls
   - Verify performance

5. **Monitor and Update**
   - Check logs
   - Update if needed
   - Redeploy new versions

---

## 14. Troubleshooting Guide

### Workspace Issues

**Problem:** Workspace won't start
- Check resource availability
- Verify Docker image selection
- Check access permissions
- Try different region/zone

**Problem:** GitLab connection fails
- Regenerate token
- Verify scopes (API + Write Repo)
- Check repository access
- Validate branch exists

**Problem:** Dependencies won't install
- Check pyproject.toml syntax
- Verify package names
- Check Python version compatibility
- Look at workspace logs

### Agent Deployment Issues

**Problem:** Model won't log to MLflow
- Verify experiment name
- Check MLflow connection
- Ensure signature defined
- Validate model format

**Problem:** Deployment fails
- Check framework selection
- Verify run ID exists
- Check resource limits
- Review deployment logs

**Problem:** Inference returns errors
- Validate input format
- Check model signature
- Verify dependencies installed
- Test locally first

### MCP Server Issues

**Problem:** Server won't deploy
- Check entry point script
- Verify port configuration (8888)
- Check host setting (0.0.0.0)
- Review server logs

**Problem:** Continue can't connect
- Verify YAML syntax
- Check indentation
- Validate URL
- Restart Continue extension

**Problem:** Tools not appearing
- Reload Continue
- Check MCP server status
- Verify tool definitions
- Review connection config

### Job Issues

**Problem:** Job stays queued
- Check resource availability
- Verify access permissions
- Check queue status
- Contact support if persistent

**Problem:** Job fails immediately
- Check file path
- Verify dependencies
- Review job logs
- Check Docker image

**Problem:** Can't access job output
- Check job completion
- Verify output path
- Check permissions
- Look in /data/jobs/

### General Issues

**Problem:** Can't see project files
- Verify project membership
- Check file permissions
- Refresh browser
- Re-link GitLab project

**Problem:** High costs
- Stop unused workspaces
- Right-size resources
- Use jobs for training
- Check running deployments

**Problem:** Access denied errors
- Verify access group
- Check approval status
- Wait for synchronization
- Contact admin

---

## 15. Best Practices

### Development Best Practices

1. **Start Small**
   - Begin with examples
   - Understand basics
   - Build incrementally
   - Test frequently

2. **Version Control**
   - Use GitLab integration
   - Commit frequently
   - Clear commit messages
   - Branch for features

3. **Experiment Tracking**
   - Always log to MLflow
   - Use descriptive names
   - Track parameters
   - Record metrics

4. **Resource Management**
   - Stop when not in use
   - Right-size resources
   - Use schedules for training
   - Monitor costs

### Agent Development Best Practices

1. **Clear System Prompts**
   - Be specific
   - Provide examples
   - Set expectations
   - Define boundaries

2. **Test Thoroughly**
   - Use test datasets
   - Try edge cases
   - Validate outputs
   - Benchmark performance

3. **Iterate and Improve**
   - Start simple
   - Add features gradually
   - Use Benchmarker
   - Track improvements

4. **Documentation**
   - Comment your code
   - Document prompts
   - Record decisions
   - Share learnings

### Collaboration Best Practices

1. **Shared Resources**
   - Use project folders
   - Document data locations
   - Share experiments
   - Communicate changes

2. **Naming Conventions**
   - Consistent naming
   - Descriptive names
   - Include version/date
   - Follow team standards

3. **Knowledge Sharing**
   - Share cookbooks
   - Document solutions
   - Help teammates
   - Contribute examples

---

## 16. Next Steps

### For New Users

1. **Week 1: Setup and Exploration**
   - Request access
   - Create first workspace
   - Run cookbook examples
   - Explore interface

2. **Week 2: First Agent**
   - Build simple agent
   - Log to MLflow
   - Deploy via UI
   - Test inference

3. **Week 3: Advanced Features**
   - Try MCP servers
   - Create web app
   - Schedule job
   - Use Benchmarker

4. **Week 4: Hackathon Prep**
   - Plan your project
   - Gather resources
   - Test your setup
   - Prepare questions

### For Hackathon Participants

**Before Event:**
- ✓ Access approved and working
- ✓ Workspace created and tested
- ✓ Familiar with deployment process
- ✓ Ideas sketched out
- ✓ Team formed (if applicable)

**During Event:**
- Build your solution
- Use provided resources
- Ask for help when stuck
- Document your work
- Prepare demo

**After Event:**
- Deploy final version
- Share with team
- Document learnings
- Continue developing

---

## 17. Glossary

**ACE Studio:** AI development platform providing workspaces, deployment, and tools

**Agent:** AI system that can use tools and make decisions

**Artifact:** File saved in MLflow (model, data, code)

**Benchmarker:** Library for evaluating agent performance

**Continue:** VS Code extension for AI coding assistance

**Databricks:** Data platform used for MLflow backend

**Deployment:** Running instance of model/agent accessible via API

**Docker Image:** Pre-configured environment template

**Entry Point:** File/script that starts application

**Experiment:** Collection of related MLflow runs

**FastAPI:** Python framework for building APIs

**GitLab:** Version control platform

**Hyperparameter:** Configuration setting for model/agent

**Inference:** Using deployed model to make predictions

**Job:** Scheduled or one-time remote script execution

**LangChain:** Framework for building LLM applications

**LangGraph:** Library for building agent workflows

**MCP Server:** Model Context Protocol server providing tools

**Metric:** Measurement of model/agent performance

**MLflow:** Platform for ML lifecycle management

**Prompt:** Instructions given to language model

**Qdrant:** Vector database for semantic search

**RAG:** Retrieval-Augmented Generation (search + generate)

**Run:** Single execution/version in MLflow experiment

**Signature:** Definition of model inputs/outputs

**Streamlit:** Python framework for data apps

**Temperature:** Randomness parameter for LLM (0-1)

**Token:** Authentication credential or text unit

**Vector Store:** Database for embeddings and semantic search

**Workspace:** Development environment in ACE Studio

---

## Appendix A: Code Templates

### Agent Template

```python
import mlflow
from langchain_openai import AzureChatOpenAI
from langgraph.graph import StateGraph

# Define agent
def create_agent():
    # LLM configuration
    llm = AzureChatOpenAI(
        deployment_name="gpt-4o",
        temperature=0,
        api_version="2024-02-15-preview"
    )

    # Create graph
    workflow = StateGraph()

    # Add nodes
    workflow.add_node("chat", chat_node)

    # Add edges
    workflow.set_entry_point("chat")
    workflow.add_edge("chat", END)

    return workflow.compile()

# Log to MLflow
mlflow.set_experiment("my-experiment")

with mlflow.start_run():
    agent = create_agent()
    mlflow.langchain.log_model(agent, "agent")
```

### MCP Server Template

```python
from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool()
def my_tool(parameter: str) -> str:
    """Description of what this tool does."""
    # Tool logic here
    return f"Result: {parameter}"

if __name__ == "__main__":
    mcp.run()
```

### Streamlit App Template

```python
import streamlit as st

st.title("My App")

user_input = st.text_input("Enter something:")

if st.button("Submit"):
    result = process(user_input)
    st.write(result)
```

### Benchmarker Template

```python
from benchmarker import EvaluationRun

hyperparams = {
    "temperature": [0, 0.5],
    "model": ["gpt-4o"]
}

test_data = [
    {"input": "Question 1", "expected": "Answer 1"},
    {"input": "Question 2", "expected": "Answer 2"}
]

eval_run = EvaluationRun(
    agent_path="agent.py",
    hyperparameters=hyperparams,
    metrics=["answer_correctness"],
    test_data=test_data,
    top_k=3
)

results = eval_run.run()
```

---

## Appendix B: Quick Reference

### Essential Commands

**Python:**
```python
import mlflow
mlflow.set_experiment("name")
with mlflow.start_run():
    mlflow.log_model(model, "model")
```

**Bash:**
```bash
streamlit run app.py --server.port=8888 --server.address=0.0.0.0
```

**Git:**
```bash
git clone <url>
git add .
git commit -m "message"
git push
```

### Important Paths

```
/data/private/USERNAME/          # Private storage
/data/projects/PROJECT_NAME/     # Shared storage
/data/jobs/JOB_ID/               # Job outputs
```

### Port Requirements

- Web apps: **8888**
- Host: **0.0.0.0**

### Access Groups

- QRM: `RISClab_AI_QRM_developer_user`
- IB: `RISClab_AI_IB_developer`
- Others: `RISClab_AI_others_developer_user`

---

## Document Information

**Version:** 1.0
**Date:** Based on training session transcription
**Authors:** Compiled from demonstration by Daniel, Natalia, Rohit
**Target Audience:** New ACE Studio users, hackathon participants
**Estimated Reading Time:** 3-4 hours

**Document Purpose:**
This comprehensive tutorial captures every detail from the ACE Studio training session, providing step-by-step guidance for new users. No detail has been omitted - every concept, button click, and code example has been documented with extensive explanations suitable for users with limited Python knowledge.

---

*End of Tutorial*