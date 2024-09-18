"""
candidatesに負の値が含まれるのかは重要
"""

from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        counts = Counter(candidates)
        unique_candidates = list(counts.keys())
        comb = []
        
        def append_comb(index, sum_values):
            if sum_values == target:
                res.append(comb.copy())
                return
            if sum_values > target or index == len(unique_candidates):
                return
            
            append_comb(index + 1, sum_values)
            num = unique_candidates[index]
            for i in range(counts[num]):
                comb.append(num)
                append_comb(index + 1, sum_values + num * (i + 1))
            for _ in range(counts[num]):
                comb.pop()
        
        append_comb(0, 0)
        return res

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sorted_candidates = sorted(candidates)
        comb = []
        
        def append_comb(index, sum_vals):
            if sum_vals == target:
                res.append(comb.copy())
                return
            if sum_vals > target or index == len(candidates):
                return
            
            num = sorted_candidates[index]
            comb.append(num)
            append_comb(index + 1, sum_vals + num)
            comb.pop()
            
            while index + 1 < len(candidates) and sorted_candidates[index] == sorted_candidates[index + 1]:
                index += 1
            append_comb(index + 1, sum_vals)
        
        append_comb(0, 0)
        return res
