import json

from app.agents.base_agent import BaseAgent
from app.graph.state import BlueprintState


class PlannerAgent(BaseAgent):

    def __init__(self):
        super().__init__("planner.txt")

    def parse(self, response):

        response = response.strip()

        if response.startswith("```json"):
            response = response.replace(
                "```json",
                "",
                1,
            )

        if response.startswith("```"):
            response = response.replace(
                "```",
                "",
                1,
            )

        if response.endswith("```"):
            response = response[:-3]

        response = response.strip()

        return json.loads(response)

    def fallback_plan(self, state):

        requested = state.get(
            "requested_modules",
            [],
        )

        execution_modules = [
            module
            for module in requested
            if module not in {
                "planning",
                "reflection",
            }
        ]

        groups = []

        if "prd" in execution_modules or \
           "technical" in execution_modules:

            groups.append([
                module
                for module in [
                    "prd",
                    "technical",
                ]
                if module in execution_modules
            ])

        if "api" in execution_modules or \
           "database" in execution_modules:

            groups.append([
                module
                for module in [
                    "api",
                    "database",
                ]
                if module in execution_modules
            ])

        if "roadmap" in execution_modules or \
           "ui" in execution_modules:

            groups.append([
                module
                for module in [
                    "roadmap",
                    "ui",
                ]
                if module in execution_modules
            ])

        return {
            "tools": [],
            "parallel_groups": groups,
            "priority": "balanced",
            "status": "fallback",
            "reason": (
                "AI planner unavailable. "
                "Using deterministic execution plan."
            ),
        }

    def execute(self, state: BlueprintState):

        try:

            result = self.run(
                idea=state["idea"],
                modules=state["requested_modules"],
            )

        except Exception as error:

            print(
                f"⚠️ Planner failed gracefully: {error}"
            )

            result = self.fallback_plan(state)

        state["execution_plan"] = result


        return state