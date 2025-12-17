
from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime
import csv


path = Path('chapter_16/weather_data/sitka_weather_2021_simple.csv')


lines = path.read_text().splitlines()


reader = csv.reader(lines)

#get the first row
header_row = next(reader)
print(header_row)

#index the items in that first row, so we can call on the data that row represents
for index, column_header in enumerate(header_row):
    print(index, column_header)
    


#extract the dates and high temperatures
dates, highs, lows = [],[],[]


for row in reader:
    #notice we call upon the order of items in the loop based on their index(2 for date, 4 for mxtmp)
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)


plt.style.use('seaborn-v0_8-deep')
fig, ax = plt.subplots()
ax.plot(dates,highs,color='red')
ax.plot(dates,lows,color='blue')
ax.fill_between(dates,highs,lows,facecolor='yellow',alpha=0.5)
ax.set_title("daily high and low temperatures, 2021")
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)",fontsize=16)
ax.tick_params(labelsize=16)

plt.ylim(top=120)
plt.show()
