class ListNode:
    def __init__(self,val =0, next= None):
        self.val = val
        self.next = next

class Solution(object):
    # One pass
    # Time complexity O(N) Space complexity O(1)
    def removeElements(self, head, val):
        sentinel = ListNode(0)
        sentinel.next = head

        prev = sentinel
        curr = head

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return sentinel.next