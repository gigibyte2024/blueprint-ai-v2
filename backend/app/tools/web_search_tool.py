from duckduckgo_search import DDGS

from app.tools.base_tool import BaseTool


class WebSearchTool(BaseTool):

    @property
    def name(self):
        return "web_search"

    def execute(self, query, max_results=2):

        with DDGS() as ddgs:

            results = list(
                ddgs.text(
                    query,
                    max_results=max_results,
                )
            )

        return results