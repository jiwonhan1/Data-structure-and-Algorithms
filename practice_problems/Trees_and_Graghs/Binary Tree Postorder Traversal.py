class Node:
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # recursion
    def postorderTraversal(self, root):
        res = []
        def recursePostorder(node, res):
            if node:
                recursePostorder(node.left, res)
                recursePostorder(node.right, res)
                res.append(node.val)
        recursePostorder(root, res)
        return res

    # Iterative
    def postorderTraversal(self, root):
        ans = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                ans.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return ans[::-1]

    # One Liner:
    def postOrderTraversal(self, root):
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []