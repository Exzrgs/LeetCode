"""
そうか、範囲の長さは固定長でいいのか
countは2個で作ったほうがわかりやすくなる?
"""

# 範囲の長さを変えていく
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

# 範囲の長さは固定で判定
# count2つ
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        NUM_LOWERCASE = 26
        s1_count = [0] * NUM_LOWERCASE
        s2_count = [0] * NUM_LOWERCASE
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1
        
        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1
        
        for right in range(len(s1), len(s2)):
            if matches == NUM_LOWERCASE:
                return True
            
            index = ord(s2[right]) - ord("a")
            if s1_count[index] == s2_count[index]:
                matches -= 1
            s2_count[index] += 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            
            index = ord(s2[right - len(s1)]) - ord("a")
            if s1_count[index] == s2_count[index]:
                matches -= 1
            s2_count[index] -= 1
            if s1_count[index] == s2_count[index]:
                matches += 1
        return matches == NUM_LOWERCASE

# count1つ
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        NUM_LOWERCASE = 26
        char_count = [0] * NUM_LOWERCASE
        for i in range(len(s1)):
            char_count[ord(s1[i]) - ord("a")] += 1
            char_count[ord(s2[i]) - ord("a")] -= 1
        
        matches = char_count.count(0)
        for right in range(len(s1), len(s2)):
            if matches == NUM_LOWERCASE:
                return True
            
            index = ord(s2[right]) - ord("a")
            if char_count[index] == 0:
                matches -= 1
            char_count[index] -= 1
            if char_count[index] == 0:
                matches += 1
            
            index = ord(s2[right - len(s1)]) - ord("a")
            if char_count[index] == 0:
                matches -= 1
            char_count[index] += 1
            if char_count[index] == 0:
                matches += 1
        return matches == NUM_LOWERCASE
