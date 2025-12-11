#three dice exercise#
#when you roll three d6 dice, the smallest number you can roll is 3 and the largest 18
#create a visualisation that shows what happens when you roll three d6 dice

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
die_3 = Die()

#results of the roll, amount of rolls depending on the range in the for statement
results = []
for roll_num in range(100000):
    result = die_1.roll_dice() + die_2.roll_dice() + die_3.roll_dice()
    results.append(result)

#find out the frequency of the rolls    
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
poss_result = range(3,max_result+1)
for frequency in poss_result:
    count = results.count(frequency)
    frequencies.append(count)

title = "results of rolling three d8 dice 100 times"
labels = {'x':'result','y':'frequency of result',}
fig = px.bar(x=poss_result,y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()



# range(start, stop) is left inclusive and right exclusive.
# It includes 'start' but does NOT include 'stop'.
# You only add +1 to 'stop' if you want the final number included.

