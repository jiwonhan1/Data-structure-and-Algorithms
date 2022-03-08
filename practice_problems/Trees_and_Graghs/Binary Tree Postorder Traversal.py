class Node:
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root):
        res = []
        def recursePostorder(node, res):
            if node:
                recursePostorder(node.left, res)
                recursePostorder(node.right, res)
                res.append(node.val)
        recursePostorder(root, res)
        return res