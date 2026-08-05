from app.tools.web_search_tool import WebSearchTool
from app.tools.tool_registry import tool_registry
from app.tools.tool_decider import ToolDecider
from app.tools.github_tool import GitHubTool

tool_registry.register(
    "web_search",
    WebSearchTool(),
)
tool_registry.register(
    "tool_decider",
    ToolDecider(),
)

tool_registry.register(
    "github_search",
    GitHubTool(),
)