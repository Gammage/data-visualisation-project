##rolling dice of different sizes##

import plotly.express as px
from die import Die

#create a d6 and d10

die_1 = Die()
die_2 = Die(10)

#make some rolls, and store results ina  list.
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2,max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
    
title = "results of rolling a d6 dice and d10 50,000 times"
labels = {'x':'result','y':'frequency of result',}
fig = px.bar(x=poss_results,y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()
    
#increased rolls to 50,000
#title change (compared to die_visual.py)

#saving figures
fig.write_html('dice_visual_d6_d10.html')
#write_html method requires one argument: name of the file to write to.


