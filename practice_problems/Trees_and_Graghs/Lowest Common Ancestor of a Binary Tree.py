class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def __init__(self):
        self.ans = None
    def lowestCommonAncestor(self, root, p, q):
        def recurse_tree(current_node):
            if not current_node:
                return False
            left = recurse_tree(current_node.left)
            right = recurse_tree(current_node.right)
            mid = current_node == p or current_node == q

            if mid + left + right >= 2:
                self.ans = current_node
        recurse_tree(root)
        return self.ans
    # Iterative using parent pointers
    # If we have parent pointers for each node we can traverse back from p and q to get their ancestors.
    # The first common node we get during this traversal would be the LCA node.
    # We can save the parent pointers in a dictionary as we traverse the tree
    # Time complexity O(N) Space complexity O(N)
    def lowestCommonAncestor2(self, root, p, q):
        stack = [root]
        parent = {root:None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        ancestors = set()

        while p:
            ancestors.add(p)
            p = parent[p]

        while q not in ancestors:
            q = parent[q]
        return q

