class TreeNode:
    def __init__(self,val=0, left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maximum_depth_top_bottom(self, root, depth):
        if not root:
            return
        if not root.left and not root.right:
            answer = max(answer, depth)
        self.maximum_depth_top_bottom(root.left, depth+1)
        self.maximum_depth_top_bottom(root.right, depth+1)
