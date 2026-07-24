from fastapi import APIRouter

from app.modules.module_executor import ModuleExecutor

router = APIRouter()


@router.post("/generate-modules")
def generate_modules(data: dict):

    state = {
        "idea": data["idea"],
        "requested_modules": data["requested_modules"],
        "project_context": {},
        "clarification_questions": [],
        "clarification_answers": data.get("answers", []),
        "current_step": "",
        "is_clarification_complete": True,

        "planning_output": {},
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
        "final_blueprint": {}
    }

    result = ModuleExecutor.execute(state)

    return {
        "success": True,
        "modules": result
    }