class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def __init__(self):
        self.ans = None
    def lowestCommonAncestor(self, root, p, q):
        def recurse_tree(current_node):
            if not current_node:
                return False
            left = recurse_tree(current_node.left)
            right = recurse_tree(current_node.right)
            mid = current_node == p or current_node == q

            if mid + left + right >= 2:
                self.ans = current_node
        recurse_tree(root)
        return self.ans