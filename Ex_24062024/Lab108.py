# Recursion
# It is a programming technique where a function calls itself to solve a problem.
# It is a common technique used in programming languages that do not have built-in support for recursion.
# Key concepts:
# 1. Base case: A condition that stops the recursion.
# 2. Recursive case: A condition that calls the function itself.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print("The factorial is:", factorial(8))

