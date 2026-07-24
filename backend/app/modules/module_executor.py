from app.modules.register_modules import registry
from app.graph.state import BlueprintState


class ModuleExecutor:

    @staticmethod
    def execute(state: BlueprintState):

        for module_name in state["requested_modules"]:

            module = registry.get(module_name)

            if module:
                state = module.execute(state)

        return state