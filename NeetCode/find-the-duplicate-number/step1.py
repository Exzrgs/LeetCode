"""
Question:
    How is the size of n?

サイクルの入り口が重複になる
fastはslowの2倍の速度で動く。
slowとfastがぶつかるってことは、fast = slow * 2
なので、slow2をそのときに走らせると、slowがfastの位置にきたとき、slow = slow2になる
よって、そこがサイクルの入り口である

あと二分探索でもできるのか
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while right - left > 1:
            mid = (left + right) // 2
            count = 0
            for n in nums:
                if n <= mid:
                    count += 1
            if count > mid:
                right = mid
            else:
                left = mid
        return right
