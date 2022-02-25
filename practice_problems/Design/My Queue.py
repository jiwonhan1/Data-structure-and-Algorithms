# Push O(N) POP O(1)
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self,x):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())
    def pop(self):
        return self.s1.pop()
    def peek(self):
        return self.s1[-1]
    def empty(self):
        return not self.s1

class MyQueue2:
    # push O(1) pop amortized O(1)
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def push(self,x):
        self.s1.append(x)
    def pop(self):
        self.peek()
        return self.s2.pop()
    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]
    def empty(self):
        return not self.s1 and not self.s2