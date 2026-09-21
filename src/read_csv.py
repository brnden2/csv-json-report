import csv

with open("data/sample.csv", "r", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        print(row)