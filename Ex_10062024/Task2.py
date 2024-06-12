# Program to calculate the square and cube of a given number
import math

num = 2
square = math.pow(num, 2)
print(square)
cube = math.pow(num, 3)
print(cube)

#  program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("a is greater than b" if a > b else "a is less than b" if a < b else "a is equal to b")
