"""
constraints:
    2 <= height.length <= 10^5
    0 <= height[i] <= 10^4

we want to get maximum width * height
the most obvious way is that
    for left, h in enumerate(heigth):
        // find suitable right
time complexity: O(n^2), n is the length of height
space complexity: O(1)

うーん、たしかに...
これも両端から狭めていけるのか
範囲をなす場合は、両端から狭めていくのが選択肢に入ってくる
we are gonna have pointers right, left
and then, make the range narrow
if height[right] > height[left], we are gonna make left go ahead

time complexity: O(n)
space complexity: O(1)

simple test:
    height: [1, 4, 3, 2]

    height: []

    height: [1, 1, 1, 1]
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
