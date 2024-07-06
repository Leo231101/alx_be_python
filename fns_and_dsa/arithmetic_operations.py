# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations on two numbers.

    Args:
        num1 (float): First number.
        num2 (float): Second number.
        operation (str): Operation ('add', 'subtract', 'multiply', or 'divide').

    Returns:
        float: Result of the arithmetic operation.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"

# Example usage:
# result = perform_operation(5, 6, 'add')
# print(f"Result: {result}")
