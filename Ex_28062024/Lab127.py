class Car:
    name = None

    def __init__(self):
        public_var = "Public"  # Public variable
        self._protected_var = "Protected"  # Protected variable
        self.__private_var = "pass@123"  # Private variable

    def __private_method(self):
        print("This is a protected method")

    def print_name(self):
        self.__private_method()
        if self.__private_var == "123":
            print("This is a private method")
        print("This is a public method")


alto = Car()
alto.print_name()
# Accessing the private variable and method by outside is not possible
# alto.__private_method() # Not possible
