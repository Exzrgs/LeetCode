"""
2m50s
"""

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        for left in reversed(range(len(nums) - 1)):
            for right in reversed(range(left + 1, len(nums))):
                if nums[left] < nums[right]:
                    nums[left], nums[right] = nums[right], nums[left]
                    nums[left + 1 :] = sorted(nums[left + 1 :])
                    return
        nums.sort()
