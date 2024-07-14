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

# test_simple_calculator.py

class TestSimpleCalculator(unittest.TestCase):
    # ... (setUp method remains the same)

    def test_subtraction(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)  # 5 - 3 = 2
        self.assertEqual(self.calc.subtract(3, 5), -2)  # 3 - 5 = -2
        # Add more assertions to thoroughly test the subtract method:
        # - Test with large positive numbers
        # - Test with large negative numbers
        # - Test with zero
        # - Test with decimal numbers
        # - Test with mixed positive and negative numbers

    # Write similar test methods for multiply and divide
    # ...

if __name__ == "__main__":
    unittest.main()



