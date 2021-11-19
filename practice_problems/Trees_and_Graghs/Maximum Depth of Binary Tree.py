class TreeNode(object):
    def __init__(self, val=0, left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution(object):
    # Recursion
    # Time complexity O(N) Space compelxity O(N)
    def maxDepth(self,root):
        if not root:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1

    # Iteration
    # Time complexity O(N) Space complextiy O(N)
    def maxDepth2(self, root):
        stack = []
        if root:
            stack.append((1, root))

            depth = 0
            while stack:
                current_depth, root = stack.pop()
                if root:
                    depth = max(depth, current_depth)
                    stack.append((current_depth+1, root.left))
                    stack.append((current_depth+1, root.right))
        return depth
