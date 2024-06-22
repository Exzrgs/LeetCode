
"""
繰り返し二乗法を実装できればよいが、実装したことがない
多分実装としては、再帰関数でやればよい
n乗を計算する場合、2乗していって、nを超える直前になったら、やめる
そのときがm乗だったとすると、n-mに対して、同じことをやる
これを1乗とかになるまで繰り返す?

マイナスもあるのか
最初にプラスで扱えるように工夫すればよい

変数名が全体的に良くない
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def compute_pow(x, n):
            if n == 0:
                return 1
            current_pow = 1
            current_num = x
            while current_pow + current_pow <= n:
                current_num *= current_num
                current_pow += current_pow
            return current_num * compute_pow(x, n - current_pow)
        if n >= 0:
            return compute_pow(x, n)
        else:
            return compute_pow(1 / x, -n)
