# finds all unique primes factors of any number, n
# e.g. if n = 500, if only has 4 unique prime factors (that do not
# belong to any number less than 500).


def unique_prime_factors(n):
    primes = []
    total = 1
    if n == 1:
        primes = [1]
        return primes
    for i in range(2, n):
        if is_prime(i):
            total = total * i
            if total < n:
                primes.append(i)
    return primes


def is_prime(x):
    prime = True
    for i in range(2, x):
        if x % i == 0:
            prime = False
    return prime

# ALL IN ONE FUNCTION

# def unique_prime_factors(n):
#     primes = []
#     total = 1
#     if n == 1:
#         return len(primes)
#     for i in range(2, n + 1):
#         prime = True
#         for multiple in range(2, i):
#             if i % multiple == 0:
#                 prime = False
#         if prime is True:
#             total = total * i
#             if total <= n:
#                 primes.append(i)
#             else:
#                 break
#     return len(primes)


# def test_unique_prime_factor():
#     assert unique_prime_factors(2) == 1


def test_return_prime():
    assert is_prime(2) is True


def test_unique_prime_factor():
    assert unique_prime_factors(20) == [2, 3]


def test_unique_prime_factor_two():
    assert unique_prime_factors(500) == [2, 3, 5, 7]
