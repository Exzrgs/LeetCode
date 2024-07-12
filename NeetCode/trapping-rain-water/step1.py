"""
Question:
    How is the limit of n?
        0 < n <= 2 * 10^4
    How is the limit of bar?
        0 <= height[i] <= 10^5
Discussion:
    I think we can compute trapping for each column
    There is water the range of left bar to right bar
    so we can solve this at least by computing for each height

    なるほど、低いほうを寄せることで、あふれる心配がなくなる
    例えば、right_maxのほうが高いとして、leftを進める場合、left_maxが水を受け止めてくれる

Simple Test:
    [1, 0, 2, 1]

    []

    [1, 1]
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
