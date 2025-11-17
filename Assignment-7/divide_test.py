def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: division by zero")
        return None

# Demonstration
print(divide(10, 0))  # should not raise; prints error message and then None
print(divide(10, 2))  # should print 5.0
