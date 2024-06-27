class Dog:
    name = None
    id = None
    def __init__(self, name = None, id = None):
        self.name = name
        self.id = id

    def sleep(self):
        print('sleeping'+ self.name)


d1 = Dog('Tom', 1)
d1.sleep()
d2 = Dog('Jerry', 2)
d2.sleep()
d3 = Dog()
print(d3.name, d3.id)



