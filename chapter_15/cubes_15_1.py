##CUBES 15 1 EXERCISE##
#a number raised to the third power is a cube. plot the first five cubic numbers and then plt the first
#5000 cubic numbers

import matplotlib.pyplot as plt

value_x = range(1,5000)
value_y = [x**3 for x in value_x]

plt.style.use('seaborn-v0_8-darkgrid')
fig,ax = plt.subplots()
ax.scatter(value_x,value_y,s=5)
ax.axis([0,5250,0,1.30e11])
ax.ticklabel_format(style="scientific")

#scientific notation
#e means x 10 to the power of 
#1.25e11 means 1.25 x (10 ** 11)
#1e9 is a billion same as 10**9
#power has higher order of precedence than multiplication

#also every time when the multiplication term becomes larger than 10,
#the power goes up by 1. 12e5 is same as 1.2e6




plt.show()