import json

from app.agents.base_agent import BaseAgent
from app.graph.state import BlueprintState
from app.rag.retriever import get_retriever
from app.tools.tool_registry import tool_registry


class ResearchAgent(BaseAgent):

    def __init__(self):
        super().__init__("research.txt")
        self.retriever = get_retriever()

    def parse(self, response):

        response = response.strip()

        if response.startswith("```json"):
            response = response.replace("```json", "", 1)

        if response.startswith("```"):
            response = response.replace("```", "", 1)

        if response.endswith("```"):
            response = response[:-3]

        response = response.strip()

        return json.loads(response)

    def execute(self, state: BlueprintState):

        docs = self.retriever.invoke(state["idea"])

        rag_context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        execution_plan = state.get("execution_plan", {})

        tools = execution_plan.get("tools")

        if not tools:

            tool_decider = tool_registry.get("tool_decider")

            decision = tool_decider.decide(
                state["idea"]
            )

            tools = decision["tools"]

        context_parts = []

        for tool_name in tools:

            tool = tool_registry.get(tool_name)

            if tool is None:
                continue

            print(f"\n🔧 Using Tool: {tool_name}\n")

            if tool_name == "web_search":

                results = tool.execute(
                    query=state["idea"],
                    max_results=2,
                )

                context_parts.append(
                    "WEB SEARCH:\n"
                    + "\n".join(
                        item["title"]
                        for item in results
                    )
                )

            elif tool_name == "github_search":

                results = tool.execute(
                    query=state["idea"]
                )

                context_parts.append(
                    "GITHUB:\n"
                    + "\n".join(
                        repo["name"]
                        for repo in results
                    )
                )

        tool_context = "\n\n".join(context_parts)

        result = self.run(
            idea=state["idea"],
            context=f"""
RAG Knowledge:

{rag_context}

Tool Results:

{tool_context}
""",
        )

        state["project_context"] = result

        return state