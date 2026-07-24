from app.graph.state import BlueprintState


class ContextBuilder:

    @staticmethod
    def build(state: BlueprintState):

        state["project_context"] = {
            "idea": state["idea"],
            "clarification_answers": state["clarification_answers"],
            "planning": state["planning_output"]
        }

        return state