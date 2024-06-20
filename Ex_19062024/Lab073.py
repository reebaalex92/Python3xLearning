# Function within a function
def outer_function():
    var1 = 10

    def inner_function():
        print(var1)

    inner_function()


outer_function()
