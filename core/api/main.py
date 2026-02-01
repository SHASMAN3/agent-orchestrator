from fastapi import FastAPI
from core.scheduler.scheduler import Scheduler
from core.scheduler.task import AgentTask
from core.agents.loader import load_agents

app = FastAPI()
agents = load_agents()

scheduler = Scheduler(agents)
scheduler.start()

@app.post("/task/submit")
def submit_task(agent_name: str, task: str):
    agent_task = AgentTask(agent_name, task)
    scheduler.submit(agent_task)
    return {
        "task_id": agent_task.id,
        "status": agent_task.status
    }
