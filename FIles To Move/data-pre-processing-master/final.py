import csv

data_set1 = []
data_set2 = []

with open("data\dataset_1.csv", "r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data_set1.append(row)

with open("data\Sorted.csv", "r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data_set2.append(row)

headers1 = data_set1[0]
planet_data1 = data_set1[1:]

headers2 = data_set2[0]
planet_data2 = data_set2[1:]

headers = headers1+headers2
planet_data = []

for index, data_row in enumerate(planet_data1):
    planet_data.append(planet_data1[index] + planet_data2[index])

with open("data/Final1.csv", "a+") as f:
    csv_writter = csv.writer(f)
    csv_writter.writerow(headers)
    csv_writter.writerows(planet_data)
    #C:\Users\USER\Desktop\Scraper-master\data-pre-processing-master\data\Final1.csv