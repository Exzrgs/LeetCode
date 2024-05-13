"""
nums[mid] == targetをすでに調べてあるから、leftやrightをmidにしなくてよい
+-1することによって、midの位置から動くことになるから、leftとrightが重なるようになる

境界を探してから左右を探索するほうがやるべきことがすっきりしていてわかりやすいかも
"""

# 一気に二分探索で探す
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while right - left >= 0:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            if nums[left] < nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

# 境界を二分探索で探してから、左右のソート済み範囲を探索。
from bisect import bisect_left

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while right - left > 1:
            mid = (left + right) // 2
            if nums[left] <= nums[mid]:
                left = mid
            else:
                right = mid
        min_num_index = right

        if nums[min_num_index] <= target <= nums[len(nums) - 1]:
            left = min_num_index
            right = len(nums) - 1
        else:
            left = 0
            right = min_num_index
        target_index = bisect_left(nums, target, left, right)
        if target_index == len(nums) or nums[target_index] != target:
            return -1
        return target_index
