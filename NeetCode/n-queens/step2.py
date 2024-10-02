"""
左上から右下への斜めは和が一定
    colが増えたらrowが減るから
左下から右上への斜めは差が一定
    colが増えたらrowも増えるから
"""

# time: < n^n
# space: n^2
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        res = []
        ng_col = set()
        ng_pros_diag = set()
        ng_minus_diag = set()
        
        def backtrack(row):
            if row == n:
                res.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                if col in ng_col or row + col in ng_pros_diag or row - col in ng_minus_diag:
                    continue
                board[row][col] = "Q"
                ng_col.add(col)
                ng_pros_diag.add(row + col)
                ng_minus_diag.add(row - col)
                
                backtrack(row + 1)
                
                board[row][col] = "."
                ng_col.remove(col)
                ng_pros_diag.remove(row + col)
                ng_minus_diag.remove(row - col)
        
        backtrack(0)
        return res
