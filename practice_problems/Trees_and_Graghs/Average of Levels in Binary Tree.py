from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Breadth First Search
    # Time and space complexity O(N)
    def averageOfLevels(self, root):
        res = []
        queue = deque([root])

        while queue:
            sum = 0
            count = 0
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                sum += node.val
                count += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append((sum * 1.0) /count)
        return res