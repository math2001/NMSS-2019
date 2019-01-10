import time
from primes import *

def generate_prime(n):
    timeout = 1000
    count = 0
    last = time.time()
    with open(FILENAME, 'a') as fo:
        while True:
            if is_prime(n):
                fo.write(f'{n}\n')
                count += 1
                if count % timeout == 0:
                    t = round(time.time() - last, 3)
                    print(f'{count} primes generated {timeout}/{t}s (up to {n}) ',
                          end='\r')
                    last = time.time()
            n += 2

def get_last_prime():
    try:
        with open(FILENAME, 'r') as fo:
            line = 2
            for line in fo:
                pass
            return int(line.strip())
    except OSError:
        return 2
    except ValueError:
        raise ValueError("The file was corrupted. Couldn't load the first prime")

if __name__ == '__main__':
    generate_prime(get_last_prime())
