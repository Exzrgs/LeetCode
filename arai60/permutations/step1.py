"""
itertoolsでいけるけど、さすがに良くない。
再帰関数で書く?
"""

from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return permutations(nums)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        def generate_permutation(nums_set, permutation):
            if len(nums_set) == 0:
                permutations.append(permutation[:])
            
            for n in nums_set:
                new_nums_set = set(nums_set)
                new_nums_set.remove(n)
                permutation.append(n)
                generate_permutation(new_nums_set, permutation)
                permutation.pop()
        generate_permutation(set(nums), [])
        return permutations
