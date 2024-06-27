class Student:

    def __init__(self):
        self.name = input("Enter name:")
        self.age = input("Enter age:")

    def show(self):
        print(f'Name is {self.name} and Age is {self.age}')


Student().show()
