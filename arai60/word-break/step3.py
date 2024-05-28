"""
再帰だけ練習
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict_set = set(wordDict)
        memo = dict()
        def can_word_break(remaining_s):
            if remaining_s in memo:
                return memo[remaining_s]
            if remaining_s in word_dict_set:
                return True
            
            for i in range(1, len(remaining_s)):
                prefix = remaining_s[:i]
                if prefix in word_dict_set and can_word_break(remaining_s[i:]):
                    memo[remaining_s] = True
                    return True
            memo[remaining_s] = False
            return False
        return can_word_break(s)

