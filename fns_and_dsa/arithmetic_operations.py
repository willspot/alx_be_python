def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform basic arithmetic operations based on the given operation.
    
    Parameters:
    - num1: The first number (float).
    - num2: The second number (float).
    - operation: A string that specifies the operation ('add', 'subtract', 'multiply', 'divide').

    Returns:
    - The result of the operation (float), or an error message for invalid operations or division by zero.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        else:
            return num1 / num2
    else:
        return "Invalid operation"
