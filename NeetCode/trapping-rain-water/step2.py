"""
https://github.com/shining-ai/leetcode/pull/63
    dpやstackを用いた解法
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        while left < right:
            if height[left] < height[right]:
                left += 1
                left_max = max(left_max, height[left])
                total_water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                total_water += right_max - height[right]
        return total_water

# maxを記録しておく。
class Solution:
    def trap(self, height: List[int]) -> int:
        max_left_heights = [0] * len(height)
        max_right_heights = [0] * len(height)
        max_left_heights[0] = height[0]
        max_right_heights[-1] = height[-1]
        for i in range(1, len(height)):
            max_left_heights[i] = max(max_left_heights[i - 1], height[i])
        for i in range(len(height) - 2, -1, -1):
            max_right_heights[i] = max(max_right_heights[i + 1], height[i])
        total_water = 0
        for i in range(len(height)):
            total_water += min(max_right_heights[i], max_left_heights[i]) - height[i]
        return total_water
