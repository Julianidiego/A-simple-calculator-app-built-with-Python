import unittest
from calculator import add, subtract, multiply, divide, power, square_root, modulo

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)
        
    def test_multiply(self):
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)
        
    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(-6, 3), -2)
        self.assertEqual(divide(0, 5), 0)
        self.assertEqual(divide(5, 0), "Error: Division by zero")
        
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(2, 0), 1)
        self.assertEqual(power(0, 0), 1)
        
    def test_square_root(self):
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(-1), "Error: Cannot calculate square root of negative number")
        
    def test_modulo(self):
        self.assertEqual(modulo(7, 3), 1)
        self.assertEqual(modulo(0, 5), 0)
        self.assertEqual(modulo(5, 0), "Error: Division by zero")

if __name__ == "__main__":
    unittest.main()
