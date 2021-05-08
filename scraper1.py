from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

browser = requests.get(START_URL, verify = False)

print(browser)

soup = bs(browser.text, 'html.parser')

star_table = soup.find_all("table")
print(len(star_table))
temp_list = []

table_rows = star_table[4].find_all('tr')

for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
print(temp_list)
star_names = []
distance = []
mass = []
radius = []

for i in range(1, len(temp_list)):
    star_names.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])
  
df2 = pd.DataFrame(list(zip(star_names,distance,mass,radius)),columns = ["star_names", "distance", "mass", "radius"])
print(df2)

df2.to_csv("dwarf_stars.csv")