from inverse import inverse

def is_prime(n):
    for d in range(2, int(n ** .5) + 1):
        if n % d == 0:
            return False
    return True

def generator_rows(table, mod):
    for y, row in enumerate(table):
        # len(table) is the number of unit
        if len(set(row)) == len(table):
            yield y

def units(mod):
    for n in range(1, mod):
        if inverse(n, mod) != -1:
            yield n

def get_table(mod):
    max_width = 1
    table = []
    for y in units(mod):
        table.append([])
        for x in range(1, mod):
            n = y ** x % mod
            table[-1].append(n)
            if len(str(n)) > max_width:
                max_width = len(str(n))
    return table, max_width

def display_table(mod):
    table, max_width = get_table(mod)
    gen_rows = list(generator_rows(table, mod))
    print('mod:', mod)

    for y, row in enumerate(table):
        for cell in row:
            print(str(cell).rjust(max_width), end=' ')
        if y in gen_rows:
            print('gen')
        else:
            print()
    return table

def graph(numbers):
    import matplotlib.pyplot as plt
    plt.plot(numbers)
    plt.show()

official_mods = []

display_table(55)
exit()

mods = []
for mod in range(100):
    table, _ = get_table(mod)
    if len(list(generator_rows(table, mod))) != 0:
        mods.append(mod)

gens = []
for n in mods:
    gens.append(n)

graph(gens)
# for mod in [9]:
#     display_table(mod)

