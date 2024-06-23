# Decorators
def my_decorator(func):
    def wrapper():
        print("************")
        print("Welcome")
        func()
        print("Good Bye")
        print("************")

    return wrapper()


@my_decorator
def say_hello():
    print("Have a nice day")
