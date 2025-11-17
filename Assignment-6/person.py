class Person:
    """Simple Person class with constructor and display_details() method."""

    def __init__(self, name: str, age: int, email: str | None = None):
        """Initialize a Person.

        Args:
            name: Person's name.
            age: Person's age (int).
            email: Optional email address.
        """
        self.name = name
        self.age = age
        self.email = email

    def display_details(self) -> str:
        """Return a formatted string with the person's details."""
        parts = [f"Name: {self.name}", f"Age: {self.age}"]
        if self.email:
            parts.append(f"Email: {self.email}")
        return "\n".join(parts)
