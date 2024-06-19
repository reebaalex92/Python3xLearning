# Functions
# Block of code which can be executed many times, reuse the code
# Builtin functions, user defined functions
# 2 types of functions
# 1. Built in functions - already defined in python
# 2. User defined functions - custom functions defined by the user
max(2, 3)
result = max(2, 3)
print(result)


# User defined functions
# Return something
# Not return anything
# have parameters
# don't have parameters/arguments

def say_hello():  # No returntype and no parameters/arguments
    print("Hello")


say_hello()


def say_hello1(name):  # No returntype and have parameters/arguments
    print("Hello", name)


say_hello1("Reeba")
say_hello1("Lisha")


def say_hello2(name="Stranger"):  # have no returntype and have default parameters/arguments
    print("Hello", name)


say_hello2()
say_hello2("Reeba")
say_hello2(name="Lisha")


def add1(a, b):
    return a + b


def add(num1, num2):
    return num1 + num2


result = add(24, 45)
print(result)
result1 = add1(31, 45)
print(result1)
result2 = add(num1=23, num2=50)
print(result2)
result3 = add1(23, 56)
print(result3)
result4 = add1(b=34, a=40)
print(result4)
