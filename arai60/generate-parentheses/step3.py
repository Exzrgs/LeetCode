"""
4m50s
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        brackets_combinations = []
        def append_bracket(bracket_limit, brackets):
            if len(brackets) == bracket_limit * 2:
                brackets_combinations.append("".join(brackets))
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
        return brackets_combinations
