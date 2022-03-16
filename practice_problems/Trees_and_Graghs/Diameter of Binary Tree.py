class TreeNode(object):
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # Depth first search
    # Time and space complexity O(N)
    def diameterOfBinaryTree(self, root):
        # Initialize an integer variable diameter to keep track of the longest path we find from the DFS

        diameter = 0
        def longest_path(node):
            if not node:
                return 0
            nonlocal diameter
            # recursively find the longest path in both left child and right child
            left_path = longest_path(node.left)
            right_path = longest_path(node.right)

            diameter = max(diameter, left_path + right_path)
            # return the longest one between left_path and right_path
            # remember to add 1 for the path connecting the node and its parent
            return max(left_path, right_path) + 1
        longest_path(root)
        return diameter