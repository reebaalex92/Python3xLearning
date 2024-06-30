class Car:
    name = None
    make = None
    model = None

    def __init__(self, o_name, o_make, o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self):
        print("Car Name is " + self.name)
        print("Car Make is " + self.make)
        print("Car Model is " + self.model)


c1 = Car("Corolla", "Toyota", "2015")
c1.start_engine()
print("*************")
c2 = Car("Verna", "Hyundai", "2014")
c2.start_engine()



