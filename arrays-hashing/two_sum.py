"""
Two Sum
https://leetcode.com/problems/two-sum/  (free)

Given an array of integers nums and an integer target, return the indices
of the two numbers that add up to target. Exactly one valid answer exists.

Pattern: complement lookup. While scanning, ask "have I already seen the
number that would complete a pair with this one?"
"""
from typing import List


def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    """O(n^2) time, O(1) space. Check every pair."""
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum(nums: List[int], target: int) -> List[int]:
    """O(n) time, O(n) space.

    Build the hashmap and check it in the SAME pass: for each num, look up
    whether (target - num) was already seen *before* inserting num itself.
    This avoids matching an element with itself and avoids a second pass.
    """
    seen: dict[int, int] = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    assert sorted(two_sum([2, 7, 11, 15], 9)) == [0, 1]
    assert sorted(two_sum([3, 2, 4], 6)) == [1, 2]
    assert sorted(two_sum([3, 3], 6)) == [0, 1]
    print("All tests passed.")
