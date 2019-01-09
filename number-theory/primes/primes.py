FILENAME = 'cache.txt'

def is_prime(n):
    for d in range(2, int(n ** .5) + 1):
        if n % d == 0:
            return False
    return True

