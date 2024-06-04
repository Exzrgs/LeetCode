"""
cacheを使う
    https://zenn.dev/judenfly/articles/judenfly-20240401
    cacheって要は引数をハッシュとしてメモをしているだけなので、やっていることは変わらない
    つまり、引数はhashableでなければならない

この@というのも、どういうものなのか調べておきたい
https://zenn.dev/ryo_kawamata/articles/learn_decorator_in_python
    デコレータ
        他の関数を装飾するための特殊な関数
        関数の動作を修正したり、拡張したり
        関数を引数にとって、新しい装飾した関数を返す
            ミドルウェアみたいなものか。関数に前処理や後処理を追加することができる
        ロギングとかキャッシュとかね
    def hoge(f):
        return f
    @hoge
    def fuga():
    こんな感じで自分でも定義して使える

浮動小数点数(floating-point number)について復習
    IEEE 754
    符号部(sign)、指数部(exponent)、仮数部(fraction)
    単精度: 32bit (1, 8, 23)
    倍精度: 64bit (1, 11, 52)
    
    0.111 * 2^4
    符号部0, 指数部100, 仮数部111
    仮数部は0.〇〇のところまで正規化する
    
    下駄ばき
        指数部は引いて考える。指数部でマイナスを扱いたいため。
        単精度の場合、0~255乗まで表せるので、-127~128にするために、127を引く
    
    その他
        指数部がMAX:
            仮数部が0: 符号方向の無限
            仮数部が0以外: 非数NaN
        指数部, 仮数部が0: 0
"""
from functools import lru_cache

def parse_inputs():
    n, divider, divide_fee, dice_fee = map(int, input().split())
    return n, divider, divide_fee, dice_fee

def main():
    n, divider, divide_fee, dice_fee = parse_inputs()
    
    @lru_cache
    def compute_expected_value(n):
        if n == 0:
            return 0
        divide_expected_value = compute_expected_value(n // divider) + divide_fee
        dice_expected_value = 6 * dice_fee
        for i in range(2, 7):
            dice_expected_value += compute_expected_value(n // i)
        dice_expected_value /= 5
        return min(divide_expected_value, dice_expected_value)
    
    print(compute_expected_value(n))

if __name__ == '__main__':
    main()
