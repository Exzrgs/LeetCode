"""
Question:
    Can matrix be empty?
        No
Discussion:
    firstly, we can find the index of target column by using binary search
    secondly, we can find the index of target row by also using binary search
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_columns = len(matrix)
        num_rows = len(matrix[0])
        
        left = 0
        right = num_columns
        while right - left > 1:
            mid = (left + right) // 2
            if matrix[mid][0] > target:
                right = mid
            else:
                left = mid
        target_column = left

        left = 0
        right = num_rows - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[target_column][mid] > target:
                right = mid - 1
            elif matrix[target_column][mid] < target:
                left = mid + 1
            else:
                return True
        return False
