from app.agents.clarification_agent import clarification_agent

state = {
    "idea": "Blueprint AI is an AI platform that converts startup ideas into complete product blueprints.",

    "clarification_questions": [],
    "clarification_answers": [],

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

result = clarification_agent(state)

print("\nGenerated Questions:\n")

for q in result["clarification_questions"]:
    print(q)