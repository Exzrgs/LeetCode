"""
board自体は(H+1)*(W+1)になってる
iとjで指すのは区間の外。i+1, j+1が左上の正方形区間
"""

num_students, gap_limit = map(int, input().split())
heights = []
weights = []
for _ in range(num_students):
    h, w = map(int, input().split())
    heights.append(h)
    weights.append(w)

board = [[0] * 5001 for _ in range(5001)]
for i in range(num_students):
    board[heights[i]][weights[i]] += 1
for i in range(5001):
    for j in range(1, 5001):
        board[i][j] += board[i][j - 1]
for i in range(5001):
    for j in range(1, 5001):
        board[j][i] += board[j - 1][i]

max_num_member = 0
for i in range(5000 - gap_limit):
    for j in range(5000 - gap_limit):
        num_member = board[i + 1 + gap_limit][j + 1 + gap_limit] - board[i + 1 + gap_limit][j] - board[i][j + 1 + gap_limit] + board[i][j]
        max_num_member = max(max_num_member, num_member)
print(max_num_member)
