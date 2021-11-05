# Stack of Value / Minimum Pairs
# Time complexity O(1) for all operations
# Space complexity O(N)
class MinStack(object):
    def __init__(self):
        self.stack = []

    def push(self,val):
        if not self.stack:
            self.stack.append((val, val))
            return
        current_min = self.stack[-1][1]
        self.stack.append((val,min(val, current_min)))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]

# Two Stacks
# Time complexity O(1) for all operations
# Space complexity O(N)
class MinStack2(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push (self, val):
        self.stack.append(val)
        if not self.min_stack or val < self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]