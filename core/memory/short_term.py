from langchain.memory.buffer import ConversationBufferMemory


memory_store = {}

def get_memory(agent_name: str):
    if agent_name not in memory_store:
        memory_store[agent_name] = ConversationBufferMemory(
            return_messages=True
        )
    return memory_store[agent_name]
