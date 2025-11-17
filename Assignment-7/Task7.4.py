# Faulty class definition - missing 'self' parameter in __init__
class Rectangle:
    def __init__(length, width):  # ERROR: Missing 'self' parameter
        self.length = length
        self.width = width

# This will cause a TypeError when trying to create an instance:
# rect = Rectangle(5, 3)  # TypeError: __init__() takes 2 positional arguments but 3 were given


# ============================================================================
# CORRECTED VERSION - Proper class definition with 'self' parameter
# ============================================================================
