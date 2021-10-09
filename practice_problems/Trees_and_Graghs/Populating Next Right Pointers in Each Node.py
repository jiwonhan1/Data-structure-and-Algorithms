class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Soltion(object):
    # Level Order Traversal
    # Time Complexity O(N) Space Complexity O(N)
    def connect(self, root):
        if not root:
            return root
        Q = deque([root])

        while Q:
            size = len(Q)
            for i in range(size):
                node = Q.popleft()
                if i < size -1:
                    node.next = Q[0]
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        return root