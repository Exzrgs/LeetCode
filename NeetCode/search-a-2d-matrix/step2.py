"""
while right - left > 1:
    mid = (left + right) // 2
    if matrix[mid][0] > target:
        right = mid - 1
    else:
        left = mid
だと、left, ?, mid, rightみたいなシチュエーションで、rightが最後答えになって終わってしまう

while left < right:
    mid = (left + right + 1) // 2
    if matrix[mid][0] > target:
        right = mid - 1
    else:
        left = mid
target_column = right
こうすればよい。要は、// 2したときに、動かす側にmidが行くようにする。midが留まらないようにする

まとめると、
・while right - left > 1
    初期値: left = 0, right = len(nums)
    mid: (left + right) // 2
    動かす: left = mid, right = mid
・while left < right
    初期値: left = 0, right = len(nums) - 1
    
    mid: (left + right) // 2
    動かす: left = mid + 1, right = mid
    
    mid: (left + right + 1) // 2
    動かす: left = mid, right = mid - 1
・while left <= right
    初期値: left = 0, right = len(nums) - 1
    mid: (left + right) // 2
    動かす: left = mid + 1, right = mid - 1
"""

# right = mid
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

# right = mid - 1
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_columns = len(matrix)
        num_rows = len(matrix[0])
        
        left = 0
        right = num_columns - 1
        while left < right:
            mid = (left + right + 1) // 2
            if matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid
        target_column = right

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
