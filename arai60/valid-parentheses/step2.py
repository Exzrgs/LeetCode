"""
closes→closers
stackの宣言の位置は直前でよい
closersがpairs.keys()でよいのはたしかに。

かっこが英語でbracketやparenthesisというのは押さえておく
"""
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        closers = pairs.keys()
        stack = []
        for c in s:
            if c in closers:
                if len(stack) == 0 or stack.pop() != pairs[c]:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
