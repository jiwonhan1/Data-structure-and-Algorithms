from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    # Iteration
    # Time complexity O(N)
    # Space complexity O(N)
    def levelOrder(self, root):
        levels = []
        if not root:
            return levels
        level = 0
        queue = deque([root,])
        while queue:
            levels.append([])
            for i in range(len(queue)):
                popped = queue.popleft()
                levels[level].append(popped)
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
            level += 1
        return levels