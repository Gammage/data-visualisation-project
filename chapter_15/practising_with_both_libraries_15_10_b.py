##random walk

import plotly.express as px
from random import choice

class RandomWalk:
    """create a random walk"""
    
    def __init__(self, num_steps=5000):
        """initilisae walk"""
        self.num_steps = num_steps
        
        self.x_pos = [0]
        self.y_pos = [0]
        
    def fill_walk(self):
        """fill the walk"""
        while len(self.x_pos) < self.num_steps:
            x_step = self.walk_count()
            y_step = self.walk_count()
            
            x = self.x_pos[-1] + x_step
            y = self.y_pos[-1] + y_step
            
            if x_step and y_step == 0:
                continue
        
            self.x_pos.append(x)
            self.y_pos.append(y)
            
    def walk_count(self):
        """create the walk counter"""
        direction = choice([-1,1])
        distance = choice([1,2,3,4,5])
        
        route = distance * direction
        
        return route
    
r_walk = RandomWalk(5000)
r_walk.fill_walk()

df = px.data.gapminder()
fig = px.scatter(df, x=r_walk.x_pos, y=r_walk.y_pos,
                 color=range(len(r_walk.x_pos)))
fig.show()
