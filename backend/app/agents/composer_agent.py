from app.graph.state import BlueprintState


class ComposerAgent:

    def execute(self, state: BlueprintState):

        state["final_blueprint"] = {

            "planning": state["planning_output"],
            "prd": state["prd_output"],
            "technical": state["technical_output"],
            "api": state["api_output"],
            "database": state["database_output"],
            "roadmap": state["roadmap_output"],
            "ui": state["ui_output"]

        }

        return state