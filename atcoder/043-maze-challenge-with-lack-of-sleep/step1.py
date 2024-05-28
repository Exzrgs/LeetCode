"""
位置、向き、回数を持って探索するとよさそう
"""
from heapq import heappop, heappush

num_rows, num_columns = map(int, input().split())
start_row, start_column = map(int, input().split())
start_row -= 1
start_column -= 1
goal_row, goal_column = map(int, input().split())
goal_row -= 1
goal_column -= 1
board = [input() for _ in range(num_rows)]

direction_x = [0, 0, 1, -1]
direction_y = [1, -1, 0, 0]
visited = [[[False] * 4 for _ in range(num_columns)] for _ in range(num_rows)]
processing = []
for direction_index in range(4):
    heappush(processing, (0, start_row, start_column, direction_index))
while processing:
    num_rotate, r, c, direction_index = heappop(processing)
    if r == goal_row and c == goal_column:
        print(num_rotate)
        exit()
    if visited[r][c][direction_index]:
        continue
    visited[r][c][direction_index] = True
    
    for i in range(4):
        next_r = r + direction_x[i]
        next_c = c + direction_y[i]
        if not (0 <= next_r < num_rows and 0 <= next_c < num_columns and board[next_r][next_c] == "." and not visited[next_r][next_c][i]):
            continue
        if i == direction_index:
            next_num_rotate = num_rotate
        else:
            next_num_rotate = num_rotate + 1
        heappush(processing, (next_num_rotate, next_r, next_c, i))

# 01bfs
from collections import deque

num_rows, num_columns = map(int, input().split())
start_row, start_column = map(int, input().split())
start_row -= 1
start_column -= 1
goal_row, goal_column = map(int, input().split())
goal_row -= 1
goal_column -= 1
board = [input() for _ in range(num_rows)]

direction_x = [0, 0, 1, -1]
direction_y = [1, -1, 0, 0]
visited = [[[False] * 4 for _ in range(num_columns)] for _ in range(num_rows)]
processing = deque()
for direction_index in range(4):
    processing.append((start_row, start_column, direction_index, 0))
while processing:
    r, c, direction_index, num_rotate = processing.popleft()
    if r == goal_row and c == goal_column:
        print(num_rotate)
        exit()
    if visited[r][c][direction_index]:
        continue
    visited[r][c][direction_index] = True
    
    for i in range(4):
        next_r = r + direction_x[i]
        next_c = c + direction_y[i]
        if not (0 <= next_r < num_rows and 0 <= next_c < num_columns and board[next_r][next_c] == "." and not visited[next_r][next_c][i]):
            continue
        if i == direction_index:
            processing.appendleft((next_r, next_c, i, num_rotate))
        else:
            processing.append((next_r, next_c, i, num_rotate + 1))
