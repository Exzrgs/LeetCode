"""
Question:
Discussion:

なんか再帰関数で管理すべき状態が2つ以上あるときは、返り値にするんじゃなくグローバルな変数として持っておくべき
そうじゃないと、返り値で何かを管理するとき煩雑になる
2つ返り値を返すとかも微妙で、返り値に対して条件分岐しないといけなくなる
更新する答えだけをグローバルとかでもダメ。両方グローバルにする
    更新した後returnしても再帰関数は終了しないので
    したのように、count += search(node.left, count) + 1の部分にNoneが返ってしまい、エラーになる
    
    class Solution:
        def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
            kth_val = 0
            def search(node, count):
                if not node:
                    return count
                
                count += search(node.left, count) + 1
                if count == k:
                    nonlocal kth_val
                    kth_val = node.val
                    return
                return search(node.right, count)
            
            search(root, 0)
            return kth_val

なので、複数の状態を管理する場合はstackで実装しちゃったほうが良いかもなあ
値が決まってからreturnしても処理が続いてるのが怖い。勝手に答えを書き換えられないか注意しないといけない
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.kth_val = None
        self.count = 0
        def search(node):
            if not node:
                return
            
            search(node.left)
            self.count += 1
            if self.count == k:
                self.kth_val = node.val
                return
            search(node.right)
        
        search(root)
        return self.kth_val

# これ良いなあ
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        node_stack = []
        cur = root
        count = 0
        while node_stack or cur:
            while cur:
                node_stack.append(cur)
                cur = cur.left
            cur = node_stack.pop()
            count += 1
            if count == k:
                return cur.val
            cur = cur.right

# 配列に入れてしまえばcountを管理しなくてよい
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.sorted_nodes = []
        
        def create_sorted_list(node):
            if not node:
                return
            
            create_sorted_list(node.left)
            self.sorted_nodes.append(node.val)
            create_sorted_list(node.right)
        
        create_sorted_list(root)
        return self.sorted_nodes[k - 1]
