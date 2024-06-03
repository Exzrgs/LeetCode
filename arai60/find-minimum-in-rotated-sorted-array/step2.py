"""
わざわざソートしなくても比較するだけでよい
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
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

# 固定値と比較して寄せていくパターン
# これならソートされていても動く
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = -1
        right = len(nums) - 1
        while right - left > 1:
            mid = (left + right) // 2
            if nums[mid] >= nums[-1]:
                left = mid
            else:
                right = mid
        return nums[right]

# leftをmidより動かすパターン
# 最小値を直接あてに行く
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= nums[-1]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
