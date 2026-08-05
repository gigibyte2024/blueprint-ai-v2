from app.services.llm_service import generate_response


class ToolDecider:

    def decide(self, idea):

        messages = [
            {
                "role": "system",
                "content": """
You are an AI Tool Router.

Available tools:

1. web_search
2. github_search

Rules:

- If the user asks about latest trends, companies, market, APIs, technologies, news or research → web_search

- If the user asks about code, repositories, open-source libraries, GitHub examples or implementation → github_search

- If both are useful, return BOTH.

Return ONLY JSON.

Example:

{
    "tools":[
        "web_search",
        "github_search"
    ]
}
""",
            },
            {
                "role": "user",
                "content": idea,
            },
        ]

        response = generate_response(messages)

        response = response.strip()

        if response.startswith("```json"):
            response = response.replace("```json", "", 1)

        if response.startswith("```"):
            response = response.replace("```", "", 1)

        if response.endswith("```"):
            response = response[:-3]

        import json

        return json.loads(response)