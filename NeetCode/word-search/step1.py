"""
time complexity: O(m * n * 4^len(word))
space complexity: O(m*n)
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        num_rows = len(board)
        num_cols = len(board[0])
        visited = set()
        
        def search(r, c, index):
            if index == len(word):
                return True
            if (
                r not in range(num_rows) or
                c not in range(num_cols) or
                board[r][c] != word[index] or
                (r, c) in visited
            ): return False
            
            visited.add((r, c))
            is_found = (
                search(r + 1, c, index + 1) or
                search(r - 1, c, index + 1) or
                search(r, c + 1, index + 1) or
                search(r, c - 1, index + 1)
            )
            visited.remove((r, c))
            return is_found
        
        for r in range(num_rows):
            for c in range(num_cols):
                if search(r, c, 0):
                    return True
        return False
