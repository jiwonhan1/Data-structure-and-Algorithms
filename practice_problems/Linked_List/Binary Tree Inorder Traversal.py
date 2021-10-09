class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def helper(self,root,res):
        if root:
            if root.left:
                self.helper(root.left, res)
            res.append(root.val)
            if root.right:
                self.helper(root.right, res)
    def inorderTraversal(self,root):
        res = []
        self.helper(root, res)
        return res

    def inorderTraversal2(self, root):
        res, stack = [], []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr.left)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res