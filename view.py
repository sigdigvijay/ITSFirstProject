import json
import os

# Load JSON file
file_path = os.path.join(os.getcwd(), "data.json")
with open(file_path, "r") as f:
    data = json.load(f)

# Make sure it's a list of dictionaries
if isinstance(data, list) and all(isinstance(d, dict) for d in data):
    # Extract headers
    headers = list(data[0].keys())

    # Calculate column widths
    col_widths = [len(header) for header in headers]
    for row in data:
        for i, header in enumerate(headers):
            col_widths[i] = max(col_widths[i], len(str(row.get(header, ""))))

    # Build format string
    row_format = " | ".join("{:<" + str(width) + "}" for width in col_widths)

    # Print header
    print(row_format.format(*headers))
    print("-" * (sum(col_widths) + 3 * (len(headers) - 1)))

    # Print rows
    for row in data:
        print(row_format.format(*[str(row.get(h, "")) for h in headers]))
else:
    print("JSON must be a list of dictionaries to display as a table.")
#2. view students
# need to add an option to search with matricola, if not knowing see a full list of contents

def view_student():
    to_append = json.load(open("studenti.json"))
    print(to_append)