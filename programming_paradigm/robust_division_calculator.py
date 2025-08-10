def safe_divide(numerator, denominator):
    try:
        if denominator == 0:
            raise ZeroDivisionError
        return f"The result of the division is {float(numerator) / float(denominator)}"
    except ZeroDivisionError:
        print(f"Error: Cannot divide by zero.")
    
    except ValueError:
        print(f"Error: Please enter numeric values only.")