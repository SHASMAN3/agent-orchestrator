from langchain.messages import HumanMessage, AIMessage, SystemMessage
# from langchain.schema import HumanMessage
from core.runtime.llm import get_chat_model
from core.tools.registry import get_tool
from core.memory.manager import get_memory
from core.cost.tracker import CostTracker
from core.policy.prompt import validate_prompt
from core.policy.tools import ToolLimiter

def run_agent(agent: dict, task: str):
    validate_prompt(task)

    memory = get_memory(agent["name"])
    memory.add_user(task)

    cost_tracker = CostTracker(agent["budget"]["max_usd"])
    tool_limiter = ToolLimiter()

    tool_output = ""
    if "search" in task.lower():
        for tool_name in agent.get("tools", []):
            tool_limiter.check()
            tool = get_tool(tool_name)
            tool_output = tool.run(task)
            break

    history_text = "\n".join(
        [f"{h['role']}: {h['content']}" for h in memory.get_history()]
    )

    prompt = f"""
You are {agent['name']}.

Conversation history:
{history_text}

Tool output:
{tool_output}

Task:
{task}
"""

    model = get_chat_model(agent["model"])
    response = model.invoke([HumanMessage(content=prompt)])

    # Approx token estimation
    input_tokens = len(prompt.split())
    output_tokens = len(response.content.split())

    cost_tracker.charge(
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        model=agent["model"]
    )

    memory.add_agent(response.content)
    return response.content
