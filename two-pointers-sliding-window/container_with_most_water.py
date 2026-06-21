"""
Container With Most Water
https://leetcode.com/problems/container-with-most-water/  (free)

Given heights[i] = height of a vertical line at position i, find two lines
that, together with the x-axis, form a container holding the most water.
Area = width * min(height[left], height[right]).

Pattern: two pointers, converging. Start as wide as possible (max width),
then narrow — but only move the pointer at the SHORTER line, since moving
the taller one can never increase the area.
"""
from typing import List


def max_area_brute_force(heights: List[int]) -> int:
    """O(n^2) time. Check every pair of lines."""
    best = 0
    n = len(heights)
    for i in range(n):
        for j in range(i + 1, n):
            area = (j - i) * min(heights[i], heights[j])
            best = max(best, area)
    return best


def max_area(heights: List[int]) -> int:
    """O(n) time, O(1) space.

    Start with the widest possible container (both ends). At each step,
    the SHORTER side is the bottleneck — moving the taller pointer inward
    can only decrease width without any chance of increasing the limiting
    height, so it's never beneficial. Moving the shorter pointer is the
    only move that *could* find a taller line and improve the area.
    """
    left, right = 0, len(heights) - 1
    best = 0

    while left < right:
        width = right - left
        area = width * min(heights[left], heights[right])
        best = max(best, area)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return best


if __name__ == "__main__":
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    print("All tests passed.")
