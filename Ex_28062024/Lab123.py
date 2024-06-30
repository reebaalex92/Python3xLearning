class Person:
    name = "John"
    age = None

    def walk(self):
        a = 10 # Local Variable
        print("I am walking")
        print("Hi", self.age)


p = Person()
p.walk()
