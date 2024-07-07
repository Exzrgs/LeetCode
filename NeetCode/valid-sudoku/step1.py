"""
check each row and column sub-boxes must contain 1-9 without repetition
これ普通の数独みたいに、解ける必要はないのか。
解けるようにしようと思ったら、候補を挙げておいて、消していく方式にしないといけない
1-9を候補にしておいて、今回みたいに列、行、ボックスに出現した要素を記録しておく
で、各要素に対して、候補を消していって、すべての要素に候補が最終的に存在するかを確認する
"""

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in columns[c] or board[r][c] in boxes[(r // 3, c // 3)]:
                    return False
                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])
        return True
