"""
まずオーバーフローが気になるが、intで収まることが制約で保証されている
オーバーフローしないのであれば、累積積を求めておいてそれぞれ割った値を出力で良い
が、divisionを使ったらだめらしい

なるほど。prefixとpostfixを前計算しておけばよい
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for n in nums:
            prefix.append(prefix[-1] * n)
        postfix = [1]
        for n in reversed(nums):
            postfix.append(postfix[-1] * n)
        postfix.reverse()
        res = []
        for idx, n in enumerate(nums):
            res.append(prefix[idx] * postfix[idx + 1])
        return res
