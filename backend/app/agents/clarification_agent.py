import json

from app.agents.base_agent import BaseAgent
from app.graph.state import BlueprintState


class ClarificationAgent(BaseAgent):

    def __init__(self):
        super().__init__("clarification.txt")

    def parse(self, response):
        return json.loads(response)

    def execute(self, state: BlueprintState):

        result = self.run(
            idea=state["idea"]
        )

        state["clarification_questions"] = result["questions"]

        return state