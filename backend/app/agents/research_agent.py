import json

from app.agents.base_agent import BaseAgent
from app.graph.state import BlueprintState
from app.rag.retriever import get_retriever
from app.tools.tool_registry import tool_registry


class ResearchAgent(BaseAgent):

    def __init__(self):
        super().__init__("research.txt")
        self.retriever = get_retriever()

    def parse(self, response):

        response = response.strip()

        if response.startswith("```json"):
            response = response.replace(
                "```json",
                "",
                1,
            )

        if response.startswith("```"):
            response = response.replace(
                "```",
                "",
                1,
            )

        if response.endswith("```"):
            response = response[:-3]

        response = response.strip()

        return json.loads(response)

    def execute(self, state: BlueprintState):

        try:

            docs = self.retriever.invoke(
                state["idea"]
            )

            rag_context = "\n\n".join(
                [
                    doc.page_content
                    for doc in docs
                ]
            )

            tool_decider = tool_registry.get(
                "tool_decider"
            )

            web_search = tool_registry.get(
                "web_search"
            )

            web_context = ""

            # -------------------------
            # Tool Decision
            # -------------------------

            try:

                should_search = (
                    tool_decider.should_search(
                        state["idea"]
                    )
                )

            except Exception as error:

                print(
                    f"⚠️ Tool decision failed: {error}"
                )

                should_search = False

                state["research_status"] = (
                    "tool_decision_failed"
                )

            # -------------------------
            # Web Search
            # -------------------------

            if should_search:

                try:

                    print(
                        "\n🔍 Using Web Search...\n"
                    )

                    web_results = (
                        web_search.execute(
                            query=state["idea"],
                            max_results=2,
                        )
                    )

                    web_context = "\n".join(
                        [
                            item["title"]
                            for item in web_results
                        ]
                    )

                except Exception as error:

                    print(
                        f"⚠️ Web search failed: {error}"
                    )

                    state["research_status"] = (
                        "web_search_failed"
                    )

            else:

                print(
                    "\n📚 Skipping Web Search...\n"
                )

            # -------------------------
            # Research LLM
            # -------------------------

            try:

                result = self.run(
                    idea=state["idea"],
                    context=f"""
RAG Knowledge:

{rag_context}

Web Search:

{web_context}
""",
                )

                state["project_context"] = result

                state["research_status"] = (
                    "completed"
                )

                return state

            except Exception as error:

                print(
                    f"⚠️ Research generation "
                    f"failed: {error}"
                )

                state["project_context"] = {
                    "status": "degraded",
                    "reason": (
                        "Research generation "
                        "was unavailable."
                    ),
                    "rag_context": rag_context,
                    "web_context": web_context,
                    "error": str(error),
                }

                state["research_status"] = (
                    "degraded"
                )

                return state

        except Exception as error:

            print(
                f"❌ Research Agent failed "
                f"gracefully: {error}"
            )

            state["project_context"] = {
                "status": "failed",
                "reason": (
                    "Research agent unavailable. "
                    "Workflow continued."
                ),
                "error": str(error),
            }

            state["research_status"] = "failed"

            return state