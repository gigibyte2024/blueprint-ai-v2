from app.graph.state import BlueprintState


class ComposerAgent:

    def execute(self, state: BlueprintState):

        state["final_blueprint"] = {
            "planning": state["planning_output"],
            "technical": state["technical_output"],
            "ui": state["ui_output"]
        }

        return state