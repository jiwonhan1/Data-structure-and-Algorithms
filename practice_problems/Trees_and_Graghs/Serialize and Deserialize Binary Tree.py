class TreeNode(object):
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Depth First Search
    # Time complexity O(N) Space complexity O(N)
    def serialize(self,root):
        def reserialize(root, string):
            if not root:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = reserialize(root.left, string)
                string = reserialize(root.right, string)
            return string

        return reserialize(root, '')

    def deserialize(self, data):
        def rdeserialize(l):
            if l[0] == 'None':
                l.pop(0)
                return None
            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root