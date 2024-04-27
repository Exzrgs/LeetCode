"""
算術をスペース入れずにやってしまう癖を直す
start_index → left
enumerateを使う
answerに代入する処理の位置を変える

char_to_indexのほうがよさそう
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_to_index = dict()
        answer = 0
        left = 0
        for right, c in enumerate(s):
            if c in char_to_index and char_to_index[c] >= left:
                left = char_to_index[c] + 1
            char_to_index[c] = right
            answer = max(answer, right - left + 1)
        
        return answer
