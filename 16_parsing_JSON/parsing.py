
import json
from pathlib import Path

file_path = Path(__file__).parent / "states.json"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # print(json.dumps(data, indent=2))
    for state in data['states'] :
        # print (state["name"],state["abbreviation"])
        del state["area_codes"]
        with open(file_path, "w",) as f:
                json.dump(data,f,indent=2)


except FileNotFoundError:
    print("Error: states.json file not found.")

except json.JSONDecodeError:
    print("Error: Invalid JSON format in states.json.")
