class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution(object):
    # Time complexity O(n) Space compexity O(1)
    def swapParis(self, head):
        dummy = ListNode()
        dummy.next = head

        prev_node = dummy

        while head and head.next:
            first_node = head
            second_node = head.next

            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            prev_node = first_node
            head = first_node.next

        return dummy.next

    # Time complexity O(N)
    # Space complexity O(N)
    def swapPairs2(self, head):
        if not head or head.next:
            return head

        first_node = head
        second_node = head.next

        first_node.next = self.swapPairs2(second_node.next)
        second_node.next = first_node

        return second_node
