# Filters in python
# Built in functions filter()
# allows to filter items from list, tuple, set, etc
# filter(function, iterable)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 != 0


def is_greater5(n):
    return n > 5


new_numbers = filter(is_even, numbers)
new_numbers1 = filter(is_odd, numbers)
new_numbers2 = filter(is_greater5, numbers)
print(list(new_numbers))
print(list(new_numbers1))
print(list(new_numbers2))
