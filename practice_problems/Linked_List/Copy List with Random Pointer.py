class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def __init__(self):
        self.visitedHash = {}
        # Recursive
        # Time complexity O(N) Space complexity O(N)
    def copyRandomList(self, head):
        if not head:
            return None

        # It we have already processed the current node, then we simply return the cloned version of it.
        if head in self.visitedHash:
            return self.visitedHash[head]

        # create a new node
        # with the value same as old node.
        node = Node(head.val, None, None)

        # Save this value in the hash map. This is needed since there might be loops during traversal due to randomness of random pointers and this help us avoid them
        self.visitedHash[head] = node

        # Recursively copy the remaining linked list starting once from the next pointer and then from the random pointer
        # Thus we have two independent recursive calls
        # Finally we update the next and random pointers for the new node created
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node

