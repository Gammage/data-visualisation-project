##world fires exercise##
#in the resources for this chapter,
#youl find a file called world_fires_1_day.csv, this file contains informaion
#about fires burning in different locations
#around the globe
#inc lat, long, and brightness of each fire
#using the data-prociessing work from the first part of this chapter
#map work from this section, make a map
#that shows whic hparts of the world are affected by fires#

#https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data
#opted for books resource instead of login to site

from pathlib import Path
import csv
from datetime import datetime
import plotly.express as plt

path = Path("./chapter_16/weather_data/world_fires_1_day.csv")
contents = path.read_text().splitlines()


reader = csv.reader(contents)

#csv.reader creates the iterator that is ready to read through the csv file
#calling next(reader) advances the iterator by one step and returns first row
    #(typically a spreadsheet first row is the column headers)
#after that, a for loop continues reading from the iterators current position
#consumes the remaining rows until the iterator is exhausted
#once loop finishes the iterator has completed its single pass through the data
#and cannot be reused

header_row = next(reader)
print(header_row)

for index, column_header in enumerate(header_row):
    print(index, column_header)

lats,lons,lights = [],[],[]

for row in reader:
    lat = float(row[0])
    lon = float(row[1])
    light = float(row[2])
    
    lats.append(lat)
    lons.append(lon)
    lights.append(light)    

fig = plt.scatter_geo(lat=lats,
                      lon=lons,
                      size=lights,
                      color=lights,
                      labels={"color":"fire_size"},
                      projection="natural earth")

fig.show()