"""
Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/  (free)

Given an unsorted array of integers, return the length of the longest run
of consecutive integers (e.g. [100,4,200,1,3,2] -> 4, for [1,2,3,4]).

Must be O(n) — so sorting (O(n log n)) doesn't fully satisfy the intended
solution, though it's a fine fallback if you blank on the O(n) approach.
"""
from typing import List


def longest_consecutive_sort(nums: List[int]) -> int:
    """O(n log n) time. Sort, then scan for the longest run."""
    if not nums:
        return 0
    nums = sorted(set(nums))
    longest = current = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            current += 1
        else:
            current = 1
        longest = max(longest, current)
    return longest


def longest_consecutive(nums: List[int]) -> int:
    """O(n) time, O(n) space.

    Put everything in a set for O(1) lookups. The key trick: only START
    counting a sequence from a number that is a true sequence START (i.e.
    num - 1 is NOT in the set). That guarantees each number is the start of
    at most one count, so the total work across all starts is O(n), not
    O(n^2) even though there's a while loop inside the for loop.
    """
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 in num_set:
            continue  # not a sequence start, skip

        length = 1
        while num + length in num_set:
            length += 1
        longest = max(longest, length)

    return longest


if __name__ == "__main__":
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert longest_consecutive([]) == 0
    print("All tests passed.")
