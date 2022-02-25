class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def searchBST(self, root, val):
        while root or root.val != val:
            root = root.left if root.val > val else root.right
        return root

    def searchBST2(self, root, val):
        if not root or root.val == val:
            return root
        return self.searchBST2(root.left, val) if root.val > val else self.searchBST2(root.right, val)