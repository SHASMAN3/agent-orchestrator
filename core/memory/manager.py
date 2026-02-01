from core.memory.redis_memory import RedisConversationMemory

def get_memory(agent_name: str):
    return RedisConversationMemory(agent_name)
