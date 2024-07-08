"""
find future day more warmer than ith day's temperature
I see, the range of temperatures are small
so, we can have the array has list as element [[] for _ in range()]
the index represents temperature
and the value list are sorted days
so you can find most recent future day by binary search
and the time complexity is O(nlogn) and n is length of temperatures array

min_heapを持っておいて今までの気温を持っておく。毎回自分より小さいやつがmin_heapに入ってるか確認して、その分popしてanswerに記録するのでもいいのか
O(nlogn)だけど、気温のぶんループしなくて済むから、定数倍が小さい

スタックでいいのか。自分より小さかったらpopできるので、自動的にスタックはdecending orderになる。
O(n)
なんだろうな、iterateするときに、そのvalueが主体だと思い込みすぎている。だからbinary searchという選択肢が出てくる
そうじゃなくて、stackにpushしておくと、あとで大きいのがきたときにpopすればよいからっていう思考
つまり、左から自分より小さいやつを見つけたいっていうふうに思考できれば、stackが思いついたかも
"""

from collections import defaultdict
from bisect import bisect_right

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        MIN_TEMPERATURE = min(temperatures)
        MAX_TEMPERATURE = max(temperatures)
        INF = 10 ** 9
        temperature_to_days = defaultdict(list)
        for d, t in enumerate(temperatures):
            temperature_to_days[t].append(d)
        for t in range(MIN_TEMPERATURE, MAX_TEMPERATURE + 1):
            temperature_to_days[t].sort()
        waits = [INF] * len(temperatures)
        for d, t in enumerate(temperatures):
            for t2 in range(t + 1, MAX_TEMPERATURE + 1):
                idx = bisect_right(temperature_to_days[t2], d)
                if idx < len(temperature_to_days[t2]) and temperature_to_days[t2][idx] > d:
                    waits[d] = min(waits[d], temperature_to_days[t2][idx] - d)
            if waits[d] == INF:
                waits[d] = 0
        return waits

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        wait_days = [0] * len(temperatures)
        stack = []
        for d, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                d2 = stack.pop()[0]
                wait_days[d2] = d - d2
            stack.append((d, t))
        return wait_days
