import json

from app.agents.base_agent import BaseAgent
from app.graph.state import BlueprintState


class APIAgent(BaseAgent):

    def __init__(self):
        super().__init__("api.txt")

    def parse(self, response):

        response = response.strip()

        if response.startswith("```json"):
            response = response.replace("```json", "", 1)

        if response.startswith("```"):
            response = response.replace("```", "", 1)

        if response.endswith("```"):
            response = response[:-3]

        return json.loads(response)

    def execute(self, state: BlueprintState):
        if "api" not in state["requested_modules"]:
            return state

        result = self.run(
            idea=state["idea"],
            planning=json.dumps(state["planning_output"], indent=2),
            prd=json.dumps(state["prd_output"], indent=2),
            research=json.dumps(state["project_context"], indent=2),
)


        state["api_output"] = result

        return state