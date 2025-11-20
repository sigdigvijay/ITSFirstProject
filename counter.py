import json
import os


def check_counter():
    if not os.path.exists("counter.json"):
        with open("counter.json", "w") as f:
            json.dump({"studenti.json": 1}, f)
        return 1
    with open("counter.json", "r") as f:
        data = json.load(f)
        return data["counter"]

def save_counter(value):
    with open("counter.json", "w") as f:
        json.dump({"counter": value}, f)

def generate_id(prefix = "MAT"):
    number  = check_counter()
    new_id = f"{prefix}{number:03d}"
    save_counter(number + 1)
    return new_id

