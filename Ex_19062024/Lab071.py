# Function scope
def my_function():
    x = 10  # Local variable
    local_var = 20
    print("Inside the function")
    print(x)
    print(local_var)


# print(x) # name 'x' is not defined
my_function()
