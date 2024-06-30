# Encapsulation
# Binding  the data variables with the methods
# Data variables - instance variables
# Methods - instance methods

# Hide the data variables(class variables or instance variables ) only using the methods.

class Car:
    name = None
    password = "123"

    def __init__(self):
        print("I am called when object is created")


    def change_password(self):
        self.password = "456"


c1 = Car()
c1.password = "456"  # Modifying the instance variable is possible here so by using encapsulation it is not possible.It can be possible by calling the method.
print(c1.password)
