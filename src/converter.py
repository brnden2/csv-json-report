import csv
import json

input_file = "data/sample.csv"
output_file = "output/report.json"

with open(input_file, "r", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)
    data = list(reader)

with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, indent=4)

print("CSV successfully converted to JSON.")
print("Output file:", output_file)