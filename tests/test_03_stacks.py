"""
Unit test runner for Lesson 03: Stacks, Queues & collections.deque.
"""

import sys
import unittest
from pathlib import Path
import importlib.util

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

practice_file = PROJECT_ROOT / "practice" / "03_stacks_and_deques.py"
if not practice_file.exists():
    raise FileNotFoundError(f"Cannot find {practice_file}")

spec = importlib.util.spec_from_file_location("user_stacks", practice_file)
user_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(user_module)


class TestLesson03(unittest.TestCase):

    def test_is_valid_brackets(self):
        self.assertTrue(hasattr(user_module, "is_valid_brackets"))
        self.assertTrue(user_module.is_valid_brackets("()"))
        self.assertTrue(user_module.is_valid_brackets("()[]{}"))
        self.assertTrue(user_module.is_valid_brackets("{[()]}"))

        self.assertFalse(user_module.is_valid_brackets("(]"))
        self.assertFalse(user_module.is_valid_brackets("([)]"))
        self.assertFalse(user_module.is_valid_brackets("["))
        self.assertFalse(user_module.is_valid_brackets("]"))

    def test_sliding_window_rate_limiter(self):
        self.assertTrue(hasattr(user_module, "SlidingWindowRateLimiter"))
        # Allow 2 requests per 10.0 seconds
        limiter = user_module.SlidingWindowRateLimiter(max_requests=2, window_seconds=10.0)
        user = "client_alpha"

        # t = 1.0: 1st request -> Allowed
        self.assertTrue(limiter.allow_request(user, 1.0))
        # t = 5.0: 2nd request -> Allowed
        self.assertTrue(limiter.allow_request(user, 5.0))
        # t = 7.0: 3rd request within 10s -> BLOCKED
        self.assertFalse(limiter.allow_request(user, 7.0))
        # t = 9.0: 4th request within 10s -> BLOCKED
        self.assertFalse(limiter.allow_request(user, 9.0))

        # t = 11.5: 1st request (t=1.0) is evicted (11.5 - 10.0 = 1.5 > 1.0) -> Allowed!
        self.assertTrue(limiter.allow_request(user, 11.5))

    def test_simplify_path(self):
        self.assertTrue(hasattr(user_module, "simplify_path"))
        self.assertEqual(user_module.simplify_path("/home/"), "/home")
        self.assertEqual(user_module.simplify_path("/../"), "/")
        self.assertEqual(user_module.simplify_path("/home//foo/"), "/home/foo")
        self.assertEqual(user_module.simplify_path("/a/./b/../../c/"), "/c")


if __name__ == "__main__":
    unittest.main()
