""" There are multiple functions that you can apply

To use a specific one (such as square), simply set f to this specific function
"""
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

ax = plt.figure().gca()

def inverse(x, mod):
    # den * i = num where 0 <= i < mod
    # because we take the inverse of x, den is x, and num is one
    for i in range(mod):
        if x * i % mod == 1:
            print(f"1 / {x} mod {mod} = {i}")
            return i
    print(f"1 / {x} mod {mod} = -1")
    return -1

def square(x, mod):
    return x ** 2 % mod

def mod(x, mod):
    return x % mod

f = inverse

def plot(mod):
    fx = []
    for x in range(mod):
        fx.append(f(x, mod))
    plt.bar(range(mod), fx)

plot(7)

ax.xaxis.set_major_locator(MaxNLocator(integer=True))
plt.show()

