"""
重複排除の工夫ができる
    setを使う
    重複じゃなくなるまでインクリメント
        でもこれちょっと面倒な上に考慮することが多い
elseのとき、k -= 1もやってよい。
枝狩も結構できる。こういうのはやっていったほうが良いかもしれない
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = set()
        for i in range(len(sorted_nums)):
            if nums[i] > 0:
                break
            
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
                    k -= 1
        return list(res)
