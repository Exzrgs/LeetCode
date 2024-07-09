"""
なるほど、p, sのpairsを作って、それをソートすればよかった。そしたらその場でtimeが計算できる
zip関数は使いこなせるようになりたい
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_and_speeds = [(p, s) for p, s in zip(position, speed)]
        pos_and_speeds.sort(reverse=True)
        fleet_count = len(position)
        fleet_time = 0
        for p, s in pos_and_speeds:
            t = (target - p) / s
            if fleet_time >= t:
                fleet_count -= 1
            else:
                fleet_time = t
        return fleet_count

# stackを使う
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_and_speeds = [(p, s) for p, s in zip(position, speed)]
        pos_and_speeds.sort(reverse=True)
        fleet_times = []
        for p, s in pos_and_speeds:
            t = (target - p) / s
            if not fleet_times or fleet_times[-1] < t:
                fleet_times.append(t)
        return len(fleet_times)
