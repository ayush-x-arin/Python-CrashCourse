# 📘 Lesson 01: Lists, Slicing & Two-Pointer Patterns

Welcome to your first lesson! In backend engineering, arrays and lists are everywhere: HTTP request bodies, database query result sets, paginated API responses, and batch processing jobs.

If you only know a little bit of programming, don't worry! This guide breaks down the core concepts with simple, real-world analogies and visual diagrams.

---

## 🧠 Core Concepts Made Simple

### 1. What is a Python List? (The Apartment Complex Analogy)
Think of a Python list as a row of numbered apartment mailboxes:
- Every mailbox has a number (an **index**), starting from **`0`**.
- Inside each mailbox is a pointer (an address card) pointing to an object in memory.

```text
Indices:     0          1          2          3
          +----------+----------+----------+----------+
List:     | "Apple"  | "Banana" | "Cherry" |  "Date"  |
          +----------+----------+----------+----------+
```

#### Why does Speed (Time Complexity) Matter?
- **Instant Lookup by Index ($O(1)$)**: If you ask for `items[2]`, Python immediately jumps directly to mailbox #2. It takes the exact same fraction of a millisecond whether the list has 4 items or 4,000,000 items!
- **Appending to the End ($O(1)$ amortized)**: Adding an item with `items.append("Elderberry")` is fast. Python leaves empty reserve slots at the end, so adding onto the tail takes 1 quick operation.
- **Inserting / Deleting at the Beginning ($O(N)$)**: 
  > ⚠️ If you insert at index 0 (`items.insert(0, "Apricot")`), **every other item has to move one spot to the right**!
  > If there are 100,000 items, Python has to shift 100,000 items in memory. In backend APIs, avoid inserting at index 0 on large lists.

---

### 2. Slicing Mechanics (How to Extract Sub-lists)
Slicing lets you take a chunk out of a list: `my_list[start:stop:step]`

#### The "Cut Lines" Mental Model:
The most common beginner mistake is forgetting that **`stop` is exclusive** (Python stops *before* reaching `stop`).

Imagine the indices as cut lines *between* the elements:

```text
Cut lines:  0          1          2          3          4
            |  "Apple" | "Banana" | "Cherry" |  "Date"  |
```

- `items[1:3]` $\rightarrow$ starts at cut line 1, stops at cut line 3 $\rightarrow$ `["Banana", "Cherry"]`.
- `items[:2]` $\rightarrow$ from beginning up to cut line 2 $\rightarrow$ `["Apple", "Banana"]`.
- `items[2:]` $\rightarrow$ from cut line 2 to the very end $\rightarrow$ `["Cherry", "Date"]`.
- `items[-1]` $\rightarrow$ the very last element (`"Date"`).
- `items[::-1]` $\rightarrow$ a reversed copy of the list.

> [!WARNING]
> **Backend Memory Gotcha**: Slicing creates a **brand-new copy** of the sliced elements in RAM. Slicing a small page (e.g., 20 items) is completely fine, but repeatedly slicing a huge list (e.g. 500,000 rows) inside a loop creates lots of temporary memory garbage!

---

### 3. Idiomatic Loops: `enumerate()` and `zip()`
In older languages like C or basic Java, people often write:
```python
# ❌ Clunky, beginner style:
for i in range(len(users)):
    print(i, users[i])
```

Python gives you much cleaner, safer tools:

#### `enumerate()`: Gives you both (index, item)
```python
fruits = ["Apple", "Banana", "Cherry"]

# start=1 makes the ranking 1-indexed (1, 2, 3...)
for rank, fruit in enumerate(fruits, start=1):
    print(f"Rank #{rank}: {fruit}")
# Output:
# Rank #1: Apple
# Rank #2: Banana
# Rank #3: Cherry
```

#### `zip()`: Pairs two lists side-by-side
```python
usernames = ["alice", "bob"]
roles = ["admin", "viewer"]

for user, role in zip(usernames, roles):
    print(f"{user} has role {role}")
```

---

### 4. The Two-Pointer Technique (Why It Beats Nested Loops)

Suppose you need to find two numbers in a list that add up to a target number (e.g. `9`).

#### The Naive Approach: Nested Loops ($O(N^2)$)
A beginner might compare every element with every other element using two loops:
```python
# Comparing every pair takes N * N operations!
# For 10,000 items -> 100,000,000 checks (API freezes!)
```

#### The Smart Approach: Two Pointers ($O(N)$)
If the list is **already sorted**, we can place one pointer at the start (`left`) and one at the end (`right`):

```text
Target = 9
List:   [ 2,    7,   11,   15 ]
          ^                 ^
        left              right
```

1. Check the sum: `2 + 15 = 17`.
   - `17 > 9` (Sum is too big!). Because the list is sorted, moving `left` forward would only make the sum bigger. So our only logical move is to make the sum smaller by moving `right` leftward (`right -= 1`).
2. Next step:
   ```text
   List:   [ 2,    7,   11,   15 ]
             ^           ^
           left        right
   ```
   - Check sum: `2 + 7 = 9`. Match found! Return the indices.
- **Why this is awesome**: Every step eliminates one candidate. We find the answer in at most $N$ steps!

#### Fast & Slow Pointers (In-Place Modifications)
Sometimes you are asked to modify a list **in-place** (meaning without creating a new `result = []` list to save RAM):
- **`slow` pointer**: Tracks where the next unique element should be written.
- **`fast` pointer**: A scout that rushes ahead looking for new, unseen numbers.

---

## 🎯 Your Assignment: `practice/01_lists.py`

Open [practice/01_lists.py](file:///Users/akshay/Codebase/Python-Crash-Course/practice/01_lists.py) and implement the following 3 functions:

### Task 1: `two_sum_sorted(numbers: list[int], target: int) -> list[int] | None`
- **Goal**: Given a sorted list of numbers (ascending order), find two numbers that sum to `target`.
- **Return**: A **1-indexed** list `[index1, index2]`. If no pair exists, return `None`.
- **Constraint**: Must run in **$O(N)$ time** and **$O(1)$ extra memory** using two pointers.
- **Example**:
  ```python
  two_sum_sorted([2, 7, 11, 15], 9)  # Returns [1, 2] because numbers[0] + numbers[1] == 9
  two_sum_sorted([1, 2, 3, 4], 10)   # Returns None
  ```

---

### Task 2: `remove_duplicates_in_place(nums: list[int]) -> int`
- **Goal**: Given a sorted list, remove duplicate values **in-place** so that each unique value appears only once at the beginning of `nums`.
- **Return**: An integer `k` representing the count of unique elements.
- **Constraint**: You must mutate `nums` directly so `nums[:k]` contains the unique items. No creating extra list copies ($O(1)$ extra space).
- **Example**:
  ```python
  nums = [1, 1, 2, 2, 3, 4, 4]
  k = remove_duplicates_in_place(nums)
  # k = 4
  # nums[:k] is [1, 2, 3, 4]
  ```

---

### Task 3: `paginate_and_format(items: list[str], page: int, page_size: int) -> list[str]`
- **Goal**: Simulate an API pagination controller.
  - When a user requests page `2` with `page_size = 2`:
    - Calculate starting index: `(page - 1) * page_size` $\rightarrow (2 - 1) \times 2 = 2$.
    - Calculate ending index: `start + page_size` $\rightarrow 2 + 2 = 4$.
    - Extract the slice `items[start:end]`.
    - Format each item with its 1-indexed global ranking: `"[Rank #<rank>] <item_name>"`.
- **Edge cases**:
  - If `page <= 0` or `page_size <= 0`, return `[]`.
  - If `page` starts beyond the length of `items`, return `[]`.
- **Example**:
  ```python
  data = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
  paginate_and_format(data, page=2, page_size=2)
  # Returns:
  # ["[Rank #3] Cherry", "[Rank #4] Date"]
  ```

---

## 🚀 How to Test Your Code
Once you've implemented your solutions in `practice/01_lists.py`:
```bash
python3 test_runner.py 1
```
Or tell me in chat: **"Test my code for Lesson 01"**!

