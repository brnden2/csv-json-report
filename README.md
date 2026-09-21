# CSV to JSON Report

## Objective

This project reads data from a CSV file and converts it into JSON format using Python.

## Requirements

- Python 3
- Git

## Project Structure

- `data/` - Contains input CSV files
- `output/` - Contains generated JSON reports
- `src/` - Contains Python source code
- `README.md` - Project documentation
- `.gitignore` - Specifies files that Git should ignore

## How to Run

Open Command Prompt in the project folder and run:

python src/converter.py

## Data Flow

1. The program reads `data/sample.csv`.
2. Python's `csv.DictReader` converts each CSV row into a dictionary.
3. The dictionaries are stored in a Python list.
4. Python's JSON module converts the list into JSON format.
5. The result is saved as `output/report.json`.

## Error Handling

The program handles:

- Missing CSV files
- CSV files without a valid header
- Unexpected program errors

The program also creates a debug log to record successful operations and errors.

## Assumptions

- The input file is in CSV format.
- The first row contains column headers.
- The input CSV file is stored inside the `data` folder.
- The generated JSON file is stored inside the `output` folder.

## Example Input

id,name,department,status
1,John,IT,Active
2,Sarah,Finance,Active
3,David,Marketing,Inactive

## Example Output

[
    {
        "id": "1",
        "name": "John",
        "department": "IT",
        "status": "Active"
    }
]