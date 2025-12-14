import matplotlib.pyplot as plt
from pathlib import Path
import csv
from datetime import datetime


path = Path('./chapter_16/weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

print(header_row)

for index, column_header in enumerate(header_row):
    print(index, column_header)
    
dates, highs, lows = [],[],[]
for row in reader:
    current_date = datetime.strptime(row[2],'%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"missing data for {current_date}")
    else:   
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
        
#format plot
fig,ax = plt.subplots()
ax.plot(dates,highs,color='red')
ax.plot(dates,lows,color='blue')
ax.fill_between(dates,highs,lows,facecolor='yellow',alpha=0.5)
title = "daily high and low temperatures, 2021\nDeath Valley, CA"
ax.set_title(title,fontsize=20)
plt.show()

#as we handle the valueerror we skip the missing data and able to display it in graph
#
