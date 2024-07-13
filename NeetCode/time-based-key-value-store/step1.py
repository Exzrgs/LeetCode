"""
Question:
    What is the format of timestamp?
    How many times the set function could be called?
    Timestamps could be duplicate?
        If these cloud be duplicate, which value should I return in get method?
    (If there is no value satisfying the condition of get method, what shoud I return?)
    (How long is the key?)
Discussion:
    We can create get method time complexity O(logn) by using binary search
    and n is the number of same value timestamps
    We can create sorted array just by appending timestamp to the array
    because time is accending
"""

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
