##random walks##
#create the RandomWalk class

from random import choice

class RandomWalk:
    """a class to generate random walks"""
    
    def __init__(self, num_points=5000):
        """initialise attributes of walk"""
        self.num_points = num_points
        
        #all walks start at (0,0)
        self.x_values = [0]
        self.y_Values = [0]
        
        