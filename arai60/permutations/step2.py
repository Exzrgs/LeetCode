"""
permutationを引数から消した
setを新しく作るのじゃなく、ループに使うほうを新しく作るほうが良い

https://github.com/SuperHotDogCat/coding-interview/pull/12/files
-> シンプルでわかりやすい実装。読みやすい
https://github.com/Mike0121/LeetCode/pull/14/files
-> itertools permutationsの内部実装の再現などが載っていて良い。いろいろな解き方を試しており非常に参考になる

"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        permutation = []
        nums_set = set(nums)
        def generate_permutation():
            if len(nums_set) == 0:
                permutations.append(permutation[:])
            
            remaining_nums = list(nums_set)
            for n in remaining_nums:
                nums_set.remove(n)
                permutation.append(n)
                generate_permutation()
                nums_set.add(n)
                permutation.pop()
        generate_permutation()
        return permutations

# 計算量は若干増えるが、すっきりする
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        permutation = []
        def generate_permutation():
            if len(permutation) == len(nums):
                permutations.append(permutation[:])
            
            for n in nums:
                if n in permutation:
                    continue
                permutation.append(n)
                generate_permutation(permutation)
                permutation.pop()
        generate_permutation()
        return permutations

# swap
# まあ結局上のやつとやってることは同じで、numsの空間を利用してるだけ
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        def append_permutation(current_index):
            if current_index == len(nums) - 1:
                permutations.append(nums[:])
            for i in range(current_index, len(nums)):
                nums[current_index], nums[i] = nums[i], nums[current_index]
                append_permutation(current_index + 1)
                nums[current_index], nums[i] = nums[i], nums[current_index]
        append_permutation(0)
        return permutations
