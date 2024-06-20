my_list = [1, 2, 3, 4, 5]


def number_list(numbers):
    numbers.append(6)
    numbers[1] = 19
    return numbers


l = number_list(my_list)
print(l)
