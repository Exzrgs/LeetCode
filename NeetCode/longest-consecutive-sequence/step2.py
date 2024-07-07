"""
nums → nums_set

重複をカウントする問題だとしたら、lengthとは別にscoreを持っておいて、num_to_countを用意しておくと解ける
setは、value持ってないだけでhash mapと同じ感じで実現できる
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_lenght = 0
        for n in nums_set:
            if n - 1 in nums_set:
                continue
            length = 1
            while n + length in nums_set:
                length += 1
            max_lenght = max(max_lenght, length)
        return max_lenght
