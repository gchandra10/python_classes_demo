import math
import statistics


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
