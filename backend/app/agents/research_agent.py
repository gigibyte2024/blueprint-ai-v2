import json

from app.agents.base_agent import BaseAgent
from app.graph.state import BlueprintState
from app.rag.retriever import get_retriever


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

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        result = self.run(
            idea=state["idea"],
            context=context,
        )

        state["project_context"] = result

        return state