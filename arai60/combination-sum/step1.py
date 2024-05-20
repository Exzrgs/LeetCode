"""
めちゃくちゃざっくり考えると、全体で候補は40!
が、実際はそうはならない。でもかなり大きくなる気がする
でも結局全通りは計算しないと解けないので、メタ読みだけど全探索はできるだろう。やるとしても枝狩り程度
再帰とかでやることを考える。重複を含まないために、自分より大きいやつしか考えなくてよい

20m

メタ読みしてしまったのがよくないが、計算量の解析が難しい...
ざっくりした数で抑えて大丈夫なことを確認したい
何か良い方法あれば教えてください><
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combination_candidate = []
        combination_value_sum = 0
        target_combinations = []
        def count_target_combinations(index):
            nonlocal combination_value_sum
            for i in range(index, len(candidates)):
                if combination_value_sum + candidates[i] > target:
                    continue
                if combination_value_sum + candidates[i] == target:
                    target_combinations.append(list(combination_candidate) + [candidates[i]])
                    continue
                combination_candidate.append(candidates[i])
                combination_value_sum += candidates[i]
                count_target_combinations(i)
                combination_candidate.pop()
                combination_value_sum -= candidates[i]
        count_target_combinations(0)
        return target_combinations

# stackでも書いてみる
