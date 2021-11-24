class TreeNode:
    def __init__(self,val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time complexity O(H)
    # Space complexity O(1)
    def searchBST(self, root, val):
        while root and root.val != val:
            root = root.left if val < root.val else root.right
        return root

    # Time complexity O(H)
    # Space complexity O(H)
    def searchBST2(self, root, val):
        if root is None or val == root.val:
            return root
        return self.searchBST2(root.left, val) if val < root.val else self.searchBST2(root.right, val)