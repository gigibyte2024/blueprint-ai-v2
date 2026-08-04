from fastapi import APIRouter

from app.graph.workflow import workflow

router = APIRouter()


@router.post("/generate-blueprint")
def generate_blueprint(data: dict):

    state = {

    # Workflow
        "current_step": "",
        "is_clarification_complete": True,

    # User Input
        "idea": data["idea"],

    # Selected Modules
        "requested_modules": data.get(
    "requested_modules",
    [
        "planning",
        "prd",
        "technical",
        "api",
        "database",
        "roadmap",
        "ui",
        "reflection"
    ]
),

    # Shared Project Context
        "project_context": {},

    # Clarification
        "clarification_questions": [],
        "clarification_answers": data.get("answers", []),

    # Planning Module
        "planning_output": {},

    # Product Modules
        "prd_output": {},
        "technical_output": {},
        "api_output": {},
        "database_output": {},
        "ui_output": {},
        "roadmap_output": {},
        "risk_output": {},
        "security_output": {},
        "qa_output": {},
        "deployment_output": {},
        "documentation_output": {},

    # Final Blueprint
        "final_blueprint": {}
}
    result = workflow.invoke(state)
    return {
        "success": True,
        "blueprint": result["final_blueprint"]
    }