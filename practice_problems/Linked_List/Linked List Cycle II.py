class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution(object):
    def getIntersect(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return fast
        return None

    def detectCycle(self, head):
        if not head:
            return None

        intersect = self.getIntersect(head)
        if intersect is None:
            return None

        ptr1 = head
        ptr2 = intersect

        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1