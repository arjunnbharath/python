# Python Virtual Environments

A **virtual environment** in Python is an isolated environment that allows you to install and manage packages separately for each project.

## Why Use Virtual Environments?

Different Python projects may require different versions of the same package.

For example:

```text
Project A → Django 4
Project B → Django 5
```

Installing everything globally can cause dependency conflicts.

A virtual environment keeps each project's dependencies isolated.

```text
Python Installation
│
├── Project A
│   └── .venv
│       └── Project A packages
│
└── Project B
    └── .venv
        └── Project B packages
```

---

## 1. Create a Virtual Environment

First, create a project folder:

```bash
mkdir my_project
cd my_project
```

Create a virtual environment:

```bash
python -m venv .venv
```

Here:

- `python` → runs Python
- `-m venv` → uses Python's built-in virtual environment module
- `.venv` → name of the environment

You can technically use another name, but `.venv` is a common convention.

---

## 2. Activate the Virtual Environment

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

After activation, you should see something similar to:

```text
(.venv) C:\Users\Arjun\my_project>
```

The `(.venv)` tells you that the virtual environment is active.

---

## 3. Install Packages

Once the environment is activated, install packages normally:

```bash
python -m pip install requests
```

For example:

```bash
python -m pip install pandas
```

You can install multiple packages:

```bash
python -m pip install pandas numpy requests
```

These packages will be installed inside your virtual environment rather than globally.

---

## 4. Check Installed Packages

Use:

```bash
python -m pip list
```

Example:

```text
Package    Version
---------- -------
numpy      2.x.x
pandas     2.x.x
requests   2.x.x
```

---

## 5. Create a Python File

Create:

```text
main.py
```

Example:

```python
import requests

print("Virtual environment is working!")
```

Run it:

```bash
python main.py
```

---

## 6. Save Project Dependencies

You can create a `requirements.txt` file containing the packages installed in your environment:

```bash
python -m pip freeze > requirements.txt
```

Example:

```text
numpy==2.x.x
pandas==2.x.x
requests==2.x.x
```

This file allows someone else to install the same dependencies.

---

## 7. Install Dependencies from requirements.txt

If you clone/download a project that contains `requirements.txt`, create and activate a virtual environment first:

```bash
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

Then install the dependencies:

```bash
python -m pip install -r requirements.txt
```

---

## 8. Deactivate the Environment

When you're finished working:

```bash
deactivate
```

The `(.venv)` will disappear from your terminal.

---

## 9. Recommended Project Structure

A simple Python project can look like this:

```text
my_project/
│
├── .venv/
│
├── main.py
│
├── requirements.txt
│
└── .gitignore
```

### Important

Do **not** normally upload `.venv` to GitHub.

Add this to `.gitignore`:

```gitignore
.venv/
```

Instead, upload:

```text
main.py
requirements.txt
.gitignore
```

Anyone can then recreate the environment using:

```bash
python -m venv .venv
python -m pip install -r requirements.txt
```

---

## Useful Commands

| Command | Purpose |
|---|---|
| `python -m venv .venv` | Create virtual environment |
| `.venv\Scripts\activate` | Activate on Windows |
| `source .venv/bin/activate` | Activate on macOS/Linux |
| `python -m pip install package` | Install a package |
| `python -m pip list` | Show installed packages |
| `python -m pip freeze` | Show exact package versions |
| `python -m pip freeze > requirements.txt` | Save dependencies |
| `python -m pip install -r requirements.txt` | Install dependencies |
| `deactivate` | Exit virtual environment |

---

## Simple Mental Model

Think of a virtual environment like a **separate toolbox for each project**.

```text
Project A
└── .venv
    ├── pandas
    └── numpy

Project B
└── .venv
    ├── flask
    └── requests
```

The projects don't interfere with each other.

---

## Quick Workflow

For most Python projects, you'll repeatedly do:

```bash
# 1. Create project
mkdir my_project
cd my_project

# 2. Create environment
python -m venv .venv

# 3. Activate
.venv\Scripts\Activate.ps1

# 4. Install packages
python -m pip install pandas

# 5. Write your Python code
python main.py

# 6. Save dependencies
python -m pip freeze > requirements.txt

# 7. When finished
deactivate
```

## Key Takeaway

> **Virtual environments keep each Python project's dependencies isolated and prevent package/version conflicts.**

For AI/ML projects, virtual environments become especially important because projects often depend on many packages such as `numpy`, `pandas`, `torch`, `transformers`, `langchain`, and others.