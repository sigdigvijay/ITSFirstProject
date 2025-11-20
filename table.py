import os
import json

FILE_PATH = "studenti.json"

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


# Run
view_student_list(FILE_PATH)
