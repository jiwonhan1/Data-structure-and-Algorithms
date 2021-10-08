class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Soltion(object):
    def addTwoNumbers(self, list1, list2):
        dummyHead = ListNode()
        p = list1
        q = list2
        carry = 0
        curr = dummyHead
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            xySum = x+y+carry
            carry = xySum / 10
            curr.next = ListNode(xySum%10)
            curr = curr.next
            if p:
                p = p.next
            if q:
                q = q.next
        if carry:
            curr.next = ListNode(carry)
        return dummyHead.next