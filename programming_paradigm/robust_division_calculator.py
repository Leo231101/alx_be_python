# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, handling potential errors.

    Args:
        numerator (str or float): Numerator value.
        denominator (str or float): Denominator value.

    Returns:
        str: Result of division or an error message.
    """
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
        return f"The result of the division is {result:.2f}"
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

# Example usage:
if __name__ == "__main__":
    print(safe_divide(10, 5))  # Normal division
    print(safe_divide(10, 0))  # Division by zero
    print(safe_divide("ten", 5))  # Non-numeric input

    # main.py

import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()

