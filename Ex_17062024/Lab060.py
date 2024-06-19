def f1(a, b, c):
    return a + b + c
    # print("Hello")  # print after return in a function is not printed but printed when outside the function


print("hello world")

result = f1(2, 3, 4)
result1 = f1(b=4, a=5, c=6)
print(result)
print(result1)
