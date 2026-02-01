from langchain.messages import HumanMessage, AIMessage, SystemMessage
import time
# from langchain.schema import HumanMessage
from core.runtime.llm import get_chat_model
from core.tools.registry import get_tool
from core.memory.manager import get_memory
from core.cost.tracker import CostTracker
from core.policy.prompt import validate_prompt
from core.policy.tools import ToolLimiter
from core.observability.logger import get_logger
from core.observability.trace import generate_trace_id
from core.observability.metrics import metrics

logger = get_logger()

def run_agent(agent: dict, task: str):
    trace_id = generate_trace_id()
    start = time.time()

    logger.info("Agent task started", extra={"trace_id": trace_id})
    metrics.incr("agent_runs_total")

    try:
        validate_prompt(task)
        memory = get_memory(agent["name"])
        memory.add_user(task)

        tool_limiter = ToolLimiter()
        tool_output = ""

        if "search" in task.lower():
            for tool_name in agent.get("tools", []):
                tool_limiter.check()
                tool = get_tool(tool_name)
                tool_output = tool.run(task)
                break

        history = "\n".join(
            f"{h['role']}: {h['content']}"
            for h in memory.get_history()
        )

        prompt = f"""
You are {agent['name']}.

History:
{history}

Tool output:
{tool_output}

Task:
{task}
"""

        model = get_chat_model(agent["model"])
        response = model.invoke([HumanMessage(content=prompt)])

        memory.add_agent(response.content)
        metrics.incr("agent_success_total")

        return response.content

    except Exception as e:
        metrics.incr("agent_failures_total")
        logger.error(
            f"Agent task failed: {e}",
            extra={"trace_id": trace_id}
        )
        raise

    finally:
        duration = time.time() - start
        metrics.timing("agent_latency_seconds", duration)
        logger.info(
            "Agent task completed",
            extra={"trace_id": trace_id}
        )
