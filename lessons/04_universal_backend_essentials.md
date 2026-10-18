# 📘 Lesson 04: Universal Python Backend Toolkit
### *(Mastering Python Backend Essentials: Enums, Comprehensions, Decorators & Async)*

Whether you're coming from Java, JavaScript, or are newer to programming, modern backend frameworks (like **FastAPI** and **Django**) rely on 5 core Python patterns.

Once you master these 5 patterns, you can read and write production backend code in any Python framework!

---

## 🧠 Core Concepts Made Simple

### 1. Enums (The Fixed Menu Analogy)
Imagine a restaurant menu that only offers: `"BURGER"`, `"PIZZA"`, and `"SALAD"`.
- If a customer asks for `"SPACESHIP"`, the waiter rejects it immediately.

#### Why not just use plain strings like `"admin"`?
If you use raw strings, typos like `"admn"` or `"ADMIN"` will silently pass through your code, creating dangerous security bugs!
- An **`Enum`** (Enumeration) restricts a variable to a strict, predefined set of valid options.

```python
from enum import Enum

# Inheriting from (str, Enum) makes it both a valid string AND an Enum!
class UserRole(str, Enum):
    ADMIN = "admin"
    EDITOR = "editor"
    VIEWER = "viewer"

# Usage:
current_role = UserRole.ADMIN

if current_role == UserRole.ADMIN:
    print("Welcome, Administrator!")
```

---

### 2. Custom Exceptions (The Emergency Brake)
When something goes wrong in backend code (e.g., wrong password or unauthorized role):
- You don't just return `False` or `-1` and hope callers notice.
- You **`raise` an Exception** (like pulling the emergency brake on a train). It halts execution immediately and lets your API middleware catch it to return an HTTP `401 Unauthorized` or `403 Forbidden` response.

```python
class AuthenticationError(Exception):
    """Raised when a user lacks required permissions."""
    pass

def verify_access(role: UserRole):
    if role != UserRole.ADMIN:
        # Halt execution immediately!
        raise AuthenticationError("Only administrators are allowed!")
    return True
```

---

### 3. List & Dict Comprehensions (The 1-Line Recipe Formula)
In many languages, filtering and transforming a list requires 5 lines of boilerplate:

```python
# ❌ Verbose loop:
completed_orders = []
for order in orders:
    if order["status"] == "COMPLETED":
        completed_orders.append(order["id"])
```

Python provides **Comprehensions**—a clean, 1-line mathematical recipe:

#### The Mental Formula:
```text
[  WHAT_YOU_WANT   for   ITEM   in   COLLECTION   if   CONDITION  ]
```

```python
# 1. List Comprehension:
completed_ids = [order["id"] for order in orders if order["status"] == "COMPLETED"]

# 2. Dict Comprehension: { KEY : VALUE for ITEM in COLLECTION if CONDITION }
# Map order_id -> price with 18% tax:
order_prices = {
    order["id"]: round(order["amount"] * 1.18, 2)
    for order in orders
    if order["status"] == "COMPLETED"
}
```

---

### 4. Decorators (The Gift Wrapping Analogy)
Imagine you have a gift box (your function, e.g. `save_to_database()`).
- A **Decorator** is festive wrapping paper: it wraps around the function without changing what is inside.
- It can execute code **before** your function runs (like checking authentication), or **after** (like logging time), or **around** it (like catching unexpected errors!).

```text
Incoming Call ───► [ Decorator Wrapper: try ... ]
                         │
                         ▼
                   [ Original Function: func(*args) ]
                         │
                         ▼
Outgoing Result ◄─ [ Decorator Wrapper: except Error ... return {"error": msg} ]
```

```python
from functools import wraps

def safe_api_endpoint(func):
    """Wraps an API function and converts any crash into a clean JSON error response."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            return {"status": "error", "message": str(err)}
    return wrapper

# Now attach it with the @ symbol:
@safe_api_endpoint
def get_user_profile(user_id):
    if user_id == "unknown":
        raise ValueError("User not found!")
    return {"id": user_id, "name": "Alice"}

# If get_user_profile crashes, it won't crash your server!
# It safely returns: {"status": "error", "message": "User not found!"}
```

---

### 5. Async / Await (The Restaurant Buzzer)
Why is Python's **FastAPI** so fast? Because of `async` and `await`!

#### The Coffee Shop Analogy:
- **Synchronous (Blocking)**: The barista takes customer 1's order, starts the espresso machine, and **stands completely frozen for 3 minutes** waiting for the coffee, ignoring the other 50 customers waiting in line!
- **Asynchronous (Non-Blocking)**: The barista starts the espresso machine, hands customer 1 a vibrating pager/buzzer (`await`), and **immediately takes customer 2's order**! When the buzzer rings, the barista hands the coffee over.

```python
import asyncio

# 'async def' tells Python: This function can pause without freezing the whole server!
async def fetch_user_profile_async(user_id: str) -> dict:
    # 'await' tells Python: "While waiting for the database to respond, go serve other users!"
    await asyncio.sleep(0.01)  # Simulates 10ms database query
    return {"id": user_id, "active": True}
```

---

## 🎯 Your Assignment: `practice/04_universal_backend_essentials.py`

Open [practice/04_universal_backend_essentials.py](file:///Users/akshay/Codebase/Python-Crash-Course/practice/04_universal_backend_essentials.py) and implement the 4 tasks:

### Task 1: `UserRole` Enum & `AuthenticationError`
1. Define `class UserRole(str, Enum)` with values:
   - `ADMIN = "admin"`
   - `EDITOR = "editor"`
   - `VIEWER = "viewer"`
2. Define `class AuthenticationError(Exception): pass`.
3. Implement `authorize_user(user_role: UserRole, allowed_roles: list[UserRole]) -> bool`:
   - If `user_role` is in `allowed_roles`, return `True`.
   - Otherwise, `raise AuthenticationError(f"Role '{user_role.value}' is not authorized")`.

---

### Task 2: Stream-Style Comprehensions (`filter_and_transform_orders`)
- Input: List of order dictionaries:
  ```python
  orders = [
      {"id": "o1", "amount": 100.0, "status": "COMPLETED"},
      {"id": "o2", "amount": 50.0,  "status": "CANCELLED"},
      {"id": "o3", "amount": 200.0, "status": "COMPLETED"}
  ]
  ```
- Goal:
  - Filter only orders with `status == "COMPLETED"`.
  - Calculate total amount with **18% tax**: `round(amount * 1.18, 2)`.
  - Return a dictionary mapping `order_id -> taxed_amount`.
  - Example output: `{"o1": 118.0, "o3": 236.0}`.
  - Must use a Python **dict comprehension**!

---

### Task 3: API Error-Handling Decorator (`@safe_api_endpoint`)
- Write a decorator `@safe_api_endpoint` that wraps any function:
  - If the function executes successfully, return its result.
  - If any `Exception` is raised during execution, catch it and return:
    ```python
    {"status": "error", "message": str(err)}
    ```

---

### Task 4: Async Service Handler (`fetch_user_profile_async`)
- Implement `async def fetch_user_profile_async(user_id: str) -> dict`:
  - `await asyncio.sleep(0.01)` (simulates async DB query).
  - Returns `{"id": user_id, "active": True}`.

---

## 🚀 How to Test Your Code
Once implemented in `practice/04_universal_backend_essentials.py`:
```bash
python3 test_runner.py 4
```
Or tell me in chat: **"Test Lesson 04"**!

🎉 Once all 4 lessons are complete, you are fully equipped for **FastAPI & production backend development**! 🚀

