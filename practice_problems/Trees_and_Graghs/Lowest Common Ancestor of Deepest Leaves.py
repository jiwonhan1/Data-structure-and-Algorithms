from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# BFS
class Solution:
    def get_deepestleaves(self,root):
        queue = deque([root])
        ans = []

        while queue:
            ans = [i for i in queue]
            for i in range(len(ans)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans

    def preorder(self, root, visited):
        if not root:
            return None

        left = self.preorder(root.left, visited)
        right = self.preorder(root.right, visited)

        if left and right:
            return root
        if left:
            return left
        if right:
            return right
        if root.val in visited:
            return root
    def lcaDeepestLeaves(self, root):
        nodes = self.get_deepestleaves(root)

        visited = [i.val for i in nodes]
        visited = set(visited)

        if len(nodes) == 1:
            return nodes[0]

        return self.preorder(root, visited)