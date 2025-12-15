##san francisco exercise##
#are temperatures in san francisco more like temperatures in sitka or temperates in death valley
#download some data for sanfrancisco, and generate a high-low temp plot for san francisco to make 
#a comparison

from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt
from data_input import Data_input as di

path_min = Path("./chapter_16/weather_data/sanfrancisco_min_temp_2021.csv")
path_max = Path("./chapter_16/weather_data/sanfrancisco_max_temp_2021.csv")

min_temp = di(path_min)
max_temp = di(path_max)

time = max_temp.time()
max = max_temp.temperature()
min = min_temp.temperature()

fig, ax = plt.subplots()
ax.plot(time,min,color='blue')
ax.plot(time,max,color='red')
fig.autofmt_xdate()
ax.set_title('min/max temperatures')
ax.tick_params(labelsize=16)
plt.show()



