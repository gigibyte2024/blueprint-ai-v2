import json

from app.agents.base_agent import BaseAgent
from app.graph.state import BlueprintState


class PlanningAgent(BaseAgent):

    def __init__(self):
        super().__init__("planning.txt")

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

        idea = state.get(
            "idea",
            "",
        )

        answers = state.get(
            "clarification_answers",
            [],
        )

        return {
            "status": "fallback",

            "project_overview": {
                "idea": idea,
                "answers": answers,
            },

            "objectives": [
                "Validate the product idea",
                "Define the MVP scope",
                "Design a scalable architecture",
                "Identify implementation requirements",
            ],

            "target_users": [
                "General users",
            ],

            "mvp_scope": [
                "Core user experience",
                "Authentication",
                "Primary application workflow",
                "Data persistence",
                "AI-powered functionality",
            ],

            "success_metrics": [
                "Successful core workflow",
                "Reliable API responses",
                "Usable frontend experience",
                "Successful blueprint generation",
            ],

            "risks": [
                "LLM availability",
                "API rate limits",
                "Data consistency",
                "Scalability",
            ],

            "reason": (
                "AI planning unavailable. "
                "Using deterministic fallback planning."
            ),
        }

    def execute(self, state: BlueprintState):

        if "planning" not in state["requested_modules"]:
            return state

        try:

            result = self.run(
                idea=state["idea"],
                answers=state["clarification_answers"],
                research=state["project_context"],
            )

            state["planning_output"] = result
            state["planning_status"] = "completed"

        except Exception as error:

            print(
                f"⚠️ Planning failed gracefully: {error}"
            )

            state["planning_output"] = (
                self.fallback_plan(state)
            )

            state["planning_status"] = "fallback"

        return state