
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def odd_number(n):
    return n % 2 != 0


odd_numbers = list(filter(odd_number, numbers))
print(odd_numbers)

# Using lambda
odd_numbers = list(filter(lambda n: n % 2 != 0, numbers))
print(odd_numbers)
