import json
import os
from datetime import *
from counter import *

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

FILE_PATH = "studenti.json"
#1. Inserting a new student
def new_student(file_path):
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

    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = {}   # file exists but is empty/broken
    else:
        data = {}       # file doesn’t exist yet

    # ---- add new entry ----
    data.update(new_student)

    # ---- save entire JSON ----
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

    print("Student successfully added!")

# 2.view registered students

def view_student_list(file_path):
    # Load JSON
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Convert dictionary-of-dicts → list of dicts
    rows = []
    for key, value in data.items():
        row = value.copy()
        row["Matricola"] = key   # Moving key of dictionary as a new column
        rows.append(row)

    # Column names
    columns = list(rows[0].keys())

    # Calculate column widths
    col_widths = {
        col: max(len(col), max(len(str(row[col])) for row in rows))
        for col in columns
    }

    # Header
    header = " ║ ".join(col.ljust(col_widths[col]) for col in columns)
    print(header)
    print("═" * len(header))

    # Rows
    for row in rows:
        line = " ║ ".join(str(row[col]).ljust(col_widths[col]) for col in columns)
        print(line)


    print("═" * len(header))


def modifica_aluno():
    exit = False
    while not exit:
        selection = int(input("Please select an option from the following menu : \n"
                              "╔══════════════════════════════════════════════════════════╗\n"
                              "║                     MODIFICA  ALUNNI                     ║\n"
                              "╠══════════════════════════════════════════════════════════╣\n"
                              "║     Please select an option from the following menu :    ║\n"
                              "╠══════════════════════════════════════════════════════════╣\n"
                              "║ 1. Search by matricola                                   ║\n"
                              "║ 2. Search by studen't name                               ║\n"
                              "║ 3. Search by student's email                             ║\n"
                              "║ 4. Return to main menu                                   ║\n"
                              "╚══════════════════════════════════════════════════════════╝\n"
                              "Your Choice / Tua Scelta : "))
        if selection == 1:
            pass
        elif selection == 2:
            pass
        elif selection == 3:
            pass
        elif selection == 4:

    pass
def elimina_aluno():
    pass
def archive_aluno():
    pass
def compito():
    pass
def registra_valutazione():
    pass
def visualizza_compiti_di_uno_studente():
    pass
def visualizza_statistiche_aluno():
    pass
def ranking_alunno():
    pass
def compiti_non_completati():
    pass
def export_data():
    pass
def salva_data():
    export_selection = int(input("Please select the format to export data to : \n"
                                 "1. CSV\n"
                                 "2. JSON\n"
                                 "3. Return to Main Menu \n"
                                 "Your Choice / Tua Scelta : "))
    if export_selection == 1:
        pass
    elif export_selection == 2:
        pass


def import_data():
    pass

def admin_menu():
    pass


exit = False
while not exit:
    selection = int(input("Please select an option from the following menu : \n"
                          "╔══════════════════════════════════════════════════════════╗\n"
                          "║                STUDENT MANAGEMENT SYSTEM                 ║\n"
                          "╠══════════════════════════════════════════════════════════╣\n"
                          "║     Please select an option from the following menu :    ║\n"
                          "╠══════════════════════════════════════════════════════════╣\n"
                          "║ 1. Insert a new student                                  ║\n"
                          "║ 2. View registered students                              ║\n"
                          "║ 3. Modify student's data                                 ║\n"
                          "║ 4. Delete - Archive student's data                       ║\n"
                          "╠══════════════════════════════════════════════════════════╣\n"
                          "║ 5. Assign Homework to a student                          ║\n"
                          "║ 6. Register Assesment                                    ║\n"
                          "║ 7. View Assesments assigned to a student                 ║\n"
                          "╠══════════════════════════════════════════════════════════╣\n"
                          "║ 8. View Stats of the students                            ║\n"
                          "║ 9. Ranking students by Final Marks                       ║\n"
                          "║ 10. Report Homework not completed                        ║\n"
                          "╠══════════════════════════════════════════════════════════╣\n"
                          "║ 11. Save Data                                            ║\n"
                          "║ 12. Import Data                                          ║\n"
                          "║ 13. View Menu                                            ║\n"
                          "╚══════════════════════════════════════════════════════════╝\n"
                          "Your Choice / Tua Scelta : "))

    if selection == 1:
        new_student()


    elif selection == 2:
        #PRESS ANY KEY TO CONTINUE MISSING
        view_student_list(FILE_PATH)
    elif selection == 3:
        pass
    elif selection == 4:
        pass
    elif selection == 5:
        pass
    elif selection == 6:
        pass
    elif selection == 7:
        pass
    elif selection == 8:
        pass
    elif selection == 9:
        pass
    elif selection == 10:
        pass
    elif selection == 11:
        pass
    elif selection == 12:
        admin_menu()
    elif selection == 13:
        pass
    else:
        pass