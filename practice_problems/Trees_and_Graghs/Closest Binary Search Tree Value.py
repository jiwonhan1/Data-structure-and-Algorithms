class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Iterative Inorder, O(k) time
    # Initiate stack as an empty array and predecessor value as a very small number
    # While root is not null:
    # To build an inorder traversal iteratively, go left as far as you can and add all nodes on the way into stack
    # Pop the last element from stack root = stack.pop()
    # If target is in-between of pred and root.val, return the closest between these two elements
    # Set predecessor value to be equal to root.val and go one step right: root= root.right
    def closestValue(self, root, target):
        stack, pred = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            if pred <= target and target < root.val:
                return min(pred, root.val, key=lambda x: abs(target-x))
            pred = root.val
            root = root.right
        return pred
    def closestValue(self, root, target):
        closest = root.val
        while root:
            closest = min(root.val, closest, key=lambda x: abs(target-x))
            root = root.left if target < root.val else root.right
        return closest