# *args - multiple arguments
print("Arjun", "Alan", "Sneha")


def add(a=1, b=10, c=5):
    return a + b + c


result1 = add()
result2 = add(10)
result3 = add(10, 20)
result4 = add(a=10, b=20, c=30)
result5 = add(b=10, a=20, c=30)
print(result1, result2, result3, result4, result5)
