from app.graph.state import BlueprintState


# class OrchestratorAgent:

#     def execute(self, state: BlueprintState):

#         if not state["clarification_answers"]:
#             state["current_step"] = "clarification"
#             state["is_clarification_complete"] = False

#         else:
#             state["current_step"] = "planning"
#             state["is_clarification_complete"] = True

#         return state

class OrchestratorAgent:

    def execute(self, state):

        if (
            not state["is_clarification_complete"]
            and not state["clarification_answers"]
        ):
            state["current_step"] = "clarification"
        else:
            state["current_step"] = "planning"

        return state