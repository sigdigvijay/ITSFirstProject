import os
import json

FILE_PATH = "studenti.json"

def print_table_from_nested_json(file_path):
    if not os.path.exists(file_path):
        print("File does not exist.")
        return

    # Load JSON
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Convert dictionary-of-dicts → list of dicts
    rows = []
    for key, value in data.items():
        row = value.copy()
        row["KEY"] = key   # optional: include dictionary key in the table
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

    header = " ║ ".join(col.ljust(col_widths[col]) for col in columns)
    print(header)
    print("═" * len(header))


# Run
print_table_from_nested_json(FILE_PATH)
