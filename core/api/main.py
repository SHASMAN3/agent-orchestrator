from fastapi import FastAPI
from pydantic import BaseModel
from core.agents.registry import load_agent
from core.runtime.engine import run_agent

app = FastAPI(title="Agent Orchestrator")

class TaskRequest(BaseModel):
    agent_name: str
    task: str

@app.post("/task/run")
def run_task(req: TaskRequest):
    agent = load_agent(req.agent_name)
    result = run_agent(agent, req.task)
    return {"result": result}

@app.get("/health")
def health_check():
    return {"status": "ok"}
