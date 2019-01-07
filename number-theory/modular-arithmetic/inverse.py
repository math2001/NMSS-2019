import matplotlib.pyplot as plt

mod = 19
def f(x):
    return x ** 2

fx = []
for x in range(mod):
    fx.append(f(x) % mod)

plt.plot(range(mod), fx)
plt.show()
