# Lambda expression is a one line function
# It is used to define a function in one line

def double(x):
    return x * 2

result = double(5)
print(result)  # Output: 10

# using lambda expression same function written as
double = lambda x: x * 2
result = double(5)
print(result)  # Output: 10