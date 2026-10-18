"""
Lesson 02: Dictionaries, Sets & Frequency Counting
==================================================
Your task: Implement the 3 functions below.
Once done, tell Antigravity: "Test my code for Lesson 02"
"""

from collections import defaultdict
from typing import List, Dict, Optional, Any


def two_sum_unsorted(nums: List[int], target: int) -> Optional[List[int]]:
    """
    Find two indices in an unsorted list that add up to target.
    Must run in O(N) time using a dictionary!

    Return a list of the two 0-indexed indices [i, j]. Return None if no pair exists.
    """
   
    return None
    


def group_anagrams(words: List[str]) -> List[List[str]]:
    """
    Group strings that are anagrams of each other (contain the exact same characters).
    Return a list of anagram groups.
    """
   
    return None


def build_user_role_index(users: List[Dict[str, Any]]) -> Optional[Dict[str, List[str]]]:
    """
    Invert user records into a role -> [usernames] index.

    Given a list of user dicts with 'username' and 'roles',
    return a dict mapping each role name to a list of usernames with that role.
    If a user has no roles, they should not create empty string keys.
    """
    return None

if __name__ == "__main__":
    print("Testing two_sum_unsorted:", two_sum_unsorted([3, 2, 4], 6))
    print("Testing group_anagrams:", group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    sample_users = [
        {"id": "u1", "username": "alice", "roles": ["admin", "developer"]},
        {"id": "u2", "username": "bob", "roles": ["developer"]},
    ]
    print("Testing build_user_role_index:", build_user_role_index(sample_users))
