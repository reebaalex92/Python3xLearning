a = 12  # a  is a global variable.Declare outside the function


def f2():
    print(a)
    print(b)


b = 13  # b  is a global variable.Declare outside the function
f2()
