"""
Question:
    how long is piles?
    how is the h?
Discussion:
    we can find minimum k by using binary search
    binary search: 0 to max(piles)
    we try speed of mid can eat all bananas within h hours
    time complexity: O(len(piles) * log(max(piles)))
    space complexity: O(1)
Simple Test:
    [3, 5, 2], 3
    -> [0, 6], [3, 6], [4, 6], [4, 5]
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 0
        right = max(piles)
        while right - left > 1:
            mid = (left + right) // 2
            total_time = 0
            for n in piles:
                total_time += (n + mid - 1) // mid
            if total_time > h:
                left = mid
            else:
                right = mid
        return right
