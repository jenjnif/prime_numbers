# list all the numbers from 1 to n using for loop
def list_numbers(n):
    numbers = []
    for i in range(n):
        numbers.append(i)
    return numbers


print(list_numbers(10))


# list all the numbers from 1 to n using recursion
def rec_list_numbers(n):
    print(n)
    if n == 0:
        return []
    return rec_list_numbers(n-1) + [n]


print(rec_list_numbers(10))
