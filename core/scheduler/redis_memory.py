import redis
import json

redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)

class RedisConversationMemory:
    def __init__(self, agent_name: str):
        self.key = f"memory:{agent_name}"

    def add_user(self, message: str):
        redis_client.rpush(self.key, json.dumps({
            "role": "user",
            "content": message
        }))

    def add_agent(self, message: str):
        redis_client.rpush(self.key, json.dumps({
            "role": "assistant",
            "content": message
        }))

    def get_history(self):
        return [json.loads(x) for x in redis_client.lrange(self.key, 0, -1)]
