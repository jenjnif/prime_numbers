def unique_prime_factors(n):
    primes = []
    for i in range(2, n + 1):
        prime = True
        for multiple in range(2, i):
            if i % multiple == 0:
                prime = False
        if prime is True:
            primes.append(i)

    print(primes)
    return primes


unique_prime_factors(10)



