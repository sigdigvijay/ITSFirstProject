import json
import os
from datetime import *

FILE_PATH = "studenti.json"
file_path = "studenti.json"
#
def wait_for_keypress():
    try:
        input("Press Enter to continue...")
    except KeyboardInterrupt:
        pass
# load json
def load_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)
# save json
def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
# <----- Funzioni per generare matricola unicavo


# in the json file id_store.json it checks the number assigned
def check_counter():
    if not os.path.exists("counter.json"):
        with open("counter.json", "w") as f:
            json.dump({"studenti.json": 1}, f)
        return 1
    with open("counter.json", "r") as f:
        data = json.load(f)
        return data["counter"]
# in the json file id_store.json it saves the number assigned
def save_counter(value):
    with open("counter.json", "w") as f:
        json.dump({"counter": value}, f)

# in the json file id_store.json it gerated a new mattricola and updates counter by a +1 number
def generate_id(prefix = "MAT"):
    number  = check_counter()
    new_id = f"{prefix}{number:03d}"
    save_counter(number + 1)
    return new_id

# <------- Funzioni generare matricola!

# <----- Funzioni per generare taskID unicavo

# in the json file id_store.json it checks the number assigned
def check_counter_per_task():
    if not os.path.exists("counter2.json"):
        with open("counter2.json", "w") as f:
            json.dump({"studenti.json": 1}, f)
        return 1
    with open("counter2.json", "r") as f:
        data = json.load(f)
        return data["counter"]
# in the json file id_store.json it saves the number assigned
def save_counter_per_task(value):
    with open("counter2.json", "w") as f:
        json.dump({"counter": value}, f)

# in the json file id_store.json it gerated a new mattricola and updates counter by a +1 number
def task_id(prefix = "TASK"):
    number  = check_counter_per_task()
    new_id = f"{prefix}{number:03d}"
    save_counter_per_task(number + 1)
    return new_id

 # <----- Funzioni per generare taskID unicavo
#
# in the json file id_store.json it checks the number assigned
def check_counter_per_user():
    if not os.path.exists("counter3.json"):
        with open("counter3.json", "w") as f:
            json.dump({"counter3.json": 1}, f)
        return 1
    with open("counter3.json", "r") as f:
        data = json.load(f)
        return data["counter"]
# in the json file id_store.json it saves the number assigned
def save_counter_per_user(value):
    with open("counter3.json", "w") as f:
        json.dump({"counter": value}, f)
#
# fin the json file id_store.json it gerated a new mattricola and updates counter by a +1 number
def new_user_id(prefix = "UTENTI"):
    number  = check_counter_per_user()
    new_id = f"{prefix}{number:04d}"
    save_counter_per_user(number + 1)
    return new_id
#
# <------- Funzioni generare taskID!
# this creates a new time stamp, used for both data creted and modification

def date_time_now():
    actual_time = datetime.now()

    actual_date_time = actual_time.strftime("%d/%m/%Y %H:%M:%S")
    return actual_date_time
#

# will check for presence of a @ if one is correct, if more than one or 0 not right
def check_email(email):
    pass

def clear_terminal():
    # os.system("cls" if os.name == "nt" else "clear")
    print("\033[2J\033[H", end="")

# This function will take a variable matricola as a string and show the student details to be edited
def search_students_by_matricola(matricola):
    # student is already a dictionary containing all fields
    if not os.path.exists(file_path):
        print("File not found!")
        return


    #Load json data
    with open(file_path, "r") as f:
        data = json.load(f)

    if "lista_alunni" not in data:
        print("Lista non trovata!")
        return
    lista = data["lista_alunni"]
    #check if mattricola exists in data
    if matricola not in lista:
        print("Student not found!")
        return
    # getting the student dictionary
    student = lista[matricola]
    # Column names and values
    columns = list(student.keys())
    values = [str(student[col]) for col in columns]

    # Calculate column widths
    col_widths = [
        max(len(columns[i]), len(values[i])) for i in range(len(columns))
    ]

    # Header
    header = " ║ ".join(columns[i].ljust(col_widths[i]) for i in range(len(columns)))
    print(header)
    separator = "═" * len(header)
    print(separator)
    # Row of values
    line = " ║ ".join(values[i].ljust(col_widths[i]) for i in range(len(values)))
    print(line)

    print(separator)

# This function returns the matricola as a key
# def search_students_by_email(email):
#     if os.path.exists(file_path):
#         with open(file_path, "r") as f:
#             data = json.load(f)
#     else:
#         data = None
#
#     for matricola, value in data.items():
#         if value.get("email") == email:
#             return matricola
#
# def search_students_by_nome(nome):
#     if os.path.exists(file_path):
#         with open(file_path, "r") as f:
#             data = json.load(f)
#     else:
#         data = None
#
#     for matricola, value in data.items():
#         if value.get("nome") == nome:
#             return matricola

def update_data(file_path, id, campo, data_aggiornata, section_key):
    data = load_json(file_path)


    # checking for key
    if section_key not in data:
        print(f"Section {section_key} not found!")
        return False

    lista = data[section_key]
    #checking if id exists in lista, be it matricola, utenti, compiti.
    if id not in lista:
        print(f"ID {id} not found!")
        return False

    valori = lista[id]

    # checking if field exists
    if campo not in valori:
        print(f"Campo {campo} non trovato!")
        return False

    # update field
    valori[campo] = data_aggiornata
    valori["data_modificazione"] = date_time_now()
    save_json(file_path, data)
    print(f"campo {campo} aggiornato con sucesso per {id}")
    return True





#<<<<<<<<<<<<<----------- utilities

#!!!!!!!!!!!!!!!!!!!!!!!!=======================!!!!!!!!!!!!!!!!!!!!!
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
    data_creazione = date_time_now()
    data_modificazione =  date_time_now()
    lista_studenti = {
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
    if "lista_alunni" not in data:
        data["lista_alunni"] = {}
    # ---- add new entry ----
    data["lista_alunni"].update(lista_studenti)

    # ---- save entire JSON ----
    with open("studenti.json", "w") as f:
        json.dump(data, f, indent=4)

    print(f"Student {nome} {cognome} with ID {matricola} successfully added!")

    wait_for_keypress()

# 2.view registered data in a tabular form
# Used to view students, compiti, deleted students , deleted users and current active users by calling function inside function


def list_view(section_key):
    # Load json to python
    with open("studenti.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # check if data exists for provided key variable
    if section_key not in data:
        print(f"Section {section_key} not found! in Studenti.json")
        return

    section = data[section_key]

    # Convert dictionary-of-dicts → list of dicts
    rows = []
    for key, value in section.items():
        row = value.copy()
        row["ID"] = key   # Moving key of dictionary as a new column
        rows.append(row)
    if not rows:
        print(f"No entries found in {section_key}")
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

    #waits for the user to press ENTER then it runs to next step
    wait_for_keypress()


# calls listview() to check for data in "lista_alunni" to show registered active students
def view_student_list():
    section_key = "lista_alunni"
    list_view(section_key)

# calls listview() to check for data in "lista_compiti" to show registered active compiti
def view_compiti():
    section_key = "lista_compiti"
    list_view(section_key)

# calls listview() to check for data in "lista_alunni_archiviati" to show alunni archviati
def view_alunni_archiviati():
    section_key = "lista_alunni_archiviati"
    list_view(section_key)

# calls listview() to check for data in "utenti_eliminati" to show deleted users
def utenti_eliminati():
    section_key = "lista_utenti_archiviati"
    list_view(section_key)

# calls listview() to check for data in "utenti attivi" to show registered active Users
def utenti_attivi():
    section_key = "lista_utenti_attivi"
    list_view(section_key)



# 3. Modifica Alunno
def modifica_aluno():
    exit = False
    while not exit:
        print("Please select an option from the following menu : \n")
        print("╔══════════════════════════════════════════════════════════╗")
        print("║                     MODIFICA  ALUNNI                     ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║     Please select an option from the following menu :    ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║ 1. Search by matricola                                   ║")
        print("║ 2. Search by student's email                             ║")
        print("║ 3. Return to main menu                                   ║")
        print("╚══════════════════════════════════════════════════════════╝")
        selection = int(input("Your Choice / Tua Scelta : "))
        if selection == 1:
            # it should show the list of the student details and ask if its okay,
            # if yes then proceed to update the details
            # if no then it should ask to try again
            matricola = input("Please enter the matricola : ")
            if os.path.exists("studenti.json"):
                try:
                    with open("studenti.json", "r") as f:
                        data = json.load(f)
                except json.JSONDecodeError:
                    data = {}

            else:
                data = {}
            matricola = data.get(matricola)


            clear_terminal()
            search_students_by_matricola(matricola)
            is_it_right = input("Is this the one you've been searching for ???? Y/N : ? y/n : ")
            if is_it_right == "Y":


                print("╔══════════════════════════════════════════════════════════╗")
                print("║                     MODIFICA  ALUNNI                     ║")
                print("╠══════════════════════════════════════════════════════════╣")
                print("║     Please select an option from the following menu :    ║")
                print("╠══════════════════════════════════════════════════════════╣")
                print("║ 1. Change Name                                           ║")
                print("║ 2. Change sirname                                        ║")
                print("║ 3. change email                                          ║")
                print("║ 4. Change Name + Surname + email                         ║")
                print("║ 5. Return to previous menu                               ║")
                print("╚══════════════════════════════════════════════════════════╝")
                select_changes_to_alunni = int(input("Your Choice / Tua Scelta : "))
                if select_changes_to_alunni == 1:
                    section_key = "lista_alunni"
                    # we already have matricola from above
                    id = matricola
                    campo = "nome"
                    data_aggiornata = input("Please enter the updated name : ")
                    update_data(file_path, id, campo, data_aggiornata, section_key)


                elif select_changes_to_alunni == 2:
                        #missing change surname
                    pass
                elif select_changes_to_alunni == 3:
                        #missing change email
                    pass
                elif select_changes_to_alunni == 4:
                        #missing change all
                    pass
                elif select_changes_to_alunni == 5:
                        #returns to previous page
                    modifica_aluno()
                else:
                    print("Select a correct option! ")
            elif is_it_right == "N":
                print("Please Select a correct option!")


            else:
                    print("Matricola non trovata")
        #Search by email
        elif selection == 2:
                email = input("Please enter the matricola : ")
                matricola = search_students_by_email(email)
                # search_students_by_matricola(to_modify)
                search_students_by_matricola(matricola)
                is_it_right = input("Is this the data you want to update? Y/N : ")
                if is_it_right == "Y":
                    pass
        elif selection == 3:
            main_menu()
        else:
            pass

# 4. Delete Archive alunno
def delete_archive_aluno():

    print("╔══════════════════════════════════════════════════════════╗")
    print("║                  DELETE / ARCHIVE MENU                   ║")
    print("╠══════════════════════════════════════════════════════════╣")
    print("║     Please select an option from the following menu :    ║")
    print("╠══════════════════════════════════════════════════════════╣")
    print("║ 1. Delete Alunni                                         ║")
    print("║ 2. Archive Alunni                                        ║")
    print("║ 3. View Archived students                                ║")
    print("║ 4. Return to previous menu                               ║")
    print("╚══════════════════════════════════════════════════════════╝")
    selection = int(input("Please select an option from the following menu : \n"))
    if selection == 1:
        matricola = input("Please enter the matricola of the student to delete: ")
    elif selection == 2:
        # here also it should ask if whether to archive or move from archive to list principle
        matricola = input("Please enter the matricola of the student to archive: ")
    elif selection == 3:
        pass
    elif selection == 4:
        main_menu()

 #5. Assign Homework to a student
def compito():
    print("╔══════════════════════════════════════════════════════════╗\n")
    print("║                  AGGIUNGI NUOVO COMPITO                  ║\n")
    print("╚══════════════════════════════════════════════════════════╝\n")
    task_description = input("Please Enter the description of the task :")
    matricola = input("Please enter the matricola of the student: ")
    choice_stato = input("Chose the state 1: in_corso, 2: Completato, 3. Assegnato: ")
    if choice_stato == "1":
        stato = "in_corso"
    elif choice_stato == "2":
        stato = "Completato"
    elif choice_stato == "3":
        stato = "Assegnato"
    else:
        print("Please enter the correct option!")
    voti_input = input("Please enter the final marks saperated by a comma: ")
    voti = [float(V) for v in voti_input.split(",")]
    task_id = task_id()
    data_assign = date_time_now()
    #task id to define
    lista_compiti[task_id] = {
        "id" : task_id,
        "description" : task_description,
        "alunno_matricola" : matricola,
        "stato" : stato,
        "data_assign" : data_assign,
        "voti" : voti
    }
# 6. Register Assessment
def register_assesment():
    pass

# 7. View Assesments assigned to a student
def view_assesments():
    pass

#8. View Stats of the students
def view_stats():
    pass

#9. Ranking students by Final Marks
def ranking_by_final_marks():
    pass

#10. Report Homework not completed
def report_compiti_not_completed():
    pass


#11. export data
def export_data():
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
    import_selection = int(input("Please select the format with what you want to import??? : \n"
                                 "1. CSV\n"
                                 "2. JSON\n"
                                 "3. Return to Main Menu \n"
                                 "Your Choice / Tua Scelta : "))
    #to ask how will the csv will be uploaded
    if import_selection == 1:
        joined = print("Do you have one single csv for both the Lista task and Lista alunni ??? Y/N : ")
        if joined == "Y" or joined == "y":
            pass
        elif joined == "N" or joined == "n":
            pass

        pass
    elif export_selection == 2:
        pass
def admin_menu():

        print("Please select an option from the following menu : \n")
        print("╔══════════════════════════════════════════════════════════╗")
        print("║                        ADMIN MENU                        ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║     Please select an option from the following menu :    ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║ 1. List Users                                            ║")
        print("║ 2. Add User                                              ║")
        print("║ 3. Remove User                                           ║")
        print("║4.History by user                                         ║")
        print("║ 5. Change Admin Password                                 ║")
        print("╚══════════════════════════════════════════════════════════╝")
        selection = int(input("Your Choice / Tua Scelta : "))
        if selection == 1:
            # list of users
            pass
        elif selection == 2:
            new_user = input("Please enter the new Username : ")
            new_password = input(f"Please enter the new Password for {new_user} : ")

            print("User added successfully!")
            # add a new user/pw, ask, check(if same is present try again), append
            pass
        elif selection == 3:
            pass
        elif selection == 4:
            # opens log file and list the operations
            pass
        elif selection == 5:
            pass
        else:
            print("Please enter the correct option!")

def admin_menu_check_password():
    admin = False
    while not admin:
        pw = input("Type The Username to enter : ")
        username = input("Type The Password to enter : ")
        if username == "superadmin" and pw == "yes":
            admin_menu()
        # for this i need to pull a data set from the json file, for the password, change it and stuff
        else:
            print("Wrong Password. Please try again")
            admin_menu()

def login():
    admin = False
    while not admin:
        pass
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



#Main Program Which calls the functions!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!=======================!!!!!!!!!!!!!!!!!!!!!
def main_menu():
    exit = False
    while not exit:
        print("Please select an option from the following menu : \n")
        print("╔══════════════════════════════════════════════════════════╗")
        print("║                STUDENT MANAGEMENT SYSTEM                 ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║     Please select an option from the following menu :    ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║ 1. Insert a new student                                  ║")
        print("║ 2. View registered students                              ║")
        print("║ 3. Modify student's data                                 ║")
        print("║ 4. Delete - Archive student's data                       ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║ 5. Assign Homework to a student                          ║")
        print("║ 6. Register Assessment                                   ║")
        print("║ 7. View Assesments assigned to a student                 ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║ 8. View Stats of the students                            ║")
        print("║ 9. Ranking students by Final Marks                       ║")
        print("║ 10. Report Homework not completed                        ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║ 11. Save Data                                            ║")
        print("║ 12. Import Data                                          ║")
        print("║ 13. View Menu                                            ║")
        print("╚══════════════════════════════════════════════════════════╝")
        selection = int(input(" Your Choice / Tua Scelta : "))

        if selection == 1:
            new_student()
        elif selection == 2:
            #PRESS ANY KEY TO CONTINUE MISSING
            view_student_list()
        elif selection == 3:
            modifica_aluno()
        elif selection == 4:
            delete_archive_aluno()
        elif selection == 5:
            compito()
        elif selection == 6:
            register_assesment()
        elif selection == 7:
            view_assesments()
        elif selection == 8:
            view_stats()
        elif selection == 9:
            ranking_by_final_marks()
        elif selection == 10:
            report_compiti_not_completed()
        elif selection == 11:
            export_data()
        elif selection == 12:
            import_data()
        elif selection == 13:
            admin_menu_check_password()
        else:
            pass


main_menu()
# when there is a call for start program i will add to ask for user name and password,
# and store that user name in a variable
# then that is passed through a process still to define which passes to log, which shows user logged in
# also in every action there should be a call to log in the system