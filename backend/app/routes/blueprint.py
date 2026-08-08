from fastapi import APIRouter

from app.graph.workflow import workflow
from fastapi.responses import StreamingResponse
import json
import time

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
                "reflection",
            ],
        ),

        # Shared Project Context
        "project_context": {},
        "execution_plan": {},
        "execution_logs": [],
        "execution_progress": [],

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
        "reflection_output": {},
        "critic_output": {},

        "reflection_done": False,

        # Final Blueprint
        "final_blueprint": {},
    }

    result = workflow.invoke(state)

    return {
        "success": True,
        "blueprint": result["final_blueprint"],
        "execution_progress": result.get(
            "execution_progress",
            [],
        ),
        "execution_logs": result.get(
            "execution_logs",
            [],
        ),
    }


@router.post("/generate-blueprint-stream")
def generate_blueprint_stream(data: dict):

    def generate():

        state = {
            "current_step": "",
            "is_clarification_complete": True,

            "idea": data["idea"],

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
                    "reflection",
                ],
            ),

            "project_context": {},
            "execution_plan": {},
            "execution_logs": [],
            "execution_progress": [],

            "clarification_questions": [],
            "clarification_answers": data.get(
                "answers",
                [],
            ),

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
            "reflection_output": {},
            "critic_output": {},

            "reflection_done": False,

            "final_blueprint": {},
        }

        yield f"data: {json.dumps({'stage': 'Starting', 'status': 'started'})}\n\n"

        result = workflow.invoke(state)

        for progress in result.get(
            "execution_progress",
            [],
        ):

            yield (
                f"data: {json.dumps(progress)}\n\n"
            )

        yield (
            f"data: {json.dumps({
                'stage': 'Complete',
                'status': 'completed',
                'blueprint': result['final_blueprint'],
            })}\n\n"
        )

    return StreamingResponse(
        generate(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        },
    )