"""
7m

似たような問題をやったことがあるので、スタックで解くのはすぐに思いついた
実装で一度ミスをしてしまって時間をロスしてしまったが、減点されるほどのロスではなさそう
stackが0の場合にpopをしてしまい、一度エラーを踏んでしまったのがよくなかった。そもそもコーナーケースの精査が甘かった。
命名や実装方針に関しては良い感じかも
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        closes = [')', '}', ']']
        for c in s:
            if c in closes:
                if len(stack) == 0 or stack.pop() != pairs[c]:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
