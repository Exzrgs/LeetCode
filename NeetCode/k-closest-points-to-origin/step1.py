"""
Question: 1m
    How is the size of k?
    How is the lenght of points?
        1 <= points.length < 10^4
Discussion: 3m
    n: length of points
    
    sort
        time: O(nlogn)
        space: O(n)

    priority queue
        time: O(n)
        space: O(k)
Coding: 7m
Simple Test: 4m
    (1, 1), (3, 3) k: 1
"""

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for i in range(len(points)):
            distance = points[i][0] ** 2 + points[i][1] ** 2
            heapq.heappush(pq, (distance, i))
        
        res = []
        for _ in range(k):
            _, index = heapq.heappop(pq)
            res.append((points[index][0], points[index][1]))
        return res
