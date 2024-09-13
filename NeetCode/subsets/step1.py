"""
queue
recursion
stack

[1, 2, 3]
"""

# recursion
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        current_sets = []
        
        def make_subsets_list(index):
            if index == len(nums):
                subsets.append(current_sets.copy())
                return
            
            make_subsets_list(index + 1)
            current_sets.append(nums[index])
            make_subsets_list(index + 1)
            current_sets.pop()
        
        make_subsets_list(0)
        return subsets

# deque
from collections import deque
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        sets_queue = deque()
        sets_queue.append(([], 0)) # sets, index
        while sets_queue:
            sets, index = sets_queue.popleft()
            if index == len(nums):
                subsets.append(sets.copy())
                continue

            sets_queue.append((sets.copy(), index + 1))
            copied = sets.copy()
            copied.append(nums[index])
            sets_queue.append((copied, index + 1))
        return subsets

# stack
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        stack = []
        stack.append(([], 0))
        while stack:
            sets, index = stack.pop()
            if index == len(nums):
                subsets.append(sets.copy())
                continue
            
            copied = sets.copy()
            copied.append(nums[index])
            stack.append((copied, index + 1))
            stack.append((sets.copy(), index + 1))
        return subsets