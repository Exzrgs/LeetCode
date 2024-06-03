"""

"""

# for
class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        for left in range(len(nums)-2, -1, -1):
            if nums[left] > nums[left + 1]:
                continue
            for right in range(len(nums)-1, left, -1):
                if nums[left] < nums[right]:
                    nums[left], nums[right] = nums[right], nums[left]
                    nums[left + 1 :] = sorted(nums[left + 1 :])
                    return
        nums.reverse()

# while
class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        left = len(nums) - 2
        while left >= 0 and nums[left] >= nums[left + 1]:
            left -= 1
        if left == -1:
            nums.reverse()
            return
        
        right = len(nums) - 1
        while nums[left] >= nums[right]:
            right -= 1
        
        nums[left], nums[right] = nums[right], nums[left]
        nums[left + 1 :] = sorted(nums[left + 1 :])
