import threading
import time
from core.runtime.engine import run_agent
from core.scheduler.task import TaskStatus

class Worker(threading.Thread):
    def __init__(self, queue, agents):
        super().__init__(daemon=True)
        self.queue = queue
        self.agents = agents

    def run(self):
        while True:
            task = self.queue.pop()
            if not task:
                time.sleep(0.5)
                continue

            task.status = TaskStatus.RUNNING
            agent = self.agents[task.agent_name]

            try:
                run_agent(agent, task.payload)
                task.status = TaskStatus.COMPLETED
            except Exception:
                task.retries += 1
                task.status = TaskStatus.FAILED
