from typing import TypedDict, List, Dict, Any


class BlueprintState(TypedDict):

    current_step: str
    is_clarification_complete: bool

    # User Input
    idea: str
    # Selected Modules
    requested_modules: List[str]

# Shared Project Context
    project_context: Dict[str, Any]

    # Clarification
    clarification_questions: List[str]
    clarification_answers: List[str]

    # Modules

    planning_output: Dict[str, Any]

    prd_output: Dict[str, Any]

    technical_output: Dict[str, Any]

    api_output: Dict[str, Any]

    database_output: Dict[str, Any]

    ui_output: Dict[str, Any]

    roadmap_output: Dict[str,Any]

    risk_output: Dict[str,Any]

    security_output: Dict[str,Any]

    qa_output: Dict[str,Any]

    deployment_output: Dict[str,Any]

    documentation_output: Dict[str,Any]
    reflection_output: Dict[str, Any]
    reflection_done: bool

    critic_output: Dict[str, Any]

    # Final

    final_blueprint: Dict[str, Any]

