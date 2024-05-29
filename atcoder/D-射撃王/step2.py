"""
priority queueを使うと、ソートを削ってO(N logN)まで落とせそう
入力を受け取る変数名もこだわってみる
    num_inputs
    heights
    speeds
high, low → upper_bound, lower_bound
limit_height, limit_times → height_limit, time_limits
"""
import math

num_inputs = int(input())
heights = []
speeds = []
for _ in range(num_inputs):
    h, s = map(int, input().split())
    heights.append(h)
    speeds.append(s)

upper_bound = 10 ** 19
lower_bound = 1
while upper_bound - lower_bound > 1:
    height_limit = (upper_bound + lower_bound) // 2
    time_limits = []
    for i in range(num_inputs):
        t = math.floor((height_limit - heights[i]) / speeds[i])
        time_limits.append(t)
    time_limits.sort()
    for i in range(num_inputs):
        if time_limits[i] < i:
            lower_bound = height_limit
            break
    else:
        upper_bound = height_limit

print(upper_bound)

# 半開区間?
import math

num_inputs = int(input())
heights = []
speeds = []
for _ in range(num_inputs):
    h, s = map(int, input().split())
    heights.append(h)
    speeds.append(s)

upper_bound = 10 ** 19
lower_bound = 1
while upper_bound >= lower_bound:
    height_limit = (upper_bound + lower_bound) // 2
    time_limits = []
    for i in range(num_inputs):
        t = math.floor((height_limit - heights[i]) / speeds[i])
        time_limits.append(t)
    time_limits.sort()
    for i in range(num_inputs):
        if time_limits[i] < i:
            lower_bound = height_limit + 1
            break
    else:
        upper_bound = height_limit

print(lower_bound)

# 開区間?
import math

num_inputs = int(input())
heights = []
speeds = []
for _ in range(num_inputs):
    h, s = map(int, input().split())
    heights.append(h)
    speeds.append(s)

upper_bound = 10 ** 19
lower_bound = 1
while upper_bound >= lower_bound:
    height_limit = (upper_bound + lower_bound) // 2
    time_limits = []
    for i in range(num_inputs):
        t = math.floor((height_limit - heights[i]) / speeds[i])
        time_limits.append(t)
    time_limits.sort()
    for i in range(num_inputs):
        if time_limits[i] < i:
            lower_bound = height_limit + 1
            break
    else:
        upper_bound = height_limit - 1

print(lower_bound)
