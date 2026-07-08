from langgraph.graph import StateGraph, END

from app.graph.state import BlueprintState
from app.agents.orchestrator_agent import OrchestratorAgent
from app.agents.clarification_agent import ClarificationAgent
from app.agents.planning_agent import PlanningAgent
from app.agents.technical_agent import TechnicalAgent
from app.agents.ui_agent import UIAgent
from app.agents.composer_agent import ComposerAgent

builder = StateGraph(BlueprintState)
planning = PlanningAgent()
orchestrator = OrchestratorAgent()
clarification = ClarificationAgent()

builder.add_node("orchestrator", orchestrator.execute)
builder.add_node("clarification", clarification.execute)

builder.set_entry_point("orchestrator")
technical = TechnicalAgent()
ui = UIAgent()
composer = ComposerAgent()

def route(state: BlueprintState):

    return state["current_step"]


builder.add_conditional_edges(
    "orchestrator",
    route,
    {
        "clarification": "clarification",
        "planning": "planning"
    },
)

builder.add_edge(
    "clarification",
    END,
)

builder.add_node(
    "planning",
    planning.execute,
)
builder.add_edge(
    "planning",
    "technical"
)

builder.add_edge(
    "technical",
    "ui",
)

builder.add_edge(
    "ui",
    "composer",
)

builder.add_edge(
    "composer",
    END,
)
builder.add_node(
    "technical",
    technical.execute
)

builder.add_node(
    "ui",
    ui.execute,
)

builder.add_node(
    "composer",
    composer.execute,
)

workflow = builder.compile()