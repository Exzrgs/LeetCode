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
            right = len(nums)
        else:
            left = 0
            right = min_num_index
        target_index = bisect_left(nums, target, left, right)
        if target_index == len(nums) or nums[target_index] != target:
            return -1
        return target_index
