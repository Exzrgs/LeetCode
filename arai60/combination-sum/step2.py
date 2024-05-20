"""
combination_value_sumは、引数にしたほうが良い
countじゃなくてgenerateのほうが適切
再帰する前に判定するよりも、再帰してからtargetに等しいかなどを判定したほうが、配列に追加済みなので簡単

combination_value_sum、ちょっと名前が冗長な気がしつつ、短縮するアイデアがない
再帰の深さにも注意。sys.setrecursionlimitとか
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combination = []
        target_combinations = []
        def generate_target_combinations(index, combination_value_sum):
            if combination_value_sum == target:
                target_combinations.append(list(combination))
                return
            if combination_value_sum > target:
                return
            for i in range(index, len(candidates)):
                combination.append(candidates[i])
                generate_target_combinations(i, combination_value_sum + candidates[i])
                combination.pop()
        generate_target_combinations(0, 0)
        return target_combinations
