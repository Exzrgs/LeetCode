"""
・答えをsetに
    無駄が多い
・リストじゃなくて、個数で管理


あと、追加しない場所を決めることでも管理できるのか
[1, 1, 1, 1, 2]
みたいなとき、
2個目の1で追加しないってなったら、もうあとの1は追加しない
こうすると、重複を消せる
"""

from collections import Counter

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        counts = Counter(nums)
        unique_nums = list(counts.keys())
        curr_subset = []
        
        def dfs(index):
            if index == len(unique_nums):
                subsets.append(curr_subset.copy())
                return
            
            num = unique_nums[index]
            dfs(index + 1)
            for _ in range(counts[num]):
                curr_subset.append(num)
                dfs(index + 1)
            for _ in range(counts[num]):
                curr_subset.pop()
        
        dfs(0)
        return subsets

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        sorted_nums = sorted(nums)
        curr_set = []

        def append_subsets(index):
            if index == len(nums):
                subsets.append(curr_set.copy())
                return
            
            curr_set.append(sorted_nums[index])
            append_subsets(index + 1)
            curr_set.pop()
            
            while index + 1 < len(nums) and sorted_nums[index] == sorted_nums[index + 1]:
                index += 1
            append_subsets(index + 1)
        
        append_subsets(0)
        return subsets
