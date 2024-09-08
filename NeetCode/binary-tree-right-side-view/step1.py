"""
Question:
    How is the num of nodes?
Test:

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        nodes_queue = deque()
        nodes_queue.append(root)
        while nodes_queue:
            for _ in range(len(nodes_queue)):
                node = nodes_queue.popleft()
                right_val = node.val
                if node.left:
                    nodes_queue.append(node.left)
                if node.right:
                    nodes_queue.append(node.right)
            res.append(right_val)
        return res
