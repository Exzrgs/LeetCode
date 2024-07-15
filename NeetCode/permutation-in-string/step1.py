"""
Question:
    How is the length of s1 and s2?
    Can I think that s1 and s2 have only number?
Discussion:
    We can solve this problem by doing sliding window
    Initially count the char of s1
    and then we have two pointers left and right
    and we are gonna scan through s2 substracting s2[right] char count by 1
    When we find count[s2[right]] <= 0, increment left and count[s2[left]] by 1 while count[s2[right]] <= 0
    
    time complexity: O(n)
    space complexity: O(1)

Simple Test:
    s1: "ab"
    s2: "bbbab"

    s1: "ab"
    s2: "aaa"
"""
from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_count = defaultdict(int)
        for c in s1:
            char_count[c] += 1
        left = 0
        for right in range(len(s2)):
            char_count[s2[right]] -= 1
            while char_count[s2[right]] < 0:
                char_count[s2[left]] += 1
                left += 1
            if right - left + 1 == len(s1):
                return True
        return False
