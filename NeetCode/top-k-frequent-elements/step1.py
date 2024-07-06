"""
num→countを用意して、countでソートできればよい
"""

from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = defaultdict(int)
        for n in nums:
            num_to_count[n] += 1
        num_and_counts = []
        for n, count in num_to_count.items():
            num_and_counts.append((n, count))
        num_and_counts.sort(key=lambda x: x[1], reverse=True)
        return [x[0] for x in num_and_counts][:k]
