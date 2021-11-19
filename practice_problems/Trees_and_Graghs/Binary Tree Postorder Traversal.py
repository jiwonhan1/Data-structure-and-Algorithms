class Node:
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root):
        res = []
        def recursePreorder(node, res):
            if node:
                recursePreorder(node.left, res)
                recursePreorder(node.right, res)
                res.append(node.val)
        recursePreorder(root, res)
        return res