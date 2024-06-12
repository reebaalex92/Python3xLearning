# Score of a student is given in range
# 0-100
# 90-100 -> A
# 80-89 -> B
# 70-79 -> C
# 60-69 -> D
# <60 -> F
# Take input of marks from the user and print the grade.
marks = int(input("Enter your marks: "))
if marks >= 90 and marks <= 100:
    print("A")
elif marks >= 80 and marks <= 89:
    print("B")
elif marks >= 70 and marks <= 79:
    print("C")
elif marks >= 60 and marks <= 69:
    print("D")
elif marks < 60:
    print("F")
else:
    print("Invalid marks")
