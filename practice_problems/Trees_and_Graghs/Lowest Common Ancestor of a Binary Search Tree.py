class TreeNode(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # Iterative
    # Time complexity O(N) Space complexity O(1)
    def lowestCommonAncestor(self, root, p, q):
        p_val = p.val
        q_val = q.val
        node = root

        while node:
            parent_val = node.val
            if p_val > parent_val and q_val > parent_val:
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                node = node.left
            else:
                return node
    # Recursive
    # Time complexity O(N) Space complexity O(1)
    def lowestCommonAncestor2(self, root, p, q):
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor2(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor2(root.right, p, q)
        else:
            return root

