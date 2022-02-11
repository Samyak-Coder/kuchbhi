from os import scandir
import pandas as pd
import csv

file1 = "proejct\128.csv"
file2 = "proejct\ConvertedStars.csv"

data_1 = []
data_2 = []

with open("proejct\proejct128.csv", "r") as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        data_1.append(i)

with open(file2, "r") as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        data_2.append(i)

headers1 = data_1[0]
headers2 = data_2[0]

planetData1 = data_1[1:]
planetData2 = data_2[1:]

headers = headers1 + headers2

planetData = []

for i in planetData1:
    planetData.append(i)

for i in planetData2:
    planetData.append(i)

with open("Final_129.csv", "w") as f:
    csv_writter = csv.writer(f)
    csv_writter.writerow(headers)
    csv_writter.writerows(planetData)


