# 📘 Lesson 02: Dictionaries, Sets & Frequency Counting

In backend engineering, dictionaries (hash maps) and sets are your most critical tools. Over 80% of real-world backend tasks involve:
- Finding a user or session by ID instantly ($O(1)$).
- Caching database and API responses in key-value memory stores (Redis-style).
- Grouping relational rows (e.g. grouping orders by `customer_id`).
- Checking user permissions and role-based access control (RBAC).

---

## 🧠 Core Concepts Made Simple

### 1. What is a Dictionary? (The Coat-Check Analogy)
Imagine you go to a theatre with 10,000 guests and check your coat:
- **Searching a List ($O(N)$)**: The attendant walks down the racks checking every single coat one by one until they find yours. If your coat is at the end, it takes 10,000 checks!
- **Using a Dictionary ($O(1)$)**: The attendant gives you a numbered claim ticket (`key`). When you return, they look at your ticket number and walk straight to that exact hook (`value`). It takes 1 single step!

```text
Key (Claim Ticket)       Hash Function       Memory Location (Value)
"user_101"           ──> hash("user_101") ──> [ {"name": "Alice", "role": "admin"} ]
"user_102"           ──> hash("user_102") ──> [ {"name": "Bob",   "role": "editor"} ]
```

#### Why Must Keys Be "Hashable" (Immutable)?
A dictionary key must be something that cannot change (like a `str`, `int`, or `tuple`).
- If you were allowed to use a mutable `list` as a key, and later modified that list (`my_list.append(5)`), its hash address would change! Python would look in the wrong memory bucket and your data would be lost forever.
- That's why **strings, numbers, and tuples can be keys**, but **lists and dictionaries cannot**.

---

### 2. Safe Access: Avoid the Dreaded `KeyError`
In backend APIs, request bodies often miss optional fields. 

```python
user = {"id": 101, "name": "Alice"}

# ❌ Risky: Crashes your API server with KeyError if 'role' is missing!
role = user["role"]

# ✅ Safe: Returns None or a default fallback value without crashing
role = user.get("role", "guest")  # Returns 'guest'
```

---

### 3. Grouping Made Easy with `collections.defaultdict`
When building indexes (e.g., grouping users by role), beginners often write tedious checks:

```python
# ❌ Tedious, error-prone way:
groups = {}
for user, role in pairs:
    if role not in groups:
        groups[role] = []   # Manually initialize list
    groups[role].append(user)
```

With `collections.defaultdict`, Python initializes the list automatically on first access:

```python
from collections import defaultdict

# Tell defaultdict: "If a key doesn't exist yet, automatically start an empty list []"
groups = defaultdict(list)

groups["admin"].append("alice")  # Automatically creates list and appends!
groups["admin"].append("charlie")
# groups is now: {"admin": ["alice", "charlie"]}
```

---

### 4. Sets & Role-Based Access Control (RBAC)
A `set` is a collection of unique elements with instant $O(1)$ lookup. It has no duplicate values.

Sets allow you to do clean mathematical operations:

```text
User Roles:    { "editor", "billing" }
Admin Roles:   { "admin", "superadmin", "editor" }
```

```python
user_roles = {"editor", "billing"}
admin_roles = {"admin", "superadmin", "editor"}

# 1. Intersection (&): What roles overlap? (Check if user has ANY admin role)
has_admin_access = bool(user_roles & admin_roles)  # True (shares "editor")

# 2. Difference (-): What required permissions is the user missing?
required_perms = {"read", "write", "delete"}
user_perms = {"read", "write"}
missing = required_perms - user_perms  # {"delete"}
```

---

## 🎯 Your Assignment: `practice/02_dicts.py`

Open [practice/02_dicts.py](file:///Users/akshay/Codebase/Python-Crash-Course/practice/02_dicts.py) and implement the following 3 functions:

### Task 1: `two_sum_unsorted(nums: list[int], target: int) -> list[int] | None`
- **Goal**: Find two indices `[i, j]` such that `nums[i] + nums[j] == target` in an **unsorted** list.
- **Why Two-Pointers Won't Work**: Because the list is not sorted, left/right pointers cannot predict whether moving will increase or decrease the sum.
- **The Dictionary Trick**:
  - As you walk through `nums`, for each number $X$, you need a partner number $Y = (\text{target} - X)$.
  - Ask: *"Have I already seen $Y$ earlier?"*
  - Store seen numbers in a dictionary: `{number: index}`.
- **Step-by-Step Example**:
  ```text
  nums = [3, 2, 4], target = 6
  1. Index 0, num = 3: Partner needed is 6 - 3 = 3. Is 3 in dict? No.
     Save: seen = {3: 0}
  2. Index 1, num = 2: Partner needed is 6 - 2 = 4. Is 4 in dict? No.
     Save: seen = {3: 0, 2: 1}
  3. Index 2, num = 4: Partner needed is 6 - 4 = 2. Is 2 in dict? YES (index 1)!
     Return [1, 2]!
  ```

---

### Task 2: `group_anagrams(words: list[str]) -> list[list[str]]`
- **Goal**: Group words that are anagrams of each other (contain the exact same letters in different order).
- **The Secret**: If you sort the letters of any anagram, they become identical!
  - `"eat"` $\rightarrow$ `sorted("eat")` $\rightarrow$ `"aet"`
  - `"tea"` $\rightarrow$ `sorted("tea")` $\rightarrow$ `"aet"`
  - `"ate"` $\rightarrow$ `sorted("ate")` $\rightarrow$ `"aet"`
- **Strategy**:
  - Use `defaultdict(list)`.
  - The key can be the sorted word: `"".join(sorted(word))`.
  - Append the original word to `grouped[key]`.
  - Return all the grouped lists: `list(grouped.values())`.
- **Example**:
  ```python
  group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
  # Returns:
  # [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
  ```

---

### Task 3: `build_user_role_index(users: list[dict]) -> dict[str, list[str]]`
- **Goal**: Invert a list of user records into a role-to-usernames index (like an in-memory database lookup).
- **Input**:
  ```python
  users = [
      {"id": "u1", "username": "alice", "roles": ["admin", "developer"]},
      {"id": "u2", "username": "bob", "roles": ["developer"]},
      {"id": "u3", "username": "charlie", "roles": []}
  ]
  ```
- **Output**:
  ```python
  {
      "admin": ["alice"],
      "developer": ["alice", "bob"]
  }
  ```
- **Rule**: If a user has no roles (like Charlie), do not add empty keys to the index.

---

## 🚀 How to Test Your Code
Once you've implemented your solutions in `practice/02_dicts.py`:
```bash
python3 test_runner.py 2
```
Or tell me in chat: **"Test my code for Lesson 02"**!

