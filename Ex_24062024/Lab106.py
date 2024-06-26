# Difference about map and filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def double_number(n):
    return n * 2


doubled_numbers = list(map(double_number, numbers))
print(doubled_numbers)

# Using lambda doubling the list elements
doubled_numbers = list(map(lambda n: n * 2, numbers))
print(doubled_numbers)


def even_number(n):
    return n % 2 == 0


even_numbers = list(filter(even_number, numbers))
print(even_numbers)

# Using lambda filtering only even numbers
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))
print(even_numbers)
