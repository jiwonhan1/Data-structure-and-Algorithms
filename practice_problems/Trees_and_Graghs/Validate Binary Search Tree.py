class TreeNode:
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive Traversal with Valid Range
    def isValidBST(self, root):
        def validate(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            return (validate(node.left, low, node.val) and validate(node.right, node.val, high))
        return validate(root)

    # Iterative Traversal with Valid Range **DFS**
    def isValidBST2(self, root):
        if not root:
            return True
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            root, lower, higher = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= higher:
                return False
            stack.append(root.left, lower, val)
            stack.append(root.right, val, higher)
        return True