"""
Question:
    How is the num of nodes?
Discussion:
    1st
        use deque
    2nd
        use recursion
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        node_stack = []
        level_to_values = defaultdict(list)
        node_stack.append((root, 0))
        while node_stack:
            node, level = node_stack.pop()
            level_to_values[level].append(node.val)
            if node.right:
                node_stack.append((node.right, level + 1))
            if node.left:
                node_stack.append((node.left, level + 1))
        return list(level_to_values.values())

# 上からレベル順に処理して、ansに追加していく
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        level_to_values = []
        node_queue = deque()
        node_queue.append(root)
        while node_queue:
            values = []
            for _ in range(len(node_queue)):
                node = node_queue.popleft()
                values.append(node.val)
                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)
            level_to_values.append(values)
        return level_to_values
