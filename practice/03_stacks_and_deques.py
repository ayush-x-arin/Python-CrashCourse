"""
Lesson 03: Stacks, Queues & collections.deque
============================================
Your task: Implement the 3 components below.
Once done, tell Antigravity: "Test Lesson 03"
"""

from collections import deque
from typing import Dict


def is_valid_brackets(s: str) -> bool:
    """
    Given a string s containing '(', ')', '{', '}', '[', ']',
    determine if the input string is valid.

    Rules:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    Constraint: Must use a list as a stack in O(N) time.
    """
    return None


class SlidingWindowRateLimiter:
    """
    Sliding window API rate limiter using collections.deque.

    Tracks request timestamps per user_id within a time window of window_seconds.
    allow_request evicts timestamps older than (current_time - window_seconds)
    and allows the request if under max_requests.
    """
    def __init__(self, max_requests: int, window_seconds: float):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        # Dictionary mapping user_id -> deque of request timestamps
        self.user_requests: Dict[str, deque] = {}

    def allow_request(self, user_id: str, current_time: float) -> bool:
        """
        Returns True if request is allowed, False if rate limited.
        Evicts timestamps older than (current_time - window_seconds) with popleft().
        """
        return None


def simplify_path(path: str) -> str:
    """
    Canonicalize an absolute Unix/URL path using a stack (LeetCode 71).

    Rules:
    - '.' means current directory (ignore).
    - '..' means move up one directory (pop from directory stack).
    - Multiple consecutive slashes '//' are treated as a single '/'.
    - Returns the canonical path starting with '/'.
    """
    return ""


if __name__ == "__main__":
    print("Testing brackets:", is_valid_brackets("{[()]}"))
    
    limiter = SlidingWindowRateLimiter(max_requests=2, window_seconds=5.0)
    print("Limiter t=1.0:", limiter.allow_request("user1", 1.0))
    print("Limiter t=2.0:", limiter.allow_request("user1", 2.0))
    print("Limiter t=3.0 (should block):", limiter.allow_request("user1", 3.0))
    
    print("Testing path:", simplify_path("/a/./b/../../c/"))
