"""ShoppingCart class for managing items and calculating total cost."""

from typing import Dict, Union


class ShoppingCart:
    """A shopping cart that allows adding/removing items and calculating total cost.

    Items are stored with their prices. Multiple items with the same name
    increase the quantity count.
    """

    def __init__(self):
        """Initialize an empty shopping cart."""
        self._items: Dict[str, Dict[str, Union[int, float]]] = {}

    def add_item(self, name: str, price: Union[int, float]) -> None:
        """Add an item to the cart.

        Args:
            name: The name of the item (must be non-empty string).
            price: The price of the item (must be >= 0).

        Raises:
            TypeError: If name is not a string or price is not numeric.
            ValueError: If name is empty, price is negative, or invalid.

        Examples:
            >>> cart = ShoppingCart()
            >>> cart.add_item("apple", 1.50)
            >>> cart.add_item("banana", 0.99)
        """
        # Validate inputs
        if not isinstance(name, str):
            raise TypeError("Item name must be a string")
        if not name or name.isspace():
            raise ValueError("Item name cannot be empty or whitespace")
        if not isinstance(price, (int, float)) or isinstance(price, bool):
            raise TypeError("Price must be a number (int or float)")
        if price < 0:
            raise ValueError("Price cannot be negative")

        # Normalize name (keep original case but store consistently)
        normalized_name = name.strip()

        # Add or update item
        if normalized_name in self._items:
            # Item already exists, increment quantity
            self._items[normalized_name]["quantity"] += 1
            # Update price (in case different price is given)
            self._items[normalized_name]["price"] = price
        else:
            # New item
            self._items[normalized_name] = {
                "quantity": 1,
                "price": float(price)
            }

    def remove_item(self, name: str) -> None:
        """Remove an item from the cart.

        Removes the entire item entry (all quantities).

        Args:
            name: The name of the item to remove.

        Raises:
            TypeError: If name is not a string.
            ValueError: If the item does not exist in the cart.

        Examples:
            >>> cart = ShoppingCart()
            >>> cart.add_item("apple", 1.50)
            >>> cart.remove_item("apple")
        """
        # Validate input
        if not isinstance(name, str):
            raise TypeError("Item name must be a string")

        normalized_name = name.strip()

        if normalized_name not in self._items:
            raise ValueError(f"Item '{name}' not found in cart")

        del self._items[normalized_name]

    def total_cost(self) -> float:
        """Calculate the total cost of all items in the cart.

        Returns:
            float: Total cost of all items (sum of price * quantity for each item).

        Examples:
            >>> cart = ShoppingCart()
            >>> cart.add_item("apple", 1.50)
            >>> cart.add_item("apple", 1.50)
            >>> cart.total_cost()
            3.0
        """
        total = 0.0
        for item_info in self._items.values():
            total += item_info["price"] * item_info["quantity"]
        return round(total, 2)

    def get_items(self) -> Dict[str, Dict[str, Union[int, float]]]:
        """Return a copy of items in the cart (for testing/debugging).

        Returns:
            dict: A copy of the items dictionary.
        """
        return self._items.copy()

    def clear(self) -> None:
        """Clear all items from the cart."""
        self._items.clear()

    def __repr__(self) -> str:
        """Return a string representation of the cart."""
        return f"ShoppingCart({len(self._items)} items, total=${self.total_cost():.2f})"


if __name__ == '__main__':
    # Quick demo
    cart = ShoppingCart()
    cart.add_item("apple", 1.50)
    cart.add_item("banana", 0.99)
    cart.add_item("apple", 1.50)  # adds quantity
    print(cart)
    print(f"Total: ${cart.total_cost():.2f}")

    cart.remove_item("banana")
    print(f"After removing banana: ${cart.total_cost():.2f}")
