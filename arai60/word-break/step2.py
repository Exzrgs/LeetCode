"""
wordの最大長で枝狩りしたほうがよいという話はたしかに
みんな再帰で書いているんだな。自分としてはスライスの計算量が気になるので、文字列連結の最適化を期待するほうが良い気がした
    文字列はimmutableなので、毎回再構築をしないといけない
    Pythonだと、参照カウントが1の場合は最適化をしてO(1)になる。が、参照カウント>=2だとO(N)かかるっぽい
    このコードだと最適化はされていなさそう?

前を削っていくような実装もできる。残ってる文字列を管理して、indexを右に見ていって、wordなら再帰する
        for i in range(1, len(remaining_s)):
            prefix = remaining_s[:i]
            if prefix in wordSet and self.dfs(remaining_s[i:], wordSet, memo):
                memo[remaining_s] = True
                return True
"""

# dp
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict_set = set(wordDict)
        max_word_len = max([len(word) for word in wordDict])
        dp = [set() for _ in range(len(s) + 1)]
        dp[0].add("")
        for i in range(1, len(s) + 1):
            for current_str in dp[i - 1]:
                if len(current_str) + 1 > max_word_len:
                    continue
                
                next_str = current_str + s[i - 1]
                dp[i].add(next_str)
                if next_str in word_dict_set:
                    dp[i].add("")
        return "" in dp[len(s)]

# メモ化再帰
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict_set = set(wordDict)
        memo = dict()
        def can_word_break(current_index, start_index):
            if current_index == len(s):
                return current_index == start_index
            
            if (current_index, start_index) in memo:
                return memo[(current_index, start_index)]
            
            if can_word_break(current_index + 1, start_index):
                memo[(current_index, start_index)] = True
                return True
            if s[start_index : current_index + 1] in word_dict_set and can_word_break(current_index + 1, current_index + 1):
                memo[(current_index, current_index)] = True
                return True
            memo[(current_index, start_index)] = False
            return False
        
        return can_word_break(0, 0)
