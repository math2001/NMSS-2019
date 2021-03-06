from inverse import inverse

def is_prime(n):
    for d in range(2, int(n ** .5) + 1):
        if n % d == 0:
            return False
    return True

def gcd(a, b):
    """ Euclid's algorithm """
    if a % b == 0:
        return b
    return gcd(b, a % b)

def units(mod):
    """ The units are all the elements that have inverses """
    u = []
    for n in range(1, mod):
        if inverse(mod, n) != -1:
            u.append(n)
    return u.copy()

class Table:

    def __init__(self, mod):
        self.mod = mod
        self.data = []
        self.units = units(self.mod)
        self.cell_width = 0

        for y in self.units:
            self.data.append([])
            for x in range(1, mod):
                self.data[-1].append(y ** x % self.mod)
                if len(str(self.data[-1][-1])) > self.cell_width:
                    self.cell_width = len(str(self.data[-1][-1]))

        self.gens = []
        for row in self.data:
            if self.is_gen(row):
                self.gens.append(row[0])

    def is_gen(self, row):
        return len(set(row)) == len(self.units)

    def _get_gens(self):
        """ Get gens return the first element of the rows that are generators
        Rememember that the first column is just x^1
        """

    def display(self):
        print('mod:       ', self.mod)
        print('prime:     ', is_prime(self.mod))
        print('units:     ', f'({len(self.units)})', ', '.join(str(u) for u in self.units))
        print('generators:', f'({len(self.gens)})', ', '.join(str(u) for u in self.gens))
        print()
        columns_names = ' '.join(
            str(n).rjust(self.cell_width) for n in range(1, self.mod))
        print(columns_names)
        print('-' * len(columns_names))
        for row in self.data:
            for cell in row:
                print(str(cell).rjust(self.cell_width), end=' ')
            if row[0] in self.gens:
                print('gen', end='')
            print()

    def first_to_all(self):
        """ Sud's conjecture
        looking at the first generators, if any, and every odd column that
        isn't a factor of the cardinality gives you the next generator row
        """
        if len(self.gens) == 0:
            raise ValueError(f"This mod {self.mod} is not cyclic")

        cardinality = len(self.units)

        first_gen_row = None
        for row in self.data:
            if row[0] == self.gens[0]:
                first_gen_row = row
                break
        else:
            raise ValueError("could not find first generator")

        for x, cell in enumerate(first_gen_row):
            if x % 2 == 1 or gcd(cardinality, (x + 1)) != 1:
                continue
            if cell not in self.gens:
                print('breaks', cell)
                return False
        return True

    def gen_inverse(self):
        """ Another conjecture: if n is a generator, 1 / n is as well """
        for gen in self.gens:
            if inverse(gen, self.mod) not in self.gens:
                return False
        return True

def showmod(*mods):
    for mod in mods:
        t = Table(mod)
        t.display()
        print()

def test_sud():
    for mod in range(1, 100):
        t = Table(mod)
        try:
            print(mod, t.first_to_all())
        except ValueError as e:
            pass

def test_sud_inverse():
    for mod in range(1, 100):
        t = Table(mod)
        try:
            print(mod, t.gen_inverse())
        except ValueError as e:
            pass

def generators():
    gen_mods = []
    for mod in range(1, 150):
        t = Table(mod)
        if len(t.gens):
            gen_mods.append(mod)
    print(gen_mods)

def repl():
    while True:
        mod = int(input('> '))
        showmod(mod)

def graph(ns):
    import matplotlib.pyplot as plt
    plt.plot(ns)
    plt.show()

def first_gen():
    g = []
    for mod in range(1, 100):
        t = Table(mod)
        if len(t.gens) and not is_prime(mod):
            g.append((mod, t.gens[0]))
    print(g)
    # graph(g)

# first_gen()
showmod(121, 81, 169)
# repl()

