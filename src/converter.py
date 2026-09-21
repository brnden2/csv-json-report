import csv
import json
import logging
import os

logging.basicConfig(
    filename="debug.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

input_file = "data/sample.csv"
output_file = "output/report.json"

try:
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")

    with open(input_file, "r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        if not reader.fieldnames:
            raise ValueError("CSV file does not contain a valid header.")

        data = list(reader)

    os.makedirs("output", exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)

    print("CSV successfully converted to JSON.")
    print("Records converted:", len(data))
    print("Output file:", output_file)

    logging.info(
        "Successfully converted %d records from CSV to JSON.",
        len(data)
    )

except FileNotFoundError as error:
    print("Error:", error)
    logging.error(error)

except ValueError as error:
    print("Invalid data:", error)
    logging.error(error)

except Exception as error:
    print("Unexpected error:", error)
    logging.exception(error)