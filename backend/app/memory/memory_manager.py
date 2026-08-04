from app.memory.memory_store import MemoryStore


class MemoryManager:

    @staticmethod
    def save_blueprint(idea, blueprint):

        memory = MemoryStore.load()

        memory.append({
            "idea": idea,
            "summary": blueprint["planning"]["product_summary"]
        })

        MemoryStore.save(memory)

    @staticmethod
    def get_projects():
        return MemoryStore.load()

    @staticmethod
    def get_last_project():

        memory = MemoryStore.load()

        if not memory:
            return None

        return memory[-1]