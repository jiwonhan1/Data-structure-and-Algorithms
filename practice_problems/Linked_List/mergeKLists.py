class ListNode(object):
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    # Time complexity O(N log N) Space complexity O(N)
    def mergeKLists(self, lists):
        self.nodes = []
        head = point = ListNode()
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next
