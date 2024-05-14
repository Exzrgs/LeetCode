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
