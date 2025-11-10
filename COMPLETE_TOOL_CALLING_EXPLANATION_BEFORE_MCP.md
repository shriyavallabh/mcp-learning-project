# Complete Tool Calling Explanation - BEFORE MCP

**A line-by-line breakdown of how tool calling works with OpenAI (pre-MCP)**

---

## Table of Contents
1. [The Complete Program](#the-complete-program)
2. [Line-by-Line Explanation](#line-by-line-explanation)
3. [Complete Execution Flow](#complete-execution-flow)
4. [Visual Diagrams](#visual-diagrams)
5. [Key Concepts Summary](#key-concepts-summary)

---

## The Complete Program

```python
# weather_chatbot.py - Complete working example
import openai
import requests
import json

# Configuration
openai.api_key = "your-openai-api-key"

# Function that actually calls the weather API
def get_weather(city):
    """Get current weather for a city"""
    api_key = "your-openweathermap-key"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    temp = data['main']['temp']
    description = data['weather'][0]['description']

    return f"Weather in {city}: {temp}°C, {description}"

# Function definition for OpenAI
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

# Main conversation loop
def chat():
    print("Weather Chatbot Started! (Type 'quit' to exit)")
    print("-" * 50)

    # Conversation history
    messages = []

    while True:
        # Get user input
        user_input = input("\nYou: ")

        if user_input.lower() == 'quit':
            print("Goodbye!")
            break

        # Add user message to history
        messages.append({"role": "user", "content": user_input})

        # Call OpenAI with function definition
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            functions=[weather_function_definition],
            function_call="auto"
        )

        # Get the assistant's response
        assistant_message = response['choices'][0]['message']

        # Check if AI wants to call a function
        if assistant_message.get('function_call'):
            # AI wants to call a function!
            function_name = assistant_message['function_call']['name']
            function_args = json.loads(assistant_message['function_call']['arguments'])

            print(f"\n[AI is calling function: {function_name} with args: {function_args}]")

            # Execute the function
            if function_name == "get_weather":
                function_result = get_weather(city=function_args['city'])
                print(f"[Function returned: {function_result}]")

            # Add assistant's function call to history
            messages.append(assistant_message)

            # Add function result to history
            messages.append({
                "role": "function",
                "name": function_name,
                "content": function_result
            })

            # Call OpenAI again with the function result
            second_response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=messages
            )

            # Get final response
            final_message = second_response['choices'][0]['message']
            print(f"\nAssistant: {final_message['content']}")

            # Add to history
            messages.append(final_message)

        else:
            # No function call needed, just a regular response
            print(f"\nAssistant: {assistant_message['content']}")
            messages.append(assistant_message)

# Run the chatbot
if __name__ == "__main__":
    chat()
```

---

## Line-by-Line Explanation

### Lines 1-4: Imports

```python
# weather_chatbot.py - Complete working example
import openai
import requests
import json
```

**Line 1:**
- `#` = Comment symbol (Python ignores this line)
- **Purpose:** Documentation for humans reading the code

**Line 2: `import openai`**
- `import` = Python keyword to bring in external code
- `openai` = A module (library) created by OpenAI
- **What is a module?** A Python file containing pre-written code
- **What does this module do?** Provides functions to talk to OpenAI's API
- **Installation:** `pip install openai`
- **After this line:** You can use `openai.ChatCompletion.create()` and other OpenAI functions

**Line 3: `import requests`**
- `requests` = A module for making HTTP requests
- **What is HTTP?** The protocol used to communicate over the internet
- **Why do we need this?** To call the weather API (which is a web service)
- **Installation:** `pip install requests`
- **After this line:** You can use `requests.get()` to fetch data from websites/APIs

**Line 4: `import json`**
- `json` = A module for working with JSON data
- **What is JSON?** JavaScript Object Notation - a text format for data
  - Example: `{"name": "John", "age": 30}`
- **Why do we need this?** OpenAI sends/receives data in JSON format
- **Built-in:** Comes with Python (no installation needed)
- **After this line:** You can use `json.loads()` to convert JSON text to Python objects

---

### Lines 6-7: Configuration

```python
# Configuration
openai.api_key = "your-openai-api-key"
```

**Line 6:**
- Comment indicating configuration section

**Line 7: `openai.api_key = "your-openai-api-key"`**
- `openai` = The module we imported
- `.` = Dot notation (accessing something inside the module)
- `api_key` = A variable inside the openai module
- `=` = Assignment operator (setting a value)
- `"your-openai-api-key"` = A string (text) - your actual API key
- **What is an API key?** Like a password to use OpenAI's services
- **What does this do?** Tells the openai module "use this key for authentication"
- **Where to get this?** From OpenAI's website after signing up
- **Example real key:** `"sk-proj-abc123def456..."`

---

### Lines 9-21: The Weather Function

```python
# Function that actually calls the weather API
def get_weather(city):
    """Get current weather for a city"""
    api_key = "your-openweathermap-key"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    temp = data['main']['temp']
    description = data['weather'][0]['description']

    return f"Weather in {city}: {temp}°C, {description}"
```

**Line 9:**
- Comment explaining what the next function does

**Line 10: `def get_weather(city):`**
- `def` = Keyword to DEFINE a function
- `get_weather` = Function name (you choose this name)
- `(city)` = Parameter (input the function expects)
  - `city` = Variable name (could be anything: "location", "place", "c")
- `:` = Colon indicates the function body starts next
- **What is a function?** A reusable block of code with a name
- **What does this do?** Creates a function called `get_weather` that accepts one parameter called `city`
- **Think of it as:** A recipe with a name and ingredients

**Line 11: `"""Get current weather for a city"""`**
- `"""..."""` = Triple quotes create a docstring
- **What is a docstring?** Documentation string - describes what the function does
- **Why?** Helps other programmers (and AI!) understand your function
- **Note:** This is NOT a regular comment (#), it's part of the function

**Line 12: `api_key = "your-openweathermap-key"`**
- `    ` = 4 spaces indentation (CRITICAL in Python!)
- **Why indentation?** Shows this line is INSIDE the function
- `api_key` = Variable name (storing the API key)
- `=` = Assignment
- `"your-openweathermap-key"` = String - your OpenWeatherMap API key
- **What does this do?** Creates a variable storing the weather API key
- **Where to get this?** Sign up at openweathermap.org

**Line 13: Building the URL**
```python
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
```

Let me break this down EXTREMELY carefully:

- `url` = Variable name (stores the web address)
- `=` = Assignment
- `f"..."` = F-string (formatted string)
  - **What is an f-string?** A string that can embed variables using `{}`
  - The `f` before the quote makes it special
- `"https://..."` = The actual URL string

**URL breakdown:**
- `https://` = Protocol (secure web connection)
- `api.openweathermap.org` = Domain (server address)
- `/data/2.5/weather` = Endpoint (specific service)
- `?` = Start of query parameters
- `q={city}` = Query parameter
  - `q` = Parameter name (means "query" - the city name)
  - `=` = Separator
  - `{city}` = Variable substitution (if city="Tokyo", becomes `q=Tokyo`)
- `&` = Separates multiple parameters
- `appid={api_key}` = API key parameter
  - `appid` = Parameter name (application ID)
  - `{api_key}` = Your API key gets inserted here
- `&units=metric` = Another parameter
  - `units=metric` = Use Celsius (not Fahrenheit)

**Example:** If `city="Tokyo"` and `api_key="abc123"`, this becomes:
```
https://api.openweathermap.org/data/2.5/weather?q=Tokyo&appid=abc123&units=metric
```

**Line 15: `response = requests.get(url)`**
- `response` = Variable to store the result
- `=` = Assignment
- `requests` = The module we imported earlier
- `.get()` = A method (function) inside the requests module
- `(url)` = Passing the URL as an argument
- **What does this do?** Makes an HTTP GET request to the weather API

**What happens:**
1. Your computer sends a request to openweathermap.org
2. Their server receives it
3. Their server looks up the weather for the city
4. Their server sends back the data
5. This line WAITS for the response
6. The response is stored in the `response` variable

**What is in `response`?**
- Status code (200 = success, 404 = not found, etc.)
- Headers (metadata)
- Body (the actual weather data as JSON text)

**THIS IS THE KITCHEN!** This line does the actual work of getting weather data.

**Line 16: `data = response.json()`**
- `data` = Variable to store the parsed data
- `=` = Assignment
- `response` = The variable from previous line
- `.json()` = A method that parses JSON text into Python objects
- **What does this do?** Converts JSON text to a Python dictionary

**Example:**

Before (JSON text in response):
```
'{"main":{"temp":15},"weather":[{"description":"cloudy"}]}'
```

After (Python dictionary in data):
```python
{
    "main": {"temp": 15},
    "weather": [{"description": "cloudy"}]
}
```

Now you can access it with: `data['main']['temp']`

**Line 18: `temp = data['main']['temp']`**
- `temp` = Variable to store the temperature
- `=` = Assignment
- `data` = The dictionary from previous line
- `['main']` = Access the 'main' key in the dictionary
  - **What are brackets `[]`?** Dictionary access operator
  - Returns another dictionary: `{"temp": 15, "pressure": 1013, ...}`
- `['temp']` = Access the 'temp' key in that dictionary
  - Returns: `15` (the temperature value)
- **What does this do?** Extracts the temperature from the nested data structure

**Visual breakdown:**
```python
data = {
    "main": {
        "temp": 15,      # ← We want this!
        "pressure": 1013
    },
    "weather": [...]
}

# Step 1: data['main'] returns {"temp": 15, "pressure": 1013}
# Step 2: ['temp'] on that returns 15
# Result: temp = 15
```

**Line 19: `description = data['weather'][0]['description']`**
- `description` = Variable to store weather description
- `=` = Assignment
- `data['weather']` = Access the 'weather' key
  - **Returns:** A list (array): `[{"description": "cloudy", "main": "Clouds"}]`
- `[0]` = Access the first item in the list
  - **What is `[0]`?** List index (0 = first item, 1 = second, etc.)
  - **Returns:** A dictionary: `{"description": "cloudy", "main": "Clouds"}`
- `['description']` = Access the 'description' key
  - **Returns:** A string: `"cloudy"`
- **What does this do?** Extracts the weather description from a nested list

**Visual breakdown:**
```python
data = {
    "weather": [
        {
            "description": "cloudy",  # ← We want this!
            "main": "Clouds"
        }
    ]
}

# Step 1: data['weather'] returns the list
# Step 2: [0] gets first item in list (the dictionary)
# Step 3: ['description'] gets the description from that dictionary
# Result: description = "cloudy"
```

**Line 21: `return f"Weather in {city}: {temp}°C, {description}"`**
- `return` = Keyword to send a value back from the function
- `f"..."` = F-string (formatted string)
- `{city}` = Variable substitution (inserts the city name)
- `{temp}` = Variable substitution (inserts the temperature)
- `{description}` = Variable substitution (inserts the description)
- `°C` = Degrees Celsius symbol (just text)
- **What does this do?** Creates a human-readable string and returns it

**Example:** If `city="Tokyo"`, `temp=15`, `description="cloudy"`, returns:
```
"Weather in Tokyo: 15°C, cloudy"
```

**IMPORTANT:** When a function returns, it exits immediately and gives the value back to the caller.

---

### Lines 23-37: Function Definition for OpenAI

```python
# Function definition for OpenAI
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
```

**Line 23:** Comment

**Line 24: `weather_function_definition = {`**
- `weather_function_definition` = Variable name
- `=` = Assignment
- `{` = Start of a dictionary
- **What is a dictionary?** A collection of key-value pairs
  - Like: `{"name": "John", "age": 30}`
  - Access with: `dict["name"]` returns `"John"`

**Line 25: `"name": "get_weather",`**
- `"name"` = Key (a string)
- `:` = Separator between key and value
- `"get_weather"` = Value (a string)
- `,` = Comma separates multiple key-value pairs
- **What does this do?** Tells OpenAI "this function is called 'get_weather'"
- **Why important?** OpenAI will reference this name when it wants to call the function

**Line 26: `"description": "Get current weather for a city",`**
- `"description"` = Key
- `"Get current weather for a city"` = Value (describes the function)
- **What does this do?** Tells OpenAI what this function does
- **Why important?** OpenAI's LLM reads this to decide if this function is relevant to the user's question

**Line 27: `"parameters": {`**
- `"parameters"` = Key
- `{` = Value is ANOTHER dictionary (nested)
- **What does this do?** Starts defining what inputs this function needs

**Line 28: `"type": "object",`**
- `"type"` = Key
- `"object"` = Value
- **What does this mean?** The parameters form an object (dictionary/JSON object)
- **Why?** JSON schema specification requires this

**Line 29: `"properties": {`**
- `"properties"` = Key
- `{` = Value is ANOTHER nested dictionary
- **What does this do?** Defines the individual properties (parameters) of the function

**Line 30: `"city": {`**
- `"city"` = Key (the parameter name)
- `{` = Value is ANOTHER nested dictionary
- **What does this do?** Starts defining the "city" parameter

**Line 31: `"type": "string",`**
- `"type"` = Key
- `"string"` = Value
- **What does this mean?** The "city" parameter should be a string (text)
- **Why?** Tells OpenAI what data type to generate

**Line 32: `"description": "The city name, e.g., London, Tokyo"`**
- `"description"` = Key
- `"The city name, e.g., London, Tokyo"` = Value (explains this parameter)
- **What does this do?** Helps OpenAI understand what kind of value to extract from user's message
- **Example:** If user says "What's the weather in Paris?", OpenAI reads this and knows to extract "Paris" as the city

**Lines 33-37:** Closing braces
- `}` = Closes the "city" parameter dictionary
- `},` = Closes the "properties" dictionary
- `"required": ["city"]` = The "city" parameter is REQUIRED (must be provided)
- `}` = Closes the "parameters" dictionary
- `}` = Closes the main dictionary

**The complete structure:**
```python
{
    "name": "get_weather",
    "description": "...",
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
```

---

### Lines 39-112: Main Chat Function

```python
# Main conversation loop
def chat():
    print("Weather Chatbot Started! (Type 'quit' to exit)")
    print("-" * 50)

    # Conversation history
    messages = []

    while True:
        # ... rest of the function
```

**Line 39:** Comment

**Line 40: `def chat():`**
- `def` = Define a function
- `chat` = Function name
- `()` = No parameters (empty parentheses)
- `:` = Function body starts next
- **What does this do?** Creates a function called `chat` that takes no inputs

**Line 41: `print("Weather Chatbot Started! (Type 'quit' to exit)")`**
- `print()` = Built-in Python function that displays text
- `"Weather Chatbot Started! (Type 'quit' to exit)"` = String to display
- **What does this do?** Shows a welcome message to the user
- **Output:** `Weather Chatbot Started! (Type 'quit' to exit)`

**Line 42: `print("-" * 50)`**
- `print()` = Display text
- `"-"` = A string containing one dash character
- `*` = Multiplication operator (for strings, it repeats them)
- `50` = Number of times to repeat
- **What does this do?** Prints 50 dashes (a visual separator)
- **Output:** `--------------------------------------------------`

**Line 45: `messages = []`**
- `messages` = Variable name
- `=` = Assignment
- `[]` = Empty list
- **What is a list?** An ordered collection of items
  - Example: `[1, 2, 3]` or `["apple", "banana"]`
- **What does this do?** Creates an empty list to store all conversation messages
- **Why?** OpenAI needs the full conversation history to understand context

**Line 47: `while True:`**
- `while` = Loop keyword (repeats code)
- `True` = Boolean value (always true)
- `:` = Loop body starts next
- **What does this do?** Creates an INFINITE loop (runs forever until we break out)
- **Why forever?** We want the chatbot to keep running until user types "quit"

**Line 49: `user_input = input("\nYou: ")`**
- `user_input` = Variable to store what user types
- `=` = Assignment
- `input()` = Built-in Python function that waits for user to type something
- `"\nYou: "` = The prompt to show
  - `\n` = Newline character (moves to next line)
  - `You: ` = Text that appears before user types
- **What does this do?** Displays "You: " and WAITS for user to type and press Enter
- **Program pauses here** until user presses Enter
- **Example:** If user types "What's the weather in Tokyo?", that text is stored in `user_input`

**Line 51: `if user_input.lower() == 'quit':`**
- `if` = Conditional keyword (checks a condition)
- `user_input` = The variable with user's text
- `.lower()` = Method that converts text to lowercase
  - "QUIT" becomes "quit"
  - "Quit" becomes "quit"
- `==` = Equality comparison operator (checks if equal)
- `'quit'` = The string we're comparing against
- `:` = If block starts next
- **What does this do?** Checks if user typed "quit" (case-insensitive)

**Line 52: `print("Goodbye!")`**
- Displays farewell message
- **When?** Only if the if condition is True (user typed quit)

**Line 53: `break`**
- `break` = Keyword that exits the current loop
- **What does this do?** Stops the while loop immediately
- **Result:** Program exits the function

**Line 56: `messages.append({"role": "user", "content": user_input})`**
- `messages` = The list we created earlier
- `.append()` = Method that adds an item to the end of a list
- `{...}` = A dictionary (the item we're adding)
- Inside the dictionary:
  - `"role": "user"` = Tells OpenAI this message is from the user
  - `"content": user_input` = The actual text the user typed
- **What does this do?** Adds the user's message to the conversation history

**Example:** If `user_input = "What's the weather in Tokyo?"`, messages becomes:
```python
[
    {"role": "user", "content": "What's the weather in Tokyo?"}
]
```

**Lines 59-64: First OpenAI API Call**
```python
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=messages,
    functions=[weather_function_definition],
    function_call="auto"
)
```

**Line 59: `response = openai.ChatCompletion.create(`**
- `response` = Variable to store the result
- `openai.ChatCompletion.create()` = Method that calls OpenAI's API
- **What does this do?** Makes an API call to OpenAI

**Line 60: `model="gpt-4",`**
- `model` = Parameter name
- `"gpt-4"` = Value (which AI model to use)
- **What does this do?** Tells OpenAI to use the GPT-4 model

**Line 61: `messages=messages,`**
- `messages` = Parameter name
- `messages` = Variable with our conversation history
- **What does this do?** Sends the entire conversation history to OpenAI

**Line 62: `functions=[weather_function_definition],`**
- `functions` = Parameter name
- `[weather_function_definition]` = A list containing our function definition
- **What does this do?** Tells OpenAI "I have these functions available"
- **CRITICAL:** This is how OpenAI knows what tools you have!

**Line 63: `function_call="auto"`**
- `function_call` = Parameter name
- `"auto"` = Value
- **What does this mean?** Let OpenAI decide whether to call a function or not
- **Options:**
  - `"auto"` = OpenAI decides
  - `"none"` = Don't call any functions
  - `{"name": "get_weather"}` = Force calling a specific function

**At this point:** The API call is made
- Your computer sends an HTTP request to OpenAI's servers
- Includes: conversation history, function definitions, model choice
- OpenAI's GPT-4 model processes the request
- OpenAI sends back a response
- The response is stored in `response` variable
- **Program WAITS here** until OpenAI responds (1-5 seconds)

**Line 67: `assistant_message = response['choices'][0]['message']`**
- Extracts the assistant's message from OpenAI's response

**The structure of `response`:**
```python
{
    "id": "chatcmpl-123",
    "choices": [
        {
            "message": {
                "role": "assistant",
                "content": "...",  # Text response
                # OR
                "function_call": {  # Function call
                    "name": "get_weather",
                    "arguments": '{"city": "Tokyo"}'
                }
            }
        }
    ]
}
```

**Line 70: `if assistant_message.get('function_call'):`**
- Checks if OpenAI wants to call a function
- `.get('function_call')` returns the value if key exists, or `None` if not
- **When is this True?** When GPT-4 wants to call a function
- **When is this False?** When GPT-4 gives a regular text response

**Line 72: `function_name = assistant_message['function_call']['name']`**
- Extracts which function GPT-4 wants to call
- **Example:** `"get_weather"`

**Line 73: `function_args = json.loads(assistant_message['function_call']['arguments'])`**
- Extracts the arguments
- `json.loads()` converts JSON string to Python dictionary
- **Before:** `'{"city": "Tokyo"}'` (string)
- **After:** `{"city": "Tokyo"}` (dictionary)

**Line 75: Debug output**
```python
print(f"\n[AI is calling function: {function_name} with args: {function_args}]")
```
- Shows the user what's happening behind the scenes
- **Output:** `[AI is calling function: get_weather with args: {'city': 'Tokyo'}]`

**Line 78: `if function_name == "get_weather":`**
- Checks which function to execute
- **Why?** In case you have multiple functions

**Line 79: `function_result = get_weather(city=function_args['city'])`**
- **THIS IS WHERE THE ACTUAL FUNCTION EXECUTES!**
- Calls OUR function (defined at line 10)
- Passes the city from the arguments
- **What happens:**
  1. Builds the weather API URL
  2. Makes HTTP request to openweathermap.org
  3. Gets weather data
  4. Parses JSON
  5. Extracts temperature and description
  6. Returns formatted string
- **After:** `function_result = "Weather in Tokyo: 15°C, cloudy"`

**Line 80: Debug output**
```python
print(f"[Function returned: {function_result}]")
```
- **Output:** `[Function returned: Weather in Tokyo: 15°C, cloudy]`

**Line 83: `messages.append(assistant_message)`**
- Adds the assistant's function call to history

**Lines 86-90: Add function result to history**
```python
messages.append({
    "role": "function",
    "name": function_name,
    "content": function_result
})
```
- Records the function's result
- `"role": "function"` = This message is FROM a function
- `"name": function_name` = Which function
- `"content": function_result` = The result

**Now messages looks like:**
```python
[
    {"role": "user", "content": "What's the weather in Tokyo?"},
    {"role": "assistant", "function_call": {...}},
    {"role": "function", "name": "get_weather", "content": "Weather in Tokyo: 15°C, cloudy"}
]
```

**Lines 93-96: Second OpenAI API Call**
```python
second_response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=messages
)
```
- **THIS IS THE SECOND API CALL!**
- Now `messages` includes the function result
- **OpenAI thinks:** "The user asked about weather, I called the function, got the result, now I'll format a nice response"

**Line 99: `final_message = second_response['choices'][0]['message']`**
- Extracts the final message from GPT-4
- **This message:** `{"role": "assistant", "content": "The weather in Tokyo is currently 15°C and cloudy."}`

**Line 100: `print(f"\nAssistant: {final_message['content']}")`**
- Shows GPT-4's final response to the user
- **Output:** `Assistant: The weather in Tokyo is currently 15°C and cloudy.`

**Line 103: `messages.append(final_message)`**
- Adds the final response to history

**Final conversation history:**
```python
[
    {"role": "user", "content": "What's the weather in Tokyo?"},
    {"role": "assistant", "function_call": {...}},
    {"role": "function", "content": "Weather in Tokyo: 15°C, cloudy"},
    {"role": "assistant", "content": "The weather in Tokyo is currently 15°C and cloudy."}
]
```

**Line 105-108: Else block (no function call)**
```python
else:
    # No function call needed, just a regular response
    print(f"\nAssistant: {assistant_message['content']}")
    messages.append(assistant_message)
```
- Handles regular text responses (when no function is needed)
- **Example:** If user says "Hello!" or "Thanks!"

**Lines 111-112: Run the chatbot**
```python
if __name__ == "__main__":
    chat()
```
- Special Python check
- Only runs if this file is run directly (not imported)
- Calls the `chat()` function to start the chatbot

---

## Complete Execution Flow

### Example Run: User asks "What's the weather in Tokyo?"

```
$ python weather_chatbot.py

Weather Chatbot Started! (Type 'quit' to exit)
--------------------------------------------------

You: What's the weather in Tokyo?
```

**Behind the scenes - Step by Step:**

#### **STEP 1: User Input (Line 49)**
- Program waits at `input()`
- User types: "What's the weather in Tokyo?"
- Presses Enter
- `user_input = "What's the weather in Tokyo?"`

#### **STEP 2: Add to Messages (Line 56)**
```python
messages = [
    {"role": "user", "content": "What's the weather in Tokyo?"}
]
```

#### **STEP 3: First OpenAI API Call (Lines 59-64)**
**Request sent to OpenAI:**
```python
{
    "model": "gpt-4",
    "messages": [
        {"role": "user", "content": "What's the weather in Tokyo?"}
    ],
    "functions": [
        {
            "name": "get_weather",
            "description": "Get current weather for a city",
            "parameters": {...}
        }
    ],
    "function_call": "auto"
}
```

**OpenAI's internal processing:**
1. GPT-4 reads the user's message: "What's the weather in Tokyo?"
2. GPT-4 sees it has a `get_weather` function available
3. GPT-4 reads the function description: "Get current weather for a city"
4. GPT-4 thinks: "Perfect! This function can help!"
5. GPT-4 reads the parameters: needs `city` (string)
6. GPT-4 extracts from user message: city = "Tokyo"
7. GPT-4 generates a function call

**OpenAI's response:**
```python
{
    "id": "chatcmpl-123",
    "choices": [{
        "message": {
            "role": "assistant",
            "function_call": {
                "name": "get_weather",
                "arguments": '{"city": "Tokyo"}'
            }
        },
        "finish_reason": "function_call"
    }]
}
```

**Program receives this response (~2 seconds later)**

#### **STEP 4: Extract Function Call (Lines 67-73)**
```python
assistant_message = {
    "role": "assistant",
    "function_call": {
        "name": "get_weather",
        "arguments": '{"city": "Tokyo"}'
    }
}

function_name = "get_weather"
function_args = {"city": "Tokyo"}  # After json.loads()
```

#### **STEP 5: Display Debug Info (Line 75)**
```
[AI is calling function: get_weather with args: {'city': 'Tokyo'}]
```

#### **STEP 6: Execute Function (Line 79)**
```python
function_result = get_weather(city="Tokyo")
```

**Inside `get_weather()` function:**

**Step 6a: Build URL (Line 13)**
```python
url = "https://api.openweathermap.org/data/2.5/weather?q=Tokyo&appid=abc123&units=metric"
```

**Step 6b: Make HTTP Request (Line 15)**
```python
response = requests.get(url)
```
- Computer sends HTTP GET request to openweathermap.org
- Weather API server receives request
- Looks up weather for Tokyo
- Sends back response
- **Program waits ~1 second**

**Step 6c: Parse JSON Response (Line 16)**
```python
data = response.json()
# Returns:
{
    "main": {
        "temp": 15,
        "pressure": 1013,
        "humidity": 72
    },
    "weather": [
        {
            "description": "cloudy",
            "main": "Clouds"
        }
    ],
    # ... more data
}
```

**Step 6d: Extract Temperature (Line 18)**
```python
temp = data['main']['temp']  # temp = 15
```

**Step 6e: Extract Description (Line 19)**
```python
description = data['weather'][0]['description']  # description = "cloudy"
```

**Step 6f: Return Result (Line 21)**
```python
return f"Weather in Tokyo: 15°C, cloudy"
```

**Back to main program:**
```python
function_result = "Weather in Tokyo: 15°C, cloudy"
```

#### **STEP 7: Display Function Result (Line 80)**
```
[Function returned: Weather in Tokyo: 15°C, cloudy]
```

#### **STEP 8: Add to Messages (Lines 83-90)**
```python
messages = [
    {"role": "user", "content": "What's the weather in Tokyo?"},
    {
        "role": "assistant",
        "function_call": {
            "name": "get_weather",
            "arguments": '{"city": "Tokyo"}'
        }
    },
    {
        "role": "function",
        "name": "get_weather",
        "content": "Weather in Tokyo: 15°C, cloudy"
    }
]
```

#### **STEP 9: Second OpenAI API Call (Lines 93-96)**
**Request sent to OpenAI:**
```python
{
    "model": "gpt-4",
    "messages": [
        {"role": "user", "content": "What's the weather in Tokyo?"},
        {"role": "assistant", "function_call": {...}},
        {"role": "function", "name": "get_weather", "content": "Weather in Tokyo: 15°C, cloudy"}
    ]
}
```

**OpenAI's internal processing:**
1. GPT-4 sees the full conversation
2. Understands: User asked → I called function → Got result
3. Now needs to format a human-friendly response
4. Generates natural language response using the data

**OpenAI's response:**
```python
{
    "id": "chatcmpl-456",
    "choices": [{
        "message": {
            "role": "assistant",
            "content": "The weather in Tokyo is currently 15°C and cloudy."
        },
        "finish_reason": "stop"
    }]
}
```

**Program receives this response (~2 seconds later)**

#### **STEP 10: Display Final Response (Line 100)**
```
Assistant: The weather in Tokyo is currently 15°C and cloudy.
```

#### **STEP 11: Add to Messages (Line 103)**
```python
messages = [
    {"role": "user", "content": "What's the weather in Tokyo?"},
    {"role": "assistant", "function_call": {...}},
    {"role": "function", "content": "Weather in Tokyo: 15°C, cloudy"},
    {"role": "assistant", "content": "The weather in Tokyo is currently 15°C and cloudy."}
]
```

#### **STEP 12: Loop Continues (Line 47)**
```
You:
```
- Program waits for next user input
- Conversation history is preserved
- User can ask another question

---

## Visual Diagrams

### Complete Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│ USER TYPES: "What's the weather in Tokyo?"                  │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 1: Add to messages array                               │
│ messages = [{"role": "user", "content": "..."}]             │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 2: Call OpenAI API                                     │
│ - Send: messages + function definitions                     │
│ - Model: gpt-4                                              │
│ - Wait for response... (~2 seconds)                         │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 3: OpenAI GPT-4 Processing                            │
│ - Reads user message                                        │
│ - Sees get_weather function available                       │
│ - Extracts city = "Tokyo"                                   │
│ - Generates function call                                   │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 4: Receive OpenAI Response                             │
│ {                                                           │
│   "function_call": {                                        │
│     "name": "get_weather",                                  │
│     "arguments": '{"city": "Tokyo"}'                        │
│   }                                                         │
│ }                                                           │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 5: Extract function details                            │
│ - function_name = "get_weather"                             │
│ - function_args = {"city": "Tokyo"}                         │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 6: Execute YOUR function                               │
│ function_result = get_weather(city="Tokyo")                 │
│                                                             │
│ Inside get_weather():                                       │
│   1. Build URL with city                                    │
│   2. Make HTTP request to weather API                       │
│   3. Wait for response... (~1 second)                       │
│   4. Parse JSON response                                    │
│   5. Extract temp and description                           │
│   6. Return formatted string                                │
│                                                             │
│ Result: "Weather in Tokyo: 15°C, cloudy"                   │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 7: Add function call and result to messages            │
│ messages = [                                                │
│   {"role": "user", "content": "..."},                       │
│   {"role": "assistant", "function_call": {...}},            │
│   {"role": "function", "content": "Weather in Tokyo..."}    │
│ ]                                                           │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 8: Call OpenAI API again (with function result)        │
│ - Send: messages (now includes function result)             │
│ - Wait for response... (~2 seconds)                         │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 9: OpenAI GPT-4 Processing (Second Time)              │
│ - Sees full conversation including function result          │
│ - Formats human-friendly response                           │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 10: Receive Final Response                             │
│ {                                                           │
│   "content": "The weather in Tokyo is currently 15°C..."    │
│ }                                                           │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 11: Display to User                                    │
│ "Assistant: The weather in Tokyo is currently 15°C and      │
│  cloudy."                                                   │
└────────────────────┬────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 12: Add to messages and loop                           │
│ messages = [                                                │
│   {"role": "user", ...},                                    │
│   {"role": "assistant", "function_call": ...},              │
│   {"role": "function", ...},                                │
│   {"role": "assistant", "content": "..."}                   │
│ ]                                                           │
│                                                             │
│ Wait for next user input...                                 │
└─────────────────────────────────────────────────────────────┘
```

### Data Flow Diagram

```
┌─────────────────┐
│   USER INPUT    │
│   "Weather in   │
│     Tokyo?"     │
└────────┬────────┘
         │
         ↓
┌─────────────────┐      ┌──────────────────────────────┐
│  YOUR PROGRAM   │─────→│  OpenAI API (First Call)     │
│  (Python code)  │      │                              │
│                 │      │  Input:                      │
│  Sends:         │      │  - User message              │
│  - messages     │      │  - Function definitions      │
│  - functions    │      │                              │
└─────────────────┘      │  GPT-4 Processing:           │
         ↑               │  - Analyzes user intent      │
         │               │  - Decides to call function  │
         │               │  - Extracts parameters       │
         │               └──────────────┬───────────────┘
         │                              │
         │                              ↓
         │               ┌──────────────────────────────┐
         │               │  OpenAI Response             │
         │               │                              │
         │               │  {                           │
         └───────────────│    "function_call": {        │
                         │      "name": "get_weather",  │
                         │      "arguments": {...}      │
                         │    }                         │
                         │  }                           │
                         └──────────────────────────────┘
                                        │
                                        ↓
┌─────────────────────────────────────────────────────────┐
│  YOUR PROGRAM EXECUTES FUNCTION                         │
│                                                         │
│  get_weather("Tokyo")                                   │
│       │                                                 │
│       ↓                                                 │
│  ┌──────────────────────────────────────┐              │
│  │  Weather API (openweathermap.org)    │              │
│  │                                       │              │
│  │  HTTP GET Request →                  │              │
│  │  ← HTTP Response (JSON data)         │              │
│  │                                       │              │
│  │  {                                    │              │
│  │    "main": {"temp": 15},              │              │
│  │    "weather": [{"description": ...}]  │              │
│  │  }                                    │              │
│  └──────────────────────────────────────┘              │
│       │                                                 │
│       ↓                                                 │
│  "Weather in Tokyo: 15°C, cloudy"                      │
└────────────────────┬────────────────────────────────────┘
                     │
                     ↓
┌─────────────────────────────────────────────────────────┐
│  YOUR PROGRAM                                           │
│                                                         │
│  Builds new messages array:                             │
│  [                                                      │
│    {"role": "user", ...},                               │
│    {"role": "assistant", "function_call": ...},         │
│    {"role": "function", "content": "Weather in..."}     │
│  ]                                                      │
└────────────────────┬────────────────────────────────────┘
                     │
                     ↓
┌──────────────────────────────────────────────────────────┐
│  OpenAI API (Second Call)                                │
│                                                          │
│  Input:                                                  │
│  - Full conversation including function result           │
│                                                          │
│  GPT-4 Processing:                                       │
│  - Sees function result                                  │
│  - Formats natural language response                     │
│                                                          │
│  Output:                                                 │
│  {                                                       │
│    "content": "The weather in Tokyo is 15°C and cloudy." │
│  }                                                       │
└────────────────────┬─────────────────────────────────────┘
                     │
                     ↓
┌─────────────────────────────────────────────────────────┐
│  YOUR PROGRAM                                           │
│                                                         │
│  Display to user:                                       │
│  "Assistant: The weather in Tokyo is currently          │
│   15°C and cloudy."                                     │
└─────────────────────────────────────────────────────────┘
```

---

## Key Concepts Summary

### 1. The Orchestration Loop

**YOU manage the back-and-forth:**
1. Send message to OpenAI with function definitions
2. Check if OpenAI wants to call a function
3. If yes:
   - Execute the function yourself
   - Add result to messages
   - Call OpenAI again
4. Display final response
5. Repeat

### 2. Function Definitions

**You provide the schema to OpenAI:**
```python
{
    "name": "function_name",
    "description": "What it does",
    "parameters": {
        "type": "object",
        "properties": {
            "param_name": {
                "type": "string",
                "description": "What this parameter is"
            }
        },
        "required": ["param_name"]
    }
}
```

**OpenAI uses this to:**
- Decide if this function is relevant
- Extract parameter values from user message
- Generate properly formatted function call

### 3. Message History Format

**OpenAI expects this structure:**
```python
[
    {"role": "user", "content": "User's message"},
    {"role": "assistant", "content": "AI's response"},
    # OR
    {"role": "assistant", "function_call": {...}},
    {"role": "function", "name": "func_name", "content": "result"}
]
```

**Roles:**
- `"user"` = Messages from the user
- `"assistant"` = Messages from GPT-4
- `"function"` = Results from function execution

### 4. Two API Calls for Function Usage

**First call:**
- Purpose: Get function call instruction
- Input: User message + function definitions
- Output: Function call details

**Second call:**
- Purpose: Get natural language response
- Input: Full conversation + function result
- Output: Human-friendly response

### 5. Where the "Kitchen" Is

**The actual work happens in YOUR code:**
```python
def get_weather(city):
    response = requests.get(url)  # ← THIS is the kitchen!
    # Your computer makes the API call
    # Your computer processes the data
    return result
```

**OpenAI does NOT execute your functions!**
- OpenAI only TELLS you which function to call
- YOU execute it
- YOU send the result back

### 6. Different Vendors, Different Formats

**The problem MCP solves:**

| Aspect | OpenAI | Claude | Google |
|--------|--------|--------|--------|
| Function key | `functions` | `tools` | `function_declarations` |
| Parameter key | `parameters` | `input_schema` | `parameters` |
| Response key | `function_call` | `tool_use` | `function_call` |
| Message format | Different | Different | Different |

**Without MCP:** You write different code for each vendor

**With MCP:** One server works with all (coming in the next file!)

---

## What's Next?

In the next file, I'll show you the **SAME weather chatbot but using MCP**, and you'll see:

1. How MCP eliminates the orchestration loop
2. How tools are discovered automatically
3. How the same server works with any MCP client
4. The standardized JSON-RPC format
5. Persistent connections vs HTTP requests

---

## Summary of Key Differences (Preview)

| Aspect | Before MCP (This File) | After MCP (Next File) |
|--------|----------------------|---------------------|
| **You manage orchestration?** | ✅ YES | ❌ NO (MCP handles it) |
| **Send function defs every call?** | ✅ YES | ❌ NO (discovered once) |
| **Different code per vendor?** | ✅ YES | ❌ NO (standard format) |
| **Connection type** | HTTP request/response | Persistent stdin/stdout |
| **Complexity** | HIGH (100+ lines) | LOW (20 lines) |

---

**End of Part 1: Tool Calling Before MCP**

Ready for Part 2 with MCP? Let me know!
