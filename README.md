# 🚀 Python for Backend Development: Interactive Learning Roadmap

Welcome! This course is designed to take you from foundational data structures to production-grade backend logic, API patterns, and framework readiness.

---

## 💻 Environment Setup (Windows, macOS, Linux)

Before writing any code, set up your Python environment. Python **3.10 or higher** is recommended.

### 1. Verify or Install Python

<details>
<summary><b>🍎 macOS</b></summary>

1. Check your Python version in Terminal:
   ```bash
   python3 --version
   ```
2. If Python is not installed or is older than 3.10, install it via [Homebrew](https://brew.sh):
   ```bash
   brew install python
   ```
</details>

<details>
<summary><b>🐧 Linux (Ubuntu / Debian / Fedora / Arch)</b></summary>

1. Check your Python version:
   ```bash
   python3 --version
   ```
2. If needed, install Python and virtual environment support:
   - **Ubuntu/Debian**:
     ```bash
     sudo apt update
     sudo apt install -y python3 python3-venv python3-pip
     ```
   - **Fedora**:
     ```bash
     sudo dnf install -y python3 python3-pip
     ```
   - **Arch Linux**:
     ```bash
     sudo pacman -S python python-pip
     ```
</details>

<details>
<summary><b>🪟 Windows</b></summary>

1. Check your Python version in PowerShell or Command Prompt:
   ```powershell
   python --version
   ```
2. If Python is not installed:
   - **Option A (Winget)**:
     ```powershell
     winget install Python.Python.3.12
     ```
   - **Option B (Official Installer)**:
     Download from [python.org](https://www.python.org/downloads/).
     > [!IMPORTANT]
     > During installation, **check the box: "Add python.exe to PATH"** before clicking Install.
</details>

---

### 2. Create & Activate a Virtual Environment

A virtual environment (`venv`) keeps dependencies isolated so they don't conflict with system packages.

Navigate to the project root directory in your terminal:

#### On macOS & Linux:
```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate
```

*(Your terminal prompt should now show `(venv)` at the beginning).*

#### On Windows:
```powershell
# In PowerShell:
python -m venv venv
.\venv\Scripts\Activate.ps1
```

> [!TIP]
> **Windows PowerShell Execution Policy Error?**
> If PowerShell says script execution is disabled, run:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```
> Or use Command Prompt (`cmd.exe`):
> ```cmd
> .\venv\Scripts\activate.bat
> ```

---

### 3. Install Optional Testing Tools

This course relies primarily on Python's built-in standard library (`unittest`, `collections`, `asyncio`, `enum`), meaning **no external packages are strictly required**!

However, if you enjoy using `pytest`:
```bash
pip install pytest
```

---

## 🧭 How to Follow This Tutorial

Each lesson is structured for progressive, hands-on learning:

```text
Python-Crash-Course/
├── lessons/          # 📖 Theory, visual intuition & problem statements
├── practice/         # ✍️ Your exercise workspace (implement your code here)
├── tests/            # 🧪 Automated unit tests validating your solutions
└── test_runner.py    # ⚡ Command-line test launcher
```

### The 4-Step Learning Workflow:

1. **Read the Theory**:
   - Open the lesson file in `lessons/` (e.g., [Lesson 01](file:///Users/akshay/Codebase/Python-Crash-Course/lessons/01_lists_and_two_pointers.md)).
   - Read the beginner-friendly visual models, real-world backend use-cases, and task requirements.

2. **Code in the Practice File**:
   - Open the matching file in `practice/` (e.g., [practice/01_lists.py](file:///Users/akshay/Codebase/Python-Crash-Course/practice/01_lists.py)).
   - Each function has a docstring with requirements and edge cases.
   - Implement your solution inside the function bodies.
   - You can run the file directly to run the local `if __name__ == "__main__":` sanity tests:
     ```bash
     python practice/01_lists.py       # (Windows)
     python3 practice/01_lists.py      # (macOS/Linux)
     ```

3. **Run the Automated Test Suite**:
   - Run tests for a specific lesson:
     ```bash
     # Test Lesson 01
     python3 test_runner.py 1          # (or 'python test_runner.py 1' on Windows)

     # Test Lesson 02
     python3 test_runner.py 2

     # Test All Lessons
     python3 test_runner.py all
     ```
   - *Alternative*: You can also run tests with `unittest` or `pytest`:
     ```bash
     python3 -m unittest discover tests
     pytest
     ```
   - *Interactive Chat*: If working with Antigravity pair programming, simply ask:
     > *"Test my code for Lesson 01"*

4. **Review & Advance**:
   - If tests fail, inspect the assertion traceback, refine your logic, and re-run.
   - When all tests pass, celebrate and move on to the next lesson!

---

## 🗺️ Course Syllabus

### Part 1: Universal Backend Python (The Foundation)
- [x] **[Lesson 01: Lists, Slices & Two Pointers](file:///Users/akshay/Codebase/Python-Crash-Course/lessons/01_lists_and_two_pointers.md)**
  - Memory layout, why inserting at 0 is slow, slicing mechanics, `enumerate`/`zip`, two-pointer technique, and API pagination controllers.
- [x] **[Lesson 02: Dictionaries, Sets & Frequency Indexing](file:///Users/akshay/Codebase/Python-Crash-Course/lessons/02_dicts_and_hashmaps.md)**
  - $O(1)$ Hash table lookups, hashability, `defaultdict`, safe `.get()`, set algebra for permissions, and in-memory database indexing.
- [x] **[Lesson 03: Stacks, Queues & collections.deque](file:///Users/akshay/Codebase/Python-Crash-Course/lessons/03_stacks_and_deques.md)**
  - The $O(N)$ danger of `list.pop(0)`, double-ended queues, sliding-window rate limiters, syntax bracket validation, and Unix path canonicalization.
- [x] **[Lesson 04: The Universal Backend Toolkit (Java/Spring Boot $\rightarrow$ Python)](file:///Users/akshay/Codebase/Python-Crash-Course/lessons/04_universal_backend_essentials.md)**
  - Enums, custom exceptions, list & dict comprehensions (Stream API equivalents), decorators, and async/await non-blocking concurrency.

---

### Part 2: Web Framework Mastery (FastAPI & Beyond)
- 🚀 **Next Milestone**: Building production REST APIs with **FastAPI** + **Pydantic** + **SQLAlchemy** (Async routes, Dependency Injection, JWT Auth, Database CRUD)!

👉 **Get started now with [Lesson 01: Lists & Two Pointers](file:///Users/akshay/Codebase/Python-Crash-Course/lessons/01_lists_and_two_pointers.md)!**
