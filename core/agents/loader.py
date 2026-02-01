import os
import yaml

AGENTS_DIR = os.path.dirname(__file__)

def load_agents():
    agents = {}

    for file in os.listdir(AGENTS_DIR):
        if file.endswith(".yaml"):
            path = os.path.join(AGENTS_DIR, file)

            with open(path, "r") as f:
                agent = yaml.safe_load(f)

            agents[agent["name"]] = agent

    return agents
