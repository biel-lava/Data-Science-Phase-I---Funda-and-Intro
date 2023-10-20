'''
Chapter 15: Generating Data (Random Walk Class)
Date: 10/20/23
Reference: Python Crash Course (Matthes, 2019)
Notes
    - Makes random decisions on the direction of the walk
    - Three attributes: one variable to store the number of points and two lists to store the coordinates (x and y value)
'''
from random import choice

# Mk1 random_walk
#'''

class RandomWalk:
    def __init__(self, num_points = 5000):
        self.num_points = num_points # sets the default number of points to 5000

        self.x_values = [0] # holds the x-value of the points
        self.y_values = [0] # holds the y-value of the points

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            
            # Update the x-value of the point
            x_direction = choice([1, -1]) # choose the direction (left or right)
            x_distance = choice([0, 1, 2, 3, 4]) # choose the distance of the step
            x_step = x_direction * x_distance # calculate for the step
            x = self.x_values[-1] + x_step # update the x-value of the current point
            self.x_values.append(x) # add the x-value into the list

            # Update the y-value of the point
            y_direction = choice([1, -1]) # choose the direction (left or right)
            y_distance = choice([0, 1, 2, 3, 4]) # choose the distance of the step
            y_step = y_direction * y_distance # calculate for the step
            y = self.y_values[-1] + y_step # update the x-value of the current point
            self.y_values.append(y) # add the x-value into the list
#'''

