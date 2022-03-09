class TreeNode(object):
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # Recursion
    # Start from not inorder traversal, usually it's preorder or postorder one
    # The value picked from preorder/postorder traversal splits the inorder traversal into left and right subtrees.

    # Build hasmap value -> its index for inorder traversal
    # Return helper function which takes as the arguments the left and right boundaries for the current subtree in the inorder traversal
    # These boundaries are used only to check if the subtree is empty or not.
    # Here is how it works helper(in_left=0, in_right n-1):
    # if in_left > in_right, the subtree is empty , return None
    # Pick the last element in postorder traversal as a root
    # Root value has index index in the inorder traversal, elements from in_left to index-1 belong to the left subtree, and elements from index + 1 to in_right belong to the right subtree
    # Following the postorder logic, proceed recursively first to contruct the right subtree helper(index+1, _in_right) and then to construct the left subtree helper(in_left, index-1)
    # Return root

    # Time complextiy O(N)
    # Space complexity O(N)
    def buildTree(self, inorder, postorder):
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            val = postorder.pop()
            root = TreeNode(val)

            index = idx_map[val]

            root.right = helper(index+1, in_right)
            root.left = helper(in_left, index-1)
            return root
        idx_map = {val:idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) -1)