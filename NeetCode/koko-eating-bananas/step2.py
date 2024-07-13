"""
なぜ
if total_time >= h:
    left = mid
else:
    right = mid
としてleftを返したらいけないのかわかってない...

閉区間に関しても、
total_time >= h:
    min_speed = mid
    left = mid + 1
にするとうまくいかない。rightの方向がTrueでleftの方向がFalseだから?
[False, False, False, True, True]
こういうことか

https://github.com/Exzrgs/LeetCode/pull/44/files#diff-d5d444e47cf7d1d20a8eb4bb65b52c18d549a6d47f587378c49815e0e75bb516R2-R7
    こっちの場合は、matrix[mid][0] > targetに関して、
    [False, False, False, True, True]みたいになって、
    Falseの側に解があるからleftか

閉区間の方は、解を含むようにする。初期値や更新もあわせて。left = 0, if (<=) left = mid
開区間の方は、解を含まないようにする。初期値や更新もあわせて right = len(nums), if (>) right = mid

例えば半開区間でも、equalを別で処理できれば、left = mid + 1のようにすることもできる。
    今回の問題だと、ドンピシャのtargetのindexを見つけるような問題ではないので、if total_time <= hで解を更新しないといけない。
    しかし、やはりright = mid - 1に更新する際は、mid = (left + right + 1) // 2としないとうまくいかない。
"""

# rightが閉区間の半開区間 (right = mid)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 0
        right = max(piles)
        while right - left > 1:
            mid = (left + right) // 2
            total_time = 0
            for n in piles:
                total_time += (n + mid - 1) // mid
            if total_time <= h:
                right = mid
            else:
                left = mid
        return right

# rightが閉区間の半開区間 (right = mid - 1)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 0
        right = max(piles)
        min_speed = right
        while left < right:
            mid = (left + right + 1) // 2
            total_time = 0
            for n in piles:
                total_time += (n + mid - 1) // mid
            if total_time <= h:
                min_speed = mid
                right = mid - 1
            else:
                left = mid
        return min_speed

# 閉区間
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        min_speed = right
        while left <= right:
            mid = (left + right) // 2
            total_time = 0
            for n in piles:
                total_time += (n + mid - 1) // mid
            if total_time <= h:
                min_speed = mid
                right = mid - 1
            else:
                left = mid + 1
        return min_speed
