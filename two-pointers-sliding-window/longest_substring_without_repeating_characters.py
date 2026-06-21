"""
Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/  (free)

Given a string s, find the length of the longest substring with no
repeating characters.

Pattern: sliding window, variable length. Expand right; whenever a
duplicate enters the window, shrink left past the previous occurrence.
"""


def length_of_longest_substring_brute_force(s: str) -> int:
    """O(n^3) time. Check every substring for uniqueness."""
    n = len(s)
    best = 0
    for i in range(n):
        for j in range(i, n):
            substring = s[i : j + 1]
            if len(set(substring)) == len(substring):
                best = max(best, len(substring))
    return best


def length_of_longest_substring(s: str) -> int:
    """O(n) time, O(min(n, charset)) space.

    last_seen_index maps char -> most recent index seen. When we hit a
    char already in the window, jump `left` to just past its last
    occurrence — NOT left += 1 one step at a time, since everything
    between left and that occurrence is still duplicate-free and doesn't
    need re-checking.
    """
    last_seen_index: dict[str, int] = {}
    left = 0
    best = 0

    for right, ch in enumerate(s):
        if ch in last_seen_index and last_seen_index[ch] >= left:
            left = last_seen_index[ch] + 1

        last_seen_index[ch] = right
        best = max(best, right - left + 1)

    return best


if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    print("All tests passed.")
