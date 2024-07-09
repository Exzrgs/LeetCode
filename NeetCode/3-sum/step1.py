"""
nums[k] == -(nums[i] + nums[j])をうまく使いたいと思った
が、これもkに関しては後ろから見ていけばよいかもしれない。
先にソートしておく
時間計算量: O(n^2)
空間計算量: O(n)
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = set()
        for i in range(len(sorted_nums)):
            j = i + 1
            k = len(sorted_nums) - 1
            while j < k:
                value = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]
                if value < 0:
                    j += 1
                elif value > 0:
                    k -= 1
                else:
                    res.add((sorted_nums[i], sorted_nums[j], sorted_nums[k]))
                    j += 1
        return list(res)
