import unittest
from simple_calculator import SimpleCalculator 

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc= SimpleCalculator
    def test_addition(self):
        self.assertEqual(self.calc.add(5,3),8)
        self.assertEqual(self.calc.add(-1, 1), 0)
    def test_sub(self):
        self.assertEqual(self.calc.subtract(5,3),2)
    def test_mul(self):
        self.assertEqual(self.calc.multiply(5,5),25)
    def test_divide(self):
        self.assertEqual(self.calc.divide(5,5),1)
            


