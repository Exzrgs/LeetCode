"""
nums[mid] == targetをすでに調べてあるから、leftやrightをmidにしなくてよい
+-1することによって、midの位置から動くことになるから、leftとrightが重なるようになる

"""

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
