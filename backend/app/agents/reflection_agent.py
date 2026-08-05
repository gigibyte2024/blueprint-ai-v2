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

        # Prevent infinite reflection loops
        if state.get("reflection_done", False):
            return state

        critic = state.get("critic_output", {})

        if critic.get("score", 10) >= 8:
            return state

        result = self.run(
            planning=state.get("planning_output", {}),
            prd=state.get("prd_output", {}),
            technical=state.get("technical_output", {}),
            api=state.get("api_output", {}),
            database=state.get("database_output", {}),
            roadmap=state.get("roadmap_output", {}),
            ui=state.get("ui_output", {}),
            critic=json.dumps(critic, indent=2),
        )

        state["reflection_output"] = result
        state["reflection_done"] = True

        return state