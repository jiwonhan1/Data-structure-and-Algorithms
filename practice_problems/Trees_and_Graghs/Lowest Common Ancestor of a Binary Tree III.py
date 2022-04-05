class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p,q):
        p1, p2 = p,q
        while p1 != p2:
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p
        return p1

    def lowestCommonAncestor(self,p,q):
        visited = set()
        while q:
            visited.add(q.val)
            q = q.parent
        while p:
            if p.val in visited: return p
            # visited.add()
            p = p.parent
        return None
