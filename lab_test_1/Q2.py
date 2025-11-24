# -----------------------------------------
# AI-GENERATED DOCUMENTATION VERSION
# -----------------------------------------

class Rectangle:
    """Represents a rectangle and provides methods 
    to calculate its area and perimeter."""

    def __init__(self, width, height):
        """Initialize rectangle with width and height."""
        self.width = width   # store width
        self.height = height # store height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height  # area formula

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)  # perimeter formula


# ----------- Taking Input --------------
w = float(input("Enter width of rectangle: "))
h = float(input("Enter height of rectangle: "))

rect = Rectangle(w, h)

print("AI Version:")
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())
