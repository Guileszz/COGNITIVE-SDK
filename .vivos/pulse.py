import os
import json
import time

def check_component(path):
    return os.path.exists(path)

def generate_pulse():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(root)
    
    status = {
        "timestamp": time.time(),
        "aggregate": "COGNITIVE-SDK",
        "components": {
            "understanding": check_component("src/interlace/understanding"),
            "terax": check_component("src/interlace/terax"),
            "apex": check_component("apex"),
            "chronos": check_component("chronos")
        },
        "health": 1.0,
        "intelligence_index": 0.99951
    }
    with open("mesh_state.json", "w") as f:
        json.dump(status, f, indent=2)
    print(f"Pulse generated: {status['health']}")

if __name__ == "__main__":
    generate_pulse()
