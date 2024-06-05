"""
even_odd → is_one
row_half_lengthを定義
条件を一行にまとめる
k % 2 != 0 → k % 2 == 1
"""

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        is_one = False
        k -= 1
        while k > 0:
            row_half_length = 2 ** (n - 1)
            if (k < row_half_length and k % 2 == 1) or (k >= row_half_length and k % 2 == 0):
                is_one = not is_one
            k //= 2
            n -= 1
        return int(is_one)

# 反転を利用する
# k < row_half_lengthだったら、圧縮後(前のrow)のままでよい・
# そうじゃなかったら、反転させたものに対してk-row_half_length番目だから、反転させるとよい
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k == 1:
            return 0
        row_half_length = 2 ** (n - 1)
        if k <= row_half_length:
            return self.kthGrammar(n - 1, k)
        return 1 - self.kthGrammar(n - 1, k - row_half_length)
