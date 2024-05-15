"""
出現した文字を集合で管理して判定するとよさそう
連続でなければならないのに気づいていなかった。サンプルを最初にちゃんと確認しなければ。
連続ならば、すでに出現したものが現れたときにリセットすればよい
いや、被りが来た時点で、被りの次のindexから始めることにしないといけない
辞書で管理するほうが良いか
if seen.get(s[i]) andというような条件にしてしまっていて、seen.get(s[i]) == 0の場合が弾かれてしまっていたのに気づくのに時間がかかってしまった...

経過時間:22m
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict()
        answer = 0
        start_index = 0
        for i in range(len(s)):
            if s[i] in seen and seen.get(s[i]) >= start_index:
                answer = max(answer, i-start_index)
                start_index = seen.get(s[i])+1
            seen[s[i]] = i
        answer = max(answer, len(s)-start_index)
        
        return answer
