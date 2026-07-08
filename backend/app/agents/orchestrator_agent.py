from app.graph.state import BlueprintState


class OrchestratorAgent:

    def execute(self, state: BlueprintState):

        if not state["clarification_answers"]:
            state["current_step"] = "clarification"
            state["is_clarification_complete"] = False

        else:
            state["current_step"] = "planning"
            state["is_clarification_complete"] = True

        return state