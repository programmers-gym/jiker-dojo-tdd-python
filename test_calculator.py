import unittest

from calculator import Calculator


class CalculatorTest(unittest.TestCase):
    def test_should_be_2_if_calculator_add_1_and_1(self):
        calculator = Calculator()

        result = calculator.add(1, 1)

        self.assertEqual(2, result)


if __name__ == '__main__':
    unittest.main()
