class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution(object):
    # Brute Force
    # Traverse all the linked lists and collection the values of the nodes into an array
    # Sort and iterate over this array to get the proper value of nodes
    # Create a new sorted linked list and extend it with the new nodes
    # Time complexity O(N log N)
    # Space complexity O(N)
    def mergeKLists(self, lists):
        nodes = []
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        dummy = ListNode()
        curr = dummy

        for node in sorted(nodes):
            curr.next = ListNode(node)
            curr = curr.next
        return dummy.next