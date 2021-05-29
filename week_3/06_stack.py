class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            newNode = Node(value).next
            newNode.next = self.head
            self.head = newNode
        return

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        delete_head = self.head
        self.head = self.head.next
        return delete_head.data

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.head.data

    def is_empty(self):
        return self.head is None


stack = Stack()
stack.push(3)
print(stack.pop())
print(stack.peek())
print(stack.is_empty())