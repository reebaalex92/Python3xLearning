class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


print(Calculator(10, 5).add())
print(Calculator(10, 5).sub())
print(Calculator(10, 5).mul())
print(Calculator(10, 5).div())
