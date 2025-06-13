import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = SimpleCalculator()
        
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(1000, 0), 1000)
        self.assertEqual(self.calc.add(2, 2), 4)
        
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(1000, 0), 1000)
        self.assertEqual(self.calc.subtract(2, 2), 0)
        
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        self.assertEqual(self.calc.multiply(1000, 0), 0)
        self.assertEqual(self.calc.multiply(-2, -2), 4)
        
    def test_dividing(self):
        self.assertEqual(self.calc.divide(2, 1), 2)
        self.assertEqual(self.calc.divide(0, 1), 0)
        self.assertEqual(self.calc.divide(1000, 0), None)
        self.assertEqual(self.calc.divide(2, 2), 1)


    