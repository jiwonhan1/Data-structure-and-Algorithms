class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Recursion
    # Time complexity O(N)
    # space complexity O(N/K)
    def reverseLinkedList(self, head, k):
        new_head, ptr = None, head

        while k:
            nextnode = ptr.next
            ptr.next = new_head
            new_head = ptr
            ptr = nextnode

            k-= 1
        return new_head

    def reverseKGroup(self, head,k):
        count = 0
        ptr = head
        while count < k and ptr:
            ptr = ptr.next
            count += 1

        if count == k:
            reverseHead = self.reverseLinkedList(head,k)
            head.next = self.reverseKGroup(ptr,k)

            return reverseHead
        return head
