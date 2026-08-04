import json

from app.agents.base_agent import BaseAgent
from app.graph.state import BlueprintState


class TechnicalAgent(BaseAgent):

    def __init__(self):
        super().__init__("technical.txt")

    def parse(self, response):

        response = response.strip()

        if response.startswith("```json"):
            response = response.replace("```json", "", 1)

        if response.endswith("```"):
            response = response[:-3]

        print("\n========== TECHNICAL AGENT OUTPUT ==========\n")
        print(response)
        print("\n===========================================\n")

        try:
            return json.loads(response)
        except json.JSONDecodeError:
            print("\n===== INVALID JSON FROM LLM =====\n")
            print(response)
            print("\n=================================\n")
            raise

    def execute(self, state: BlueprintState):
        if "technical" not in state["requested_modules"]:
            return state

        planning = state["planning_output"]

        result = self.run(
            summary=planning["product_summary"],
            features=planning["features"],
            research=state["project_context"]
)
        state["technical_output"] = result

        return state