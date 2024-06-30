class MyClass:

    def __init__(self):
        self.name = "Reeba"
        self._email = "reeba123@gmail.com"

    def public_method(self):
        print("This is a public method")

    def __private_method(self):  # private method can be called using function within a class
        print("This is a private method")

    def public_method_2(self):
        self.__private_method()
        print(self._email)


obj = MyClass()
obj.public_method()
obj.public_method_2()  # used to call private method
