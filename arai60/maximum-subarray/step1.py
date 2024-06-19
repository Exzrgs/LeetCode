"""
配列を見ていきながら、最大値を更新すればよい
max_sumの初期値については少し悩んだ。-10**18のようにしようかとも思ったが、マジックナンバーは微妙だと思った。
    よって、配列の1番目にしておくのが安全かな、と思ってそうした
また、その場合配列の長さが0の場合にエラーになるな、とは思ったが、制約で保障されているので特別な処理は入れなかった
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(current_sum + nums[i], nums[i])
            max_sum = max(max_sum, current_sum)
        return max_sum
