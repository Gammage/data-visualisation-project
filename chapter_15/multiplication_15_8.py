##multiplication##
#when you roll two dice, you usually add two numbers together to get the result
#create a visualiation that shows what happens if you multiply these numbers by each other instead

import plotly.express as px
from random import randint

class Die:
    """determine a 6d die"""
    
    def __init__(self, num_sides=6):
        """determine the dice"""
        self.num_sides = num_sides
        
    def roll_dice(self):
        return randint(1,self.num_sides)
    
die_1 = Die()
die_2 = Die()

#results of the roll, amount of rolls depending on the range in the for statement
results = []
for roll_num in range(10000):
    result = die_1.roll_dice() * die_2.roll_dice()
    results.append(result)


#find out the frequency of the rolls    
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
poss_result = range(1,max_result+1)
for frequency in poss_result:
    count = results.count(frequency)
    frequencies.append(count)

title = "results of multiplying rolling 2 d6 dice 10000 times"
labels = {'x':'result','y':'frequency of result',}
fig = px.bar(x=poss_result,y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()

