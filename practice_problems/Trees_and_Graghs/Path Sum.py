class TreNode:
    def __init__(self, val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        targetSum -= root.val
        if not root.left and not root.left:
            return targetSum == 0
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        de = [(root, targetSum - root.val)]
        while de:
            node, curr_sum = de.pop()
            if not node.right and node.left and curr_sum == 0:
                return True
            if node.left:
                de.append((node.left, targetSum - node.left.val))
            if node.right:
                de.append((node.right, targetSum - node.right.val))
        return False
