import json
from pathlib import Path

MEMORY_FILE = Path("memory.json")


def load_memory():

    if not MEMORY_FILE.exists():
        return []

    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def save_memory(memory):

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)