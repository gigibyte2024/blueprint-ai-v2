import json

from app.agents.base_agent import BaseAgent
from app.graph.state import BlueprintState


class DatabaseAgent(BaseAgent):

    def __init__(self):
        super().__init__("database.txt")

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

        result = self.run(
            idea=state["idea"],
            planning=json.dumps(state["planning_output"], indent=2),
            prd=json.dumps(state["prd_output"], indent=2),
            research=json.dumps(state["project_context"], indent=2),
)

        state["database_output"] = result

        return state