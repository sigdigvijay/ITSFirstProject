import os
import json

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
            if os.path.exists("../studenti.json"):
                try:
                    with open("../studenti.json", "r") as f:
                        data = json.load(f)
                except json.JSONDecodeError:
                    data = {}

            else:
                data = {}
            to_modify = data.get(matricola_update)

            if to_modify:
                clear_terminal()
                search_students_by_matricola(to_modify)
                is_it_right = input("Is this the one you've been searching for ???? Y/N : ? y/n : ")
                if is_it_right == "Y":
                    select_changes_to_alunni = int(input(
                                          "╔══════════════════════════════════════════════════════════╗\n"
                                          "║                     MODIFICA  ALUNNI                     ║\n"
                                          "╠══════════════════════════════════════════════════════════╣\n"
                                          "║     Please select an option from the following menu :    ║\n"
                                          "╠══════════════════════════════════════════════════════════╣\n"
                                          "║ 1. Change Name                                           ║\n"
                                          "║ 2. Change sirname                                        ║\n"
                                          "║ 3. change email                                          ║\n"
                                          "║ 4. Change Name + Sirname +                               ║\n"
                                          "║                                                          ║\n"
                                          "╚══════════════════════════════════════════════════════════╝\n"
                                          "Your Choice / Tua Scelta : "))
                        if select_changes_to_alunni == 1:
                            pass


            else:
                print("Matricola non trovata")

        elif selection == 2:
            pass
        elif selection == 3:
            pass
        else:
            pass