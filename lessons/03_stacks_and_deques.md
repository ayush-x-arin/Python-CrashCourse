# 📘 Lesson 03: Stacks, Queues & Double-Ended Queues (collections.deque)

In backend engineering, stacks and queues are the heartbeat of asynchronous architecture:
- **Background workers & job queues**: Processing email notifications, payment jobs, or video encoding (RabbitMQ, Redis, Celery).
- **Rate limiting**: API gateways preventing spam and DDoS attacks by tracking requests per second.
- **Syntax parsers & schema validators**: Validating JSON payloads, matching HTML/XML tags, or checking bracket syntax.
- **Undo / Navigation stacks**: Browser history (Back/Forward) and database transaction rollback points.

---

## 🧠 Core Concepts Made Simple

### 1. What is a Stack? (The Cafeteria Tray Analogy)
Think of a spring-loaded stack of trays in a cafeteria:
- When clean trays are washed, they are placed on top (**Push** / `append`).
- When you take a tray, you take it from the very top (**Pop** / `pop`).
- You cannot pull out the bottom tray without causing a disaster!

This is **LIFO (Last-In, First-Out)**: The most recent item added is the first one removed.

```text
       Push (append)           Pop (pop)
            │                     ▲
            ▼                     │
         ┌─────┐               ┌─────┐
         │  C  │ ◄── Top       │     │
         ├─────┤               ├─────┤
         │  B  │               │  B  │
         ├─────┤               ├─────┤
         │  A  │               │  A  │
         └─────┘               └─────┘
```

#### Common Stack Use Case: Syntax Bracket Matching
When matching brackets like `"{[()]}"`:
1. Whenever you see an open bracket `(`, `[`, `{`, **push** it onto the stack.
2. Whenever you see a closing bracket `)`, `]`, `}`, look at the top of the stack. It **must** match the opening type! If it does, **pop** it off. If it doesn't match or the stack is empty, the string is invalid.
3. At the end, if the stack is completely empty, all opened brackets were properly closed!

---

### 2. What is a Queue? (The Coffee Shop Line)
Think of customers waiting in line at a coffee shop:
- New customers arrive and join at the back of the line (**Enqueue** / `append`).
- The barista serves the customer at the front of the line (**Dequeue** / `popleft`).

This is **FIFO (First-In, First-Out)**: The first customer to arrive is the first customer served.

```text
 Arrival (append)                                 Departure (popleft)
───────────────────► [ Task 3 ] [ Task 2 ] [ Task 1 ] ─────────────────►
                     (Back/Tail)          (Front/Head)
```

---

### 3. The Dangerous Rookie Trap: `list.pop(0)`
Many beginners use standard Python lists for queues:

```python
# ⚠️ DANGEROUS IN PRODUCTION:
queue = []
queue.append("task_1")
queue.pop(0)  # O(N) SLOW!
```

#### Why is `list.pop(0)` Terrible?
Remember that lists are contiguous memory blocks. When you remove index `0`, **every single remaining element must shift one position left in RAM**:

```text
Index:      0       1       2       3
Initial:  [ 50 ]  [ 60 ]  [ 70 ]  [ 80 ]
           └── Remove index 0
Shift:     [ 60 ] ◄─ [ 70 ] ◄─ [ 80 ]
```

If your queue has 50,000 tasks, every single `pop(0)` performs 50,000 memory moves. Calling it 50,000 times results in **2.5 billion memory operations** $\rightarrow$ your backend server hangs!

---

### 4. The Hero: `collections.deque` (Double-Ended Queue)
Python's built-in `collections.deque` is implemented as linked blocks of memory:
- Adding or removing from **either end** is instantaneous ($O(1)$)!

```python
from collections import deque

q = deque()
q.append("task1")        # Add to right/back: O(1)
q.append("task2")
served = q.popleft()     # Remove from left/front: O(1) INSTANT!
```

| Operation | Regular `list` | `collections.deque` |
|---|---|---|
| Append to right (`append`) | $O(1)$ | $O(1)$ |
| Pop from right (`pop`) | $O(1)$ | $O(1)$ |
| Append to left (`appendleft`) | $O(N)$ (Slow!) | **$O(1)$ (Instant)** |
| Pop from left (`popleft`) | $O(N)$ (Devastating!) | **$O(1)$ (Instant)** |

---

## 🎯 Your Assignment: `practice/03_stacks_and_deques.py`

Open [practice/03_stacks_and_deques.py](file:///Users/akshay/Codebase/Python-Crash-Course/practice/03_stacks_and_deques.py) and implement:

### Task 1: `is_valid_brackets(s: str) -> bool`
- **Goal**: Check if a string containing `'('`, `')'`, `'{'`, `'}'`, `'['`, `']'` has valid bracket pairs.
- **Rules**:
  1. Open brackets must be closed by the same type of bracket.
  2. Open brackets must be closed in the correct order.
- **Examples**:
  - `"()[]{}"` $\rightarrow$ `True`
  - `"{[()]}"` $\rightarrow$ `True`
  - `"(]"` $\rightarrow$ `False` (mismatched closing bracket)
  - `"([)]"` $\rightarrow$ `False` (wrong ordering)
  - `")("` $\rightarrow$ `False` (closed before open)

---

### Task 2: `class SlidingWindowRateLimiter`
Build a real-world API rate limiter class using `collections.deque`!

- **The Bouncer Metaphor**:
  - Imagine a club bouncer with a rule: *"No more than 3 requests every 10 seconds per user."*
  - The bouncer keeps a notepad for each user containing arrival timestamps.
  - When user `"u1"` asks to make a request at time `current_time = 12.0`:
    1. Look up user `"u1"`'s deque of previous timestamps.
    2. Evict any timestamp older than `12.0 - 10.0 = 2.0` using `timestamps.popleft()`.
    3. If fewer than 3 timestamps remain, record `12.0` and return `True` (allow request).
    4. If 3 or more timestamps remain, return `False` (rate limited!).

- **Implementation Details**:
  - `__init__(self, max_requests: int, window_seconds: float)`:
    - Stores `max_requests` and `window_seconds`.
    - Initializes a dictionary `self.user_requests: Dict[str, deque] = {}`.
  - `allow_request(self, user_id: str, current_time: float) -> bool`:
    - Evicts expired timestamps with `popleft()`.
    - Returns `True` (and appends `current_time`) if under limit; otherwise returns `False`.

---

### Task 3: `simplify_path(path: str) -> str` (Unix & URL Canonicalizer)
- **Goal**: Web API clients often send messy URL paths or file upload paths like `/home//foo/../bar/`. Canonicalize it into `/home/bar`.
- **How to Think About It**:
  1. Split the string by `/`: `path.split("/")`.
  2. Walk through the tokens:
     - `""` or `"."` (current directory): Ignore, do nothing.
     - `".."` (go up one directory): Pop the top directory off the stack (if stack is not empty).
     - Any actual folder name (e.g. `"home"`, `"bar"`): Push onto the stack.
  3. Join the stack elements with `"/"`: `"/" + "/".join(stack)`.
- **Examples**:
  - `"/home/"` $\rightarrow$ `"/home"`
  - `"/../"` $\rightarrow$ `"/"` (cannot go higher than root)
  - `"/home//foo/"` $\rightarrow$ `"/home/foo"`
  - `"/a/./b/../../c/"` $\rightarrow$ `"/c"`

---

## 🚀 How to Test Your Code
Once implemented in `practice/03_stacks_and_deques.py`:
```bash
python3 test_runner.py 3
```
Or tell me in chat: **"Test Lesson 03"**!

