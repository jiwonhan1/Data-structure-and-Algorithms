class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time complexity : O(N) Space complexity : O(N)
    def treeToDoublyList(self, root):
        stack = [root]
        first, curr, last = None, root.left, None

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
                continue
            if stack:
                curr = stack.pop()
                if not first:
                    first = curr
                if last:
                    last.right = curr
                    curr.left = last
                last = curr
                curr = curr.right
        first.left = last
        last.right = first
        return first