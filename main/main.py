import json
import os
from datetime import *
from counter import *
from view import file_path
from utilities import *
from importing_students import *
from view_registered_students import *
from modifica_alunno import *


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
        modifica_aluno()
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