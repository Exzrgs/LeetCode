"""
部分和問題的なやつ
動的計画法で解けそう
というか、この制約ならそもそも全探索できる
あ、10^4か
負の数があるから累積和を取って二分探索とかはできない
累積和を取って、出現したやつを辞書に入れておく。左からk-和が存在するかどうかを見ていく
    これだと、自分より右にある累積和と左にある累積和で区別がつかない
    右にある場合は、差は-kになってしまうので
進行しながら行えば問題ない

step1はスピード重視でやるようにしよう。いざやるときにのんびりしてたらダメなので...
"""
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        num_equal_subarray = 0
        sum_subarray_values = 0
        subarray_sum_to_count = defaultdict(int)
        subarray_sum_to_count[0] = 1
        for n in nums:
            sum_subarray_values += n
            num_equal_subarray += subarray_sum_to_count[sum_subarray_values - k]
            subarray_sum_to_count[sum_subarray_values] += 1
        return num_equal_subarray
