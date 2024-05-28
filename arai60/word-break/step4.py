"""
"""

# dp
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        can_break = [False] * (len(s) + 1)
        can_break[0] = True
        max_word_len = max([len(word) for word in wordDict])
        word_dict_set = set(wordDict)
        for start in range(len(s)):
            if not can_break[start]:
                continue
            for end in range(start + 1, min(start + max_word_len + 1, len(s) + 1)):
                if s[start:end] in word_dict_set:
                    can_break[end] = True
        return can_break[len(s)]

# メモ化再帰
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict_set = set(wordDict)
        max_word_len = max([len(word) for word in wordDict])
        memo = dict()
        def can_word_break(start):
            if start == len(s):
                return True
            
            if start in memo:
                return memo[start]
            
            for end in range(start + 1, min(start + max_word_len + 1, len(s) + 1)):
                if s[start:end] in word_dict_set and can_word_break(end):
                    memo[start] = True
                    return True
            memo[start] = False
            return False
        
        return can_word_break(0)

# startswith
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        can_break = [False] * (len(s) + 1)
        can_break[0] = True
        for start in range(len(s)):
            if not can_break[start]:
                continue
            for word in wordDict:
                if s.startswith(word, start):
                    can_break[start + len(word)] = True
        return can_break[len(s)]
