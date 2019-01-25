# returns all primes up to the index n (zero-based numbering)
# e.g. if n = 4, returns all primes in up to index 4

# index 0, 1, 2, 3, 4
# prime 2, 3, 5, 7, 11


def list_primes_to_index(index):
    primes = []
    x = 2
    while len(primes) <= index:
        if is_prime(x):
            prime = is_prime(x)
            primes.append(prime)
            x += 1
        else:
            x += 1
    print(primes)
    return primes


def is_prime(prime):
    is_prime = True
    for i in range(2, prime):
        if prime % i == 0:
            is_prime = False
    if is_prime is True:
        return prime


def test_is_prime():
    assert is_prime(5) == 5


def test_list_primes_to_index():
    assert list_primes_to_index(3) == [2, 3, 5, 7]
