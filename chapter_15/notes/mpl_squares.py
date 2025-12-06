import matplotlib.pyplot as plt


#using matplotlib to plot a simple line graph

# squares = [1,4,9,16,25]

# fig, ax = plt.subplots()
# ax.plot(squares)

# plt.show()

#pyplot module contains a number of functions that help generate charts and plots
#we create a list called squares to hold the data that we'll plot

#variable fig represents the entire figure, which is the collection of plots that are generated

#variable ax represents a single plot in the figure; this is the var we'll use
#most of the time when defining and customizing a single plot

#the plot() method tries to plot the data its given in a meaningfull way
#function plot.show() opens matplotlibs viewer and displays the plot.
    #viewer allows you to zoom and navigate the plot, and you can save any plot images
    #you like by clicking the disc icon

#the x axis values (this prevents making assumptions on graph)
input_values = [1,2,3,4,5]

# the data    
squares = [1,4,9,16,25]

#creating the table. inside the plot goes the values
#styling the graph
plt.style.use('seaborn-v0_8-darkgrid')
#creating graph:
fig, ax = plt.subplots()
#plotting the values:
ax.plot(input_values, squares, linewidth=3)


#set chart title and label axes.
ax.set_title("square numbers", fontsize=24)

#naming of x/y axis labels
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("square of value", fontsize=14)

# set size of tick labels
ax.tick_params(labelsize=14)

#shows graph
plt.show()

##USING BUILT IN STYLES##
#in shell (type python) import library and plt.style.available
#style in use: plt.style.use('seaborn-v0_8-darkgrid')





