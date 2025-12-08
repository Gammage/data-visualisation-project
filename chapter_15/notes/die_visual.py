from die import Die
import plotly.express as px

#create a die
die = Die()
    
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#analyse results
frequencies = []
#stops before last number, hence plus 1. exclusive to range
poss_results = range(1,die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
    
# print(frequencies)

#in the above, we create an object using the die class
#we then roll it 1000 times and append the results in results list

#we then analyse the results in frequencies, referencing the dice
#for each roll result, we count the frequency each time in a for loop
 #we append the frequency in the list frequencies. this calculates how many
 #times each roll landed between the given sided dice
 
#visualise the results in a histogram
title = "Results of Rolling one D6 1000, times"
labels = {'x':'result','y':'frequency of result',}
fig = px.line(x=poss_results,y=frequencies, title=title, labels=labels)
fig.show()

#simple bar chart, but plotly is designed to be simple, represent the data  the way you want it to
#

