from collections import defaultdict , deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    # Time complexity O(NlogN)
    # Space complexity O(N)
    def verticalOrder(self, root):

        columnTable = defaultdict(list)
        queue = deque([root,0])

        while queue:
            node, column = queue.popleft()
            if node:
                columnTable[column].append(node.val)
                queue.append((node.left, column-1))
                queue.append(node.right, column+1)
        return [columnTable[x] for x in sorted(columnTable.keys())]
