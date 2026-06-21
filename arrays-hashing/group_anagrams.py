"""
Group Anagrams
https://leetcode.com/problems/group-anagrams/  (free)

Given an array of strings, group the anagrams together (any order).

Pattern: use a canonical form of each string as a hashmap KEY, so anagrams
collide into the same bucket. Two approaches to building that key below.
"""
from collections import defaultdict
from typing import List


def group_anagrams_sorted_key(strs: List[str]) -> List[List[str]]:
    """O(n * k log k) time, where k = avg string length.

    Simplest approach: sorted(word) is identical for all anagrams of each
    other, so it's a perfect, if slightly slower, hashmap key.
    """
    groups: dict[str, List[str]] = defaultdict(list)
    for word in strs:
        key = "".join(sorted(word))
        groups[key].append(word)
    return list(groups.values())


def group_anagrams_count_key(strs: List[str]) -> List[List[str]]:
    """O(n * k) time — avoids the sort by using a 26-letter count tuple
    as the key instead. Faster for longer strings.
    """
    groups: dict[tuple, List[str]] = defaultdict(list)
    for word in strs:
        counts = [0] * 26
        for ch in word:
            counts[ord(ch) - ord("a")] += 1
        groups[tuple(counts)].append(word)
    return list(groups.values())


if __name__ == "__main__":
    def normalize(result):
        return sorted(sorted(group) for group in result)

    inp = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected = normalize([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])

    assert normalize(group_anagrams_sorted_key(inp)) == expected
    assert normalize(group_anagrams_count_key(inp)) == expected
    print("All tests passed.")
