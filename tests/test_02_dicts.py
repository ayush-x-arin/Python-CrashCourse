"""
Unit test runner for Lesson 02: Dictionaries, Sets & Frequency Counting.
"""

import sys
import unittest
from pathlib import Path
import importlib.util

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

practice_file = PROJECT_ROOT / "practice" / "02_dicts.py"
if not practice_file.exists():
    raise FileNotFoundError(f"Cannot find {practice_file}")

spec = importlib.util.spec_from_file_location("user_dicts", practice_file)
user_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(user_module)


class TestLesson02(unittest.TestCase):

    def test_two_sum_unsorted(self):
        self.assertTrue(hasattr(user_module, "two_sum_unsorted"))
        nums = [3, 2, 4]
        target = 6
        result = user_module.two_sum_unsorted(nums, target)
        self.assertIsNotNone(result)
        self.assertEqual(sorted(result), [1, 2])

        # No match
        self.assertIsNone(user_module.two_sum_unsorted([1, 2, 3], 10))

    def test_group_anagrams(self):
        self.assertTrue(hasattr(user_module, "group_anagrams"))
        words = ["eat", "tea", "tan", "ate", "nat", "bat"]
        result = user_module.group_anagrams(words)

        # Normalize results for unordered comparison
        normalized = sorted([sorted(group) for group in result])
        expected = sorted([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
        self.assertEqual(normalized, expected)

    def test_build_user_role_index(self):
        self.assertTrue(hasattr(user_module, "build_user_role_index"))
        users = [
            {"id": "u1", "username": "alice", "roles": ["admin", "developer"]},
            {"id": "u2", "username": "bob", "roles": ["developer"]},
            {"id": "u3", "username": "charlie", "roles": []},
            {"id": "u4", "username": "diana", "roles": ["admin"]}
        ]
        index = user_module.build_user_role_index(users)
        self.assertIn("admin", index)
        self.assertIn("developer", index)
        self.assertEqual(sorted(index["admin"]), ["alice", "diana"])
        self.assertEqual(sorted(index["developer"]), ["alice", "bob"])
        self.assertNotIn("", index)


if __name__ == "__main__":
    unittest.main()
