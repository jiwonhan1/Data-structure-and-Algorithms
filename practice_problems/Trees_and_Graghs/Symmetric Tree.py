from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    # Time complexity O(N)
    # Space complexity O(N) : The number of recursive calls is bound by the height of the tree

    def isMirror(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return t1.val == t2.val and self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right)
    def isSymmetric(self, root):
        return self.isMirror(root, root)

    def isSymmetric2(self, root):
        q = deque()
        q.append(root)

        while q:
            len_q = len(q)
            tmplist = []
            for i in range(len_q):
                node = q.popleft()
                if not node:
                    tmplist.append(None)
                else:
                    tmplist.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                if tmplist != tmplist[::-1]:
                    return False
        return True