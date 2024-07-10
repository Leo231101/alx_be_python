import unittest
from simple_calculator import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()
    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)  # 2 + 3 = 5
        self.assertEqual(self.calc.add(-1, 1), 0)  # -1 + 1 = 0
        # Add more assertions to thoroughly test the add method.
    def test_division(self):
        """Test the divide method."""
        # Normal division
        self.assertEqual(self.calc.divide(10, 2), 5)  # 10 / 2 = 5
        # Division by zero
        self.assertIsNone(self.calc.divide(5, 0))  # Should return None
