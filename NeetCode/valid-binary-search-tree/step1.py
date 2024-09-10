"""
Question:
    How is the num of nodes?
Discussion:
    bfs
        use deque
    dfs
        use stack or recursion

左部分木は今までのどの親よりも小さくなければならない
右部分木は今までのどの親よりも大きくなければならない

つまり、
    右に行く場合は、大きい分にはいいが、自分より小さいのはいけない。
    左に行く場合は、小さい分にはいいが、自分より大きいのはいけない
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            return check(node.left, left, node.val) and check(node.right, node.val, right)
        
        return check(root, float('-inf'), float('inf'))

from collections import deque

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        node_queue = deque()
        node_queue.append((root, float('-inf'), float('inf')))
        while node_queue:
            node, left, right = node_queue.pop()
            if not node:
                continue
            
            if not (left < node.val < right):
                return False
            node_queue.append((node.left, left, node.val))
            node_queue.append((node.right, node.val, right))
        return True

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        node_stack = []
        node_stack.append((root, float('-inf'), float('inf')))
        while node_stack:
            node, left, right = node_stack.pop()
            if not node:
                continue
            
            if not (left < node.val < right):
                return False
            node_stack.append((node.right, node.val, right))
            node_stack.append((node.left, left, node.val))
        return True
