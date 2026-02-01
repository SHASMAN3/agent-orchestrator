from core.memory.in_memory import InMemoryConversation

_memory_store = {}

def get_memory(agent_name: str):
    if agent_name not in _memory_store:
        _memory_store[agent_name] = InMemoryConversation()
    return _memory_store[agent_name]
