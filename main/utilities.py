# ---- Utilities >>>>
def dante_created():
    actual_time = datetime.now()

    actual_date_time = actual_time.strftime("%d/%m/%Y %H:%M:%S")
    return actual_date_time

def date_modified():
    actual_time = datetime.now()
    actual_date_time = actual_time.strftime("%d/%m/%Y %H:%M:%S")
    return actual_date_time

def check_email(email):
    pass

def clear_terminal():
    # os.system("cls" if os.name == "nt" else "clear")
    print("\033[2J\033[H", end="")

# Search Student by key i.e. matricola
def search_students_by_matricola(to_modify):
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

# <<< Utilities ---