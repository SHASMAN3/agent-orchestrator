from core.tools.base import Tool

class WebSearchTool(Tool):
    name = "web_search"
    description = "Search the web for information"

    def run(self, input: str) -> str:
        # Placeholder (replace with real API later)
        return f"[WebSearch Result for '{input}']"
