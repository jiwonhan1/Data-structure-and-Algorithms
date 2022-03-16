from collections import deque
class TreeNode(object):
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # BFS: One Queue + Sentinel
    # Time complexity O(N)
    # Space complexity O(D) to keep the queues, where D is a tree diameter
    def rightSideView(self, root):
        if not root:
            return []

        queue = deque([root, None])
        rightside = []

        curr = root
        while queue:
            prev, curr = curr, queue.popleft()

            while curr:
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

                prev, curr = curr, queue.popleft()
            # the current level is finished
            # and prev is its rightmost element
            rightside.append(prev.val)
            # add a sentinel to mark the end of the next level
            if queue:
                queue.append(None)
        return rightside

    # BFS: One Queue + Level Size Measurements
    # Instead of using the sentinel, we could write down the length of the current level
    # Time complexity O(N)
    # Space complexity O(D)
    def rightSideView(self, root):
        if not root:
            return []
        queue = deque([root])
        rightside = []

        while queue:
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()
                if i == level_length - 1:
                    rightside.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return rightside