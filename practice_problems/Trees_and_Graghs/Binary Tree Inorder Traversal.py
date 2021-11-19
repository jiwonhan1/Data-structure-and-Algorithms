class TreeNode(object):
    def __init__(self, val = 0, left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # Recursive Approach
    # Time complexity O(N)
    # Space complexity O(N)
    def inorderTraversal(self,root):
        res = []
        self.helper(root, res)
        return res
    def helper(self, node, res):
        if node:
            if node.left:
                self.helper(node.left, res)
            res.append(node.val)
            if node.right:
                self.helper(node.right, res)

    # Iterating method using Stack
    # Time complexity O(N)
    # Space complexity O(N)
    def inorderTraversal(self,root):
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop
            res.append(curr.val)
            curr = curr.right
        return res