import json
import redis
from core.scheduler.task import AgentTask

redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)

QUEUE_KEY = "agent_tasks"

class RedisTaskQueue:
    def push(self, task: AgentTask):
        redis_client.rpush(QUEUE_KEY, json.dumps(task.__dict__))

    def pop(self):
        data = redis_client.lpop(QUEUE_KEY)
        if not data:
            return None

        payload = json.loads(data)
        task = AgentTask(payload["agent_name"], payload["payload"])
        task.__dict__.update(payload)
        return task
