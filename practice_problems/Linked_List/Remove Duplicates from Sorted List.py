class ListNode(object):
    def __init__(self, val=0,next=None):
        self.val = val
        self.next = next

class Solution(object):
    # Time complexity O(N) Space complexity O(1)
    def deleteDuplicates(self, head):
        curr = head
        while curr and curr.next:
            if curr.val == curr.next:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head