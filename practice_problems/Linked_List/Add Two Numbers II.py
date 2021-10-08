class ListNode(object):
    def __init__(self, val=0, next =None):
        self.val = val
        self.next = next
class Solution(object):
    def reverse(self, list):
        prev = None
        curr = list
        while curr:
            currNext = curr.next
            curr.next = prev
            prev = curr
            curr = currNext
        return prev

    def addTwoNumbers(self, l1, l2):
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        carry = 0
        dummyHead = ListNode()
        cur = dummyHead
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            xySum = x+y+carry
            carry = xySum / 10
            cur.next = ListNode(xySum % 10)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            cur = cur.next
        if carry:
            cur.next = ListNode(carry)
        return self.reverse(dummyHead.next)
