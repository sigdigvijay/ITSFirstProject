import json
import os.path
from datetime import *
from counter import *
import pandas as pd

#
#
# # fromlanguage_dictionary =
# language = int(input("Please Select the Language of the interface : \n"
#                      "Seleziona lingua per il programma: "
#                      "1. English \n"
#                      "2. Italiano \n"
#                      "Your Choice / Tua Scelta : "))
#
# main_menu = int(input("Please select an option from the following menu : \n"
#                    "1. Insert a new student\n"
#                    "2. View registered students\n"
#                    "3. Modify student's data \n"
#                    "4. Delete - Archive student's data \n"
#                    "=================================================\n"
#                    "5. Assign Homework to a student\n"
#                    "6. Register Assesment\n"
#                    "7. View Assesments assigned to a student\n"
#                    "=================================================\n"
#                    "8. View Stats of the students \n"
#                    "9. Ranking students by Final Marks \n"
#                    "10. Report Homework not completed \n"
#                    "=================================================\n"
#                    "11. Save Data \n"
#                    "12. Import Data \n"
#                    "13. View Menu"
#                    "Your Choice / Tua Scelta : "))

def date_created():
    actual_time = datetime.now()

    actual_date_time = actual_time.strftime("%d/%m/%Y %H:%M:%S")
    return actual_date_time

def date_modified():
    actual_time = datetime.now()
    actual_date_time = actual_time.strftime("%d/%m/%Y %H:%M:%S")
    return actual_date_time

def check_email(email):
    pass


#1. Inserting a new student
def new_student():
    nome = input("Please Enter the name of the student: ")
    cognome = input("Please Enter the sirname of the student: ")
    email = input("Enter the email of the student: ")
    check_email(email)
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

    if os.path.exists("studenti.json"):
        try:
            with open("studenti.json", "r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = {}   # file exists but is empty/broken
    else:
        data = {}       # file doesn’t exist yet

    # ---- add new entry ----
    data.update(new_student)

    # ---- save entire JSON ----
    with open("studenti.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Student successfully added!")
# new_student()
# # # 2. View registered students
def view_student():



