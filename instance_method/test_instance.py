import unittest
from MathClasses import SimpleOps, ComplexOps


class TestSimpleOps(unittest.TestCase):
    def setUp(self):
        self.simple_ops = SimpleOps()

    def test_add(self):
        self.simple_ops.set_values(10, 5)
        self.assertEqual(self.simple_ops.add(), 15)

    def test_sub(self):
        self.simple_ops.set_values(10, 5)
        self.assertEqual(self.simple_ops.sub(), 5)

    def test_mul(self):
        self.simple_ops.set_values(10, 5)
        self.assertEqual(self.simple_ops.mul(), 50)

    def test_divide(self):
        self.simple_ops.set_values(10, 5)
        self.assertEqual(self.simple_ops.divide(), 2)
        self.simple_ops.set_values(10, 0)
        with self.assertRaises(ValueError):
            self.simple_ops.divide()


class TestComplexOps(unittest.TestCase):
    def setUp(self):
        self.complex_ops = ComplexOps()

    def test_sqrt(self):
        self.complex_ops.set_value(16)
        self.assertEqual(self.complex_ops.sqrt(), 4)

    def test_cubert(self):
        self.complex_ops.set_value(27)
        self.assertAlmostEqual(self.complex_ops.cubert(), 3)

    def test_std_deviation(self):
        self.complex_ops.set_data([10, 12, 23, 23, 16])
        self.assertAlmostEqual(
            self.complex_ops.std_deviation(), 6.058052492344384
        )  # Example std deviation


if __name__ == "__main__":
    unittest.main()
