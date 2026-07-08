import json

from app.agents.base_agent import BaseAgent
from app.graph.state import BlueprintState


class UIAgent(BaseAgent):

    def __init__(self):
        super().__init__("ui.txt")

    def parse(self, response):

        response = response.strip()

        if response.startswith("```json"):
            response = response.replace("```json", "", 1)

        if response.endswith("```"):
            response = response[:-3]

        response = response.strip()

        return json.loads(response)

    def execute(self, state: BlueprintState):

        planning = state["planning_output"]

        result = self.run(
            summary=planning["product_summary"],
            features=planning["features"]
        )

        state["ui_output"] = result

        return state