"""
10m
最初は貪欲に辞書にあれば消していこうとしたが、消さなければ辞書に存在していた可能性にすぐに気づく
そこで、消す、消さないを管理するためにdpを使って、最後が空文字になればよいなと思い実装
空文字が2回入ったりするなと思い、配列の中身はsetを選択
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict_set = set(wordDict)
        dp = [set() for _ in range(len(s) + 1)]
        dp[0].add("")
        for i in range(1, len(s) + 1):
            for current_str in dp[i - 1]:
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
