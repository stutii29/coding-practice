# Arrays & Hashing

**Tutorial:** [NeetCode Arrays & Hashing](https://neetcode.io/practice/arrays-and-hashing) (free, includes short videos per problem)

## The core idea

Most "brute force is O(n²)" array problems become O(n) by trading time for
space: store something you've already seen in a hashmap/hashset so the next
lookup is O(1) instead of a nested loop.

Three recurring sub-patterns:

1. **Membership / duplicate check** → `set()`. *"Have I seen this before?"*
   (e.g. Contains Duplicate)
2. **Frequency counting** → `dict()` or `collections.Counter`. *"How many
   times does X appear?"* (e.g. Top K Frequent, Group Anagrams)
3. **Complement lookup** → `dict()` mapping value → index, checked *while*
   building it. *"Does the number I need already exist?"* (e.g. Two Sum)

## Complexity cheat sheet

| Operation | Array (unsorted) | Hashmap/Hashset |
|---|---|---|
| Search | O(n) | O(1) avg |
| Insert | O(1) amortized | O(1) avg |
| Delete | O(n) | O(1) avg |

The "O(1) avg" caveat: worst case is O(n) under hash collisions, but you can
treat it as O(1) for interview purposes unless asked about it directly.

## Problems in this folder

| File | Pattern | Difficulty |
|---|---|---|
| [two_sum](https://leetcode.com/problems/two-sum/editorial/) | Complement lookup | Easy |
| [best_time_to_buy_and_sell_stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/editorial/) | Single-pass min-tracking | Easy |
| [product_of_array_except_self](https://leetcode.com/problems/product-of-array-except-self/editorial/) | Prefix/suffix products | Medium |
| [group_anagrams](https://leetcode.com/problems/group-anagrams/editorial/) | Frequency counting as a hash key | Medium |
| [top_k_frequent_elements](https://leetcode.com/problems/top-k-frequent-elements/editorial/) | Frequency counting + bucket sort | Medium |
| [longest_consecutive_seq](https://leetcode.com/problems/longest-consecutive-sequence/editorial/) | Set membership sequence detection | Medium |

Work top to bottom — each one reinforces the previous pattern before adding
a twist.
