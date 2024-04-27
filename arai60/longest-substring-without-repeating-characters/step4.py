"""
returnの前の改行をなくす
answer → max_length
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_to_index = dict()
        max_length = 0
        left = 0
        for right, c in enumerate(s):
            if c in char_to_index and char_to_index[c] >= left:
                left = char_to_index[c] + 1
            char_to_index[c] = right
            max_length = max(max_length, right - left + 1)
        return max_length
