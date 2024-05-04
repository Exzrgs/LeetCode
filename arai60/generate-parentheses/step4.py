"""
nは定数だから引数に含めなくてよい
関数名がparenthesisだから変数名もそれに合わせたほうが良い
毎回open_countを数えると計算量がn倍増えるから引数で管理
毎回list化すると計算量がn倍増えるからpopするようにする
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        brackets_combinations = []
        def append_bracket(parentheses, open_count):
            if len(parentheses) == n * 2:
                brackets_combinations.append("".join(parentheses))
                return

            close_count = len(parentheses) - open_count
            if open_count < n:
                parentheses.append("(")
                append_bracket(parentheses, open_count+1)
                parentheses.pop()
            if open_count > close_count:
                parentheses.append(")")
                append_bracket(parentheses, open_count)
                parentheses.pop()

        append_bracket([], 0)
        return brackets_combinations
