class TreeNode:
    def __init__(self,val=0, left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maximum_depth_bottom_up(self, root):
        if not root:
            return 0
        left_depth = self.maximum_depth_bottom_up(root.left)
        right_depth = self.maximum_depth_bottom_up(root.right)
        return max(left_depth, right_depth) + 1
