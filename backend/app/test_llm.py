from app.services.llm_service import generate_response

response = generate_response(
    "Explain LangGraph in one sentence."
)

print(response)