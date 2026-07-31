import json

from app.agents.base_agent import BaseAgent
from app.graph.state import BlueprintState


class ResearchAgent(BaseAgent):

    def __init__(self):
        super().__init__("research.txt")

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

        result = self.run(
            idea=state["idea"]
        )

        state["project_context"] = result

        return state