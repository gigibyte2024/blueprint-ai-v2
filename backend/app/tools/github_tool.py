import requests

from app.tools.base_tool import BaseTool


class GitHubTool(BaseTool):

    @property
    def name(self):
        return "github_search"

    def execute(self, query):

        url = "https://api.github.com/search/repositories"

        response = requests.get(
            url,
            params={
                "q": query,
                "sort": "stars",
                "per_page": 5,
            },
            timeout=10,
        )

        if response.status_code != 200:
            return []

        items = response.json().get("items", [])

        return [
            {
                "name": repo["full_name"],
                "url": repo["html_url"],
                "stars": repo["stargazers_count"],
                "description": repo["description"],
            }
            for repo in items
        ]