# Program to find the maximum of three numbers using if -else statement
num1 = int(input("Enter the first number\n"))
num2 = int(input("Enter the second number\n"))
num3 = int(input("Enter the third number\n"))
if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)