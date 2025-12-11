##Two D8s##
#create a simulation showing what happens when you toll two D8 eight sided dice 100 times
#APPAZ MOST LIKELY TO GET 7 

import plotly.express as px
from random import randint

class Die:
    """creating a die"""
    
    def __init__(self, num_sides=6):
        """assume a six sided die"""
        
        self.num_sides = num_sides
        
    def roll_dice(self):
        """rolling the dice"""
        
        return randint(1,6)
    
die_1 = Die(8)
die_2 = Die(8)

results = []
for roll_num in range(100000):
    result = die_1.roll_dice() + die_2.roll_dice()
    results.append(result)
    
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2,max_result+1)
for frequency in poss_results:
    count = results.count(frequency)
    frequencies.append(count)

title = "results of rolling two d8 dice 100 times"
labels = {'x':'result','y':'frequency of result',}
fig = px.bar(x=poss_results,y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()        