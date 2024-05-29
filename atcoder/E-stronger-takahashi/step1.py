"""
パンチを出した回数を持っておく
***
x**
***
xを壊そうと思ったら、その周りも全部壊せる。
つまり、パンチを1増やしたときは、3*3の区間に対して進めばよい
"""

from collections import deque
num_rows, num_columns = map(int, input().split())
board = [input() for _ in range(num_rows)]
START_ROW = 0
START_COLUMN = 0
GOAL_ROW = num_rows - 1
GOAL_COLUMN = num_columns - 1
NOT_VISITED = 10 ** 18
direction_r = [0, 0, 1, -1]
direction_c = [1, -1, 0, 0]
punch_counts = [[NOT_VISITED] * num_columns for _ in range(num_rows)]

def can_visit(r, c):
    return (0 <= r < num_rows and 0 <= c < num_columns and punch_counts[r][c] == NOT_VISITED)

current_informations = deque()
current_informations.append((START_ROW, START_COLUMN, 0))
while current_informations:
    r, c, num_punches = current_informations.popleft()
    if r == GOAL_ROW and c == GOAL_COLUMN:
        print(num_punches)
        exit()
    
    if punch_counts[r][c] != NOT_VISITED:
        continue
    punch_counts[r][c] = num_punches
    
    for i in range(4):
        next_r = r + direction_r[i]
        next_c = c + direction_c[i]
        if not can_visit(next_r, next_c):
            continue
        if board[next_r][next_c] == ".":
            current_informations.appendleft((next_r, next_c, num_punches))
        else:
            current_informations.append((next_r, next_c, num_punches + 1))
            for j in range(-1, 2):
                for k in range(-1, 2):
                    next_next_r = next_r + j
                    next_next_c = next_c + k
                    if not can_visit(next_next_r, next_next_c):
                        continue
                    current_informations.append((next_next_r, next_next_c, num_punches + 1))
