def inverse(x, mod):
    # den * i = num where 0 <= i < mod
    # because we take the inverse of x, den is x, and num is one
    for i in range(mod):
        if x * i % mod == 1:
            print(f"1 / {x} mod {mod} = {i}")
            return i
    print(f"1 / {x} mod {mod} = -1")
    return -1

inverse(7, 15)
exit()
mod = 11
for i in range(mod):
    inverse(i, mod)
