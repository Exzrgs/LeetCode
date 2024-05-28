"""
割とみんな同じような解き方。

char_count → char_to_count
"""

from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_to_count = defaultdict(int)
        for c in s:
            char_to_count[c] += 1
        for i, c in enumerate(s):
            if char_to_count[c] == 1:
                return i
        return -1
