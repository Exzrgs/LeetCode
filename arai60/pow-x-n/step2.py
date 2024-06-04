"""
https://github.com/hayashi-ay/leetcode/pull/41/files
    解き方がとても豊富
    関数の中でマイナスの工夫をしている
    再帰呼び出しで書いている。これも一度書いてみてもよいかも
    変数名poweredは確かに。何をされる数なのかというところを説明する変数名にするのが良い。powered_numとかでもよいかも
https://github.com/SuperHotDogCat/coding-interview/pull/15/files
    1/xを入れるんじゃなくて、xを入れてから最後に逆数を取る。なるほど
    なんとなく引数のnを触るの嫌だなあと思っていたが、値渡しだから別に良いのかも
https://github.com/shining-ai/leetcode/pull/45/files
    returnのときelseで処理しなくてよいのか、なるほど
    
    pow()の実装を見ている。(https://github.com/python/cpython/blob/109fc2792a490ee5cd8a423e17d415fbdedec5c8/Objects/longobject.c#L4244-L4447)
    def calculate_power(base, exp):
        current_bit = 1 << exp.bit_length() - 1
        power_result = 1
        while current_bit:
            power_result *= power_result
            if exp & current_bit:
                power_result *= base
            current_bit >>= 1
        return power_result

繰り返し二乗法(Binary Exponentation)
関数名powerでよい
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x, n):
            if n == 0:
                return 1
            exp = 1
            powered = n
            while exp + exp <= n:
                powered *= powered
                exp += exp
            return powered * power(x, n - powered)
        
        if n < 0:
            return 1 / power(x, -n)
        return power(x, n)

# nを2進数でみて、2^?乗をすべきかどうかを見ていく
# 同じ状態にはならないので、メモ化はいらない
# 再帰
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x, n):
            if n == 0:
                return 1
            if n % 2 == 1:
                return x * power(x * x, n // 2)
            return power(x * x, n // 2)
        
        if n < 0:
            return 1 / power(x, -n)
        return power(x, n)

# ループ
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x, n):
            powered = 1
            binary_exp = x
            while n > 0:
                if n % 2 == 1:
                    powered *= binary_exp
                n //= 2
                binary_exp *= binary_exp
            return powered
        
        if n < 0:
            return 1 / power(x, -n)
        return power(x, n)
