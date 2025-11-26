import json
import os

KEY = "counter_matricola"

# in the json file id_store.json it checks the number assigned
def check_counter():
    if not os.path.exists("studenti.json"):
        with open("studenti.json", "w") as f:
            json.dump({KEY: {"matricola": 1}}, f, indent=4)
        return 1

    with open("counter.json", "r") as f:
        data = json.load(f)
        return data[KEY]["matricola"]

# in the json file id_store.json it saves the number assigned
def save_counter(value):
    with open("counter.json", "w") as f:
        json.dump({KEY: {"matricola": value}}, f, indent = 4)



# in the json file id_store.json it gerated a new mattricola and updates counter by a +1 number
def generate_id(prefix = "MAT"):
    number  = check_counter()
    new_id = f"{prefix}{number:03d}"
    save_counter(number + 1)
    return new_id
#
#
# import json
# import os
#
# KEY = "counter_matricola"
#
# def check_counter():
#     if not os.path.exists("counter.json"):
#         with open("counter.json", "w") as f:
#             json.dump({KEY: {"matricola": 1}}, f, indent=4)
#         return 1
#
#     with open("counter.json", "r") as f:
#         data = json.load(f)
#         return data[KEY]["matricola"]
#
#
# def save_counter(value):
#     with open("counter.json", "w") as f:
#         json.dump({KEY: {"matricola": value}}, f, indent=4)
#
#
# def generate_id(prefix="MAT"):
#     number = check_counter()
#     new_id = f"{prefix}{number:03d}"
#     save_counter(number + 1)
#     return new_id
#
#
import json
import os

KEY = "counter_matricola"

def check_counter():
    if not os.path.exists("counter.json"):
        with open("counter.json", "w") as f:
            json.dump({KEY: {"matricola": 1}}, f, indent=4)
        return 1

    with open("counter.json", "r") as f:
        data = json.load(f)
        return data[KEY]["matricola"]  # ✅ FIXED


def save_counter(value):
    with open("counter.json", "w") as f:
        json.dump({KEY: {"matricola": value}}, f, indent=4)


def generate_id(prefix="MAT"):
    number = check_counter()
    new_id = f"{prefix}{number:03d}"
    save_counter(number + 1)
    return new_id
