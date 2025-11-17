
# Debug the following code
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print(f"Error: Cannot divide {a} by zero!")
        return None

# Test the function with safe error handling
print(divide(10, 0))  # This will now handle the error gracefully instead of crashing
print(divide(10, 2))  # This will work normally: 5.0

