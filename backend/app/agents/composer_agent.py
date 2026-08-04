from app.graph.state import BlueprintState
from app.memory.memory_manager import MemoryManager


class ComposerAgent:

    def __init__(self):
        self.memory = MemoryManager()

    def execute(self, state: BlueprintState):

        modules = {
    "planning": state.get("planning_output", {}),
    "prd": state.get("prd_output", {}),
    "technical": state.get("technical_output", {}),
    "api": state.get("api_output", {}),
    "database": state.get("database_output", {}),
    "roadmap": state.get("roadmap_output", {}),
    "ui": state.get("ui_output", {}),
    "reflection": state.get("reflection_output", {}),
}

        state["final_blueprint"] = {
            key: value
            for key, value in modules.items()
            if key in state["requested_modules"]
        }

        self.memory.save_blueprint(
            state["idea"],
            state["final_blueprint"],
        )

        return state