class MyCircularQueue(object):
    def __init__(self,k):
        self.queue = [0] * k
        self.headIndex = 0
        self.count = 0
        self.capacity = k

    def enQueue(self, value):
        if self.count == self.capacity:
            return False
        self.queue[(self.headIndex + self.count) % self.capacity] = value
        return True

    def deQueue(self):
        if self.count == 0:
            return False
        self.headIndex = (self.headIndex + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self):
        if self.count == 0:
            return -1
        return self.queue[self.headIndex]

    def Rear(self):
        if self.count == 0:
            return -1
        return self.queue[(self.headIndex + self.count) % self.capacity]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.capacity