# finds all unique primes factors of any number, n
# e.g. if n = 500, if only has 4 unique prime factors (that do not
# belong to any number less than 500).


def find_primes(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    print(primes)
    return(primes)


def is_prime(x):
    prime = True
    for i in range(2, x):
        if x % i == 0:
            prime = False
    print(prime)
    return prime


def test_list_prime_to_n():
    assert find_primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]
