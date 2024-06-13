# Program to check given year is leap year or not
leap_year = 2024
if leap_year%4 == 0 and leap_year%100 != 0 or leap_year%400 == 0:
    print("Leap year")
else:
    print("Not a leap year")

# Write a program that classifies a triangle based on its side lengths.
side1 = int(input("Enter the length of side 1: "))
side2 = int(input("Enter the length of side 2: "))
side3 = int(input("Enter the length of side 3: "))
if side1 == side2 and side2 == side3:
    print("Equilateral triangle")
elif side1 == side2 or side2  == side3 or side1 == side3:
    print("Isosceles triangle")
else:
    print("Scalene triangle")

# 3. Factorial
# n = 5
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 24
n = 5
fact = 1
for i in range(1, n+1):
    fact = fact * i
print(fact)
n = 3
fact = 1
for i in range(1, n+1):
    fact = fact * i
print(fact)
n = 4
fact = 1
for i in range(1, n+1):
    fact = fact * i
    print(fact)







