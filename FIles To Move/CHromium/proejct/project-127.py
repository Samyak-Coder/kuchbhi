from bs4 import BeautifulSoup as bs
from selenium import webdriver
import requests
import pandas as pd

bright_starsURL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(bright_starsURL)


soup = bs(page.text, "html.parser")

startable = soup.find('table')

temp_list = []
table_rows = startable.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

StarNames = []
Distance = []
Radius = []
Mass = []
Lum = []

for i in range(1, len(temp_list)):
    StarNames.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    Lum.append(temp_list[i][7])

df2 = pd.DataFrame(list(zip(StarNames, Distance, Radius, Mass, Lum)), columns=['StarNames', 'Distance', 'Radius', 'Mass', 'Luminosity' ])
df2.to_csv('stars.csv')