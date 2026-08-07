from langgraph.graph import StateGraph, END

from app.graph.state import BlueprintState
from app.agents.orchestrator_agent import OrchestratorAgent
from app.agents.clarification_agent import ClarificationAgent
from app.agents.planning_agent import PlanningAgent
from app.agents.technical_agent import TechnicalAgent
from app.agents.ui_agent import UIAgent
from app.agents.composer_agent import ComposerAgent
from app.agents.prd_agent import PRDAgent
from app.agents.api_agent import APIAgent
from app.agents.database_agent import DatabaseAgent
from app.agents.roadmap_agent import RoadmapAgent
from app.agents.reflection_agent import ReflectionAgent
from app.agents.research_agent import ResearchAgent
from app.agents.memory_agent import MemoryAgent
from app.agents.critic_agent import CriticAgent
from app.agents.planner_agent import PlannerAgent

builder = StateGraph(BlueprintState)

planning = PlanningAgent()
orchestrator = OrchestratorAgent()
planner = PlannerAgent()
clarification = ClarificationAgent()
technical = TechnicalAgent()
ui = UIAgent()
composer = ComposerAgent()
prd = PRDAgent()
api = APIAgent()
database = DatabaseAgent()
roadmap = RoadmapAgent()
reflection = ReflectionAgent()
critic = CriticAgent()
research = ResearchAgent()
memory = MemoryAgent()

builder.set_entry_point("orchestrator")

builder.add_node("orchestrator", orchestrator.execute)
builder.add_node("planner",planner.execute)
builder.add_node("clarification", clarification.execute)
builder.add_node("research", research.execute)
builder.add_node("memory", memory.execute)
builder.add_node("planning", planning.execute)
builder.add_node("prd", prd.execute)
builder.add_node("technical", technical.execute)
builder.add_node("api", api.execute)
builder.add_node("database", database.execute)
builder.add_node("roadmap", roadmap.execute)
builder.add_node("ui", ui.execute)
builder.add_node("reflection", reflection.execute)
builder.add_node("critic",critic.execute)
builder.add_node("composer", composer.execute)


def route(state: BlueprintState):
    return state["current_step"]

def should_run(module):

    def router(state: BlueprintState):

        if module in state["requested_modules"]:
            return "run"

        return "skip"

    return router

def critic_route(state: BlueprintState):

    score = state["critic_output"].get("score", 10)

    if state.get("reflection_done", False):
        return "finish"

    if score >= 8:
        return "finish"

    return "reflect"


builder.add_conditional_edges(
    "orchestrator",
    route,
    {
        "clarification": "clarification",
        "research": "research",
    },
)

builder.add_edge("clarification", END)

builder.add_edge("research", "planner")
builder.add_edge("planner", "memory")

builder.add_conditional_edges(
    "memory",
    should_run("planning"),
    {
        "run": "planning",
        "skip": "composer",
    },
)

builder.add_edge("planning", "prd")
builder.add_edge("prd", "technical")
builder.add_edge("technical", "api")
builder.add_edge("api", "database")
builder.add_edge("database", "roadmap")
builder.add_edge("roadmap", "ui")

builder.add_conditional_edges(
    "ui",
    should_run("reflection"),
    {
        "run": "reflection",
        "skip": "composer",
    },
)

builder.add_edge("reflection", "composer")
builder.add_edge("composer", "critic")

builder.add_conditional_edges(
    "critic",
    critic_route,
    {
        "reflect": "reflection",
        "finish": END,
    },
)

workflow = builder.compile()