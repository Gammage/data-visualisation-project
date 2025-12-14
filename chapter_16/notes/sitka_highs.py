##PARSING THE CSV FILE HEADERS##
#pythons csv module in the standard library parses the lines in a csv file and allows us
#to quickly extract the values we're interested in.

from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime
import csv

#CHECK WHERE THE PATH IS FROM, SEE THE TERMINAL FOLDER NAME. THATS THE BEGINNING OF THE PATH

#we build a path object that looks in the weather data folder
path = Path('chapter_16/weather_data/sitka_weather_2021_simple.csv')

#we read the file and chain the splitlines() method
lines = path.read_text().splitlines()

#build the reader object, can be used to parse each line in the file
reader = csv.reader(lines)

#here we call next() only once, so we get the first line of the file
#which contains the file headers
header_row = next(reader)
print(header_row)

#Printing the headers and their positions#
#to make it easier to understand the file header data, let's print each header and its 
#position in the list

#enumerate() function returns both the index of each item and the value of each item as you
#loop through the list
for index, column_header in enumerate(header_row):
    print(index, column_header)

#we can see that date and high temperators are in columns 2,4 (we include 0 in a index)

##extracting and reading data##
#we now know which column is what
#we'll read in the high temperature for each day



#reader object continues from where it left off in the csv file and automatically
#retruns each line following its current position. becuase we've already read the
#header row, the loop will begin at the second line where the actual data begins
#on each pass through the loop we pull the data from index 4, corresponding to the header
#TMAX and assign it to the variable high

#extract the dates and high temperatures
dates, highs = [],[]

#stripping date example
# first_date= datetime.strptime('2021-07-01','%Y-%m-%d')
# print(first_date)

# %a- = weekday name, such as monday
# %Y- = four digit year
# %y- = 2 digit year


for row in reader:
    #notice we call upon the order of items in the loop based on their index(2 for date, 4 for mxtmp)
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    dates.append(current_date)
    highs.append(high)



plt.style.use('seaborn-v0_8-deep')
fig, ax = plt.subplots()
ax.plot(dates,highs,color='red')

ax.set_title("daily high temperatures, 2021")
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)",fontsize=16)
ax.tick_params(labelsize=16)

plt.show()

#plotting a longer timeframe


