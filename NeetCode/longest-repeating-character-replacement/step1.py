"""
Question:
    Can you tell me example of this problem?
    How is the length of string s?
    What char is contained string s?
        Does string s contains only uppercase English char?
Discussion:
    We can solve this problem by doing dynamic programming
    counts[char][op_count]
    time complexity: O(k * n), n is the length of string s

    なるほど
    範囲を持っておく
    その範囲の中で、一番多いchar_countを持っておく
    範囲 - max_count(= 置換しないといけない数)がkより大きかったら、範囲を狭めないといけない
    そのとき、範囲から出たcharのcountを減らしておく
"""
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = defaultdict(int)
        left = 0
        for right in range(len(s)):
            char_count[s[right]] += 1
            if (right - left + 1) - max(char_count.values()) > k:
                char_count[s[left]] -= 1
                left += 1
        return right - left + 1
