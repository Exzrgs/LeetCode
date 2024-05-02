"""
条件が満たされたときにその場で追加すればよい。返り値で管理しようとしてたのに引っ張られて実装してしまった

listじゃなく文字列で管理すれば簡潔には書けるが、再構築の可能性があるのがちょっと微妙
leetcodeのsolutionsだとみんなopen_countとclose_countを引数にして、状態は文字列で管理してるんだな
初期値を["("]にするのはたしかに
"""

#dfs listで管理
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        bracket_combinations = []
        def append_bracket(bracket_limit, brackets):
            if len(brackets) == bracket_limit * 2:
                bracket_combinations.append("".join(brackets))
                return
            
            open_count = brackets.count("(")
            close_count = brackets.count(")")
            if open_count < bracket_limit:
                new_brackets = list(brackets)
                new_brackets.append("(")
                append_bracket(bracket_limit, new_brackets)
            if open_count > close_count:
                new_brackets = list(brackets)
                new_brackets.append(")")
                append_bracket(bracket_limit, new_brackets)
        
        append_bracket(n, [])
        return bracket_combinations

#bfs
from collections import deque

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        bracket_combinations = []
        processing_brackets = deque()
        processing_brackets.append([])

        while len(processing_brackets) > 0:
            brackets = processing_brackets.popleft()
            if len(brackets) == 2 * n:
                bracket_combinations.append("".join(brackets))
                continue
            
            open_count = brackets.count("(")
            close_count = brackets.count(")")
            if open_count < n:
                new_brackets = list(brackets)
                new_brackets.append("(")
                processing_brackets.append(new_brackets)
            if open_count > close_count:
                new_brackets = list(brackets)
                new_brackets.append(")")
                processing_brackets.append(new_brackets)
        
        return bracket_combinations
