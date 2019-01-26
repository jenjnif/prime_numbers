# finds all unique primes factors of any number, n
# e.g. if n = 500, if only has 4 unique prime factors (that do not
# belong to any number less than 500).


def unique_prime_factors(n):
    primes = []
    total = 1
    if n == 1:
        return 0
    for i in range(2, n):
        if is_prime(i):
            total = total * i
            if total < n:
                primes.append(i)
    print(primes)
    return(primes)


def is_prime(x):
    prime = True
    for i in range(2, x):
        if x % i == 0:
            prime = False
    return prime


def test_return_prime():
    assert is_prime(5) is True


def test_unique_prime_factor():
    assert unique_prime_factors(20) == [2, 3]
