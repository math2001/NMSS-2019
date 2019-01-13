from inverse import inverse

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

def display_table(table, max_width, mod, generators):
    print('mod:', mod)
    for y, row in enumerate(table):
        for cell in row:
            print(str(cell).rjust(max_width), end=' ')
        if y in generators:
            print('gen')
        else:
            print()
    return table

def gen_row_numbers(table, generators):
    if len(generators) == 0:
        return "This set isn't cyclic"
    cardinality = len(table)
    first = generators[0]
    for x, cell in enumerate(table[first]):
        if x % 2 == 1 or cardinality % (x + 1) == 0:
            continue
        if cell - 1 not in generators:
            print(table[first], generators, cell, x, cardinality)
            return False
    return True

def graph(numbers):
    import matplotlib.pyplot as plt
    plt.plot(numbers)
    plt.show()

mod = 15
table, max_width = get_table(mod)
generators = list(generator_rows(table, mod))
display_table(table, max_width, mod, generators)
print(gen_row_numbers(table, generators))

