class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        permutation = []
        nums_set = set(nums)
        def append_permutation():
            if len(nums_set) == 0:
                permutations.append(permutation[:])
            remaining_nums = list(nums_set)
            for n in remaining_nums:
                nums_set.remove(n)
                permutation.append(n)
                append_permutation()
                nums_set.add(n)
                permutation.pop()
        append_permutation()
        return permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        def append_permutation(current_index):
            if current_index == len(nums) - 1:
                permutations.append(nums[:])
                return
            for i in range(current_index, len(nums)):
                nums[current_index], nums[i] = nums[i], nums[current_index]
                append_permutation(current_index + 1)
                nums[current_index], nums[i] = nums[i], nums[current_index]
        append_permutation(0)
        return permutations
