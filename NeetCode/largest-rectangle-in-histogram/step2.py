"""
https://github.com/shining-ai/leetcode/pull/68/files
    番兵を使うの賢すぎる
    heightsに0をappendしておくと、
    while index_and_heights and index_and_heights[-1][1] >= h:
    の中で最後に全部計算してくれる。h=0だから、stackが空になるまでループが回るので
    ただ、heightsにappendするのはちょっと嫌かな...というので不採用。
    最初にコピーを作ってappendはアリかもしれない。空間計算量が少し悪くなるけど
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        index_and_heights = []
        max_area = 0
        for i, h in enumerate(heights):
            start = i
            while index_and_heights and index_and_heights[-1][1] >= h:
                before_index, before_height = index_and_heights.pop()
                max_area = max(max_area, (i - before_index) * before_height)
                start = before_index
            index_and_heights.append((start, h))
        for i, h in index_and_heights:
            max_area = max(max_area, (len(heights) - i) * h)
        return max_area
