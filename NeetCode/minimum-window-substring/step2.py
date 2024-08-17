from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        right = 0
        left = 0
        t_char_count = Counter(t)
        min_substr = ""
        while right < len(s):
            while max(t_char_count.values()) > 0:
                if right == len(s):
                    return min_substr

                t_char_count[s[right]] -= 1
                right += 1
            while left < len(s) and left <= right and max(t_char_count.values()) <= 0:
                t_char_count[s[left]] += 1
                left += 1
            if min_substr == "" or right - left + 1 < len(min_substr):
                min_substr = s[left - 1 : right]
        return min_substr
