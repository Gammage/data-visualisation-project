##automatic index exercise##
#use the reader row to determine the indexes for these values, so your program can work for sitka
#or death valley
#so your program works for sitka or death valley. use the station name to auto generate
#an appriopiate title for your graph as well.

from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt
from data_input import Data_input as Di

path_1 = Path("./chapter_16/weather_data/sitka_weather_2021_full.csv")
path_2 = Path("./chapter_16/weather_data/death_valley_2021_full.csv")

sitka = Di(path_1)
death = Di(path_2)

sitka.index_column()
#sitka
#7 tmax
#8 tmin
death.index_column()
#death
#6 tmax
#7 tmin

sitka_station = sitka.station_name(1)
sitka_temp_min = sitka.temperature(8)
sitka_temp_max = sitka.temperature(7)
sitka_date = sitka.time(2)

death_station = death.station_name(1)
death_temp_min = death.temperature(7)
death_temp_max = death.temperature(6)
death_date = death.time(2)

plt.style.use('seaborn-v0_8-deep')
fig,ax = plt.subplots()
ax.plot(death_date,death_temp_min,color='blue')
ax.plot(death_date,death_temp_max,color='red')
# ax.set_ylim(0,100)

# ax.fill_between(sitka_date,sitka_temp_min,sitka_temp_max,facecolor='yellow',alpha=)
ax.set_title(f"Data from {death_station}")
plt.show()



