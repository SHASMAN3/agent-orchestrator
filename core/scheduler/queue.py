from collections import deque

class TaskQueue:
    def __init__(self):
        self.queue = deque()

    def push(self, task):
        self.queue.append(task)

    def pop(self):
        return self.queue.popleft() if self.queue else None
