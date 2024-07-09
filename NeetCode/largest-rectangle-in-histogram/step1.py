"""
なるほど。stackに(index, height)を格納していく
stackの後ろが自分より高かったら、自分の高さに更新する。indexはそのまま。
自分より低かったら、そのまま自分を入れるだけでよい
これで、stackは昇順になるから、stackの一番後ろを見るだけで、残りは続いてることが保証される
O(n)か

これってstackじゃないと実現できないのか?
むずかしい。昇順を表現して、後ろだけ見るようにしたいから
今までの高さを管理しようとすると、stackのデータ構造を使うのが最適
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
