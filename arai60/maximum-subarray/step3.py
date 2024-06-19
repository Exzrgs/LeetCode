"""
1m
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_subarray_sum = nums[0]
        for i in range(1, len(nums)):
            current_subarray_sum = max(current_subarray_sum + nums[i], nums[i])
            max_sum = max(max_sum, current_subarray_sum)
        return max_sum
