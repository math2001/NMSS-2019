while True:
    divisors = []
    n = int(input('> '))
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)

    print(len(divisors), '->', ', '.join(str(n) for n in divisors))
