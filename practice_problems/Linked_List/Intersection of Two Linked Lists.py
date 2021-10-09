class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    # Brute Force
    # Time Complexity O(N * M) Space Complexity O(1)
    def getIntersectionNode(self, headA, headB):
        while headA:
            pB = headB
            while pB:
                if headA == pB:
                    return headA
                pB = pB.next
            headA = headA.next
        return None

    # Set
    # Time Complexity O(N + M) Space Compexity O(N)
    def getIntersectionNode2(self, headA, headB):
        nodes_seen_B = set()

        while headB:
            nodes_seen_B.add(headB)
            headB = headB.next
        while headA:
            if headA in nodes_seen_B:
                return headA
            headA = headA.next
        return None

