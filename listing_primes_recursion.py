# list all the numbers from 1 to n using for loop
def list_numbers(n):
    numbers = []
    for i in range(1, n + 1):
        numbers.append(i)
    return numbers


print(list_numbers(10))


# list all the numbers from 1 to n using recursion
def rec_list_numbers(n):
    if n == 0:
        return []
    return rec_list_numbers(n-1) + [n]


print(rec_list_numbers(10))


# list all the PRIME numbers from 1 to n using a for loop
# def listing_primes(n):
#     primes = []
#     for i in range(2, n + 1):
#         prime = True
#         for multiple in range(2, i):
#             if i % multiple == 0:
#                 prime = False
#         if prime is True:
#             primes.append(i)
#     return primes


# print(listing_primes(10))


# # list all the PRIME numbers from 1 to n using recursion
# def listing_primes_recursion(n):
#     primes = []
#     for i in range(2, n + 1):
#         prime = True
#         for multiple in range(2, i):
#             if i % multiple == 0:
#                 prime = False
#         if prime is True:
#             primes.append(i)

#     print(primes)
#     return primes


# print(listing_primes_recursion(10))
