import unittest
from main import Calculator, CalculatorTypeError, CalculatorDivideByZeroError


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)

    def test_divide(self):
        self.assertEqual(self.calc.divide(8, 2), 4)

    def test_divide_by_zero(self):
        with self.assertRaises(CalculatorDivideByZeroError):
            self.calc.divide(5, 0)

    def test_wrong_types(self):
        # строки
        with self.assertRaises(CalculatorTypeError):
            self.calc.add("2", 3)
        # список
        with self.assertRaises(CalculatorTypeError):
            self.calc.subtract([1, 2], 3)
        # None
        with self.assertRaises(CalculatorTypeError):
            self.calc.multiply(None, 3)
        # булевы значения
        with self.assertRaises(CalculatorTypeError):
            self.calc.add(True, 5)


if __name__ == "__main__":
    unittest.main()
