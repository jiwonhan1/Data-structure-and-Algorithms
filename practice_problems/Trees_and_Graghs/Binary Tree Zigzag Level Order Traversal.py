class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BST
# from collections import deque
# class Solution(object):
#     def zigzagLevelOrder(self, root):
#         ret = []
#         level_list = deque()
#         if root is None:
#             return []
#         node_queue = deque([root, None])
#         is_order_left = True
#
#         while node_queue:
#             curr_node = node_queue.popleft()
# to be continued..