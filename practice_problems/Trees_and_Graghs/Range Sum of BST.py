class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time complexity O(N)
    # Space complexity O(N)
    def rangeSumBST(self, root, low, high):
        self.ans = 0
        def dfs(node):
            if node:
                if low <= node.val <=high:
                    self.ans += node.val
                if low < node.val:
                    dfs(node.left)
                if node.val < high:
                    dfs(node.right)
        dfs(root)

        return self.ans