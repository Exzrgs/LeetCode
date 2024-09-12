"""
Question:
    
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = root.val
        
        def sum(node):
            if not node:
                return 0
            
            left_sum = sum(node.left)
            right_sum = sum(node.right)
            self.ans = max(self.ans, node.val + max(left_sum, 0) + max(right_sum, 0))
            return node.val + max(left_sum, right_sum, 0)
        
        sum(root)
        return self.ans
