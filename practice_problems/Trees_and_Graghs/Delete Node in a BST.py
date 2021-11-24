class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time complexity O(logN)
    # Space complexity O(H)
    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val
    def deleteNode(self, root, key):
        if not root:
            return None
        # If key > root.val then delete the node to delete is in the right subtree root.right = delete(root.right, key)
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # If key < root.val then delete the node to delete is in the left subtree root.left = deleteNode(root.left, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # if key == root.val then the node to delete is right here
        else:
            # if the node is a leaf, the delete process is straightforward: root = null
            if not (root.right or root.left):
                root = None
            # If the node is not a leaf and has the right child, then replace the node value by a successor value root.val = successsor.val
            # and then recursively delete the successor in the right subtree root.right = deleteNode(root.right, root.val)
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # if the node is not a leaf and has only the left child, then replace the node value by a predecessor value root.val = predecessor.val
            # and then recursively delete the predecessor in the left subtree root.left = deleteNode(root.left, root.val)
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        return root