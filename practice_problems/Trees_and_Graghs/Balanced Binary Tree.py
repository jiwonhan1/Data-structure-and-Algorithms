class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # Top-down recursion
    # Time complexity O(NlongN)
    def height(self, root):
        if not root:
            return -1
        return 1+max(self.height(root.left), self.height(root.right))
    def isBlanaced(self, root):
        if not root:
            return root
        return abs(self.height(root.left) - self.height(root.right)) < 2 and self.isBlanaced(root.right) and self.isBalanced(root.left)