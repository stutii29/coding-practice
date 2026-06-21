"""
Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/  (free)

Given strings s and t, find the smallest substring of s that contains all
characters of t (with at least the same multiplicity). Return "" if none
exists.

Pattern: sliding window, variable length, with a "how many required chars
are currently satisfied" counter — the hardest version of this pattern, so
it's a good gut-check for whether the technique has really sunk in.
"""
from collections import Counter


def min_window(s: str, t: str) -> str:
    """O(n + m) time, O(charset) space, where n = len(s), m = len(t).

    need: required count of each char in t.
    window: current count of each char in the window that's also in `need`.
    have / need_count: how many of t's required (char, count) pairs are
    currently fully satisfied — when have == need_count, the window is
    valid and we try to SHRINK it from the left to find a smaller one.
    """
    if not t or not s:
        return ""

    need = Counter(t)
    need_count = len(need)

    window: dict[str, int] = {}
    have = 0

    best_len = float("inf")
    best_left = 0

    left = 0
    for right, ch in enumerate(s):
        window[ch] = window.get(ch, 0) + 1

        if ch in need and window[ch] == need[ch]:
            have += 1

        while have == need_count:
            if (right - left + 1) < best_len:
                best_len = right - left + 1
                best_left = left

            left_ch = s[left]
            window[left_ch] -= 1
            if left_ch in need and window[left_ch] < need[left_ch]:
                have -= 1
            left += 1

    return "" if best_len == float("inf") else s[best_left : best_left + best_len]


if __name__ == "__main__":
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
    assert min_window("a", "aa") == ""
    print("All tests passed.")
