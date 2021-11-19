class TreeNode(object):
    def __init__(self,val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def preorderTraversal(self,root):
        res = []
        def recurse(node):
            if not node:
                return
            if node:
                res.append(node)
            recurse(node.left)
            recurse(node.right)
        recurse(root)
        return res

    def preorderTraversal2(self, root):
        if not root:
            return []
        stack, output = [root,], []

        while stack:
            root = stack.pop()
            if root:
                output.append(root.val)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
        return output