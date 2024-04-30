"""
pairs→closer_to_opener
"""
class Solution:
    def isValid(self, s: str) -> bool:
        closer_to_opener = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        stack = []
        for c in s:
            if c in closer_to_opener:
                if len(stack) == 0 or stack.pop() != closer_to_opener[c]:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
