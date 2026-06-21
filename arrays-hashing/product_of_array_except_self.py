"""
Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/  (free)

Return an array where answer[i] = product of all elements except nums[i],
WITHOUT using division and in O(n) time.

Pattern: prefix/suffix products. answer[i] = (product of everything to the
left of i) * (product of everything to the right of i).
"""
from typing import List


def product_except_self_brute_force(nums: List[int]) -> List[int]:
    """O(n^2) time. Recompute the product for every index."""
    n = len(nums)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= nums[j]
        result.append(product)
    return result


def product_except_self(nums: List[int]) -> List[int]:
    """O(n) time, O(1) extra space (output array doesn't count).

    Pass 1 (left to right): result[i] = product of everything BEFORE i.
    Pass 2 (right to left): multiply in the product of everything AFTER i,
    using a running suffix product instead of a second array.
    """
    n = len(nums)
    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


if __name__ == "__main__":
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    print("All tests passed.")
