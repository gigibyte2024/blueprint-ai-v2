import json

from app.agents.base_agent import BaseAgent
from app.graph.state import BlueprintState


class ReflectionAgent(BaseAgent):

    def __init__(self):
        super().__init__("reflection.txt")

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
            planning=state["planning_output"],
            prd=state["prd_output"],
            technical=state["technical_output"],
            api=state["api_output"],
            database=state["database_output"],
            roadmap=state["roadmap_output"],
            ui=state["ui_output"],
        )

        state["reflection_output"] = result

        return state