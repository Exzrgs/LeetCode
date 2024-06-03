'''
9m13s

numRowsの分だけListを用意して、そこに文字を入れていく
rowsの最初か最後までいったときに、addingを切り替えればよい
テストを走らせる前に頭の中で簡単なテストをして、addingが最初-1でないといけないと気付けたのは良かった
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [[] for _ in range(numRows)]
        current = 0
        adding = -1
        for i in range(len(s)):
            rows[current].append(s[i])

            if current == numRows-1 or current == 0:
                adding *= -1

            current += adding

        zigzag = ""
        for i in range(numRows):
            zigzag += "".join(rows[i])
        return zigzag        
