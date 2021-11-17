class ListNode(object):
    # Copy into Array List and then Use Two Pointer Technique
    # Time complextiy O(N)
    # Space complexity O(1)
    def isPalindrome(self, head):
        vals = []
        current_node = head

        while current_node:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]

    # Recursive
    # The order in which nodes are processed by the recursion is in reverse
    # Each node compares itself against frontPointer and then moves frontPointer don by 1, ready for the next node in the recursion
    # In essence, we are iterating both backwrads and forwards at the same time
    # Time complexity O(N) Space complexity O(N)
    def isPalindrome2(self, head):
        self.front_pointer = head

        def recursively_check(current_node = head):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer != current_node:
                    return False
                self.front_pointer = self.front_pointer.next
            return True
        return recursively_check();
