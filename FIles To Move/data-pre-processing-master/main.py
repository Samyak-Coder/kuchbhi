import csv

data = []

with open("data\dataset_2.csv", "r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data.append(row)

headers = data[0]

planet_data = data[1:]

#converting all planets names to lower case
for data_pt in planet_data:
    data_pt[2] = data_pt[2].lower()

#sorting planet names in alphabatical order
planet_data.sort(key=lambda planet_data:planet_data[2])

with open("data/Sorted.csv", "a+") as f:
    csv_writter = csv.writer(f)
    csv_writter.writerow(headers)
    csv_writter.writerows(planet_data)