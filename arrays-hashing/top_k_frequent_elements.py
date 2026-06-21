"""
Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/  (free)

Given an integer array and k, return the k most frequent elements.

Pattern: frequency counting, then a way to find the top k without a full
O(n log n) sort. Two valid approaches below — know both, since interviewers
often ask "can you do better than sorting?"
"""
import heapq
from collections import Counter
from typing import List


def top_k_frequent_heap(nums: List[int], k: int) -> List[int]:
    """O(n log k) time, O(n) space.

    Count frequencies, then use a min-heap of size k: push every (freq,
    num) pair, popping the smallest whenever the heap exceeds size k. This
    is faster than sorting all n elements when k is small.
    """
    counts = Counter(nums)
    heap: List[tuple] = []

    for num, freq in counts.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)

    return [num for _, num in heap]


def top_k_frequent_bucket_sort(nums: List[int], k: int) -> List[int]:
    """O(n) time, O(n) space.

    Bucket sort by frequency: bucket[f] = list of numbers that occur
    exactly f times. Since frequency is bounded by len(nums), this beats
    O(n log n) sorting entirely.
    """
    counts = Counter(nums)
    buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]

    for num, freq in counts.items():
        buckets[freq].append(num)

    result: List[int] = []
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
    return result


if __name__ == "__main__":
    assert sorted(top_k_frequent_heap([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert sorted(top_k_frequent_bucket_sort([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    print("All tests passed.")
