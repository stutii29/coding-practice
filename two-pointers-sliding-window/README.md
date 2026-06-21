# Two Pointers & Sliding Window

**Tutorials (free):**
- [NeetCode Two Pointers](https://neetcode.io/practice/problem-list/two-pointers)
- [NeetCode Sliding Window](https://neetcode.io/practice/problem-list/sliding-window)
- [Written primer with templates](https://dev.to/jayk0001/dsa-fundamentals-two-pointers-sliding-window-from-theory-to-leetcode-practice-80f)

## The core idea

Both patterns avoid nested loops (O(n²)) by moving pointers *intelligently*
instead of checking every pair/substring.

**Two pointers** — one pointer from each end (or two moving at different
speeds), converging toward each other based on a condition. Classic use:
sorted array, "find a pair/triplet matching some target."

**Sliding window** — a contiguous range `[left, right]` that *expands* by
moving `right`, and *shrinks* by moving `left` when some constraint is
violated. Classic use: substrings/subarrays satisfying a condition
("longest", "shortest", "contains at most/exactly K of X").

## Templates

```python
# Two pointers (converging)
left, right = 0, len(arr) - 1
while left < right:
    if condition_met(arr[left], arr[right]):
        ...
    elif need_to_grow:
        left += 1
    else:
        right -= 1
```

```python
# Sliding window (variable length)
left = 0
window_state = {}
best = 0
for right in range(len(s)):
    # expand: add s[right] to window_state
    while window_invalid(window_state):
        # shrink: remove s[left] from window_state
        left += 1
    best = max(best, right - left + 1)
```

## Problems in this folder

| File | Pattern | Difficulty |
|---|---|---|
| `container_with_most_water.py` | Two pointers, converging | Medium |
| `longest_substring_without_repeating_characters.py` | Sliding window, variable length | Medium |
| `minimum_window_substring.py` | Sliding window, variable length (stretch) | Hard |

This is the area worth the most live narration practice — say the
brute-force out loud first ("naively I'd check every substring, O(n²)..."),
then explain *why* the window avoids re-checking work.
