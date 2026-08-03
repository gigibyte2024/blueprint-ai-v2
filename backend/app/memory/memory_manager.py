from app.memory.memory_store import load_memory, save_memory


class MemoryManager:

    def save_blueprint(self, idea, blueprint):

        memory = load_memory()

        memory.append(
            {
                "idea": idea,
                "blueprint": blueprint
            }
        )

        save_memory(memory)

    def get_previous_projects(self):

        return load_memory()