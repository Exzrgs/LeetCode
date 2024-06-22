"""
再帰では、関数の中でnが負の場合を判定するようにした。
ループでは関数化するのをやめた
binary_exp → base
"""

# 再帰
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n < 0:
            x = 1 / x
            n = -n
        if n % 2 == 1:
            return x * self.myPow(x * x, n // 2)
        return self.myPow(x * x, n // 2)

# ループ
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1 / x
        
        powered = 1
        base = x
        while n > 0:
            if n % 2 == 1:
                powered *= base
            n //= 2
            base *= base
        return powered
