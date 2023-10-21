'''
Chapter 15: Generating Data (Die Class)
Date: 10/21/23
Reference: Python Crash Course (Matthes, 2019)
Notes
    - Class that represents the die 
'''

from random import randint

class Die:

    def __init__(self, num_sides = 6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)