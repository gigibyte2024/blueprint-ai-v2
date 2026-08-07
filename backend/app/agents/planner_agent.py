import json

from app.agents.base_agent import BaseAgent
from app.graph.state import BlueprintState
from app.execution.executor import ExecutionEngine

class PlannerAgent(BaseAgent):

    def __init__(self):
        super().__init__("planner.txt")

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
            idea=state["idea"],
            modules=state["requested_modules"],
        )

        state["execution_plan"] = result

        engine = ExecutionEngine()

        state = engine.execute(
            result,
            state,
        )   

        return state