"""
https://leetcode.com/problems/subarray-sum-equals-k/solutions/1759711/python-simple-python-solution-using-prefixsum-and-dictionary/?envType=problem-list-v2&envId=me1nua2e
-> 命名が参考になった
https://leetcode.com/problems/subarray-sum-equals-k/solutions/5143436/560-subarray-sum-equals-k-brute-force-tle-hashmap-prefix-sum-approaches-better-comments/?envType=problem-list-v2&envId=me1nua2e
-> running_numはなるほど。
https://github.com/hayashi-ay/leetcode/pull/31/files
-> ほぼ同じ
https://github.com/ryoooooory/LeetCode/pull/3/files
-> java。javaのmapってgetOrDefaultとかあるんだ。便利~~
https://github.com/sakupan102/arai60-practice/pull/17/files
-> ほぼ同じ2

sum_subarray_values → prefix_sum
num_equal_subarray → num_equal_subarrays 複数形にしよう
"""

from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        num_equal_subarrays = 0
        prefix_sum = 0
        prefix_sum_to_count = defaultdict(int)
        prefix_sum_to_count[0] = 1
        for n in nums:
            prefix_sum += n
            num_equal_subarrays += prefix_sum_to_count[prefix_sum  - k]
            prefix_sum_to_count[prefix_sum] += 1
        return num_equal_subarrays
