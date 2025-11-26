#1. Inserting a new student
import json
from main import *
import os

def new_user():
    #Input all the key details for the student
    nome = input("Enter the name for this user: ")
    cognome = input("Enter the surname for this user: ")

    user_id = new_user_id()

    print(f"Auto Generated User id is : {new_user_id}, please write this down")
    password = input(f"Please Enter the password for {new_user_id}: ")
    email = input("Enter the email of the User: ")
    date_created =  date_time_now()

    new_user_data = {
        user_id: {
            "nome": nome,
            "cognome": cognome,
            "email": email,
            "user id": user_id,
            "password": password,
            "data_creazione": date_created,
            "data_modifica": date_created,
        }
    }

    if os.path.exists("studenti.json"):
        try:
            with open("studenti.json", "r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = {}   # when the file is broken
    else:
        data = {}       # file does not exist

    # check if data exists
    if "lista_utenti" not in data:
        data["lista_utenti"] = {}
    # ---- add new entry ----
    data["lista_utenti"].update(new_user_data)

    # ---- save entire JSON ----
    with open("studenti.json", "w") as f:
        json.dump(data, f, indent=4)

    print("User successfully added!")
new_user()