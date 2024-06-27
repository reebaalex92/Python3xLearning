class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


c = Calculator()
print(c.add(10, 5))
print(c.sub(10, 5))
print(c.mul(10, 5))
print(c.div(10, 5))
