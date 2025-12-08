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
                
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            #calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            
            #reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue
            
            self.x_values.append(x)
            self.y_values.append(y)
         
    def get_step(self):
        """calculates the step"""
        #keep taking steps unitl the walk reaches the desired length
        direction = choice([1,-1])
        distance = choice([0,1,2,3,4,5])
        steps = direction * distance
        
        return steps
            

        
        
        
            





    
             
        