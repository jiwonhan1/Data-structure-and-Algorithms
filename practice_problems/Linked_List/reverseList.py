class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        cur = head
        while cur:
            nextNode = head.next
            cur.next = prev
            prev = cur
            cur = nextNode
        return prev

    def reverseList2(self, head):
        if not head or not head.next:
            return head
        p = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return p
