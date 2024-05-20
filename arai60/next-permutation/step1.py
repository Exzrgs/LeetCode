"""
25m

思考
    右から見て、左に小さくなってる部分が存在したら、そこを入れ替える。
    それより右の部分は降順でソート
    もしどれにも当てはまらなかったら、全体を降順ソートした配列
    
    これだと順番がうまく入れ替わらなくて、右側に自分より大きいものが存在すれば入れ替えてそれより右をソート

反省
    正しいロジックを導き出すのに時間がかかってしまった。たくさんWrong Answerを出してしまった
    自分で長さ4とか5とかのケースを作ってテストすればよかったが、それを怠ってしまった
"""

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        for i in reversed(range(len(nums)-1)):
            for j in reversed(range(i+1, len(nums))):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    nums[i+1:] = sorted(nums[i+1:])
                    return
        nums.sort()
