import csv


data_path = "raw_output.csv"
source_path = "../data/Slovak_towns.csv"

output_path = "clear_output.csv"

output_file = open(output_path, "w+")

with open(source_path, newline='') as csvsource:
    source_towns = list(csv.reader(csvsource))

with open(data_path, newline='') as csvnew:
    new_towns = list(csv.reader(csvnew))

for town in new_towns:
    if town and town not in source_towns:
        output_file.write(str(town[0]) + "\n")
