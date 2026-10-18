"""
Lesson 01: Lists, Slicing & Two-Pointer Patterns
================================================
Your task: Implement the 3 functions below.
Once done, tell Antigravity: "Test my code for Lesson 01"
"""

from typing import List, Optional


def two_sum_sorted(numbers: List[int], target: int) -> Optional[List[int]]:
    """
    Given a sorted list of integers (ascending order), find two numbers such
    that they add up to target.

    Return a 1-indexed list containing [index1, index2]. If no pair exists, return None.
    Constraint: Must run in O(N) time and O(1) extra space.
    """
    return None
    


def remove_duplicates_in_place(nums: List[int]) -> int:
    """
    Given a sorted list, remove duplicates in-place.
    Return k (the count of unique elements).
    nums[:k] must contain the unique elements.
    Must run in O(1) extra space!
    """
    return -1       



def paginate_and_format(items: List[str], page: int, page_size: int) -> List[str]:
    """
    Simulate an API pagination controller.

    Given a list of item names, a 1-indexed page number, and page_size:
    - Extract the slice corresponding to that page.
    - Return each item formatted with its 1-indexed global ranking:
      "[Rank #<global_idx>] <item_name>"

    Edge cases:
    - If page <= 0 or page_size <= 0, return an empty list [].
    - If page is out of bounds, return an empty list [].
    """
    return None


if __name__ == "__main__":
    # You can run manual tests here:
    print("Testing two_sum_sorted:", two_sum_sorted([2, 7, 11, 15], 9))
    
    test_nums = [1, 1, 2, 3, 3]
    k = remove_duplicates_in_place(test_nums)
    print("Testing remove_duplicates:", k, test_nums[:k])
    
    items = ["Apple", "Banana", "Cherry", "Date"]
    print("Testing pagination:", paginate_and_format(items, page=1, page_size=2))
