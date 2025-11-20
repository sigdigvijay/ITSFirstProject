import os

from datetime import *
from errno import EUSERS
from http.cookiejar import user_domain_match

print("Please Select Your Preffred language of choice : \n"
      "1. English \n"
      "2. Italiano \n"
      "Your Choice/ Tua Scelta :- ")

# https://sentry.io/answers/print-colored-text-to-terminal-with-python/

print(GREEN + BACKGROUND_RED + "green on red" + RESET)

print("Seleziona un'opzione: \n"
      "1. Inserisci nuovo alunno \n"
      "2. Visualizza alunni registrati "
      "3. Modifica dati alunno \n"
      "4. Elimina\Archive alunno \n"
      
      "5. Assegna compito a studente \n"
      "6. Registra valutazione \n"
      "7. Visualizza compiti di uno studente \n"
      
      "8. Visualizza statistiche alunnon \n"  
      "9. Ranking alunni per media voti\n"
      "10. Report compiti non completati\n"
      
      "11. Salva dati (backup) "
      "         1. CSV"
      "         2. JSON\n"
      "12. Carica dati \n"
        json
        csv
      "13. Visualizza menu \n"
            add new user
            view EUSERS
            delete user
            admin forgot password
      "14. Esci \n")


"""
Here is the translation in English:
login as user i will add user unique id with which system can be used
1. **Quick Search** – Search students by first name, last name, or student ID
2. **CSV Export** – Generate reports in CSV format
3. **Email Validation** – Verify that the email address is valid
4. **Unique Student ID** – Prevent duplicate IDs
5. **Soft Deletion** – Mark students as “archived” instead of deleting them
6. **Change History** – Track who modified what and when
7. **Advanced Filters** – View students by grade ranges
8. **Execution Times** – Show the time taken for long tasks
9. **Friendly Notifications** – Emojis and colors in the terminal for feedback
10. **Data Import** – Load initial data from a CSV file
"""