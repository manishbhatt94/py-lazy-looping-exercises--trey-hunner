import sys
from math import isqrt


def is_prime(candidate):
    if candidate < 2:
        return False
    for n in range(2, isqrt(candidate) + 1):
        if candidate % n == 0:
            return False
    return True


def get_big_primes(limit):
    print("start")
    n = 999999
    count = 0
    while count < limit:
        if is_prime(n):
            print(f"found prime: {n}")
            yield n
            count += 1
        n += 1
    print("end")


def main():
    limit = int(sys.argv[1])
    for prime in get_big_primes(limit):
        print(prime)


if __name__ == "__main__":
    main()
