# %%
import matplotlib.pyplot as plt

from random_walk import RandomWalk


# plt.show()



#keep making walks whilst program is active


#make a random walk
# make a random walk
rw = RandomWalk(50_000)
rw.fill_Walk()


# plot the points in the walk
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15,9)) #*
#matplotlib assumes screen resolution is 100 pixels per inch
#figsize parameter takes a tuple that tells the dimensions of plotting window in inches
#you can use the dpi parameter, which would be sublots(figsize = (10,6),dpi=128)

#*
# fig, ax = plt.subplots()
# # is equivalent to
# result = plt.subplots()
# fig = result[0]
# ax = result[1]s



#coloring the points
point_numbers = range(rw.num_points)

ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
            edgecolors='none', s=1)
ax.set_aspect('equal')

#emphasising first and last points
ax.scatter(0,0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)
#-1 index is last item in a list

#removing the axes
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()

#styling the walk
#customise plots to emphases characteristics of each walk
    #such as where walk began, ended
    #characteristics to deemphasize

#adding plot points
#increase number of points, give more data to work with









# %%
