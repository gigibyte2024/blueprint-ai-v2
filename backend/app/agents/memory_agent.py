from app.graph.state import BlueprintState
from app.memory.memory_manager import MemoryManager


class MemoryAgent:

    def __init__(self):
        self.memory = MemoryManager()

    def execute(self, state: BlueprintState):

        last_project = self.memory.get_last_project()

        if last_project:
            state["project_context"]["memory"] = last_project
        else:
            state["project_context"]["memory"] = {}

        return state