class TreeNode(object):
    def __init__(self,val=0, left=None, right=None):
        self.val=val
        self.left=None
        self.right=None

class Solution:
    # Time complexity O(N)
    # Space complexity O(H)
    def countUnivalSubtrees(self, root):
        if not root:
            return 0

        self.count = 0
        self.uni(root)
        return self.count

    def is_uni(self,node):
        if not node.left and not node.right:
            self.count += 1
            return True

        is_uni = True
        if node.left:
            is_uni = self.is_uni(node.left) and is_uni and node.left.val == node.val
        if node.right:
            is_uni = self.is_uni(node.right) and is_uni and node.right.val == node.val
        self.count += is_uni
        return is_uni