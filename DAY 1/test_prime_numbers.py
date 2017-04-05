import unittest
from CalculatePrime import PrimeNum


class PrimeNumbersTestCase(unittest.TestCase):
    def SetUp(self):
        self.number = CalcPrime()

    def test_is_not_zero_or_one(self):
        self.assertIn(self.number, [0, 1], msg='0 and 1 are not prime numbers')

    def test_is_input_positive(self):
        self.assertIsInstance(self.number, int)

    def test__returns_error_message_if__args_not_numbers(self):
        self.assertRaises(ValueError, self.number, str)

if __name__ == '__main__':
    unittest.main()
