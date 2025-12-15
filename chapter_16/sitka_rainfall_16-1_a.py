##sitka_rainfall_exercise##
#in the data file sitka_weather_2021_full.csv is a header called PRCP, whilch represents daily
#rainful amounts. make a visualisation focusing on the data in this column
#you can repeat the exercise for Death valley if you're curious how little rainful occurs in a
#desert

from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path("./chapter_16/weather_data/sitka_weather_2021_full.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)
    
date, prcp = [],[]

for row in reader:
    current_date = datetime.strptime(row[2],'%Y-%m-%d')
    rainfall = float(row[5])
    date.append(current_date)
    prcp.append(rainfall)
    
fig, ax = plt.subplots()
ax.plot(date,prcp,color='blue')
fig.autofmt_xdate()
ax.set_title('daily rainfall in sitka 2021')
ax.tick_params(labelsize=16)
plt.show()

