'''
5m7s

思考もしつつ完全に再現できてよかった
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [[] for _ in range(numRows)]
        current_row = 0
        step = 1
        for i in range(len(s)):
            rows[current_row].append(s[i])
            current_row += step
            if current_row == 0 or current_row == numRows-1:
                step *= -1
        
        merged_rows = []
        for i in range(numRows):
            merged_rows.extend(rows[i])
        zigzag = "".join(merged_rows)
        return zigzag
