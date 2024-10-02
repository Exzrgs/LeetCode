"""
ダメだったやつ
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[None] * n for _ in range(n)]
        
        def mark_vertical(w, mark):
            for i in range(n):
                if not board[i][w]:
                    board[i][w] = mark
        
        def mark_horizontal(r, mark):
            for i in range(n):
                if not board[r][i]:
                    board[r][i] = mark
        
        def mark_diagonal(r, w, mark):
            for i in range(-n, n):
                cur_r = r + i
                cur_w = w + i
                if (cur_r not in range(n) or
                    cur_w not in range(n) or
                    board[cur_r][cur_w]
                ): continue
                board[cur_r][cur_w] = mark
            for i in range(-n, n):
                cur_r = r + i
                cur_w = w - i
                if (cur_r not in range(n) or
                    cur_w not in range(n) or
                    board[cur_r][cur_w]
                ): continue
                board[cur_r][cur_w] = mark
        
        def mark_attack_tiles(r, w, mark):
            mark_vertical(w, mark)
            mark_horizontal(r, mark)
            mark_diagonal(r, w, mark)
        
        def fill_none():
            for i in range(n):
                for j in range(n):
                    if not board[i][j]:
                        board[i][j] = "."
        
        res = []
        
        def append_queen_paterns():
            for i in range(n):
                for j in range(n):
                    if not board[i][j]:
                        board[i][j] = "Q"
                        mark_attack_tiles(i, j, ".")
                        append_queen_paterns()
                        board[i][j] = None
                        mark_attack_tiles(i, j, None)
            fill_none()
            formatted_board = []
            for row in board:
                formatted_board.append("".join(row))
            res.append(formatted_board)
        
        append_queen_paterns()
        return res
