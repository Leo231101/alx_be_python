# match_case_calculator.py

def main():
    try:
        # Prompt the user to enter two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Prompt the user to choose an operation
        operation = input("Choose the operation (+, -, *, /): ").strip()
        
        # Perform the calculation using a match statement
        match operation:
            case "+":
                result = num1 + num2
                print(f"The result is {result}.")
            case "-":
                result = num1 - num2
                print(f"The result is {result}.")
            case "*":
                result = num1 * num2
                print(f"The result is {result}.")
            case "/":
                if num2 != 0:
                    result = num1 / num2
                    print(f"The result is {result}.")
                else:
                    print("Cannot divide by zero.")
            case _:
                print("Invalid operation. Please choose from +, -, *, /.")
    except ValueError:
        print("Invalid input. Please enter numeric values for the numbers.")

# Ensures that the main function runs when the script is executed
if __name__ == "__main__":
    main()
