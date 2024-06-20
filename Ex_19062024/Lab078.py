# lambda arguments:expression
# Function to check if a number is even or odd
def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(even_or_odd(10))  # Output: Even

# Using lambda expression

check_even_odd = lambda number: "Even" if number % 2 == 0 else "Odd"
result = print(check_even_odd(3))
