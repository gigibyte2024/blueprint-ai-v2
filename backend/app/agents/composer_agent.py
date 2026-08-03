from app.graph.state import BlueprintState
from app.memory.memory_manager import MemoryManager


class ComposerAgent:

    def __init__(self):
        self.memory = MemoryManager()

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

        self.memory.save_blueprint(
            state["idea"],
            state["final_blueprint"],
        )

        return state