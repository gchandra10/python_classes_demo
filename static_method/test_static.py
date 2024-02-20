import unittest
from SimpleOperations import *
from ComplexOperations import *


class TestCalculator(unittest.TestCase):
    def test_simple_operations(self):
        self.assertEqual(SimpleOperations.add(1, 2), 3)
        self.assertEqual(SimpleOperations.sub(5, 3), 2)
        self.assertEqual(SimpleOperations.mul(2, 3), 6)
        self.assertRaises(ValueError, SimpleOperations.divide, 10, 0)
        self.assertAlmostEqual(SimpleOperations.divide(10, 4), 2.5)

    def test_complex_operations(self):
        self.assertAlmostEqual(ComplexOperations.sqrt(16), 4)
        self.assertAlmostEqual(ComplexOperations.cubert(27), 3)
        self.assertAlmostEqual(
            ComplexOperations.std_deviation([10, 12, 23, 23, 16]), 6.058052492344384
        )


if __name__ == "__main__":
    unittest.main()
