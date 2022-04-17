class ListNode(object):
    def __init__(self, val =0, Next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self,l1, l2):
        dummy = ListNode()
        curr = dummy
        p = l1
        q = l2
        carry = 0

        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            xySum = (x+y+carry) % 10
            carry = (x+y+carry) // 10

            curr.next = ListNode(xySum)
            curr = curr.next

            if p:
                p = p.next
            if q:
                q = q.next
        if carry:
            curr.next = ListNode(carry)
        return dummy.next
