import json

def write_output(assignments, file_path="output.json"):

    "Writes the assignment results to an output JSON file"

    output = {"assignments": assignments}
    with open(file_path, "w") as f:
        json.dump(output, f, indent=4)
