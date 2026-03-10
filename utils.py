import json

def save_results(data):
    with open("results.json", "w") as file:
        json.dump(data, file, indent=4)
