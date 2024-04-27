"""
算術をスペース入れずにやってしまう癖を直す
start_index → left
enumerateを使う
answerに代入する処理の位置を変える
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict()
        answer = 0
        left = 0
        for right, c in enumerate(s):
            if c in seen and seen[c] >= left:
                left = seen[c] + 1
            seen[c] = right
            answer = max(answer, right - left + 1)
        
        return answer
