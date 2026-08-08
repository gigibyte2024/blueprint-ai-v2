import json

from app.agents.base_agent import BaseAgent
from app.graph.state import BlueprintState


class CriticAgent(BaseAgent):

    def __init__(self):
        super().__init__("critic.txt")

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

        try:

            result = self.run(
                blueprint=json.dumps(
                    state.get(
                        "final_blueprint",
                        {}
                    )
                )
            )

            state["critic_output"] = result

            return state

        except Exception as error:

            print(
                f"⚠️ Critic failed gracefully: {error}"
            )

            state["critic_output"] = {
                "status": "failed",
                "score": 10,
                "reason": (
                    "Critic unavailable. "
                    "Blueprint generation continued."
                ),
                "error": str(error),
            }

            return state