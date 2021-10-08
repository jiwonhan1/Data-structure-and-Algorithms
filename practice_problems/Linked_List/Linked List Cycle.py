class Solution(object):
    #Time complexity O(n) Space complexity O(n)
    def hasCylce(self, head):
        node_seen = set()
        while head:
            if head in node_seen:
                return True
            node_seen.add(head)
            head = head.next
        return False

    # Floyd's Cycle Finding Algorithm
    def hasCyle2(self, head):
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
