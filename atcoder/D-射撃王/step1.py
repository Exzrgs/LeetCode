"""
割る順番を決める
高度を二分探索して、その高度になるまでの時間のリストを達成できるかを調べる

O(N (logN)^2)
"""
import math

N = int(input())
H = []
S = []
for _ in range(N):
    h, s = map(int, input().split())
    H.append(h)
    S.append(s)

high = 10 ** 19
low = 1
while high - low > 1:
    limit_height = (high + low) // 2
    limit_times = []
    for i in range(N):
        t = math.floor((limit_height - H[i]) / S[i])
        limit_times.append(t)
    limit_times.sort()
    for i in range(N):
        if limit_times[i] < i:
            low = limit_height
            break
    else:
        high = limit_height

print(high)
