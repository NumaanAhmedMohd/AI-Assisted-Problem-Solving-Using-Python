# -----------------------------------------
# MANUAL DOCUMENTATION VERSION
# -----------------------------------------

class RectangleManual:
    """
    A simple Rectangle class used to calculate 
    the area and perimeter of a rectangle.
    """

    def __init__(self, width, height):
        """
        Creates a rectangle using width and height.
        """
        self.width = width      # assigning width
        self.height = height    # assigning height

    def area(self):
        """
        Calculates the total area inside the rectangle.
        Formula: width × height
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the total boundary length of the rectangle.
        Formula: 2 × (width + height)
        """
        return 2 * (self.width + self.height)


# ----------- Taking Input --------------
w = float(input("Enter width of rectangle: "))
h = float(input("Enter height of rectangle: "))

rect2 = RectangleManual(w, h)

print("\nManual Version:")
print("Area:", rect2.area())
print("Perimeter:", rect2.perimeter())
