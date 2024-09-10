# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes_stack = []
        count = 0
        cur = root
        while nodes_stack or cur:
            while cur:
                nodes_stack.append(cur)
                cur = cur.left
            cur = nodes_stack.pop()
            count += 1
            if count == k:
                return cur.val
            cur = cur.right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.smallest = None
        self.count = 0

        def search(node):
            if not node:
                return
            
            search(node.left)
            self.count += 1
            if self.count == k:
                self.smallest = node.val
                return
            search(node.right)
        
        search(root)
        return self.smallest
