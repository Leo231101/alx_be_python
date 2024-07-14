# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # Write your test methods here
    # ...

if __name__ == "__main__":
    unittest.main()
# test_simple_calculator.py

class TestSimpleCalculator(unittest.TestCase):
    # ... (setUp method remains the same)

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)  # 2 + 3 = 5
        self.assertEqual(self.calc.add(-1, 1), 0)  # -1 + 1 = 0
        # Add more assertions to thoroughly test the add method:
        # - Test with large positive numbers
        # - Test with large negative numbers
        # - Test with zero
        # - Test with decimal numbers
        # - Test with mixed positive and negative numbers

    # Write similar test methods for subtract, multiply, and divide
    # ...

if __name__ == "__main__":
    unittest.main()




