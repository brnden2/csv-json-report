import csv
import json

data = []

with open("data/sample.csv", "r", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        data.append(row)

print("Python data:")
print(data)

print("\nJSON data:")
print(json.dumps(data, indent=4))

with open("output/report.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, indent=4)

print("\nJSON file successfully saved to output/report.json")