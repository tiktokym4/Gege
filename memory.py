import json
from pathlib import Path

MEMORY_FILE = Path("data/memory.json")

DEFAULT_MEMORY = {
    "user_name": "حمودي",
    "facts": [],
    "interests": [],
    "important_topics": []
}

def load_memory():
    MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not MEMORY_FILE.exists():
        save_memory(DEFAULT_MEMORY.copy())
    return json.loads(MEMORY_FILE.read_text(encoding="utf-8"))

def save_memory(memory):
    MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)
    MEMORY_FILE.write_text(
        json.dumps(memory, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

def remember(fact):
    memory = load_memory()
    if fact and fact not in memory["facts"]:
        memory["facts"].append(fact)
        save_memory(memory)

def get_memory():
    return load_memory()
