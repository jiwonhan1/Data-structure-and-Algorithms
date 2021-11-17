class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = None

class MyLinkedLIst:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1

        curr = self.head

        for _ in range(index + 1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        if index > self.size:
            return
        if index < 0:
            index = 0

        self.size += 1

        pred = self.head

        to_add = ListNode(val)
        for _ in range(index+1):
            pred = pred.next

        to_add.next = pred.next
        pred.next = to_add

    def deleteAtIndex(self, index):
        if index < 0 or index > self.size:
            return

        self.size -= 1

        pred = self.head
        for _ in range(index + 1):
            pred = pred.next

        pred.next = pred.next.next

