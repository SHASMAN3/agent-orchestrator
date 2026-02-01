from uuid import uuid4
from enum import Enum

class TaskStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    FAILED = "failed"
    COMPLETED = "completed"

class AgentTask:
    def __init__(self, agent_name: str, payload: str):
        self.id = str(uuid4())
        self.agent_name = agent_name
        self.payload = payload
        self.status = TaskStatus.PENDING
        self.retries = 0
