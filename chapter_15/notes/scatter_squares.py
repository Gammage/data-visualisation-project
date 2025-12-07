#plotting and styling individual points with scatter()
#sometimes its useful to plot and style individual points based on certian characteristics
#for example, plot small values in one colour and larger ones in a different colour
#plotting a large dataset with one set of styling options and then emphasise indivudal poitns by
#replotting them with different options.

import matplotlib.pyplot as plt

# x_values = [1,2,3,4,5]
# y_values = [1,4,9,16,25]

# plt.style.use('seaborn-v0_8-darkgrid')
# fig,ax = plt.subplots()
# ax.scatter(x_values,y_values,s=200)

# #set chart title and axes
# ax.set_title("square numbers",fontsize=24)
# ax.set_xlabel("value",fontsize=14)
# ax.set_ylabel("square of value",fontsize=14)

# #set size of tick labels
# ax.tick_params(labelsize=14)

# plt.show()

#collecting data automatically
#writing lists by hand inefficient
#using a loop to do the calculations for us

x_values = range(1,1001)
y_values = [x**2 for x in x_values]
#using a list comprehension x squared for x in the x_values

plt.style.use('seaborn-v0_8-darkgrid')
fig,ax = plt.subplots()
# ax.scatter(x_values,y_values,color=(0,0.8,0), s=10)
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues, s=10)
ax.axis([0,1100, 0, 1_100_000])
ax.ticklabel_format(style="plain")
#the axis method needs four values, the min and maximum value of x, y axis

#set chart title and axes
ax.set_title("square numbers",fontsize=24)
ax.set_xlabel("value",fontsize=14)
ax.set_ylabel("square of value",fontsize=14)

#set size of tick labels
ax.tick_params(labelsize=14)


# plt.show()

##customizing tick labels
#when the numbers on an axis get large enough, matplotlib defaults to scientific notation for tick
#labels. this is good, as large larger numbers in plain notation take up alot of unneccessary space
#almost every element on a chart is customiseable, soy ou can tell matplotlib to keep using plain
#notation if one prefers

#saving your plats automatically

#save to a file using plt.savefig() instead of plt.show()
plt.savefig('squares_plot.png',bbox_inches='tight')

