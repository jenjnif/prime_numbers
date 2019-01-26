# finds all unique primes factors of any number, n
# e.g. if n = 500, if only has 4 unique prime factors (that do not
# belong to any number less than 500).


def find_primes(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return(primes)


def is_prime(x):
    prime = True
    for i in range(2, x):
        if x % i == 0:
            prime = False
    return prime


def unique_prime_factors():
    pass


def test_list_prime_to_n():
    assert find_primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_unique_prime_factor():
    assert unique_prime_factors(20) == [2, 3]
