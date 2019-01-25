# returns all primes up to the index n (zero-based numbering)
# e.g. if n = 4, returns all primes in up to index 4

# index 0, 1, 2, 3, 4
# prime 2, 3, 5, 7, 11


def find_primes_to_index(n):
    pass


def is_prime(x):
    prime = True
    for i in range(2, x):
        if x % i == 0:
            prime = False
    return prime


def test_list_index_zero_prime():
    assert find_primes_to_index(0) == [2]
