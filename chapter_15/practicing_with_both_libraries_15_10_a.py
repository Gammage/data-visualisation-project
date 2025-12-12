##practicing with both libraries##
#try using matplotlib to make a die-rolling visulisation
#use plotlty to make the visualisation for a random walk (you'll need to consult the
#documentation for each library to complete this exercise.)

#for die-rolling visualisation see below
#for plotly to make visualisation for random walk see version b of file

#die rolling visualisation
import matplotlib.pyplot as plt
from random import randint

class Die:
    """creates a dice"""
    
    def __init__(self, num_sides=6):
        """defines the dice"""
        
        self.num_sides = num_sides
        
    def roll_dice(self):
        """roll the dice"""
        roll = randint(1,self.num_sides)
        
        return roll

dice = Die()

#we want to roll a dice and get the results and frequency of those rolls

#range determines how many rolls
results = [dice.roll_dice() for n in range(1000)]

#frequencie of roll results
poss_results = range(1,dice.num_sides+1)
frequencies = [results.count(n) for n in poss_results]

#in matplotlib, you are CREATING the figure and axis, not defining them
fig, ax = plt.subplots()

#here you create if its a bar, or a line graph etc and the values of axis go in parenthesis:
ax.bar(poss_results,frequencies)

plt.show()


