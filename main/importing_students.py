import json
import os
from counter import *

from utilities import *

FILE_PATH = "../studenti.json"
#1. Inserting a new student
def new_student():
    #Input all the key details for the student
    nome = input("Please Enter the name of the student: ")
    cognome = input("Please Enter the sirname of the student: ")
    email = input("Enter the email of the student: ")
    #checking if email is valid
    check_email(email)
    #a new id is generated for every student
    matricola = generate_id()
    data_creazione = date_created()
    data_modificazione =  date_modified()
    new_student = {
        matricola: {
            "matricola": matricola,
            "nome": nome,
            "cognome": cognome,
            "email": email,
            "data_creazione": data_creazione,
            "data_modificazione": data_modificazione
        }
    }

    if os.path.exists("../studenti.json"):
        try:
            with open("../studenti.json", "r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = {}   # file exists but is empty/broken
    else:
        data = {}       # file doesn’t exist yet

    # ---- add new entry ----
    data.update(new_student)

    # ---- save entire JSON ----
    with open("../studenti.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Student successfully added!")
