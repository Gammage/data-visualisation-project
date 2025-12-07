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
        self.y_values = [0]
        
    def fill_Walk(self):
        """calculate all the points in the walk"""
        
        #keep taking steps unitl the walk reaches the desired length
        while len(self.x_values) < self.num_points:
            
            #decide which direction to go, and how far to go
                #the distance choice has a 0 because one can potentially not move in one direction
                
            #just a reminder this is a list not a [:] slice
            
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4,5])
            x_step = x_direction * x_distance
            
            
            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4,5])
            y_Step = y_direction * y_distance
            
            #reject moves that go nowhere
            if x_step == 0 and y_Step == 0:
                continue
            
            #calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_Step
            
            self.x_values.append(x)
            self.y_values.append(y)
            





    
             
        