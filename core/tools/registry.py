from core.tools.web_search import WebSearchTool

TOOL_REGISTRY = {
    "web_search": WebSearchTool()
}

def get_tool(name: str):
    if name not in TOOL_REGISTRY:
        raise ValueError(f"Tool '{name}' not registered")
    return TOOL_REGISTRY[name]
