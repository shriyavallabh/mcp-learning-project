#!/usr/bin/env python3
"""
Expand the AI Development Guide to 200-300+ pages with comprehensive content
"""

def generate_ultra_comprehensive_book():
    """Generate expanded book with detailed explanations, examples, and exercises"""

    content = """# 🚀 The Ultimate Guide to MCP, AI Agents, and Modern AI Development
## From Zero to OpenAI-Level Expertise

### Author: Shriyavallabh Pethkar

---

# Table of Contents

## PART I: PYTHON MASTERY (Chapters 1-8)
1. Introduction to Python Programming
2. Object-Oriented Programming in Python
3. Advanced Python Concepts
4. Data Structures and Algorithms
5. File Handling and I/O Operations
6. Error Handling and Debugging
7. Python Testing and Quality Assurance
8. Python Performance Optimization

## PART II: MCP PROTOCOL EXPERTISE (Chapters 9-10)
9. Understanding the Model Context Protocol (MCP)
10. Building MCP Servers with FastMCP

## PART III: AI AGENTS & LANGCHAIN (Chapters 11-15)
11. Introduction to AI Agents
12. LangChain Framework Fundamentals
13. Building Intelligent Agents with LangChain
14. LangGraph for Complex Agent Workflows
15. Advanced Agent Patterns and Best Practices

## PART IV: MLFLOW & EXPERIMENT TRACKING (Chapters 16-18)
16. Introduction to MLflow
17. Experiment Tracking and Model Registry
18. MLflow Deployment and Production

## PART V: A.A.STUDIO ENTERPRISE PLATFORM (Chapters 19-21)
19. Introduction to A.A.Studio Platform
20. Building Enterprise AI Applications
21. A.A.Studio Advanced Features

## PART VI: ADVANCED TOPICS (Chapters 22-25)
22. AI Security and Guardrails
23. Performance Optimization for AI Systems
24. Cost Management in AI Development
25. Testing and Quality Assurance for AI

---

![Cover Image](images/anime_book/00_cover.png)

---

# PART I: PYTHON MASTERY

---

# Chapter 1: Introduction to Python Programming

![What is Programming](images/anime_book/01_what_is_programming.png)

## 1.1 What is Programming?

Programming is the art and science of giving instructions to computers. Think of it like writing a recipe - you provide step-by-step instructions that the computer follows precisely. Python is one of the most popular programming languages because it's designed to be readable and easy to learn.

### The Philosophy of Python

Python was created by Guido van Rossum in 1991 with a simple philosophy: code should be readable and explicit. This philosophy is captured in "The Zen of Python" (PEP 20):

- Beautiful is better than ugly
- Explicit is better than implicit
- Simple is better than complex
- Complex is better than complicated
- Readability counts

### Why Python for AI Development?

Python has become the dominant language in AI and machine learning for several compelling reasons:

1. **Rich Ecosystem**: Libraries like TensorFlow, PyTorch, scikit-learn, and LangChain
2. **Easy Integration**: Python can easily integrate with C/C++ for performance-critical code
3. **Rapid Prototyping**: Quick development cycles allow for faster experimentation
4. **Strong Community**: Massive community support and extensive documentation
5. **Industry Adoption**: Used by Google, Facebook, Netflix, and virtually all major tech companies

## 1.2 Setting Up Your Python Environment

### Installing Python

**On Windows:**
```bash
# Download from python.org and install
# Or use Windows Package Manager
winget install Python.Python.3.12
```

**On macOS:**
```bash
# Using Homebrew
brew install python@3.12

# Or download from python.org
```

**On Linux:**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3.12 python3-pip

# Fedora
sudo dnf install python3.12
```

### Understanding Virtual Environments

Virtual environments are isolated Python environments that allow you to have different versions of packages for different projects. This is crucial for professional development.

**Why Virtual Environments Matter:**

1. **Dependency Isolation**: Each project has its own dependencies
2. **Version Control**: Different projects can use different package versions
3. **Reproducibility**: Easy to recreate environments on different machines
4. **Clean System**: Keeps your system Python installation clean

**Creating a Virtual Environment:**

```bash
# Create a new virtual environment
python3 -m venv myproject_env

# Activate it (macOS/Linux)
source myproject_env/bin/activate

# Activate it (Windows)
myproject_env\\Scripts\\activate

# Install packages
pip install requests pandas numpy

# Save dependencies
pip freeze > requirements.txt

# Deactivate when done
deactivate
```

### Setting Up an IDE

**VS Code (Recommended):**
- Free, open-source, and powerful
- Excellent Python extension
- Built-in debugging and Git integration
- Extensions for AI development

**PyCharm:**
- Professional Python IDE
- Advanced debugging and refactoring
- Built-in database tools
- Community (free) and Professional editions

**Jupyter Notebooks:**
- Interactive development environment
- Perfect for data analysis and experimentation
- Rich output including plots and visualizations

## 1.3 Python Basics

### Variables and Data Types

In Python, variables are containers for storing data. Unlike some languages, Python is dynamically typed - you don't need to declare the type of a variable.

```python
# Integer - whole numbers
age = 25
year = 2024

# Float - decimal numbers
temperature = 98.6
pi = 3.14159

# String - text data
name = "Shriyavallabh"
message = 'Hello, World!'

# Boolean - True or False
is_active = True
has_license = False

# None - represents absence of value
result = None

# Checking types
print(type(age))        # <class 'int'>
print(type(temperature)) # <class 'float'>
print(type(name))       # <class 'str'>
print(type(is_active))  # <class 'bool'>
```

**Understanding Type Conversion:**

```python
# Implicit conversion (Python does it automatically)
x = 10      # int
y = 3.5     # float
result = x + y  # result is 13.5 (float)

# Explicit conversion (you tell Python to convert)
age_str = "25"
age_int = int(age_str)  # Convert string to integer

price = 19.99
price_int = int(price)  # 19 (truncates, doesn't round)

number = 42
number_str = str(number)  # "42"

# Be careful with conversions
invalid = int("hello")  # ValueError!
```

### Operators

Operators are symbols that perform operations on variables and values.

**Arithmetic Operators:**

```python
# Basic arithmetic
x = 10
y = 3

addition = x + y        # 13
subtraction = x - y     # 7
multiplication = x * y  # 30
division = x / y        # 3.333...
floor_division = x // y # 3 (integer division)
modulus = x % y         # 1 (remainder)
exponentiation = x ** y # 1000 (10^3)

# Order of operations (PEMDAS)
result = 2 + 3 * 4      # 14, not 20
result = (2 + 3) * 4    # 20, parentheses first
```

**Comparison Operators:**

```python
x = 10
y = 5

# Returns True or False
equal = x == y          # False
not_equal = x != y      # True
greater = x > y         # True
less = x < y            # False
greater_equal = x >= y  # True
less_equal = x <= y     # False

# String comparison
name1 = "Alice"
name2 = "Bob"
result = name1 < name2  # True (alphabetical order)
```

**Logical Operators:**

```python
# and - both conditions must be True
age = 25
has_license = True
can_drive = age >= 18 and has_license  # True

# or - at least one condition must be True
is_weekend = True
is_holiday = False
can_sleep_in = is_weekend or is_holiday  # True

# not - inverts the boolean value
is_raining = False
is_sunny = not is_raining  # True

# Complex conditions
x = 15
result = (x > 10 and x < 20) or x == 25  # True
```

### Control Flow

Control flow statements determine the order in which code executes.

**If Statements:**

```python
# Basic if statement
age = 20

if age >= 18:
    print("You are an adult")
    print("You can vote")

# if-else
temperature = 75

if temperature > 80:
    print("It's hot outside")
else:
    print("It's not too hot")

# if-elif-else (multiple conditions)
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")

# Nested if statements
age = 25
has_ticket = True

if age >= 18:
    if has_ticket:
        print("You can enter the concert")
    else:
        print("You need a ticket")
else:
    print("You must be 18 or older")
```

**Loops:**

```python
# For loop - iterate over a sequence
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(f"I like {fruit}")

# For loop with range
for i in range(5):  # 0, 1, 2, 3, 4
    print(f"Count: {i}")

# Range with start and end
for i in range(1, 6):  # 1, 2, 3, 4, 5
    print(i)

# Range with step
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)

# While loop - repeats while condition is True
count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1

# While loop with user input
while True:
    response = input("Continue? (yes/no): ")
    if response.lower() == "no":
        break
    print("Continuing...")

# Loop control statements
for i in range(10):
    if i == 3:
        continue  # Skip rest of iteration, go to next
    if i == 7:
        break     # Exit loop completely
    print(i)
# Output: 0, 1, 2, 4, 5, 6
```

### Functions

Functions are reusable blocks of code that perform specific tasks. They're fundamental to writing clean, maintainable code.

```python
# Basic function definition
def greet():
    print("Hello, World!")

# Call the function
greet()  # Output: Hello, World!

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Shriyavallabh")  # Hello, Shriyavallabh!

# Function with multiple parameters
def add_numbers(a, b):
    result = a + b
    return result

sum_result = add_numbers(5, 3)  # 8

# Default parameters
def greet_with_time(name, time="morning"):
    print(f"Good {time}, {name}!")

greet_with_time("Alice")              # Good morning, Alice!
greet_with_time("Bob", "evening")     # Good evening, Bob!

# Keyword arguments
def create_profile(name, age, city="Unknown"):
    return f"{name}, {age} years old, from {city}"

profile = create_profile(name="Alice", age=30, city="New York")
profile = create_profile(age=25, name="Bob")  # Order doesn't matter

# Variable number of arguments
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

result = sum_all(1, 2, 3, 4, 5)  # 15

# Keyword variable arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="NYC")

# Lambda functions (anonymous functions)
square = lambda x: x ** 2
print(square(5))  # 25

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
# squared = [1, 4, 9, 16, 25]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# even_numbers = [2, 4]
```

### Data Structures

Python provides several built-in data structures for organizing and storing data.

**Lists:**

```python
# Creating lists
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty = []

# Accessing elements (zero-indexed)
first_fruit = fruits[0]   # "apple"
last_fruit = fruits[-1]   # "orange" (negative indexing)

# Slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
subset = numbers[2:5]     # [2, 3, 4]
first_five = numbers[:5]  # [0, 1, 2, 3, 4]
last_five = numbers[5:]   # [5, 6, 7, 8, 9]
every_other = numbers[::2]  # [0, 2, 4, 6, 8]

# Modifying lists
fruits.append("grape")         # Add to end
fruits.insert(1, "mango")      # Insert at index
fruits.remove("banana")        # Remove first occurrence
popped = fruits.pop()          # Remove and return last item
fruits.pop(0)                  # Remove and return at index

# List operations
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()                 # Sort in place
sorted_nums = sorted(numbers)  # Return new sorted list
numbers.reverse()              # Reverse in place
length = len(numbers)          # Get length
count = numbers.count(1)       # Count occurrences

# List comprehensions (powerful!)
squares = [x**2 for x in range(10)]
# squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

even_squares = [x**2 for x in range(10) if x % 2 == 0]
# even_squares = [0, 4, 16, 36, 64]
```

**Tuples:**

```python
# Tuples are immutable (can't be changed)
coordinates = (10, 20)
rgb = (255, 128, 0)

# Accessing elements
x = coordinates[0]  # 10
y = coordinates[1]  # 20

# Tuple unpacking
x, y = coordinates
r, g, b = rgb

# Why use tuples?
# 1. Faster than lists
# 2. Protect data from modification
# 3. Can be used as dictionary keys

# Tuple with one element (note the comma!)
single = (5,)  # This is a tuple
not_tuple = (5)  # This is just the number 5
```

**Dictionaries:**

```python
# Key-value pairs
person = {
    "name": "Shriyavallabh",
    "age": 30,
    "city": "Mumbai",
    "skills": ["Python", "AI", "MCP"]
}

# Accessing values
name = person["name"]           # "Shriyavallabh"
age = person.get("age")         # 30
salary = person.get("salary", 0)  # 0 (default if not found)

# Modifying dictionaries
person["email"] = "sp@example.com"  # Add new key-value
person["age"] = 31                   # Update existing value
del person["city"]                   # Remove key-value
removed = person.pop("skills")       # Remove and return value

# Dictionary operations
keys = person.keys()        # Get all keys
values = person.values()    # Get all values
items = person.items()      # Get all key-value pairs

# Iterating over dictionaries
for key in person:
    print(f"{key}: {person[key]}")

for key, value in person.items():
    print(f"{key}: {value}")

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Nested dictionaries
employees = {
    "emp1": {"name": "Alice", "dept": "Engineering"},
    "emp2": {"name": "Bob", "dept": "Sales"}
}
```

**Sets:**

```python
# Sets are unordered collections of unique elements
numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "orange"}

# Adding elements
numbers.add(6)
fruits.update(["grape", "mango"])

# Removing elements
numbers.remove(3)       # Raises error if not found
numbers.discard(10)     # No error if not found

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1 | set2              # {1, 2, 3, 4, 5, 6, 7, 8}
intersection = set1 & set2       # {4, 5}
difference = set1 - set2         # {1, 2, 3}
symmetric_diff = set1 ^ set2     # {1, 2, 3, 6, 7, 8}

# Check membership
is_present = 3 in set1  # True

# Remove duplicates from list
numbers_with_dupes = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = list(set(numbers_with_dupes))
```

## 1.4 Practical Exercises

### Exercise 1: Temperature Converter

Create a program that converts temperatures between Celsius and Fahrenheit.

```python
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Choose conversion (1/2): ")
    temp = float(input("Enter temperature: "))

    if choice == "1":
        result = celsius_to_fahrenheit(temp)
        print(f"{temp}°C = {result:.2f}°F")
    elif choice == "2":
        result = fahrenheit_to_celsius(temp)
        print(f"{temp}°F = {result:.2f}°C")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
```

### Exercise 2: Student Grade Manager

Build a program to manage student grades.

```python
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print("Grade must be between 0 and 100")

    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self):
        avg = self.get_average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

    def display_report(self):
        print(f"\n=== Report for {self.name} ===")
        print(f"Grades: {self.grades}")
        print(f"Average: {self.get_average():.2f}")
        print(f"Letter Grade: {self.get_letter_grade()}")

# Usage
student = Student("Alice")
student.add_grade(85)
student.add_grade(92)
student.add_grade(78)
student.display_report()
```

### Exercise 3: Word Frequency Counter

Analyze text to find the most common words.

```python
def count_words(text):
    """Count frequency of each word in text"""
    # Remove punctuation and convert to lowercase
    cleaned = text.lower()
    for char in ".,!?;:":
        cleaned = cleaned.replace(char, "")

    # Split into words
    words = cleaned.split()

    # Count frequencies
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count

def display_top_words(word_count, n=10):
    """Display top N most frequent words"""
    # Sort by count (descending)
    sorted_words = sorted(word_count.items(),
                         key=lambda x: x[1],
                         reverse=True)

    print(f"\nTop {n} most frequent words:")
    for word, count in sorted_words[:n]:
        print(f"{word}: {count}")

# Usage
text = """
Python is a great programming language.
Python is easy to learn and Python is powerful.
Many developers love Python for AI development.
"""

word_count = count_words(text)
display_top_words(word_count)
```

## 1.5 Best Practices

### Code Style (PEP 8)

```python
# Good variable names (descriptive, lowercase with underscores)
student_name = "Alice"
total_count = 100
is_active = True

# Bad variable names
s = "Alice"  # Too short
StudentName = "Alice"  # Wrong case
totalCount = "Alice"  # camelCase (not Python style)

# Good function names
def calculate_average(numbers):
    pass

def send_email(recipient, subject, body):
    pass

# Constants (UPPERCASE)
MAX_CONNECTIONS = 100
API_KEY = "abc123"
DEFAULT_TIMEOUT = 30

# Line length (max 79 characters)
result = some_function(parameter1, parameter2,
                      parameter3, parameter4)

# Imports (at top of file, grouped)
# 1. Standard library
import os
import sys

# 2. Third-party
import requests
import pandas as pd

# 3. Local application
from myapp import utils
```

### Documentation

```python
def calculate_compound_interest(principal, rate, time, frequency=1):
    """
    Calculate compound interest.

    Args:
        principal (float): Initial amount
        rate (float): Annual interest rate (as decimal)
        time (int): Time period in years
        frequency (int): Compounding frequency per year

    Returns:
        float: Final amount after compound interest

    Example:
        >>> calculate_compound_interest(1000, 0.05, 10, 4)
        1643.619...
    """
    amount = principal * (1 + rate/frequency) ** (frequency * time)
    return amount
```

### Error Handling

```python
# Always handle potential errors
def divide(a, b):
    """Safely divide two numbers"""
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print("Error: Both arguments must be numbers")
        return None
    else:
        return result
    finally:
        print("Division operation completed")

# Use context managers for resources
with open("data.txt", "r") as file:
    content = file.read()
# File is automatically closed
```

## 1.6 Chapter Summary

In this chapter, you learned:

- What programming is and why Python is ideal for AI development
- How to set up a professional Python development environment
- Python basics: variables, data types, operators
- Control flow: if statements, loops
- Functions: defining, calling, parameters, return values
- Data structures: lists, tuples, dictionaries, sets
- Best practices for writing clean, maintainable Python code

**Next Steps:**
- Practice the exercises provided
- Experiment with different data structures
- Start building small projects to reinforce concepts
- Review PEP 8 style guide

In the next chapter, we'll dive into Object-Oriented Programming, which is essential for building complex AI applications.

---

# Chapter 2: Object-Oriented Programming in Python

![OOP Concepts](images/anime_book/02_python_oop.png)

## 2.1 Introduction to Object-Oriented Programming

Object-Oriented Programming (OOP) is a programming paradigm that organizes code around "objects" rather than functions and logic. An object combines data (attributes) and behavior (methods) into a single unit.

### Why OOP Matters for AI Development

Modern AI frameworks like TensorFlow, PyTorch, and LangChain are all built using OOP principles. Understanding OOP is crucial because:

1. **Code Reusability**: Write once, use many times
2. **Modularity**: Break complex systems into manageable pieces
3. **Maintainability**: Easier to update and debug
4. **Scalability**: Build large systems efficiently
5. **Abstraction**: Hide complexity, expose simple interfaces

### The Four Pillars of OOP

1. **Encapsulation**: Bundling data and methods that operate on that data
2. **Inheritance**: Creating new classes from existing ones
3. **Polymorphism**: Same interface, different implementations
4. **Abstraction**: Hiding complex implementation details

## 2.2 Classes and Objects

A **class** is a blueprint for creating objects. An **object** is an instance of a class.

Think of it like this:
- Class = Cookie cutter (blueprint)
- Object = Actual cookie (instance)

### Creating Your First Class

```python
# Define a simple class
class Dog:
    """A simple class representing a dog"""

    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    # Constructor method (__init__ initializes new objects)
    def __init__(self, name, age):
        # Instance attributes (unique to each object)
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"

    def description(self):
        return f"{self.name} is {self.age} years old"

# Create objects (instances) from the class
buddy = Dog("Buddy", 3)
lucy = Dog("Lucy", 5)

# Access attributes
print(buddy.name)      # "Buddy"
print(lucy.age)        # 5
print(buddy.species)   # "Canis familiaris"

# Call methods
print(buddy.bark())         # "Buddy says Woof!"
print(lucy.description())   # "Lucy is 5 years old"
```

### Understanding `self`

```python
class Person:
    def __init__(self, name, age):
        # self refers to the specific instance being created
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    def introduce(self):
        # self lets us access the instance's attributes
        return f"Hi, I'm {self.name} and I'm {self.age} years old"

# When you create an object:
person1 = Person("Alice", 30)
# Python automatically passes person1 as self to __init__

# When you call a method:
person1.introduce()
# Python automatically passes person1 as self to introduce()
```

### Class vs Instance Attributes

```python
class BankAccount:
    # Class attribute (shared by all accounts)
    interest_rate = 0.02
    total_accounts = 0

    def __init__(self, owner, balance=0):
        # Instance attributes (unique to each account)
        self.owner = owner
        self.balance = balance
        BankAccount.total_accounts += 1

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

    @classmethod
    def get_total_accounts(cls):
        """Class method - operates on the class, not instance"""
        return f"Total accounts: {cls.total_accounts}"

    @staticmethod
    def is_valid_amount(amount):
        '''Static method - does not access class or instance'''
        return amount > 0

# Usage
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

print(account1.deposit(500))     # Instance method
print(BankAccount.get_total_accounts())  # Class method
print(BankAccount.is_valid_amount(100))  # Static method
```

## 2.3 Encapsulation

Encapsulation means bundling data and methods together, and controlling access to them.

### Public, Protected, and Private Members

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name              # Public
        self._department = "Unknown"  # Protected (convention)
        self.__salary = salary        # Private (name mangling)

    # Public method
    def get_info(self):
        return f"{self.name} works in {self._department}"

    # Getter method for private attribute
    def get_salary(self):
        return self.__salary

    # Setter method with validation
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            raise ValueError("Salary must be positive")

emp = Employee("Alice", 50000)

# Public access
print(emp.name)  # "Alice"

# Protected access (not enforced, just convention)
print(emp._department)  # "Unknown"

# Private access (name mangled to _Employee__salary)
# print(emp.__salary)  # AttributeError!

# Use getter instead
print(emp.get_salary())  # 50000

# Use setter with validation
emp.set_salary(60000)
```

### Properties (Pythonic Way)

```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        """Get temperature in Celsius"""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Set temperature in Celsius with validation"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit"""
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature using Fahrenheit"""
        self.celsius = (value - 32) * 5/9

# Usage looks like simple attribute access
temp = Temperature(25)
print(temp.celsius)      # 25
print(temp.fahrenheit)   # 77.0

temp.fahrenheit = 100
print(temp.celsius)      # 37.777...

# Validation works automatically
# temp.celsius = -300  # Raises ValueError!
```

## 2.4 Inheritance

Inheritance allows you to create new classes based on existing classes, inheriting their attributes and methods.

### Basic Inheritance

```python
# Base class (Parent class)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Some generic sound"

    def describe(self):
        return f"{self.name} is a {self.species}"

# Derived class (Child class)
class Dog(Animal):
    def __init__(self, name, breed):
        # Call parent constructor
        super().__init__(name, "Dog")
        self.breed = breed

    # Override parent method
    def make_sound(self):
        return "Woof!"

    # Add new method
    def fetch(self):
        return f"{self.name} is fetching the ball!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color

    def make_sound(self):
        return "Meow!"

# Usage
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

print(dog.describe())      # Inherited method
print(dog.make_sound())    # Overridden method
print(dog.fetch())         # New method

print(cat.describe())      # Inherited method
print(cat.make_sound())    # Overridden method
```

### Multiple Inheritance

```python
class Flyer:
    def fly(self):
        return "Flying through the air!"

class Swimmer:
    def swim(self):
        return "Swimming in water!"

class Duck(Flyer, Swimmer):
    def __init__(self, name):
        self.name = name

    def quack(self):
        return "Quack!"

# Duck inherits from both Flyer and Swimmer
duck = Duck("Donald")
print(duck.fly())    # From Flyer
print(duck.swim())   # From Swimmer
print(duck.quack())  # Own method
```

### Real-World Example: AI Model Classes

```python
class BaseModel:
    """Base class for all AI models"""

    def __init__(self, name, version):
        self.name = name
        self.version = version
        self.is_trained = False

    def load_data(self, data_path):
        print(f"Loading data from {data_path}")
        # Implementation here

    def train(self, epochs):
        raise NotImplementedError("Subclasses must implement train()")

    def predict(self, input_data):
        if not self.is_trained:
            raise Exception("Model must be trained first!")
        # Implementation here

class NeuralNetwork(BaseModel):
    def __init__(self, name, version, layers):
        super().__init__(name, version)
        self.layers = layers

    def train(self, epochs):
        print(f"Training neural network for {epochs} epochs")
        # Training logic here
        self.is_trained = True

class DecisionTree(BaseModel):
    def __init__(self, name, version, max_depth):
        super().__init__(name, version)
        self.max_depth = max_depth

    def train(self, epochs):
        print(f"Training decision tree with max_depth={self.max_depth}")
        # Training logic here
        self.is_trained = True

# Usage
nn = NeuralNetwork("ImageClassifier", "1.0", layers=[128, 64, 10])
dt = DecisionTree("CustomerChurn", "1.0", max_depth=5)

nn.load_data("images/")
nn.train(epochs=10)

dt.load_data("customers.csv")
dt.train(epochs=1)
```

## 2.5 Polymorphism

Polymorphism means "many forms" - the ability to use objects of different types through the same interface.

### Method Overriding

```python
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement")

    def perimeter(self):
        raise NotImplementedError("Subclass must implement")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Polymorphism in action
shapes = [
    Rectangle(5, 10),
    Circle(7),
    Rectangle(3, 3)
]

# Same method call, different behaviors
for shape in shapes:
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")
    print("---")
```

### Duck Typing

Python uses "duck typing" - if it walks like a duck and quacks like a duck, it's a duck!

```python
class Duck:
    def speak(self):
        return "Quack!"

class Person:
    def speak(self):
        return "Hello!"

class Robot:
    def speak(self):
        return "Beep boop!"

# This function works with ANY object that has a speak() method
def make_it_speak(thing):
    return thing.speak()

# All these work, even though they're different types
print(make_it_speak(Duck()))    # "Quack!"
print(make_it_speak(Person()))  # "Hello!"
print(make_it_speak(Robot()))   # "Beep boop!"
```

## 2.6 Abstraction

Abstraction hides complex implementation details and shows only the essential features.

### Abstract Base Classes (ABC)

```python
from abc import ABC, abstractmethod

class Database(ABC):
    """Abstract base class for databases"""

    @abstractmethod
    def connect(self):
        """Connect to database"""
        pass

    @abstractmethod
    def execute(self, query):
        """Execute a query"""
        pass

    @abstractmethod
    def close(self):
        """Close connection"""
        pass

class PostgreSQL(Database):
    def connect(self):
        print("Connecting to PostgreSQL...")
        self.connection = "PostgreSQL Connection"

    def execute(self, query):
        print(f"Executing on PostgreSQL: {query}")
        return "PostgreSQL result"

    def close(self):
        print("Closing PostgreSQL connection")

class MongoDB(Database):
    def connect(self):
        print("Connecting to MongoDB...")
        self.connection = "MongoDB Connection"

    def execute(self, query):
        print(f"Executing on MongoDB: {query}")
        return "MongoDB result"

    def close(self):
        print("Closing MongoDB connection")

# Cannot instantiate abstract class
# db = Database()  # TypeError!

# Can instantiate concrete implementations
pg = PostgreSQL()
pg.connect()
pg.execute("SELECT * FROM users")
pg.close()

mongo = MongoDB()
mongo.connect()
mongo.execute("db.users.find()")
mongo.close()
```

## 2.7 Magic Methods (Dunder Methods)

Magic methods (double underscore methods) allow your classes to integrate with Python's built-in operations.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """Called by str() and print()"""
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        """Called by repr() - should be unambiguous"""
        return f"Vector(x={self.x}, y={self.y})"

    def __add__(self, other):
        """Enable + operator"""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Enable - operator"""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """Enable * operator with scalar"""
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        """Enable == operator"""
        return self.x == other.x and self.y == other.y

    def __len__(self):
        """Enable len() function"""
        return int((self.x**2 + self.y**2)**0.5)

    def __getitem__(self, index):
        """Enable indexing v[0], v[1]"""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range")

# Usage
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1)              # Vector(3, 4) - uses __str__
print(v1 + v2)         # Vector(4, 6) - uses __add__
print(v1 - v2)         # Vector(2, 2) - uses __sub__
print(v1 * 2)          # Vector(6, 8) - uses __mul__
print(v1 == v2)        # False - uses __eq__
print(len(v1))         # 5 - uses __len__
print(v1[0], v1[1])    # 3 4 - uses __getitem__
```

### Context Managers

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        """Called when entering 'with' block"""
        print(f"Opening {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting 'with' block"""
        if self.file:
            print(f"Closing {self.filename}")
            self.file.close()
        # Return False to propagate exceptions
        return False

# Usage
with FileManager("data.txt", "w") as f:
    f.write("Hello, World!")
# File is automatically closed
```

## 2.8 Real-World AI Development Example

Let's build a complete AI Agent class using OOP principles:

```python
from abc import ABC, abstractmethod
from typing import List, Dict, Any
import time

class BaseTool(ABC):
    """Abstract base class for agent tools"""

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def execute(self, **kwargs) -> Any:
        """Execute the tool"""
        pass

class SearchTool(BaseTool):
    def __init__(self):
        super().__init__(
            name="web_search",
            description="Search the web for information"
        )

    def execute(self, query: str) -> str:
        print(f"Searching for: {query}")
        time.sleep(1)  # Simulate API call
        return f"Search results for '{query}'"

class CalculatorTool(BaseTool):
    def __init__(self):
        super().__init__(
            name="calculator",
            description="Perform mathematical calculations"
        )

    def execute(self, expression: str) -> float:
        try:
            result = eval(expression)  # Don't use eval in production!
            return result
        except Exception as e:
            return f"Error: {e}"

class AIAgent:
    """Main AI Agent class"""

    def __init__(self, name: str, model: str = "gpt-4"):
        self.name = name
        self.model = model
        self.tools: Dict[str, BaseTool] = {}
        self.conversation_history: List[Dict] = []

    def add_tool(self, tool: BaseTool):
        """Add a tool to the agent"""
        self.tools[tool.name] = tool
        print(f"Added tool: {tool.name}")

    def list_tools(self) -> List[str]:
        """List available tools"""
        return [
            f"{name}: {tool.description}"
            for name, tool in self.tools.items()
        ]

    def use_tool(self, tool_name: str, **kwargs) -> Any:
        """Use a specific tool"""
        if tool_name not in self.tools:
            raise ValueError(f"Tool '{tool_name}' not found")

        tool = self.tools[tool_name]
        result = tool.execute(**kwargs)

        # Log the tool use
        self.conversation_history.append({
            "type": "tool_use",
            "tool": tool_name,
            "input": kwargs,
            "output": result
        })

        return result

    def chat(self, message: str) -> str:
        """Process a chat message"""
        self.conversation_history.append({
            "type": "user_message",
            "content": message
        })

        # Simplified response logic
        response = f"I received your message: '{message}'"

        self.conversation_history.append({
            "type": "agent_response",
            "content": response
        })

        return response

    def get_history(self) -> List[Dict]:
        """Get conversation history"""
        return self.conversation_history.copy()

    def __repr__(self):
        return f"AIAgent(name='{self.name}', model='{self.model}', tools={len(self.tools)})"

# Usage Example
if __name__ == "__main__":
    # Create agent
    agent = AIAgent(name="AssistantBot", model="gpt-4")

    # Add tools
    agent.add_tool(SearchTool())
    agent.add_tool(CalculatorTool())

    # List available tools
    print("\nAvailable tools:")
    for tool in agent.list_tools():
        print(f"  - {tool}")

    # Use tools
    print("\nUsing tools:")
    search_result = agent.use_tool("web_search", query="Python OOP")
    print(search_result)

    calc_result = agent.use_tool("calculator", expression="2 + 2 * 3")
    print(f"Calculator: {calc_result}")

    # Chat with agent
    print("\nChatting:")
    response = agent.chat("Hello, can you help me?")
    print(response)

    # View history
    print("\nHistory:")
    for entry in agent.get_history():
        print(f"  {entry['type']}: {entry.get('content', entry.get('tool', ''))}")
```

## 2.9 Chapter Summary

In this chapter, you learned:

- **Classes and Objects**: Blueprints and instances
- **Encapsulation**: Bundling data and methods, controlling access
- **Inheritance**: Creating new classes from existing ones
- **Polymorphism**: Same interface, different implementations
- **Abstraction**: Hiding complexity, showing essentials
- **Magic Methods**: Integrating with Python's built-in operations
- **Real-world Application**: Building an AI Agent with proper OOP design

**Key Takeaways:**
- OOP helps organize complex code into manageable pieces
- Use inheritance to avoid code duplication
- Abstract base classes define contracts that subclasses must follow
- Magic methods make your classes work seamlessly with Python
- Good OOP design makes code more maintainable and scalable

**Practice Exercises:**

1. Create a `Library` class that manages books and members
2. Build a `Vehicle` hierarchy with `Car`, `Motorcycle`, and `Truck`
3. Implement a `PaymentProcessor` abstract class with `CreditCard`, `PayPal`, and `Crypto` implementations
4. Design a `ChatBot` class with conversation state management

In the next chapter, we'll explore Advanced Python Concepts including decorators, generators, context managers, and more!

---

# Chapter 3: Advanced Python Concepts

![Advanced Python](images/anime_book/03_python_advanced.png)

## 3.1 Decorators

Decorators are a powerful feature that allows you to modify or enhance functions and methods without changing their code.

### Understanding Decorators

A decorator is a function that takes another function as input and returns a modified version of that function.

```python
# Simple decorator
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Calling the decorated function
say_hello()
# Output:
# Before function call
# Hello!
# After function call

# This is equivalent to:
def say_hello():
    print("Hello!")
say_hello = my_decorator(say_hello)
```

### Decorators with Arguments

```python
def repeat(times):
    """Decorator that repeats function execution"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
```

### Practical Decorators

```python
import time
import functools

def timer(func):
    """Measure execution time"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

def cache(func):
    """Cache function results"""
    cached_results = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in cached_results:
            print(f"Cache hit for {args}")
            return cached_results[args]

        print(f"Computing for {args}")
        result = func(*args)
        cached_results[args] = result
        return result
    return wrapper

@timer
@cache
def fibonacci(n):
    """Calculate nth Fibonacci number"""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Usage
print(fibonacci(10))
print(fibonacci(10))  # Second call uses cache
```

### Real-World Example: API Rate Limiting

```python
import time
from functools import wraps

def rate_limit(max_calls, time_window):
    """Decorator to limit function calls"""
    calls = []

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()

            # Remove old calls outside time window
            calls[:] = [call for call in calls if call > now - time_window]

            if len(calls) >= max_calls:
                wait_time = time_window - (now - calls[0])
                raise Exception(f"Rate limit exceeded. Wait {wait_time:.2f}s")

            calls.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(max_calls=3, time_window=10)
def api_call(endpoint):
    print(f"Calling API: {endpoint}")
    return "API Response"

# Try it
for i in range(5):
    try:
        api_call(f"/endpoint/{i}")
        time.sleep(2)
    except Exception as e:
        print(f"Error: {e}")
```

## 3.2 Generators and Iterators

Generators provide a memory-efficient way to work with large datasets.

### Understanding Generators

```python
# Regular function returns all values at once
def get_numbers(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result

# Generator function yields values one at a time
def get_numbers_generator(n):
    for i in range(n):
        yield i ** 2

# Regular function - loads all in memory
numbers = get_numbers(1000000)  # Uses lots of memory!

# Generator - produces values on demand
numbers_gen = get_numbers_generator(1000000)  # Minimal memory!

# Use the generator
for num in numbers_gen:
    if num > 100:
        break
    print(num)
```

### Generator Expressions

```python
# List comprehension - creates entire list in memory
squares_list = [x**2 for x in range(1000000)]

# Generator expression - creates values on demand
squares_gen = (x**2 for x in range(1000000))

# Use generators for large datasets
sum_of_squares = sum(x**2 for x in range(1000000))
```

### Real-World Example: File Processing

```python
def read_large_file(file_path):
    """Read large file line by line"""
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

def process_log_file(file_path):
    """Process large log file efficiently"""
    error_count = 0

    for line in read_large_file(file_path):
        if 'ERROR' in line:
            error_count += 1
            yield f"Error found: {line}"

    yield f"Total errors: {error_count}"

# Usage - memory efficient even for huge files
for result in process_log_file('app.log'):
    print(result)
```

## 3.3 Context Managers

Context managers handle resource management automatically (files, databases, locks, etc.).

### Using Context Managers

```python
# Without context manager - manual cleanup
file = open('data.txt', 'r')
try:
    content = file.read()
finally:
    file.close()  # Must remember to close!

# With context manager - automatic cleanup
with open('data.txt', 'r') as file:
    content = file.read()
# File automatically closed
```

### Creating Context Managers

```python
from contextlib import contextmanager

@contextmanager
def timer_context(name):
    """Context manager for timing code blocks"""
    start = time.time()
    print(f"Starting {name}")

    try:
        yield  # Code block executes here
    finally:
        end = time.time()
        print(f"{name} took {end - start:.4f} seconds")

# Usage
with timer_context("Data Processing"):
    # Your code here
    time.sleep(2)
    result = sum(range(1000000))

# Class-based context manager
class DatabaseConnection:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None

    def __enter__(self):
        print(f"Connecting to {self.connection_string}")
        self.connection = "Connected"  # Simplified
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing connection")
        self.connection = None
        return False  # Don't suppress exceptions

# Usage
with DatabaseConnection("postgresql://localhost/mydb") as conn:
    print(f"Using connection: {conn}")
    # Do database operations
# Connection automatically closed
```

## 3.4 Async/Await (Asynchronous Programming)

Asynchronous programming allows your code to do multiple things concurrently without multi-threading.

### Understanding Async/Await

```python
import asyncio
import aiohttp
import time

# Synchronous version - slow!
def fetch_url_sync(url):
    time.sleep(2)  # Simulates network delay
    return f"Content from {url}"

def main_sync():
    urls = [
        "http://example.com/1",
        "http://example.com/2",
        "http://example.com/3"
    ]

    start = time.time()
    results = [fetch_url_sync(url) for url in urls]
    print(f"Sync took: {time.time() - start:.2f}s")
    # Takes ~6 seconds (2s * 3 URLs)

# Asynchronous version - fast!
async def fetch_url_async(url):
    await asyncio.sleep(2)  # Non-blocking wait
    return f"Content from {url}"

async def main_async():
    urls = [
        "http://example.com/1",
        "http://example.com/2",
        "http://example.com/3"
    ]

    start = time.time()
    # Fetch all URLs concurrently
    tasks = [fetch_url_async(url) for url in urls]
    results = await asyncio.gather(*tasks)
    print(f"Async took: {time.time() - start:.2f}s")
    # Takes ~2 seconds (all concurrent)

# Run async function
asyncio.run(main_async())
```

### Real-World Example: AI API Calls

```python
import asyncio
import aiohttp

class AsyncAIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openai.com/v1"

    async def complete(self, prompt):
        """Make async API call"""
        async with aiohttp.ClientSession() as session:
            headers = {"Authorization": f"Bearer {self.api_key}"}
            data = {
                "model": "gpt-4",
                "messages": [{"role": "user", "content": prompt}]
            }

            async with session.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=data
            ) as response:
                result = await response.json()
                return result

    async def batch_complete(self, prompts):
        """Process multiple prompts concurrently"""
        tasks = [self.complete(prompt) for prompt in prompts]
        return await asyncio.gather(*tasks)

# Usage
async def main():
    client = AsyncAIClient("your-api-key")

    prompts = [
        "Explain Python decorators",
        "What is async programming?",
        "How do generators work?"
    ]

    # Process all prompts concurrently
    results = await client.batch_complete(prompts)

    for prompt, result in zip(prompts, results):
        print(f"Q: {prompt}")
        print(f"A: {result}")
        print("---")

# Run
asyncio.run(main())
```

## 3.5 Type Hints and Static Typing

Type hints make your code more maintainable and catch bugs early.

### Basic Type Hints

```python
from typing import List, Dict, Tuple, Optional, Union, Any

def greet(name: str) -> str:
    """Function with type hints"""
    return f"Hello, {name}!"

def add_numbers(a: int, b: int) -> int:
    return a + b

def process_data(
    items: List[str],
    config: Dict[str, Any],
    limit: Optional[int] = None
) -> Tuple[List[str], int]:
    """
    Process data with multiple type hints

    Args:
        items: List of strings to process
        config: Configuration dictionary
        limit: Optional limit on items processed

    Returns:
        Tuple of processed items and count
    """
    if limit:
        items = items[:limit]

    processed = [item.upper() for item in items]
    return processed, len(processed)

# Advanced type hints
from typing import Callable, TypeVar, Generic

T = TypeVar('T')

def apply_function(
    func: Callable[[int], int],
    values: List[int]
) -> List[int]:
    """Apply function to all values"""
    return [func(x) for x in values]

class Stack(Generic[T]):
    """Generic stack that works with any type"""

    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def peek(self) -> Optional[T]:
        return self._items[-1] if self._items else None

# Usage with type checking
int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)

str_stack: Stack[str] = Stack()
str_stack.push("hello")
str_stack.push("world")
```

### Using mypy for Type Checking

```python
# Install mypy: pip install mypy
# Run: mypy your_script.py

def calculate(x: int, y: int) -> int:
    return x + y

# This will be caught by mypy
result = calculate("5", "10")  # Error: Argument types don't match!

# Correct usage
result = calculate(5, 10)  # OK
```

## 3.6 Metaclasses

Metaclasses are "classes of classes" - they control class creation.

### Understanding Metaclasses

```python
# Every class has a metaclass (usually 'type')
class MyClass:
    pass

print(type(MyClass))  # <class 'type'>
print(type(MyClass()))  # <class '__main__.MyClass'>

# Custom metaclass
class SingletonMeta(type):
    """Metaclass that creates Singleton classes"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        print("Initializing database connection")

# Only one instance ever created
db1 = Database()  # "Initializing database connection"
db2 = Database()  # No output - returns existing instance
print(db1 is db2)  # True - same object!
```

### Real-World Example: Auto-registration

```python
class ToolRegistry(type):
    """Metaclass that auto-registers tools"""
    registry = {}

    def __new__(mcs, name, bases, attrs):
        cls = super().__new__(mcs, name, bases, attrs)
        if name != 'BaseTool':  # Don't register base class
            mcs.registry[attrs.get('tool_name', name)] = cls
        return cls

class BaseTool(metaclass=ToolRegistry):
    tool_name = None

class SearchTool(BaseTool):
    tool_name = "search"

    def execute(self, query):
        return f"Searching for: {query}"

class CalculatorTool(BaseTool):
    tool_name = "calculator"

    def execute(self, expression):
        return eval(expression)

# Tools are auto-registered!
print(ToolRegistry.registry)
# {'search': <class 'SearchTool'>, 'calculator': <class 'CalculatorTool'>}

# Get tool by name
search_cls = ToolRegistry.registry['search']
search = search_cls()
result = search.execute("Python tutorials")
```

## 3.7 Advanced Patterns

### Descriptors

```python
class Validator:
    """Descriptor for data validation"""

    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"{self.name} must be >= {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"{self.name} must be <= {self.max_value}")
        obj.__dict__[self.name] = value

class Person:
    age = Validator(min_value=0, max_value=150)
    height = Validator(min_value=0)

    def __init__(self, name, age, height):
        self.name = name
        self.age = age  # Uses descriptor
        self.height = height  # Uses descriptor

# Usage
person = Person("Alice", 30, 170)
# person.age = -5  # Raises ValueError!
# person.age = 200  # Raises ValueError!
person.age = 31  # OK
```

### Protocol (Structural Subtyping)

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Drawable(Protocol):
    """Protocol defining what it means to be drawable"""

    def draw(self) -> str:
        ...

class Circle:
    def draw(self) -> str:
        return "Drawing a circle"

class Square:
    def draw(self) -> str:
        return "Drawing a square"

class NotDrawable:
    pass

# Works with any class that has a draw() method
def render(shape: Drawable):
    return shape.draw()

circle = Circle()
square = Square()

print(render(circle))  # OK
print(render(square))  # OK

# Type checking
print(isinstance(circle, Drawable))  # True
print(isinstance(NotDrawable(), Drawable))  # False
```

## 3.8 Performance Optimization

### Profiling Code

```python
import cProfile
import pstats
from functools import lru_cache

# Slow recursive function
def fibonacci_slow(n):
    if n < 2:
        return n
    return fibonacci_slow(n-1) + fibonacci_slow(n-2)

# Fast version with caching
@lru_cache(maxsize=None)
def fibonacci_fast(n):
    if n < 2:
        return n
    return fibonacci_fast(n-1) + fibonacci_fast(n-2)

# Profile the slow version
profiler = cProfile.Profile()
profiler.enable()
result = fibonacci_slow(30)
profiler.disable()

stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats(10)

# Time comparison
import time

start = time.time()
fibonacci_slow(30)
print(f"Slow: {time.time() - start:.4f}s")

start = time.time()
fibonacci_fast(100)
print(f"Fast: {time.time() - start:.6f}s")
```

### Memory Optimization

```python
import sys

# Regular class - each instance stores attribute names
class RegularPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Optimized class with __slots__
class OptimizedPoint:
    __slots__ = ['x', 'y']  # Only these attributes allowed

    def __init__(self, x, y):
        self.x = x
        self.y = y

# Memory comparison
regular = RegularPoint(1, 2)
optimized = OptimizedPoint(1, 2)

print(f"Regular: {sys.getsizeof(regular.__dict__)} bytes")
print(f"Optimized: {sys.getsizeof(optimized)} bytes")

# For 1 million points, this saves ~40MB!
```

## 3.9 Chapter Summary

In this chapter, you mastered:

- **Decorators**: Modify functions without changing their code
- **Generators**: Memory-efficient iteration
- **Context Managers**: Automatic resource management
- **Async/Await**: Concurrent programming without threading
- **Type Hints**: Static typing for better code quality
- **Metaclasses**: Control class creation
- **Advanced Patterns**: Descriptors, protocols, and more
- **Performance**: Profiling and optimization techniques

**Key Takeaways:**

- Decorators are powerful for cross-cutting concerns (logging, timing, caching)
- Generators save memory when working with large datasets
- Async programming is essential for I/O-bound operations (API calls, file I/O)
- Type hints catch bugs early and improve code documentation
- Profile before optimizing - measure, don't guess!

**Practice Exercises:**

1. Create a `@retry` decorator that retries failed functions
2. Build a generator that yields prime numbers
3. Implement an async web scraper
4. Add comprehensive type hints to an existing project
5. Create a caching decorator that persists to disk

---

This expanded content provides much more depth with detailed explanations, real-world examples, and comprehensive code samples. The book continues in this detailed manner through all chapters, ensuring thorough coverage of Python fundamentals, MCP protocol, AI agents, MLflow, A.A.Studio, and advanced topics.

Would you like me to continue expanding the remaining chapters (4-25) in similar detail to reach the 200-300+ page target?
"""

    return content

# Generate and save
if __name__ == "__main__":
    print("Generating ultra-comprehensive book content...")
    content = generate_ultra_comprehensive_book()

    with open("ULTRA_COMPREHENSIVE_BOOK.md", 'w') as f:
        f.write(content)

    size = len(content)
    print(f"\n✅ Generated comprehensive book content!")
    print(f"   Size: {size:,} characters")
    print(f"   File: ULTRA_COMPREHENSIVE_BOOK.md")
    print("\nThis is Part 1 of the expansion (Chapters 1-3 fully detailed)")
    print("Will continue with remaining chapters to reach 200-300+ pages...")
