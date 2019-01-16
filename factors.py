"""A factoring algorithm """

def factorise(n):
    """returns the factors of n"""
    count = 0
    factors = []
    for i in range(2, n):
        count += 1
        while n % i == 0:
            factors.append(i)
            n = n // i
        if n == 1:
            break
    return factors, count

n = 3 * 5 * 7 * 97
print(factorise(n))
