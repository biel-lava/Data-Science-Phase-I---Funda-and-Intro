'''
Chapter 15: Generating Data (Lab)
Date: 10/18/23
Reference: Python Crash Course (Matthes, 2019)
Topics:
    1. Matplotlib installation
    2. Plotting Simple Line Graph
    3. Random Walks
    3. Rolling Dice
'''

# Play 1: Plotting simple lie graph
'''
import matplotlib.pyplot as plt # create an alias para hindi na ulit ulitin yung name ng package

raw = [] # raw numbers only
square = [] # squares of the raw numbers
cube = [] # subes of the raw numbers

for num in range(11):
    raw.append(num)
    square.append(num*num)
    cube.append(num*num*num)
plt.style.use('dark_background')

fig, rw = plt.subplots()
fig, sq = plt.subplots()
fig, cb = plt.subplots()

rw.plot(raw)
sq.plot(square)
cb.plot(cube)

plt.show()

'''

# Play 2: Using the full syntax of plot()
'''
import matplotlib.pyplot as plt

raw = [1, 3, 4, 8, 15, 17, 19, 25, 37, 38]
square = []

for num in raw:
    square.append(num * num * num)

plt.plot(raw, square)
plt.show()

'''

# Problem # 1: Cubes

'''
import matplotlib.pyplot as plt

raw = [x for x in range(0,5001)]
square = [y**2 for y in raw]
cube = [z**3 for z in raw]

plt.style.use('dark_background')

fig, pl = plt.subplots(3)

pl[0].plot(raw, raw, color = 'g')
pl[1].plot(raw, square, color = 'c')
pl[2].plot(raw, cube, color = 'y')

pl[0].set_title("Raw Numbers", fontsize = 14)
pl[0].set_xlabel("Value", fontsize = 10)
pl[0].set_ylabel("Value", fontsize = 10)

pl[1].set_title("Square of Numbers", fontsize = 14)
pl[1].set_xlabel("Value", fontsize = 10)
pl[1].set_ylabel("Squares", fontsize = 10)

pl[2].set_title("Cube of Numbers", fontsize = 14)
pl[2].set_xlabel("Value", fontsize = 10)
pl[2].set_ylabel("Cubes", fontsize = 10)


plt.show()

'''

# Problem # 3: Molecular motion

'''
import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw_trial = RandomWalk() # create a RandomWalk instance 

rw_trial.fill_walk() # call the fill_walk() method


plt.style.use('dark_background')

fig, rw = plt.subplots()

rw.plot(rw_trial.x_values, rw_trial.y_values, linewidth = 1) # syntax ay scatter(x-coordinate, y-coordinate)

rw.set_title("Molecular Motion", fontsize = 15)
rw.set_xlabel("x-value", fontsize = 14)
rw.set_ylabel("y-value", fontsize = 14)

plt.show()

'''
