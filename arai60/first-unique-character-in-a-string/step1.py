"""
2m30s

ループ1回で終わらせたいとは思ったが、2回にしてしまったほうがシンプルになると思ったのでそうした
"""

from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = defaultdict(int)
        for c in s:
            char_count[c] += 1
        for i, c in enumerate(s):
            if char_count[c] == 1:
                return i
        return -1
