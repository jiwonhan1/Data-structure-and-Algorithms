class TreeNode(object):
    def __init__(self,val=0,left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict

class Solution(object):
    def findDuplicateSubtrees(self,root):
        if not root:
            return []

        duplicates = defaultdict(int)
        result = set()

        def dfs(root):
            if not root: return None
            left = dfs(root.left)
            right = dfs(root.right)

            key = tuple([root.val, left, right])

            duplicates[key] += 1
            if duplicates[key] >= 2: result.add(root)

            return key
        dfs(root)
        return result