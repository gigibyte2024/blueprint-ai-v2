from app.graph.workflow import workflow

state = {
    "current_step": "",

    "is_clarification_complete": False,
    "idea": "Blueprint AI converts startup ideas into complete product blueprints.",

    "clarification_questions": [],
    "clarification_answers": [
    "Startup founders",
    "Yes",
    "Web platform",
    "Editable blueprint",
    "Yes"
],

    "prd": "",
    "user_stories": "",
    "feature_list": "",

    "database_schema": "",
    "api_specification": "",
    "tech_stack": "",

    "ui_prompt": "",
    "roadmap": "",

    "final_blueprint": {}
}

result = workflow.invoke(state)

print("\nPlanning Output:\n")

from pprint import pprint

print("\n========== Planning ==========\n")
pprint(result["planning_output"])

print("\n========== Technical ==========\n")
pprint(result["technical_output"])

print("\n========== UI ==========\n")
pprint(result["ui_output"])

print("\n========== FINAL BLUEPRINT ==========\n")

from pprint import pprint

pprint(result["final_blueprint"])
