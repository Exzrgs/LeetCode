"""
見返してみて、row_half_lengthって2^(n-1)じゃなくて2^(n-2)だよなと思って修正

すると、1つ目の解き方がおかしいことに気づく。k >= row_half_lengthの場合分けなんてありえないんじゃないかと思って消したら通った。
ということは、nに依存しないなと思ってめちゃくちゃ削ったが、通った。
0
01
01 10
01 10 10 01
01 10 10 01 10 01 01 10
0-indexedでkが奇数の場合に反転させると正しくなるということ
prev_rowは、偶数番目を抜き出すか、奇数番目を抜き出して反転させたものになる
だから、奇数番目の時だけ反転させるんだな
なんで初期値が0なのかっていう話だけど、一度も反転しないk=0の場合を考えると、0になるから。
"""

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        is_one = False
        k -= 1
        while k > 0:
            if k % 2 == 1:
                is_one = not is_one
            k //= 2
        return int(is_one)

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k == 1:
            return 0
        row_half_length = 2 ** (n - 2)
        if k <= row_half_length:
            return self.kthGrammar(n - 1, k)
        return 1 - self.kthGrammar(n - 1, k - row_half_length)
