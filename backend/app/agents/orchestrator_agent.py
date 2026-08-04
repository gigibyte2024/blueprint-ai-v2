from app.graph.state import BlueprintState


class OrchestratorAgent:

    def execute(self, state: BlueprintState):

        if (
            not state["is_clarification_complete"]
            and not state["clarification_answers"]
        ):
            state["current_step"] = "clarification"
        else:
            state["current_step"] = "research"

        return state