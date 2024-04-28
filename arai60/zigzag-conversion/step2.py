'''
改行入れすぎだったから消す
文字列への追加は遅いので、リストにまとめてから文字列に変換
if current_row == 0 or current_row == numRows-1に順番を変更
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
