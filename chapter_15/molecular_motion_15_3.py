##molecular motion exercise##
# modify rw_visual.py, by replacing ax.scatter() with ax.plot()
    #to simulate the path of a pollen grain on the surface of a drop of water
    #pass in the rw.x_values and rw.y_values, include a lindewidth argument
    #use 5000 instead of 50,000 to keep the plot from being too busy

import matplotlib.pyplot as plt

from notes.random_walk import RandomWalk

#keep making walks whilst program is active
while True:
    #make a random walk
    # make a random walk
    rw = RandomWalk()
    rw.fill_Walk()

    # plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.plot(rw.x_values, rw.y_values, color='red', linewidth=2)

    plt.show()
    
    keep_running = input("make another graph? y/n")
    if keep_running == 'n':
        break