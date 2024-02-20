import math
import statistics


class SimpleOps:
    def __init__(self):
        print("SimpleOperations instance created.")
        self.x = None
        self.y = None

    def __del__(self):
        print("SimpleOperations instance destroyed.")

    def set_values(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def mul(self):
        return self.x * self.y

    def divide(self):
        if self.y == 0:
            raise ValueError("Cannot divide by zero.")
        return self.x / self.y


class ComplexOps:
    def __init__(self):
        print("ComplexOperations instance created.")
        self.value = None
        self.data = None

    def __del__(self):
        print("ComplexOperations instance destroyed.")

    def set_value(self, value):
        self.value = value

    def set_data(self, data):
        self.data = data

    def sqrt(self):
        return math.sqrt(self.value)

    def cubert(self):
        return self.value ** (1 / 3)

    def std_deviation(self):
        return statistics.stdev(self.data)
