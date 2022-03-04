from Queue import PriorityQueue

class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution(object):
    # Brute Force
    # Traverse all the linked lists and collection the values of the nodes into an array
    # Sort and iterate over this array to get the proper value of nodes
    # Create a new sorted linked list and extend it with the new nodes
    # Time complexity O(N log N)
    # Space complexity O(N)
    def mergeKLists(self, lists):
        nodes = []
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        dummy = ListNode()
        curr = dummy

        for node in sorted(nodes):
            curr.next = ListNode(node)
            curr = curr.next
        return dummy.next

    # Optimize by Priority Queue
    # Time complexity O(N log K) where k is the number of linked lists.
    # The comparison cost will be reduced to O(logk) for every pop and insertion to priority queue. But finding the node with the smallest value just costs O(1) time.
    # There are N nodes in the final linked list.
    # Space complexity O(N) creating a new linked list costs O(n) space
    # O(k) The node above present applies in-place method which cost O(1) space.
    # Priority queue costs O(k) space
    def mergeKLists2(self, lists):
        def mergeKLists(self, lists):
            head = pointer = ListNode()
            q = PriorityQueue()
            for l in lists:
                if l:
                    q.put((l.val, l))
            while not q.empty():
                val, node = q.get()
                pointer.next = ListNode(val)
                point = point.next
                node = node.next
                if node:
                    q.put((node.val, node))
            return head.next