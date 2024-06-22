"""
6/4
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x: int, n: int):
            powered = 1
            exp = x
            while n > 0:
                if n % 2 == 1:
                    powered *= exp
                n //= 2
                exp *= exp
            return powered
        if n < 0:
            return 1 / power(x, -n)
        return power(x, n)
