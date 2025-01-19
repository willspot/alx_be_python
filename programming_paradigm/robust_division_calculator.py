# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Performs division with error handling for division by zero and non-numeric input."""
    try:
        # Convert inputs to floats to handle numeric values
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Perform division
        result = numerator / denominator
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        # Handle division by zero error
        return "Error: Cannot divide by zero."
    
    except ValueError:
        # Handle non-numeric input error
        return "Error: Please enter numeric values only."
