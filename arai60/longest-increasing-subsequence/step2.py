"""
ある時点での最大の長さを保持するほうが自然そう
dpはいろいろなパターンがあるからどれが良いか比較検討できるとよい
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_lengths = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    max_lengths[i] = max(max_lengths[i], max_lengths[j] + 1)
        return max(max_lengths)

# 二分探索でより小さい値に更新する
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        MAX_NUM = 10 ** 4
        increasing_subsequence = [MAX_NUM + 1] * len(nums)
        for n in nums:
            index = bisect_left(increasing_subsequence, n)
            increasing_subsequence[index] = n
        return bisect_left(increasing_subsequence, MAX_NUM + 1)
