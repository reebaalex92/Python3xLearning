# Adding three numbers
def sum_three(a, b, c):
    return a + b + c


sum = sum_three(1, 2, 3)
print(sum)  # Output: 6

# Using a lambda expression
sum_three = lambda a, b, c: a + b + c
sum = sum_three(1, 2, 3)
print(sum)  # Output: 6
