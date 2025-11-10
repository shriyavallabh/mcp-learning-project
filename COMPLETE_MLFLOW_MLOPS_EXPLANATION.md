# Complete MLflow & MLOps Explanation
## From Hackathon Call - Every Concept Explained in Extreme Detail

**Purpose**: This document explains EVERY concept mentioned in the hackathon call about MLflow, model registry, experimentation, and deployment. Written specifically for someone learning Python and ML operations.

---

## Table of Contents
1. [What Problem Are We Solving?](#what-problem-are-we-solving)
2. [Core Concepts](#core-concepts)
3. [The Complete Workflow](#the-complete-workflow)
4. [Code Breakdown](#code-breakdown)
5. [Enterprise Components (ACE, AI-Mart)](#enterprise-components)
6. [Deployment Concepts](#deployment-concepts)
7. [Practical Example](#practical-example)

---

## What Problem Are We Solving?

### The Problem Without MLflow

Imagine you're baking cakes (models) and trying different recipes (experiments):

**WITHOUT a system like MLflow:**
- ❌ You write recipe in notebook, forget exact measurements next day
- ❌ You bake 50 cakes, can't remember which recipe made the best one
- ❌ Your team member asks "which cake was good?", you can't show them
- ❌ 6 months later, auditor asks "prove this cake recipe works", you have no evidence
- ❌ You want to put best cake in store, but recipe is lost

**WITH MLflow:**
- ✅ Every recipe automatically saved with exact measurements
- ✅ Every cake photographed, taste-tested, results recorded
- ✅ Compare all 50 cakes side-by-side in a table
- ✅ Evidence stored forever (even if recipe retired)
- ✅ One-click to put winning recipe in production

### Real ML Problem

**Machine Learning Model Lifecycle** has these challenges:
1. **Experimentation** - Try 100s of model variations
2. **Tracking** - Remember what worked and what didn't
3. **Reproducibility** - Run same experiment again, get same result
4. **Deployment** - Move model from laptop to production server
5. **Auditing** - Prove model behavior 2 years later
6. **Collaboration** - Share models with team

**MLflow solves ALL of these problems.**

---

## Core Concepts

### 1. MLflow (The Platform)

**What is MLflow?**
- **Type**: Open-source Python library + platform
- **Purpose**: Manages the complete machine learning lifecycle
- **Created by**: Databricks company
- **Think of it as**: A "version control system" for ML models (like Git is for code)

**Four Components of MLflow:**

```
┌─────────────────────────────────────────────────────────┐
│                     MLflow Platform                      │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  1. MLflow Tracking     ← Log experiments & metrics     │
│  2. MLflow Projects     ← Package code in reusable way  │
│  3. MLflow Models       ← Standard format for models    │
│  4. MLflow Registry     ← Central model storage         │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### 2. Experiment (Container for Attempts)

**What is an Experiment?**
- **Definition**: A named container that holds multiple related attempts (runs)
- **Purpose**: Group similar model training attempts together
- **Analogy**: A folder that contains all your attempts at solving one problem

**Example:**
```
Experiment: "Predict Customer Churn - December 2025"
  ├── Run 1: Random Forest with 100 trees → 85% accuracy
  ├── Run 2: Random Forest with 200 trees → 87% accuracy
  ├── Run 3: XGBoost with default params → 89% accuracy
  └── Run 4: XGBoost tuned parameters → 92% accuracy ← WINNER!
```

**In Python:**
```python
import mlflow

# Creating an experiment
# ----------------------
# mlflow = MODULE (imported library)
# . = DOT notation (accessing something inside the module)
# create_experiment = FUNCTION (action to perform)
# () = Parentheses mean we're CALLING/EXECUTING the function
# "my-first-experiment" = STRING parameter (text in quotes)

experiment_id = mlflow.create_experiment("my-first-experiment")
```

**Line-by-line breakdown:**
- `import mlflow`
  - **import** = Keyword that brings in external code
  - **mlflow** = Name of the library we're importing
  - **Effect**: Makes all MLflow functions available to use

- `experiment_id = mlflow.create_experiment("my-first-experiment")`
  - **experiment_id** = VARIABLE NAME (our chosen label to store the result)
  - **=** = Assignment operator (puts right side into left side)
  - **mlflow** = The imported module
  - **.** = Dot notation (accessing function inside mlflow module)
  - **create_experiment** = FUNCTION NAME (creates a new experiment)
  - **()** = Parentheses mean "execute this function now"
  - **"my-first-experiment"** = STRING argument (text name for the experiment)
  - **Quotes mean**: This is literal text, not a variable name
  - **Whole line effect**: Creates new experiment in MLflow, stores its ID in variable

### 3. Run (Single Attempt)

**What is a Run?**
- **Definition**: A single execution of model training code
- **Purpose**: Record one specific attempt with its parameters and results
- **Analogy**: One entry in your lab notebook

**What Gets Logged in a Run:**
```
Run #42
├── Parameters (inputs to the model)
│   ├── n_estimators: 100
│   ├── max_depth: 10
│   └── learning_rate: 0.01
│
├── Metrics (performance measures)
│   ├── accuracy: 0.92
│   ├── f1_score: 0.89
│   └── training_time: 45 seconds
│
├── Artifacts (files produced)
│   ├── model.pkl (the trained model)
│   ├── confusion_matrix.png (visualization)
│   └── feature_importance.csv (analysis)
│
└── Metadata
    ├── Start time: 2025-11-07 10:30:00
    ├── End time: 2025-11-07 10:30:45
    ├── User: shriya
    └── Git commit: abc123def
```

**In Python:**
```python
with mlflow.start_run():
    # Train model
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    # Log parameter
    mlflow.log_param("n_estimators", 100)

    # Log metric
    accuracy = model.score(X_test, y_test)
    mlflow.log_metric("accuracy", accuracy)

    # Log model
    mlflow.sklearn.log_model(model, "random_forest_model")
```

**Detailed breakdown:**

```python
with mlflow.start_run():
```
- **with** = KEYWORD (Python context manager - handles setup/cleanup)
- **mlflow.start_run()** = FUNCTION that starts logging
- **:** = Colon starts an indented block
- **Effect**: Everything indented below gets logged to MLflow

```python
    model = RandomForestClassifier(n_estimators=100)
```
- **model** = VARIABLE NAME (our label for the model)
- **=** = Assignment
- **RandomForestClassifier** = CLASS (blueprint for ML model)
- **()** = Parentheses mean creating an OBJECT from the class
- **n_estimators=100** = Named parameter (setting a configuration)
- **100** = Number (no quotes, so it's a number not text)

```python
    model.fit(X_train, y_train)
```
- **model** = VARIABLE we created above
- **.** = Dot notation (accessing something inside model)
- **fit** = METHOD (function inside the model object)
- **()** = Execute the method
- **X_train, y_train** = Two variables separated by comma (training data)
- **Effect**: Train the model on the data

```python
    mlflow.log_param("n_estimators", 100)
```
- **mlflow.log_param** = FUNCTION to record a parameter
- **()** = Execute the function
- **"n_estimators"** = STRING (name of parameter, in quotes = text)
- **,** = Comma separates arguments
- **100** = NUMBER (value of parameter, no quotes = number)
- **Effect**: Records "n_estimators=100" in MLflow run

```python
    accuracy = model.score(X_test, y_test)
```
- **accuracy** = VARIABLE to store the result
- **model.score()** = METHOD that calculates accuracy
- **X_test, y_test** = Test data
- **Effect**: Calculate how accurate the model is, store in variable

```python
    mlflow.log_metric("accuracy", accuracy)
```
- **mlflow.log_metric** = FUNCTION to record a metric
- **"accuracy"** = STRING name of the metric
- **accuracy** = VARIABLE (no quotes = use the value stored in variable)
- **Effect**: Records the accuracy value in MLflow

```python
    mlflow.sklearn.log_model(model, "random_forest_model")
```
- **mlflow.sklearn** = Sub-module for scikit-learn models
- **.log_model** = METHOD to save the entire model
- **model** = VARIABLE containing our trained model
- **"random_forest_model"** = STRING name to save it as
- **Effect**: Saves complete model file to MLflow

### 4. Model Registry (The Storage Warehouse)

**What is Model Registry?**
- **Definition**: Centralized storage for trained models with versioning
- **Purpose**: Store, organize, and manage models across their lifecycle
- **Analogy**: A library with version-controlled books

**Model Stages:**
```
Model: "Customer Churn Predictor"
│
├── Version 1 (Staging) ← Being tested
├── Version 2 (Production) ← Currently serving predictions
├── Version 3 (Staging) ← New version being validated
└── Version 4 (Archived) ← Old version, kept for audit
```

**Lifecycle Flow:**
```
Developer's Laptop
      ↓ (experiment & train)
  Experiment Run
      ↓ (select best)
   Registered Model
      ↓ (validate)
    [Staging]
      ↓ (approve)
   [Production]
      ↓ (replace with newer)
    [Archived]
```

### 5. Databricks (The Platform/Environment)

**What is Databricks?**
- **Type**: Cloud-based platform (runs on Azure/AWS/Google Cloud)
- **Purpose**: Unified environment for data engineering, ML, and analytics
- **Components**: Notebooks + Compute + Storage + MLflow (built-in)

**Why mentioned in the call:**
- MLflow was created by Databricks
- Databricks has MLflow built-in (no setup needed)
- The hackathon uses Databricks as the environment
- When you run experiments in Databricks, they auto-log to MLflow

**Architecture:**
```
┌───────────────────────────────────────────────────┐
│              Databricks Workspace                 │
├───────────────────────────────────────────────────┤
│                                                   │
│  Notebooks  ← Write code here                    │
│     ↓                                             │
│  Clusters   ← Compute resources run code         │
│     ↓                                             │
│  MLflow     ← Auto-tracks experiments            │
│     ↓                                             │
│  Storage    ← Saves models & artifacts           │
│                                                   │
└───────────────────────────────────────────────────┘
```

---

## The Complete Workflow

### Step-by-Step: From Idea to Production

**STEP 1: Create Experiment**
```python
import mlflow

# Create container for our attempts
experiment_name = "Fraud Detection Model"
experiment_id = mlflow.create_experiment(experiment_name)

# Set this as active experiment
mlflow.set_experiment(experiment_name)
```

**STEP 2: Run Multiple Experiments**
```python
# Attempt 1: Try Random Forest
with mlflow.start_run(run_name="random_forest_v1"):
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    mlflow.log_param("algorithm", "RandomForest")
    mlflow.log_param("n_estimators", 100)

    accuracy = model.score(X_test, y_test)
    mlflow.log_metric("accuracy", accuracy)

    mlflow.sklearn.log_model(model, "model")

# Attempt 2: Try XGBoost
with mlflow.start_run(run_name="xgboost_v1"):
    model = XGBClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    mlflow.log_param("algorithm", "XGBoost")
    mlflow.log_param("n_estimators", 100)

    accuracy = model.score(X_test, y_test)
    mlflow.log_metric("accuracy", accuracy)

    mlflow.sklearn.log_model(model, "model")
```

**What happens after this code runs:**

```
MLflow UI (http://localhost:5000 or Databricks UI)

Experiment: "Fraud Detection Model"
┌─────────────────────────────────────────────────────┐
│ Run Name        │ Accuracy │ Algorithm     │ Status │
├─────────────────────────────────────────────────────┤
│ random_forest_v1│ 0.85     │ RandomForest  │ ✓      │
│ xgboost_v1      │ 0.92     │ XGBoost       │ ✓      │
└─────────────────────────────────────────────────────┘
```

**STEP 3: Compare and Select Best**

You click on runs in the UI and see detailed comparison:
```
┌───────────────────────────────────────┐
│      Model Comparison                 │
├───────────────────────────────────────┤
│ Metric          RF      XGBoost       │
│ Accuracy        85%     92%    ← BEST │
│ Training Time   45s     120s          │
│ Memory          200MB   500MB         │
└───────────────────────────────────────┘
```

**STEP 4: Register Best Model**
```python
# Get the run ID of the best model
best_run_id = "abc123def456"  # From MLflow UI

# Register the model
model_uri = f"runs:/{best_run_id}/model"
model_name = "fraud_detector_production"

mlflow.register_model(
    model_uri=model_uri,
    name=model_name
)
```

**Line-by-line:**
```python
best_run_id = "abc123def456"
```
- **best_run_id** = VARIABLE NAME (our label)
- **=** = Assignment
- **"abc123def456"** = STRING (unique ID from MLflow)
- **Quotes** = This is text/identifier, not code

```python
model_uri = f"runs:/{best_run_id}/model"
```
- **model_uri** = VARIABLE NAME (URI = Universal Resource Identifier, like a path)
- **=** = Assignment
- **f"..."** = F-STRING (special string that can embed variables)
- **"runs:/"** = Text part of the path
- **{best_run_id}** = VARIABLE SUBSTITUTION (curly braces in f-string)
- **"/model"** = More text
- **Effect**: Creates path like "runs:/abc123def456/model"

```python
model_name = "fraud_detector_production"
```
- **model_name** = VARIABLE NAME
- **=** = Assignment
- **"fraud_detector_production"** = STRING (human-readable name)

```python
mlflow.register_model(
    model_uri=model_uri,
    name=model_name
)
```
- **mlflow.register_model** = FUNCTION to register model
- **()** = Execute function
- **model_uri=model_uri** = NAMED ARGUMENT (parameter_name=value)
  - First `model_uri` = parameter name (part of function definition)
  - Second `model_uri` = variable we created above
- **name=model_name** = Another named argument
- **Effect**: Registers model in the Model Registry

**STEP 5: Promote Through Stages**
```python
from mlflow.tracking import MlflowClient

client = MlflowClient()

# Transition to Staging for testing
client.transition_model_version_stage(
    name="fraud_detector_production",
    version=1,
    stage="Staging"
)

# After testing, promote to Production
client.transition_model_version_stage(
    name="fraud_detector_production",
    version=1,
    stage="Production"
)
```

**STEP 6: Load Model in Production**
```python
import mlflow.pyfunc

# Load the production model
model = mlflow.pyfunc.load_model(
    model_uri="models:/fraud_detector_production/Production"
)

# Use it for predictions
predictions = model.predict(new_data)
```

---

## Code Breakdown: From the Transcript

The transcript mentioned this code pattern:

```python
# Create experiment
experiment_id = mlflow.create_experiment("my_experiment")

# Start run
with mlflow.start_run():
    # Create Random Forest
    model = RandomForestClassifier()

    # Train it
    model.fit(X_train, y_train)

    # Log inputs
    mlflow.log_param("max_depth", 10)
    mlflow.log_param("n_estimators", 100)

    # Get run ID
    run_id = mlflow.active_run().info.run_id

# Register model
model_uri = f"runs:/{run_id}/model"
mlflow.register_model(model_uri, "my_model")
```

### Extreme Detail Breakdown

**Line 1-2: Create Experiment**
```python
experiment_id = mlflow.create_experiment("my_experiment")
```

**What each part IS:**
- `experiment_id` → **VARIABLE** (storage location)
- `=` → **OPERATOR** (assignment operator)
- `mlflow` → **MODULE** (imported library)
- `.` → **DOT OPERATOR** (access member of module)
- `create_experiment` → **FUNCTION** (creates experiment)
- `()` → **PARENTHESES** (execute function)
- `"my_experiment"` → **STRING** (text parameter)
- `"` → **QUOTES** (indicate text, not variable)

**What it DOES:**
1. Calls MLflow's create_experiment function
2. Passes "my_experiment" as the name
3. MLflow creates new experiment in its database
4. Returns a unique ID (like "12345")
5. Stores that ID in variable experiment_id

**Why variable name doesn't matter:**
```python
# These all do THE SAME THING:
experiment_id = mlflow.create_experiment("my_experiment")
exp_id = mlflow.create_experiment("my_experiment")
x = mlflow.create_experiment("my_experiment")
banana = mlflow.create_experiment("my_experiment")

# Variable name is just a label you choose!
```

**Line 4-5: Start Run Context**
```python
with mlflow.start_run():
```

**What each part IS:**
- `with` → **KEYWORD** (Python context manager)
- `mlflow.start_run` → **FUNCTION** (starts a run)
- `()` → **PARENTHESES** (execute function)
- `:` → **COLON** (starts indented block)

**What CONTEXT MANAGER means:**
```python
# WITHOUT context manager:
run = mlflow.start_run()
# ... do stuff ...
mlflow.end_run()  # Easy to forget!

# WITH context manager:
with mlflow.start_run():
    # ... do stuff ...
# Automatically ends run when done!
```

**Why we use `with`:**
- Automatically starts run
- Automatically ends run when done
- Ensures proper cleanup even if error occurs

**Line 7-8: Create Model**
```python
    model = RandomForestClassifier()
```

**What each part IS:**
- `model` → **VARIABLE** (our chosen name)
- `=` → **OPERATOR** (assignment)
- `RandomForestClassifier` → **CLASS** (blueprint for model)
- `()` → **PARENTHESES** (create object from class)

**Class vs Object (CRUCIAL CONCEPT):**
```
CLASS = Blueprint/Recipe
├── RandomForestClassifier ← The recipe
│
OBJECT = Actual Thing Built from Blueprint
├── model ← The cake baked from recipe
```

**Analogy:**
- `RandomForestClassifier` = Cookie cutter shape (class)
- `model` = Actual cookie made with cutter (object)
- `()` = Pressing the cutter to make cookie (instantiation)

**Line 10-11: Train Model**
```python
    model.fit(X_train, y_train)
```

**What each part IS:**
- `model` → **OBJECT** (the model we created)
- `.` → **DOT OPERATOR** (access member of object)
- `fit` → **METHOD** (function inside object)
- `()` → **PARENTHESES** (execute method)
- `X_train, y_train` → **VARIABLES** (training data)
- `,` → **COMMA** (separates arguments)

**What METHOD means:**
```
FUNCTION = Standalone action
├── print("hello")  ← Just sitting there

METHOD = Function attached to object
├── model.fit()  ← Belongs to model object
├── text.upper()  ← Belongs to text object
```

**Why DOT notation:**
```python
model.fit(X_train, y_train)
#     ↑
#     "Hey model object, use YOUR fit method"

# NOT a separate function:
# fit(model, X_train, y_train)  ← Wrong!
```

**Line 14-15: Log Parameter**
```python
    mlflow.log_param("max_depth", 10)
```

**What each part IS:**
- `mlflow` → **MODULE**
- `.log_param` → **FUNCTION**
- `()` → **EXECUTE**
- `"max_depth"` → **STRING** (text in quotes)
- `,` → **SEPARATOR**
- `10` → **INTEGER** (number, no quotes)

**Quotes vs No Quotes (CRITICAL):**
```python
# WITH QUOTES = Text/String
"max_depth"  → The word "max_depth"
"10"         → The text "10"

# WITHOUT QUOTES = Variable/Number
max_depth    → Look for variable named max_depth
10           → The number 10
```

**Example showing the difference:**
```python
# This logs the TEXT "max_depth" with NUMBER 10
mlflow.log_param("max_depth", 10)

# This would try to find a VARIABLE named max_depth
max_depth = 5
mlflow.log_param("my_param", max_depth)  # Logs value 5
```

**Line 19: Get Run ID**
```python
    run_id = mlflow.active_run().info.run_id
```

**What each part IS:**
- `run_id` → **VARIABLE**
- `=` → **ASSIGNMENT**
- `mlflow.active_run()` → **FUNCTION CALL** (returns run object)
- `.info` → **ATTRIBUTE ACCESS** (get info property)
- `.run_id` → **ATTRIBUTE ACCESS** (get run_id property)

**Chained dot notation (like walking through rooms):**
```
mlflow.active_run().info.run_id
  ↓            ↓       ↓      ↓
Module    Function  Object Property
  └─→ Go to mlflow module
          └─→ Call active_run() function
                  └─→ Access info property of result
                          └─→ Access run_id property of info
```

**Visual representation:**
```
mlflow (module)
  └── active_run() → Returns RunObject
                         └── info → Returns InfoObject
                                      └── run_id → "abc123"
```

**Line 22-23: Register Model**
```python
model_uri = f"runs:/{run_id}/model"
```

**What F-STRING means:**
```python
# Regular string - static
"runs:/abc123/model"

# F-string - dynamic (notice the 'f' before quote)
f"runs:/{run_id}/model"
#↑       ↑       ↑
#f      curly    variable
#prefix braces   name

# The {run_id} gets REPLACED with variable value
```

**Step-by-step substitution:**
```python
run_id = "abc123def456"

# Python sees:
f"runs:/{run_id}/model"

# Python thinks:
# "Okay, I need to replace {run_id} with its value"

# Python creates:
"runs:/abc123def456/model"

# This final string goes into model_uri variable
```

**Why we use f-strings:**
```python
# OLD WAY (ugly):
model_uri = "runs:/" + run_id + "/model"

# F-STRING WAY (clean):
model_uri = f"runs:/{run_id}/model"

# MUCH easier to read and write!
```

---

## Enterprise Components (From Transcript)

### ACE (Enterprise Platform)

**What is ACE?**
- **Type**: Enterprise platform (specific to their organization)
- **Purpose**: Centralized environment for AI development
- **Components**: Project management, deployment, access control

**From the transcript, ACE provides:**
- Project namespaces (isolated environments for teams)
- AI product registration (onboarding ML products)
- Integration with MLflow/Databricks
- Deployment to Kubernetes
- Access control (owner, developer roles)

**How ACE fits in:**
```
Developer Workspace (Databricks)
        ↓
    MLflow Tracking
        ↓
   ACE Platform ← Centralized governance
        ↓
  AI-Mart Registry ← Model storage
        ↓
  Production (Kubernetes) ← Deployment
```

### AI-Mart (Model Registry)

**What is AI-Mart?**
- **Type**: Enterprise model registry (their organization's system)
- **Purpose**: Centralized, auditable model storage
- **Think of it as**: Enterprise version of MLflow Registry

**Why they built AI-Mart (from transcript):**

1. **Audit Requirements**: Models must be stored longer than their production lifetime
2. **Compliance**: STLT compliance (models can't be mutated after registration)
3. **Centralization**: Single point for MRMC validation
4. **Evidence**: Keep all evidence for model approval

**AI-Mart vs MLflow Registry:**
```
┌─────────────────────────────────────────────────┐
│            MLflow Registry                      │
│  - Stores models                                │
│  - Versioning                                   │
│  - Staging/Production                           │
└─────────────────────────────────────────────────┘
                    ↓ Enhanced by
┌─────────────────────────────────────────────────┐
│            AI-Mart                              │
│  - All MLflow features                          │
│  + Long-term audit storage                      │
│  + Immutable (can't change after registration)  │
│  + Enterprise governance                        │
│  + MRMC validation integration                  │
└─────────────────────────────────────────────────┘
```

### AIPROD API (The Bridge)

**What is AIPROD API?**
- **Type**: Python library/package
- **Purpose**: Interface to interact with AI-Mart
- **Analogy**: Like MLflow's API, but for their enterprise system

**From transcript - how to use:**
```python
# 1. Add dependency in your project
# In pyproject.toml or requirements.txt:
aiprod-api==1.2.3

# 2. Import in your code
from aiprod_api import register_model, create_experiment

# 3. Use instead of direct MLflow calls
experiment_id = create_experiment("my_experiment")
```

**Why they created AIPROD API:**
- Direct MLflow registration wouldn't meet compliance
- Need to register as NPTA (non-personal technical account)
- Ensures models are immutable after registration
- Adds enterprise-specific metadata

### Plugin (Convenience Tool)

**What is the Plugin?**
- **Type**: Pre-built code package
- **Purpose**: Makes it easy to work with AI-Mart
- **Location**: Provided by their platform team

**From transcript:**
> "We will add this information for the plugin into an email"

**What the plugin does:**
```python
# WITHOUT plugin:
# - Manually create experiments via API
# - Manually construct model URIs
# - Handle authentication yourself
# - Remember all the endpoints

# WITH plugin:
from hackathon_plugin import AIModelHelper

helper = AIModelHelper()
helper.create_experiment("my_exp")  # Easier!
helper.register_model(run_id, "my_model")  # Simpler!
```

### Swagger Endpoints (Alternative)

**What is Swagger?**
- **Type**: API documentation standard
- **Purpose**: Shows all available API endpoints
- **Format**: Interactive web interface

**From transcript:**
> "We also have the swagger for the endpoints... in case anybody doesn't like the plugin"

**What Swagger provides:**
```
Swagger UI (https://api.company.com/docs)

┌─────────────────────────────────────────────────┐
│ POST /experiments/create                        │
│ GET  /experiments/{id}                          │
│ POST /models/register                           │
│ GET  /models/{name}/versions                    │
└─────────────────────────────────────────────────┘

Each endpoint shows:
  - Required parameters
  - Example request
  - Example response
  - Try it out button (test directly)
```

### MRMC (Model Review)

**What is MRMC?**
- **Type**: Organizational process
- **Purpose**: Model Risk Management Committee validation
- **When**: Before deploying models to production

**From transcript:**
> "facilitate your endeavor of making your case with MRMC"

**What MRMC checks:**
- Is the model accurate?
- Is it safe to use?
- Is there bias?
- What are the risks?
- Is documentation complete?

**How MLflow helps MRMC:**
```
Model Registered in AI-Mart
├── All experiments tracked
├── Parameters logged
├── Metrics recorded
├── Artifacts saved
├── Code version linked
└── Plots and charts attached

→ MRMC can review EVERYTHING
→ Makes approval much easier
```

---

## Deployment Concepts

### From Model to Production

**The Journey:**
```
1. Development
   └── Laptop/Databricks notebook

2. Experimentation
   └── MLflow tracking

3. Registration
   └── AI-Mart model registry

4. Staging
   └── Test environment

5. Production
   └── Kubernetes cluster serving predictions
```

### ML Server (From Transcript)

**What is ML Server?**
- **Type**: Runtime environment for serving models
- **Purpose**: Loads model and exposes API for predictions
- **How it works**: Wraps your model in a web service

**From transcript code:**
```bash
# Start the ML server
mlserver start /path/to/model/settings
```

**What this command does:**
1. `mlserver` → The ML Server program
2. `start` → Command to start the server
3. `/path/to/model/settings` → Where to find model configuration

**What happens:**
```
1. ML Server reads model settings JSON file
2. Downloads model artifacts from registry
3. Loads model into memory
4. Starts web server (usually on localhost:8080)
5. Creates API endpoints for predictions
```

**Architecture:**
```
┌───────────────────────────────────────────┐
│         ML Server                         │
├───────────────────────────────────────────┤
│                                           │
│  HTTP API (port 8080)                     │
│    ↓                                      │
│  /predict endpoint                        │
│    ↓                                      │
│  Load Model from Registry                 │
│    ↓                                      │
│  Run Inference                            │
│    ↓                                      │
│  Return Predictions                       │
│                                           │
└───────────────────────────────────────────┘
```

### Localhost (What Does It Mean?)

**What is localhost?**
- **Definition**: Your own computer (refers to itself)
- **IP Address**: 127.0.0.1
- **Purpose**: Test services on your machine before deploying

**When you see `localhost:8080`:**
```
localhost → Your computer
:         → Port separator
8080      → Port number (like apartment number)
```

**Analogy:**
```
localhost = Your house
8080 = Room number in your house

localhost:8080 = "Look in room 8080 of my house"
```

### Swagger UI for Model

**From transcript:**
> "you can come to your localhost and look for that model... here you can find the swagger"

**What you see:**
```
Browser: http://localhost:8080/docs

┌─────────────────────────────────────────────────┐
│         Model API Documentation                 │
├─────────────────────────────────────────────────┤
│                                                 │
│  POST /v2/models/my_model/infer                 │
│                                                 │
│  Request Body:                                  │
│  {                                              │
│    "inputs": [                                  │
│      {"name": "feature1", "data": [1, 2, 3]}   │
│    ]                                            │
│  }                                              │
│                                                 │
│  [Try it out] button                            │
│                                                 │
└─────────────────────────────────────────────────┘
```

### Kubernetes/AKS Deployment

**From transcript:**
> "pass from tool deployment into a tool like your Kubernetes cluster"

**What is Kubernetes (K8s)?**
- **Type**: Container orchestration platform
- **Purpose**: Manage many containers across many servers
- **Think of it as**: Manager that keeps your app running

**What is AKS?**
- **Type**: Azure Kubernetes Service (Microsoft's managed Kubernetes)
- **Purpose**: Kubernetes without managing infrastructure yourself
- **Benefit**: Azure handles the hard parts

**Deployment flow:**
```
1. Model in Registry
   ↓
2. Create Docker Container
   ├── Model files
   ├── ML Server
   └── Dependencies
   ↓
3. Push to Container Registry
   ↓
4. Deploy to Kubernetes
   ├── Creates 3 replicas (copies)
   ├── Load balancer distributes requests
   └── Auto-scaling based on load
   ↓
5. Production Service
   └── https://api.company.com/models/predict
```

---

## Practical Example: Complete Hackathon Workflow

### Scenario
You're in a hackathon, building a fraud detection model. Your team is "Team Awesome".

### Step 1: Setup (One-time, Team Lead Does This)

**In ACE Platform:**
1. Navigate to ACE web interface
2. Click "Onboard AI Product"
3. Enter product name: "Team Awesome Fraud Detector"
4. Click "Create"
5. Share project ID with team

**Everyone on team can now see the project.**

### Step 2: First Team Member Experiments

**Databricks Notebook:**
```python
# Cell 1: Setup
import mlflow
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Set the team's experiment
mlflow.set_experiment("/team-awesome/fraud-detection-v1")

# Cell 2: Load data
df = pd.read_csv("/data/transactions.csv")
X = df.drop('is_fraud', axis=1)
y = df['is_fraud']
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Cell 3: First attempt - Random Forest
with mlflow.start_run(run_name="rf_attempt_1"):
    # Train
    model = RandomForestClassifier(n_estimators=100, max_depth=10)
    model.fit(X_train, y_train)

    # Evaluate
    accuracy = model.score(X_test, y_test)
    precision = precision_score(y_test, model.predict(X_test))

    # Log everything
    mlflow.log_param("algorithm", "RandomForest")
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("max_depth", 10)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("precision", precision)

    # Save model
    mlflow.sklearn.log_model(model, "model")

    print(f"Accuracy: {accuracy:.2f}")
    print(f"Run ID: {mlflow.active_run().info.run_id}")
```

**Output:**
```
Accuracy: 0.87
Run ID: abc123def456
MLflow UI: https://databricks.company.com/#/experiments/42/runs/abc123def456
```

### Step 3: Second Team Member Experiments

**Different notebook, same experiment:**
```python
# Setup (same experiment name)
mlflow.set_experiment("/team-awesome/fraud-detection-v1")

# Try XGBoost instead
with mlflow.start_run(run_name="xgb_attempt_1"):
    model = XGBClassifier(n_estimators=200, learning_rate=0.1)
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)

    mlflow.log_param("algorithm", "XGBoost")
    mlflow.log_param("n_estimators", 200)
    mlflow.log_param("learning_rate", 0.1)
    mlflow.log_metric("accuracy", accuracy)

    mlflow.sklearn.log_model(model, "model")
```

**Both runs appear in same experiment!**

### Step 4: Compare Results

**MLflow UI shows:**
```
Experiment: /team-awesome/fraud-detection-v1

┌────────────────────────────────────────────────────────┐
│ Run Name     │ Algorithm  │ Accuracy │ User    │ Date  │
├────────────────────────────────────────────────────────┤
│ rf_attempt_1 │ RandomForest│ 0.87    │ Alice   │ Nov 7 │
│ xgb_attempt_1│ XGBoost     │ 0.92    │ Bob     │ Nov 7 │
└────────────────────────────────────────────────────────┘
```

**Team decides: XGBoost is better!**

### Step 5: Register Model (Using AIPROD API)

```python
from aiprod_api import register_model

# XGBoost run ID
best_run_id = "xyz789abc123"  # Bob's run

# Register
model_info = register_model(
    run_id=best_run_id,
    model_name="team_awesome_fraud_detector",
    description="XGBoost model with 92% accuracy"
)

print(f"Model registered: {model_info}")
```

**What happens behind the scenes:**
1. AIPROD API validates the run exists
2. Creates entry in AI-Mart registry
3. Copies model artifacts to long-term storage
4. Marks experiment as "locked" (immutable)
5. Returns model version info

### Step 6: Cannot Register to Same Experiment Again

**From transcript:**
> "once you have registered a model, that experiment will be locked"

**Team tries:**
```python
# Try to add another run to locked experiment
mlflow.set_experiment("/team-awesome/fraud-detection-v1")

with mlflow.start_run():  # ERROR!
    # This will FAIL because experiment is locked after registration
```

**Solution:**
```python
# Create NEW experiment for next iteration
mlflow.set_experiment("/team-awesome/fraud-detection-v2")

with mlflow.start_run():  # Works!
    # Continue experimenting
```

### Step 7: Test Model Locally

```python
# Install dependencies
# pip install aiprod-api mlserver

# Create model-settings.json
{
  "name": "team_awesome_fraud_detector",
  "version": "1",
  "implementation": "mlserver_sklearn.SKLearnModel",
  "parameters": {
    "uri": "models:/team_awesome_fraud_detector/1"
  }
}
```

**Start server:**
```bash
# Terminal
mlserver start .
```

**Output:**
```
INFO: Started server on http://localhost:8080
INFO: Loaded model: team_awesome_fraud_detector
INFO: Ready to serve predictions
```

**Test it:**
```python
import requests

# Prepare test data
data = {
    "inputs": [
        {
            "name": "transactions",
            "data": [[100.0, 1, 0, 1, 50.0]]  # One transaction
        }
    ]
}

# Send prediction request
response = requests.post(
    "http://localhost:8080/v2/models/team_awesome_fraud_detector/infer",
    json=data
)

print(response.json())
# Output: {"predictions": [0]}  # Not fraud
```

### Step 8: Deploy to Production (If Selected)

**From transcript:**
> "one possible extension of the hackathon may be for the selected few... to actually do a demo run on how to deploy"

**Deployment steps (handled by platform team):**
```bash
# 1. Build Docker image
docker build -t fraud-detector:v1 .

# 2. Push to Azure Container Registry
az acr login --name myregistry
docker push myregistry.azurecr.io/fraud-detector:v1

# 3. Deploy to AKS
kubectl apply -f deployment.yaml
```

**deployment.yaml:**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fraud-detector
spec:
  replicas: 3  # Run 3 copies
  template:
    spec:
      containers:
      - name: model-server
        image: myregistry.azurecr.io/fraud-detector:v1
        ports:
        - containerPort: 8080
```

**Result:**
```
Production endpoint:
https://api.company.com/models/fraud-detector/predict

Available 24/7, auto-scaling, load-balanced!
```

---

## Summary: What You've Learned

### Core Concepts
1. **MLflow** = Platform for managing ML lifecycle
2. **Experiment** = Container for multiple training attempts
3. **Run** = Single training attempt with parameters/metrics
4. **Model Registry** = Storage for trained models with versioning
5. **Databricks** = Cloud platform with MLflow built-in

### Enterprise Additions
6. **ACE** = Enterprise platform for governance
7. **AI-Mart** = Enterprise model registry (auditable, immutable)
8. **AIPROD API** = Library to interact with AI-Mart
9. **MRMC** = Model review process before production

### Deployment
10. **ML Server** = Wraps model in web service
11. **Kubernetes/AKS** = Production deployment platform
12. **Localhost** = Your own computer for testing

### Key Workflows
- **Experiment → Compare → Register → Stage → Production**
- **Team collaboration via shared experiments**
- **Immutable registration after model approval**
- **Evidence collection for audits**

---

## Connection to Your IntelligentScan Project

### How This Applies to IntelligentScan

Your IntelligentScan MCP server could benefit from MLflow:

```python
# In intelligentscan/server/main.py

import mlflow

@mcp.tool()
async def scan_vulnerabilities(repo_path: str):
    """Scan for vulnerabilities and track experiments"""

    # Set up MLflow
    mlflow.set_experiment("vulnerability_scanning")

    with mlflow.start_run():
        # Run scan
        scanner = VulnerabilityScanner()
        results = await scanner.scan(repo_path)

        # Log metrics
        mlflow.log_metric("vulnerabilities_found", len(results))
        mlflow.log_metric("critical_count", results.count_critical())

        # Log parameters
        mlflow.log_param("repo_path", repo_path)
        mlflow.log_param("scanner_version", "1.0.0")

        # Log artifacts (reports)
        report_path = generate_report(results)
        mlflow.log_artifact(report_path)

        return results
```

**Benefits:**
- Track how scanning improves over time
- Compare different scanning strategies
- Keep audit trail of all scans
- Register "best" scanning configurations as models

---

## Next Steps for Learning

1. **Install MLflow locally:**
   ```bash
   pip install mlflow
   mlflow ui  # Start UI at localhost:5000
   ```

2. **Run simple experiment:**
   - Create experiment
   - Log parameters
   - Log metrics
   - View in UI

3. **Try model registration:**
   - Register a simple model
   - Transition through stages
   - Load model back

4. **Read official docs:**
   - https://mlflow.org/docs/latest/index.html
   - Focus on Tracking and Model Registry sections

5. **Practice with your IntelligentScan project:**
   - Add MLflow tracking to scanners
   - Log scan results as experiments
   - Compare different scanning approaches

---

## Questions to Consider

As you learn more, think about:

1. **How would you track IntelligentScan experiments?**
   - What parameters to log?
   - What metrics matter?
   - What artifacts to save?

2. **How could model registry help IntelligentScan?**
   - Version control for scanning rules?
   - Track different rule configurations?
   - Deploy rule updates systematically?

3. **How would you deploy IntelligentScan at scale?**
   - Use MLflow to track performance?
   - A/B test different scanning approaches?
   - Automatically deploy best configurations?

---

**Document Status**: Complete explanation of MLflow and MLOps concepts from hackathon call
**Created**: 2025-11-07
**Purpose**: Help understand ML lifecycle management with extreme detail
**Next**: Practice with hands-on MLflow experiments
