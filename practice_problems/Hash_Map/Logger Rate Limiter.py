class Logger(object):
    # Time complexity O(1)
    # Space complexity O(M)
    def __init__(self):
        self.msg_dict = {}

    def shouldPrintMessage(self, timestamp, message):
        if message not in self.msg_dict:
            self.msg_dict[message] = timestamp
            return True
        if timestamp - self.msg_dict[message] >= 10:
            self.msg_dict[message] = timestamp
            return True
        else:
            return False
from collections import deque
class Logger2(object):
    # Time complexity O(N)
    # Space complexity O(N)
    def __init__(self):
        self.msg_set = set()
        self.msg_queue = deque()

    def shouldPrintMessage(self, timestamp, message):
        while self.msg_queue:
            msg, ts = self.msg_queue[0]
            if timestamp - ts >= 10:
                self.msg_queue.popleft()
                self.msg_set.remove(msg)
            else:
                break
        if message not in self.msg_set:
            self.msg_set.add(message)
            self.msg_queue.append((message, timestamp))
            return True
        else:
            return False

    # The main difference between this approach with hashtable and the previous approach with queue is that
    # in previous approach we do proactive cleaning at each invocation of fuction, we first remove those expired message

    # While in this approach, we keep all the messages even when they are expired. This characteristics might become problematic,
    # since the usage of memory would keep on growing over the time.
    # Sometimes it might be more desirable to have the garbage collection property of the prvious approach.

