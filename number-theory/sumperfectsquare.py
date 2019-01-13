 def graph(ns):
    import matplotlib.pyplot as plt
    plt.plot(ns)
    plt.show()

upto = 2a10mport *
0
sum_perfect_square = []

def add_ps(ps, a, b, upto):
    ps.append(a ** 2 + b ** 2)
    b += 1
    if b > a:
        a += 1
        b = 0
    if a >= upto:
        return ps
    return add_ps(ps, a, b, upto)

ps = add_ps([], 0, 0, upto)
graph(ps)
