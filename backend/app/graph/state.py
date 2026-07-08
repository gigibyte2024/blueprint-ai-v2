from typing import TypedDict, List, Dict, Any


class BlueprintState(TypedDict):
    """
    Shared state passed between all agents.
    """
    current_step: str
    is_clarification_complete: bool
    # User Input
    idea: str

    # Clarification Phase
    clarification_questions: List[str]
    clarification_answers: List[str]

    # Planning Phase
    planning_output: dict

    # Technical Phase
    technical_output: dict

    # UI Phase
    ui_output: dict

    # Planning
    roadmap: str

    # Final Output
    final_blueprint: Dict[str, Any]