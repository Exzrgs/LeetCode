"""
5m30s
前やったのとほぼ同じ
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums == sorted(nums):
            return nums[0]

        left = 0
        right = len(nums) - 1
        while right - left > 1:
            mid = (left + right) // 2
            if nums[left] <= nums[mid]:
                left = mid
            else:
                right = mid
        return nums[right]
