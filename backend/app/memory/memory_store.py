import json
import os


MEMORY_FILE = "memory.json"


class MemoryStore:

    @staticmethod
    def load():

        if not os.path.exists(MEMORY_FILE):
            return []

        with open(MEMORY_FILE, "r") as f:
            return json.load(f)

    @staticmethod
    def save(data):

        with open(MEMORY_FILE, "w") as f:
            json.dump(data, f, indent=4)