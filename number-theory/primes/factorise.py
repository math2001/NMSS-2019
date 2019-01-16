from primes import *

def factorise(n):
    factors = []
    with open(FILENAME, 'r') as fo:
        for d in fo:
            d = int(d)
            while n % d == 0:
                factors.append(d)
                n = n // d
            if n == 1:
                break
    return factors, n

if __name__ == '__main__':
    n = None
    while True:
        try:
            n = int(input('> '))
        except ValueError:
            print('invalid number')
            break
        else:
            factors, left = factorise(n)
            print(', '.join(str(n) for n in factors), '=>', left)
