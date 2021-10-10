class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution(object):
    # Recursive
    # Time complexity O(N) Space complexity O(logN)
    def sameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.sameTree(p.right, q.right) and self.sameTree(p.left, q.left)
    # Level Order
    # TIme complexity O(N) Space complexity O(logN)
    def sameTree2(self):
        def check(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
        return True
        queue = deque([(p,q),])

        while queue:
            p,q = deque.popleft()
            if not check(p,q):
                return False
            if p and q:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
        return True
