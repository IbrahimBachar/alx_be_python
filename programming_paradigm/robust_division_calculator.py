def safe_divide(numerator: int, denominator: int):
    try:
        if denominator == 0:
            raise ZeroDivisionError
        return f"The result of the division is {int(numerator) / int(denominator)}"
    except ZeroDivisionError:
        print(f"Error: Cannot divide by zero.")
    
    except ValueError:
        print(f"Error: Please enter numeric values only.")