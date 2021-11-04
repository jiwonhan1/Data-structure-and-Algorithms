class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BST
from collections import deque
class Solution(object):
    # Time complexity O(N) Space compexity O(N)
    def zigzagLevelOrder(self, root):
        results = []
        if not root:
            return results
        def dfs(node, level):
            if level >= len(results):
                results.append(deque([node.val]))
            else:
                if level % 2 == 0:
                    results[level].append(node.val)
                else:
                    results[level].appendleft(node.val)
                for next_node in [node.left, node.right]:
                    if next_node:
                        dfs(next_node, level +1)
        dfs(root, 0)
        return results