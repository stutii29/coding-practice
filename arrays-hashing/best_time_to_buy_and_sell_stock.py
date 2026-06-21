"""
Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/  (free)

Given prices[i] = price on day i, you may buy once and sell once (sell
after buy). Return the max profit, or 0 if no profit is possible.

Pattern: single-pass min-tracking. You don't need to check every (buy, sell)
pair — only "the lowest price seen so far" matters at each step.
"""
from typing import List


def max_profit_brute_force(prices: List[int]) -> int:
    """O(n^2) time. Check every buy/sell pair."""
    best = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            best = max(best, prices[j] - prices[i])
    return best


def max_profit(prices: List[int]) -> int:
    """O(n) time, O(1) space.

    Track the minimum price seen so far. At each day, the best possible
    sell is "today's price minus the lowest buy price before today."
    """
    if not prices:
        return 0

    min_price_so_far = prices[0]
    best_profit = 0

    for price in prices[1:]:
        best_profit = max(best_profit, price - min_price_so_far)
        min_price_so_far = min(min_price_so_far, price)

    return best_profit


if __name__ == "__main__":
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit([]) == 0
    print("All tests passed.")
