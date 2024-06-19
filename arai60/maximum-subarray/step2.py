"""
https://github.com/YukiMichishita/LeetCode/pull/13/files
    mathのinfを使っている。Pythonのinf周りは調べたことがなかったので、これを機に詳しく調べてみよう
    
    https://docs.python.org/ja/3/library/math.html#math.inf
    math.inf
        float('inf')と等価
        math.isinf()で確認できる
        
        float
            https://docs.python.org/ja/3/library/functions.html#float
            floatはクラスで、float()でコンストラクタを呼び出している。この辺よく考えたことなかったけど、たしかにそうだ
            だからfloatクラスに文字列型を引数としてとるコンストラクタを作っておく。それでfloat("inf")とかを表現する
            
            <- 一般の Python オブジェクト x に対して、float(x) は x.__float__() に委譲します。 __float__() が定義されていない場合、__index__() へフォールバックします。
                https://docs.python.org/ja/3/reference/datamodel.html#object.__float__
                __float__()は数値型のオブジェクトに実装されているメソッド。数値型の抽象クラスに抽象メソッドとして定義されている?
                このdatamodelのドキュメント、今じゃなくていいが、javaの勉強が終わったタイミングで通読しよう
                ~のドキュメント通読とかのPR作るとよい
            <- 引数が与えられなければ、0.0 が返されます。
        
    math.nan
        float('nan')と等価
        math.isnan()で確認できる
        
        NAN
            https://ja.wikipedia.org/wiki/NaN
            非数
            主に浮動小数点演算の結果として、不正なオペランドを与えられたために生じた結果を表す値またはシンボル
            
            quiet nan(qNAN)
                不正な操作や不正な値で生じる誤りを伝播させるために使用
            signaling nan(sNAN)
                (読んだけどよくわからなかった)
    math.e
        自然対数の底
    math.pi
        π
    
    mathモジュール
        ほとんどがC言語の数学ライブラリ関数に対する薄いラッパでできている

https://github.com/SuperHotDogCat/coding-interview/pull/14/files
    cumulative sum: 累積和

https://github.com/shining-ai/leetcode/pull/33/files
    <- 個人的には変数名はフルスペルで書いたほうが良いと思います。所属チーム内でどのような省略形を用いて良いか合意形成が得られているのであれば、それに従って省略しても良いと思います。
        この視点は重要。一概に省略が悪いのではなく、慣習に従うのが良いということ
    current_sumじゃなくてcurrent_subarray_sumのほうが良いのかも
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_subarray_sum = nums[0]
        for i in range(1, len(nums)):
            current_subarray_sum = max(current_subarray_sum + nums[i], nums[i])
            max_sum = max(max_sum, current_subarray_sum)
        return max_sum
