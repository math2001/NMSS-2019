FILENAME = 'number-theory/primes/cache.txt'

def is_prime(n):
    for d in range(2, int(n ** .5) + 1):
        if n % d == 0:
            return False
    return True

if __name__ == "__main__":
    for n in range(100):
        if is_prime(n):
            print(n, n % 4)
