from core.scheduler.redis_queue import RedisTaskQueue
from core.scheduler.worker import Worker

class Scheduler:
    def __init__(self, agents, workers=2):
        self.queue = RedisTaskQueue()
        self.workers = [
            Worker(self.queue, agents)
            for _ in range(workers)
        ]

    def start(self):
        for w in self.workers:
            w.start()

    def submit(self, task):
        self.queue.push(task)
