"""
コーナーケースが多い。注意
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums = sorted(list(set(nums)))
        max_length = 1
        current_count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                current_count += 1
            else:
                current_count = 1
            max_length = max(max_length, current_count)
        return max_length

# O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_lenght = 0
        for n in nums:
            if n - 1 in nums:
                continue
            length = 1
            while n + length in nums:
                length += 1
            max_lenght = max(max_lenght, length)
        return max_lenght
