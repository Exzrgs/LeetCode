"""
https://github.com/YukiMichishita/LeetCode/pull/13/files
    mathのinfを使っている。Pythonのinf周りは調べたことがなかったので、これを機に詳しく調べてみよう

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
