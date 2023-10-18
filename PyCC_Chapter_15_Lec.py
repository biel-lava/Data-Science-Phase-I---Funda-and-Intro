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

# Plotting simple lie graph
#'''
import matplotlib.pyplot as plt # create an alias para hindi na ulit ulitin yung name ng package

raw = [] # raw numbers only
square = [] # squares of the raw numbers
cube = [] # subes of the raw numbers

for num in range(11):
    raw.append(num)
    square.append(num*num)
    cube.append(num*num*num)

fig, rw = plt.subplots()
fig, sq = plt.subplots()
fig, cb = plt.subplots()

rw.plot(raw)
sq.plot(square)
cb.plot(cube)

plt.show()

#'''