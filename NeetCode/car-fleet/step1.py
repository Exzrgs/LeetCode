"""
until target, how many cars fleets
compute the time to visit target for each car
but you have to be care the car cannot pass another car
you have to iterate through cars decending order by position
while you find the car less time than initially extra position car, increment fleet count by 1
and get max fleet count as result

runするまでバグが多いのと、変数名がちょっと悪い...
一発で通せるようになりたい
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [0] * len(position)
        for i in range(len(position)):
            times[i] = (target - position[i]) / speed[i] 
        index_and_position = []
        for i, p in enumerate(position):
            index_and_position.append((i, p))
        index_and_position.sort(key=lambda x: x[1], reverse=True)
        fleet_count = len(position)
        first_fleet_idx = index_and_position[0][0]
        for i in range(1, len(index_and_position)):
            car_index, _ = index_and_position[i]
            if times[first_fleet_idx] >= times[car_index]:
                fleet_count -= 1
            else:
                first_fleet_idx = car_index
        return fleet_count
