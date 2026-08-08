class MemoryManager:

    def __init__(self):
        self.memory = []

    def save_blueprint(self, idea, blueprint):

        planning = blueprint.get(
            "planning",
            {},
        )

        summary = planning.get(
            "product_summary",
            planning.get(
                "project_overview",
                {},
            ),
        )

        if isinstance(summary, dict):

            summary = summary.get(
                "idea",
                "Blueprint generated",
            )

        self.memory.append(
            {
                "idea": idea,
                "summary": summary,
                "blueprint": blueprint,
            }
        )

        print(
            "🧠 Blueprint saved to memory"
        )

        return True

    def get_last_project(self):

        if not self.memory:
            return None

        return self.memory[-1]

    def get_memory(self):

        return self.memory