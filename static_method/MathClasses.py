import math
import statistics


class SimpleOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def sub(x, y):
        return x - y

    @staticmethod
    def mul(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        return x / y


class ComplexOperations:
    @staticmethod
    def sqrt(x):
        return math.sqrt(x)

    @staticmethod
    def cubert(x):
        return x ** (1 / 3)

    @staticmethod
    def std_deviation(data):
        return statistics.stdev(data)
