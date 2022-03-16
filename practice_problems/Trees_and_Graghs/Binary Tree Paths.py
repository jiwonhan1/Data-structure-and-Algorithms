class Solution:
    # Recursion
    # The most intuitive way is to use a recursion here.
    # One is going through the tree by considering at each step the node itself and its children
    # if node is not a leaf, one extends the current path by a node value and calls recursively the path construction for tis children
    # If node is a leaf, one closes the current path and adds it into the list of paths
    def binaryTreePaths(self, root):

        def construct_paths(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path += '->'
                    construct_paths(root.left, path)
                    construct_paths(root.right, path)
            paths = []
            construct_paths(root, '')
            return paths

    # Iterations
    # Time and space complexity O(N)
    def binaryTreePaths(self, root):
        if not root:
            return []
        paths = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path + '->' + str(node.left)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right)))
        return paths