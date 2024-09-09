"""
Question:
    Can value be negative number?
Discussion:
    have greatest value in the path
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        node_queue = deque()
        node_queue.append((root, root.val))
        while node_queue:
            node, greatest = node_queue.popleft()
            if node.val >= greatest:
                res += 1
                greatest = node.val
            if node.left:
                node_queue.append((node.left, greatest))
            if node.right:
                node_queue.append((node.right, greatest))
        return res

# stack
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        node_stack = []
        node_stack.append((root, root.val))
        while node_stack:
            node, greatest = node_stack.pop()
            if node.val >= greatest:
                res += 1
                greatest = node.val
            if node.right:
                node_stack.append((node.right, greatest))
            if node.left:
                node_stack.append((node.left, greatest))
        return res

# dfs
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        
        def count_good_nodes(node, greatest):
            nonlocal res
            if node.val >= greatest:
                res += 1
                greatest = node.val
            if node.left:
                count_good_nodes(node.left, greatest)
            if node.right:
                count_good_nodes(node.right, greatest)
        
        count_good_nodes(root, root.val)
        return res

# dfs
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count_good_nodes(node, greatest):
            if not node:
                return 0
            
            if node.val >= greatest:
                res = 1
                greatest = node.val
            else:
                res = 0
            res += count_good_nodes(node.left, greatest)
            res += count_good_nodes(node.right, greatest)
            return res
        return count_good_nodes(root, root.val)
