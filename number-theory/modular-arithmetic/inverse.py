def inverse(mod, x):
    # den * i = num where 0 <= i < mod
    # because we take the inverse of x, den is x, and num is one
    for i in range(mod):
        if x * i % mod == 1:
            return i
    return -1

if __name__ == '__main__':
    while True:
        print(inverse(int(input('mod: ')), int(input('x: '))))
