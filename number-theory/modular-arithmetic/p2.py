"""
13x + 8y = 1

Plot the minimal difference between 13x and 8y.
"""

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

ax = plt.figure().gca()

def f(a, b, x):
    top = a * x
    while top > b:
        top -= b
    return top

upto = 20
a = 13
b = 8
plt.plot(range(upto), [f(a, b, x) for x in range(upto)])
plt.bar(range(upto), [a * x % b for x in range(upto)])

ax.xaxis.set_major_locator(MaxNLocator(integer=True))
plt.show()
