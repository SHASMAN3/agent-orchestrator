import yaml
from pathlib import Path

AGENT_DIR = Path(__file__).parent

def load_agent(name: str):
    for file in AGENT_DIR.glob("*.yaml"):
        with open(file, "r") as f:
            agent = yaml.safe_load(f)
            if agent["name"] == name:
                return agent
    raise ValueError(f"Agent '{name}' not found")
