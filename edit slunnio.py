import os
import json

FILE_PATH = "studenti.json"
# def view_view(to_modify):
#         # Convert dictionary-of-dicts → list of dicts
#         rows = []
#         for value in to_modify.items():
#             row = list(value)
#             # row["Matricola"] = key  # Moving key of dictionary as a new column
#             rows.append(row)
#
#         # Column names
#         columns = list(rows[0].keys())
#
#         # Calculate column widths
#         col_widths = {
#             col: max(len(col), max(len(str(row[col])) for row in rows))
#             for col in columns
#         }
#
#         # Header
#         header = " ║ ".join(col.ljust(col_widths[col]) for col in columns)
#         print(header)
#         print("═" * len(header))
#
#         # Rows
#         for row in rows:
#             line = " ║ ".join(str(row[col]).ljust(col_widths[col]) for col in columns)
#             print(line)
#
#         print("═" * len(header))

def view_view(to_modify):
    # student is already a dictionary containing all fields

    # Column names and values
    columns = list(to_modify.keys())
    values = [str(to_modify[col]) for col in columns]

    # Calculate column widths
    col_widths = [
        max(len(columns[i]), len(values[i])) for i in range(len(columns))
    ]

    # Header
    header = " ║ ".join(columns[i].ljust(col_widths[i]) for i in range(len(columns)))
    separator = "═" * len(header)
    print(separator)
    print(header)
    print(separator)

    # Row of values
    line = " ║ ".join(values[i].ljust(col_widths[i]) for i in range(len(values)))
    print(line)

    print(separator)

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
                              "║ 2. Search by student's email                             ║\n"
                              "║ 3. Return to main menu                                   ║\n"
                              "╚══════════════════════════════════════════════════════════╝\n"
                              "Your Choice / Tua Scelta : "))
        if selection == 1:
            # it should show the list of the studnet details and ask if its okay,
            # if yes then proceed to update the details
            # if no then it should ask to try again
            matricola_update = input("Please enter the matricola : ")
            if os.path.exists("studenti.json"):
                try:
                    with open("studenti.json", "r") as f:
                        data = json.load(f)
                except json.JSONDecodeError:
                    data ={}

            else:
                data = {}
            to_modify = data.get(matricola_update)

            if to_modify:
                view_view(to_modify)
            else:
                print("Matricola non trovata")
            # rows = []
            # # trying to get the field in the provided matricola
            # for value in to_modify.items:
            #     row = value.copy()
            #     rows.append(row)
            # #column names
            # columns = list.(rows[0].keys)
            #
            # #calculate column width
            # col_widths = {
            #     col: max(len(col), max(len(str(row[col])) for row in rows))
            #     for col in columns
            # }
            #
            # # header
            # header = "║".join(col.ljust(col_widths[col]) for col in columns)
            # print(header)
            # print("═") * len(header)





            # print(to_modify["nome"])
        elif selection == 2:
            pass
        elif selection == 3:
            pass
        else:
            pass
modifica_aluno()