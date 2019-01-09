def square(mod, rest):
    solutions = []
    for n in range(mod):
        if n ** 2 % mod == rest % mod:
            solutions.append(n)
    return solutions

def display(mod, rest):
    solutions = square(13, -1)
    if len(solutions) == 0:
        print('no solution')
    elif len(solutions) != 2:
        print('weird number of solution', found)
    else:
        print(f'solutions mod {mod} rest {rest}:',
              ', '.join(str(s) for s in solutions))

for mod in [5, 6, 7]:
    for rest in [0, 1, 2, 3, 4]:
        display(mod, rest)
