"""
二分探索をうまく使えばできそうというのは考えたが、良いやり方は思いつかなかった

leftとmidを比べることで、少なくともその間が昇順になっているかどうかはわかる
なっていなければ、その間に境界線があるはず。
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] == target:
            return 0
        if nums[-1] == target:
            return len(nums) - 1

        left = 0
        right = len(nums) - 1
        while right - left > 1:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            if nums[left] < nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid
        return -1
