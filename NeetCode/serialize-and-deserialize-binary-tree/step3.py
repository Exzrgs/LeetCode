# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        res = []
        
        def append_value(node):
            if not node:
                res.append("N")
                return
            
            res.append(str(node.val))
            append_value(node.left)
            append_value(node.right)
        
        append_value(root)
        return ",".join(res)

    def deserialize(self, data):
        values = data.split(",")
        self.index = 0

        def make_node():
            if values[self.index] == "N":
                self.index += 1
                return None

            node = TreeNode(int(values[self.index]))
            self.index += 1
            node.left = make_node()
            node.right = make_node()
            return node
        
        return make_node()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
