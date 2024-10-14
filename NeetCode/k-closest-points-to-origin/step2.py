"""
enumerate
tuple
"""

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for i, (x, y) in enumerate(points):
            distance = x ** 2 + y ** 2
            heapq.heappush(pq, (distance, i))
        
        res = []
        for _ in range(k):
            _, index = heapq.heappop(pq)
            res.append(tuple(points[index]))
        return res
