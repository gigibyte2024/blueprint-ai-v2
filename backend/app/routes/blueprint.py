from fastapi import APIRouter

from app.graph.workflow import workflow

router = APIRouter()


@router.post("/generate-blueprint")
def generate_blueprint(data: dict):

    state = {
        "current_step": "",
        "is_clarification_complete": True,

        "idea": data["idea"],

        "clarification_questions": [],
        "clarification_answers": data.get("answers", []),

        "planning_output": {},
        "technical_output": {},
        "ui_output": {},

        "final_blueprint": {}
    }
    result = workflow.invoke(state)

    return {
        "success": True,
        "blueprint": result["final_blueprint"]
    }