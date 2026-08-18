import json

def load_memory():
    try:
        with open("data/memory.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
        
def save_memory(memory):
    with open("data/memory.json", "w") as file:
        json.dump(memory, file, indent=4)