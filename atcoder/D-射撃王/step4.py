"""
二分探索の部分を関数として切り分けることはできた。
が、classの部分の理解が浅いので、ちゃんと勉強したい
    SはListの特性をもった独自型だろう
    __getitem__は、配列のアクセスに対する振る舞いを定義できるのだろう
    __len__は、len()に対する振る舞いを定義できるのだろう
というくらいの理解
"""

import math
from bisect import bisect_left
from collections.abc import Sequence

def parse_inputs():
    num_inputs = int(input())
    heights = []
    speeds = []
    for _ in range(num_inputs):
        h, s = map(int, input().split())
        heights.append(h)
        speeds.append(s)
    return num_inputs, heights, speeds

def compute_min_score(num_inputs, heights, speeds):
    class S(Sequence):
        def __getitem__(self, index):
            if not (0 <= index < len(self)):
                raise IndexError
            return index
        def __len__(self):
            return max(heights) + max(speeds) * num_inputs
    
    def scorable(height_limit):
        time_limits = []
        for i in range(num_inputs):
            t = math.floor((height_limit - heights[i]) / speeds[i])
            time_limits.append(t)
        time_limits.sort()
        for i in range(num_inputs):
            if time_limits[i] < i:
                return False
        return True
    
    s = S()
    return bisect_left(s, True, key=scorable)

def main():
    num_inputs, heights, speeds = parse_inputs()
    print(compute_min_score(num_inputs, heights, speeds))

if __name__ == '__main__':
    main()
