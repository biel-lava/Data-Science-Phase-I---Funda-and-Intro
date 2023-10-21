'''
Chapter 15: Generating Data
Date: 10/18/23
Reference: Python Crash Course (Matthes, 2019)
Topics:
    1. Matplotlib installation
    2. Plotting Simple Line Graph
    3. Random Walks
    3. Rolling Dice
'''

# PLOTTING SIMPLE LINE GRAPH

# Most basic line graph
'''
import matplotlib.pyplot as plt # create an alias para hindi na ulit ulitin yung name ng package

square = [] # squares of the numbers

for num in range(11):
    square.append(num*num)

fig, sq = plt.subplots()

sq.plot(square)

plt.show()

'''

# Modifying line graph
'''

import matplotlib.pyplot as plt # create an alias para hindi na ulit ulitin yung name ng package

square = [] # squares of the numbers

for num in range(11):
    square.append(num*num)

fig, sq = plt.subplots()

sq.plot(square, linewidth = 3) # increases the thickness of the line

sq.set_title("Square of Numbers", fontsize = 24)
sq.set_xlabel("Value", fontsize = 14)
sq.set_ylabel("Square", fontsize = 14)

plt.show()

'''

# Using Built-in Styles
'''

import matplotlib.pyplot as plt # create an alias para hindi na ulit ulitin yung name ng package

square = [] # squares of the numbers

for num in range(11):
    square.append(num*num)
plt.style.use('dark_background')

fig, sq = plt.subplots()

sq.plot(square, linewidth = 3) # increases the thickness of the line

sq.set_title("Square of Numbers", fontsize = 24)
sq.set_xlabel("Value", fontsize = 14)
sq.set_ylabel("Square", fontsize = 14)

plt.show()

'''

# Using scatter()

'''
import matplotlib.pyplot as plt # create an alias para hindi na ulit ulitin yung name ng package

raw = []
square = [] # squares of the numbers

for num in range(11):
    raw.append(num)
    square.append(num*num)
plt.style.use('dark_background')

fig, sq = plt.subplots()

sq.scatter(raw, square) # syntax ay scatter(x-coordinate, y-coordinate)

sq.set_title("Square of Numbers", fontsize = 24)
sq.set_xlabel("Value", fontsize = 14)
sq.set_ylabel("Square", fontsize = 14)

plt.show()


'''

# Using list comprehension with scatter()

'''
import matplotlib.pyplot as plt # create an alias para hindi na ulit ulitin yung name ng package

raw = [x for x in range(0, 26)] # 
square = [ y**2 for y in raw] # squares of the numbers using the syntax 'y**'

plt.style.use('dark_background')

fig, sq = plt.subplots()

sq.scatter(raw, square, s = 25) # syntax ay scatter(x-coordinate, y-coordinate)

sq.set_title("Square of Numbers", fontsize = 24)
sq.set_xlabel("Value", fontsize = 14)
sq.set_ylabel("Square", fontsize = 14)

plt.show()

'''

# RANDOM WALKS

# Using the Mk1 random_walk
'''

import matplotlib.pyplot as plt

from random_walk import RandomWalk # import the class from the random_walk script

rw_trial = RandomWalk() # create a RandomWalk instance 

rw_trial.fill_walk() # call the fill_walk() method


plt.style.use('dark_background')

fig, rw = plt.subplots()

rw.scatter(rw_trial.x_values, rw_trial.y_values, s = 25) # syntax ay scatter(x-coordinate, y-coordinate)

rw.set_title("Random Walks Mk 1", fontsize = 15)
rw.set_xlabel("x-value", fontsize = 14)
rw.set_ylabel("y-value", fontsize = 14)

plt.show()
'''

# ROLLING DICE

# Trying the Die class

from die import Die

die = Die()

results = []

for x in range(100):
    results.append(die.roll())

print(results)

