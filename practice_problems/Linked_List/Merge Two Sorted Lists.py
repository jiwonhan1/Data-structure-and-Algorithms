class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    # Time complexity O(N+M) Space complexity O(1)
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next
    # Recursive
    # Time complexity O(N+M) Space complexity O(N+M)
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l2
        elif l1.val < l2.val:
            self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            self.mergeTwoLists(l1, l2.next)
            return l2