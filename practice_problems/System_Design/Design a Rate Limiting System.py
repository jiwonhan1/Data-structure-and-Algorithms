from collections import deque

class RateLimiter:

    def __init__(self, n, t):
        self.Q = deque(maxlen=n)
        self.t = t
        self.n = n

    def shouldAllow(self, timestamp):
        if len(self.Q) < self.n:
            self.Q.append(timestamp)
            return True
        else:
            if timestamp - self.Q[0] >= self.t:
                self.Q.popleft()
                self.Q.append(timestamp)
                return True
            else:
                return False