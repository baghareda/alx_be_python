def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        res = num / denom
        return f"the redult of the division is: {res}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."