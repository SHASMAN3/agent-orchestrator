from core.runtime.llm import call_llm

def run_agent(agent: dict, task: str):
    prompt = f"""
You are an AI agent named {agent['name']}.

Role:
{agent.get('description', '')}

Task:
{task}

Respond clearly and concisely.
"""
    return call_llm(prompt, agent["model"])
