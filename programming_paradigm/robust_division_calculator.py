# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)

        # Handle division by zero
        if denominator == 0:
            return "Error: Cannot divide by zero."

        # Perform the division
        result = numerator / denominator
        return f"The result of the division is {result:.2f}"
    except ValueError:
        return "Error: Please enter numeric values only."

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


