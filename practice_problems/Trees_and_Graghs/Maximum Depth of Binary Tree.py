class TreeNode(object):
    def __init__(self, val=0, left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution(object):
    # Time complexity O(N)
    def maxDepth(self, root):
        level = 0
        if not root:
            return level

        Q = deque([root])

        while Q:
            size = len(Q)
            for i in range(size):
                popped = Q.popleft()
                if popped.left:
                    Q.append(popped.left)
                if popped.right:
                    Q.append(popped.right)
            level += 1
        return level
