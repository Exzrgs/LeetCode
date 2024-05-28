"""
動的計画法である長さでの最小の数を管理する
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        MAX_NUM = 10 ** 4
        MIN_NUM = -(10 ** 4)
        min_for_lengths = [MAX_NUM + 1] * (len(nums) + 1)
        min_for_lengths[0] = MIN_NUM - 1
        for i in range(len(nums)):
            for j in range(1, len(nums) + 1):
                if nums[i] > min_for_lengths[j - 1]:
                    min_for_lengths[j] = min(min_for_lengths[j], nums[i])
        for i in reversed(range(1, len(nums) + 1)):
            if min_for_lengths[i] != MAX_NUM + 1:
                return i
