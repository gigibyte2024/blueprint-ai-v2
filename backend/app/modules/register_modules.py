from app.modules.module_registry import ModuleRegistry

from app.agents.planning_agent import PlanningAgent
from app.agents.technical_agent import TechnicalAgent
from app.agents.ui_agent import UIAgent
from app.agents.prd_agent import PRDAgent

registry = ModuleRegistry()
registry.register("planning", PlanningAgent())
registry.register("prd", PRDAgent())
registry.register("technical", TechnicalAgent())
registry.register("ui", UIAgent())