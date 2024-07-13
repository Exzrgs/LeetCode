"""
res, values = "", self.keyStore.get(key, [])
もしかして、こうやって一度listを取り出しておいた方がアクセス速いのか..?
実際、配列のポインタを直接持つわけだから、速くなりそう

半開区間がやっとわかったかもしれない。
二分探索のkey(条件)に対して、
[True, True, True, False, False]
みたいになるときに、
Trueの側を閉区間、Falseの側を開区間にする。

まず、[True..., False...]なのか[False..., True...]なのか考える
で、
閉区間
    == targetのようにドンピシャ
        == の場合を別で処理してよい
    <= targetのようにドンピシャではない
        <= の場合に、resを更新して、範囲から外す(left = mid + 1)
半開区間
    [True..., False]
        right - left > 1, right = mid
            mid = (left + right) // 2
            left = 0
            right = len(nums)
            (なぜかというと、
                最後右に寄った時は、(left + right) // 2なので最右までmidが移らず、2つ目に移る
                最後左に寄った時は、(left + right) // 2なので最左まではmidが移る
            )
        left < right, right = mid - 1
            mid = (left + right + 1) // 2
            left = -1
            right = len(nums) - 1
            (なぜかというと、
                最後右に寄った時は、(left + right + 1) // 2なので最右までmidが移る。
                最後左に寄った時は、(left + right + 1) // 2なので最左まではmidが移らず、2つ目に移る
            )
    [False..., True]
        right - left > 1, left = mid
            mid = (left + right) // 2
            left = 0
            right = len(nums) - 1
            (なぜかというと、
                最後右に寄った時([...False])は、(left + right) // 2なので最右までmidが移らず、2つ目に移る。が、そのとき更新されるのはleftなので、rightが解になる
                    が、rightが正しい解であるかのチェックが必要
                最後左に寄った時([True...])は、(left + right) // 2なので最左までmidが移る。
            )
        left < right, left = mid + 1
            mid = (left + right) // 2
            left = 0
            right = len(nums) - 1

頭がこんがらがったので、一時中断。また今度考えよう...
"""

# bisect_right
from collections import defaultdict
from bisect import bisect_right

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        index = bisect_right(self.store[key], timestamp, key=lambda x: x[1])
        if index == 0:
            return ""
        return self.store[key][index - 1][0]

# 閉区間
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        right = len(self.store[key]) - 1
        res = ""
        while left <= right:
            mid = (left + right) // 2
            if self.store[key][mid][1] <= timestamp:
                left = mid + 1
                res = self.store[key][mid][0]
            else:
                right = mid - 1
        return res

# 半開区間 (right = mid - 1)
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        left = -1
        right = len(self.store[key]) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if self.store[key][mid][1] <= timestamp:
                left = mid
            else:
                right = mid - 1
        if left == -1:
            return ""
        return self.store[key][left][0]

# 半開区間 (right = mid)
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        right = len(self.store[key])
        while right - left > 1:
            mid = (left + right) // 2
            if self.store[key][mid][1] <= timestamp:
                left = mid
            else:
                right = mid
        if (not self.store[key]) or (left == 0 and self.store[key][0][1] > timestamp):
            return ""
        return self.store[key][left][0]
