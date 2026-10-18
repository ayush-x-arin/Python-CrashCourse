"""
Unit test runner for Lesson 01: Lists, Slicing & Two Pointers.
This runs automatically when you ask Antigravity to test your code.
"""

import sys
import unittest
from pathlib import Path

# Add project root to sys.path so practice modules can be imported
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

try:
    from practice import lists as user_module
except ImportError:
    # Try direct import if named 01_lists.py
    import importlib.util
    practice_file = PROJECT_ROOT / "practice" / "01_lists.py"
    if not practice_file.exists():
        raise FileNotFoundError(
            f"\n\n❌ Could not find your code file at: {practice_file}\n"
            f"Please create 'practice/01_lists.py' and write your functions there!"
        )
    spec = importlib.util.spec_from_file_location("user_lists", practice_file)
    user_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(user_module)


class TestLesson01(unittest.TestCase):

    def test_two_sum_sorted_found(self):
        """Test two_sum_sorted finds correct 1-indexed pair."""
        self.assertTrue(
            hasattr(user_module, "two_sum_sorted"),
            "Function 'two_sum_sorted' is not defined in practice/01_lists.py!"
        )
        nums = [2, 7, 11, 15]
        target = 9
        result = user_module.two_sum_sorted(nums, target)
        self.assertEqual(result, [1, 2], f"Expected [1, 2], got {result}")

        nums2 = [1, 3, 4, 6, 8, 10]
        target2 = 14
        result2 = user_module.two_sum_sorted(nums2, target2)
        self.assertEqual(result2, [3, 6], f"Expected [3, 6], got {result2}")

    def test_two_sum_sorted_not_found(self):
        """Test two_sum_sorted returns None when target cannot be formed."""
        nums = [1, 2, 3, 9]
        target = 8
        result = user_module.two_sum_sorted(nums, target)
        self.assertIsNone(result, f"Expected None, got {result}")

    def test_remove_duplicates_in_place(self):
        """Test remove_duplicates_in_place modifies array in-place and returns correct count."""
        self.assertTrue(
            hasattr(user_module, "remove_duplicates_in_place"),
            "Function 'remove_duplicates_in_place' is not defined in practice/01_lists.py!"
        )
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        k = user_module.remove_duplicates_in_place(nums)
        self.assertEqual(k, 5, f"Expected 5 unique elements, got k={k}")
        self.assertEqual(nums[:k], [0, 1, 2, 3, 4], f"Expected first {k} elements to be [0, 1, 2, 3, 4], got {nums[:k]}")

    def test_remove_duplicates_empty_and_single(self):
        """Test edge cases with empty and single-element lists."""
        nums_empty = []
        k_empty = user_module.remove_duplicates_in_place(nums_empty)
        self.assertEqual(k_empty, 0, f"Expected 0 for empty list, got {k_empty}")

        nums_single = [42]
        k_single = user_module.remove_duplicates_in_place(nums_single)
        self.assertEqual(k_single, 1)
        self.assertEqual(nums_single[:k_single], [42])

    def test_paginate_and_format(self):
        """Test paginate_and_format slices and ranks items correctly."""
        self.assertTrue(
            hasattr(user_module, "paginate_and_format"),
            "Function 'paginate_and_format' is not defined in practice/01_lists.py!"
        )
        items = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta"]
        page_2 = user_module.paginate_and_format(items, page=2, page_size=2)
        expected = ["[Rank #3] Gamma", "[Rank #4] Delta"]
        self.assertEqual(page_2, expected, f"Expected {expected}, got {page_2}")

        # Page 3: last 2
        page_3 = user_module.paginate_and_format(items, page=3, page_size=2)
        expected_3 = ["[Rank #5] Epsilon", "[Rank #6] Zeta"]
        self.assertEqual(page_3, expected_3)

    def test_paginate_and_format_edge_cases(self):
        """Test pagination out of bounds and invalid page arguments."""
        items = ["ItemA", "ItemB"]
        out_of_bounds = user_module.paginate_and_format(items, page=5, page_size=2)
        self.assertEqual(out_of_bounds, [], "Expected [] when page exceeds item range")

        invalid_page = user_module.paginate_and_format(items, page=0, page_size=2)
        self.assertEqual(invalid_page, [], "Expected [] when page <= 0")

        invalid_size = user_module.paginate_and_format(items, page=1, page_size=0)
        self.assertEqual(invalid_size, [], "Expected [] when page_size <= 0")


if __name__ == "__main__":
    unittest.main()
