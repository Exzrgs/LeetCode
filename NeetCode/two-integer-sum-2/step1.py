"""
of course you can solve this problem if you use for roop twice
the time complexity is O(n^2)

but you can solve this problem O(nlogn) if you use binary search
you can find index2 by search numbers array using (target - index1) as binary search key

これすげえ
たしかに左右でポインターを持っておくと、小さかったら左を寄せて、大きかったら右を寄せるでいける
なぜなら、右はすでに最大で、左はすでに最小だから
こういう同調させる系みたいなのが苦手だな。どうしても片方固定したくなってしまう
それと、二分探索で解ける典型的な問題だったのもある
単調性を利用する手段として、左右から見るという視点がなかった
考えてみると尺取り法っぽさがある。苦手
O(n)
"""
from bisect import bisect_left

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index1 in range(len(numbers)):
            index2 = bisect_left(numbers, target - numbers[index1], lo=index1 + 1)
            if index2 == len(numbers) or numbers[index1] + numbers[index2] != target:
                continue
            return [index1 + 1, index2 + 1]

# O(n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            res = numbers[left] + numbers[right]
            if res < target:
                left += 1
            elif res > target:
                right -= 1
            else:
                return [left + 1, right + 1]
