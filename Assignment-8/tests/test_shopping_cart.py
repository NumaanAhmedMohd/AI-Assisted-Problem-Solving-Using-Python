import unittest

from shopping_cart import ShoppingCart


class TestShoppingCart(unittest.TestCase):
    """Test cases for ShoppingCart class."""

    def setUp(self):
        """Create a fresh cart for each test."""
        self.cart = ShoppingCart()

    # ============ add_item tests ============
    def test_add_single_item(self):
        """Add a single item to the cart."""
        self.cart.add_item("apple", 1.50)
        items = self.cart.get_items()
        self.assertIn("apple", items)
        self.assertEqual(items["apple"]["quantity"], 1)
        self.assertEqual(items["apple"]["price"], 1.50)

    def test_add_multiple_different_items(self):
        """Add multiple different items."""
        self.cart.add_item("apple", 1.50)
        self.cart.add_item("banana", 0.99)
        self.cart.add_item("orange", 2.00)
        items = self.cart.get_items()
        self.assertEqual(len(items), 3)

    def test_add_duplicate_item_increases_quantity(self):
        """Adding duplicate item increases quantity, not creates new entry."""
        self.cart.add_item("apple", 1.50)
        self.cart.add_item("apple", 1.50)
        items = self.cart.get_items()
        self.assertEqual(len(items), 1)
        self.assertEqual(items["apple"]["quantity"], 2)

    def test_add_item_with_int_price(self):
        """Add item with integer price."""
        self.cart.add_item("milk", 5)
        items = self.cart.get_items()
        self.assertEqual(items["milk"]["price"], 5.0)

    def test_add_item_with_float_price(self):
        """Add item with float price."""
        self.cart.add_item("bread", 2.99)
        items = self.cart.get_items()
        self.assertEqual(items["bread"]["price"], 2.99)

    def test_add_item_with_zero_price(self):
        """Add item with zero price (free item)."""
        self.cart.add_item("sample", 0)
        items = self.cart.get_items()
        self.assertEqual(items["sample"]["price"], 0.0)

    def test_add_item_with_very_small_price(self):
        """Add item with very small price."""
        self.cart.add_item("candy", 0.01)
        items = self.cart.get_items()
        self.assertEqual(items["candy"]["price"], 0.01)

    def test_add_item_with_very_large_price(self):
        """Add item with very large price."""
        self.cart.add_item("diamond", 10000.00)
        items = self.cart.get_items()
        self.assertEqual(items["diamond"]["price"], 10000.00)

    def test_add_item_name_with_spaces(self):
        """Add item with spaces in name."""
        self.cart.add_item("green apple", 1.75)
        items = self.cart.get_items()
        self.assertIn("green apple", items)

    def test_add_item_invalid_name_type(self):
        """Adding item with non-string name raises TypeError."""
        with self.assertRaises(TypeError):
            self.cart.add_item(123, 1.50)

    def test_add_item_invalid_price_type_string(self):
        """Adding item with string price raises TypeError."""
        with self.assertRaises(TypeError):
            self.cart.add_item("apple", "1.50")

    def test_add_item_invalid_price_type_none(self):
        """Adding item with None price raises TypeError."""
        with self.assertRaises(TypeError):
            self.cart.add_item("apple", None)

    def test_add_item_invalid_price_negative(self):
        """Adding item with negative price raises ValueError."""
        with self.assertRaises(ValueError):
            self.cart.add_item("apple", -1.50)

    def test_add_item_empty_name(self):
        """Adding item with empty name raises ValueError."""
        with self.assertRaises(ValueError):
            self.cart.add_item("", 1.50)

    def test_add_item_whitespace_only_name(self):
        """Adding item with whitespace-only name raises ValueError."""
        with self.assertRaises(ValueError):
            self.cart.add_item("   ", 1.50)

    def test_add_item_boolean_as_price(self):
        """Adding item with boolean price raises TypeError."""
        with self.assertRaises(TypeError):
            self.cart.add_item("apple", True)

    # ============ remove_item tests ============
    def test_remove_existing_item(self):
        """Remove an item that exists in the cart."""
        self.cart.add_item("apple", 1.50)
        self.cart.remove_item("apple")
        items = self.cart.get_items()
        self.assertNotIn("apple", items)

    def test_remove_item_from_empty_cart(self):
        """Removing from empty cart raises ValueError."""
        with self.assertRaises(ValueError):
            self.cart.remove_item("apple")

    def test_remove_nonexistent_item(self):
        """Removing non-existent item raises ValueError."""
        self.cart.add_item("apple", 1.50)
        with self.assertRaises(ValueError):
            self.cart.remove_item("banana")

    def test_remove_item_with_multiple_quantities(self):
        """Removing item removes all quantities."""
        self.cart.add_item("apple", 1.50)
        self.cart.add_item("apple", 1.50)
        self.assertEqual(self.cart.get_items()["apple"]["quantity"], 2)
        self.cart.remove_item("apple")
        items = self.cart.get_items()
        self.assertNotIn("apple", items)

    def test_remove_item_invalid_type(self):
        """Removing item with non-string name raises TypeError."""
        with self.assertRaises(TypeError):
            self.cart.remove_item(123)

    def test_remove_item_none(self):
        """Removing item with None name raises TypeError."""
        with self.assertRaises(TypeError):
            self.cart.remove_item(None)

    def test_remove_one_of_multiple_items(self):
        """Removing one item doesn't affect others."""
        self.cart.add_item("apple", 1.50)
        self.cart.add_item("banana", 0.99)
        self.cart.add_item("orange", 2.00)
        self.cart.remove_item("banana")
        items = self.cart.get_items()
        self.assertEqual(len(items), 2)
        self.assertIn("apple", items)
        self.assertIn("orange", items)
        self.assertNotIn("banana", items)

    # ============ total_cost tests ============
    def test_total_cost_empty_cart(self):
        """Total cost of empty cart is 0."""
        self.assertEqual(self.cart.total_cost(), 0.0)

    def test_total_cost_single_item(self):
        """Total cost with single item."""
        self.cart.add_item("apple", 1.50)
        self.assertEqual(self.cart.total_cost(), 1.50)

    def test_total_cost_multiple_items(self):
        """Total cost with multiple different items."""
        self.cart.add_item("apple", 1.50)
        self.cart.add_item("banana", 0.99)
        self.cart.add_item("orange", 2.00)
        expected = 1.50 + 0.99 + 2.00
        self.assertEqual(self.cart.total_cost(), expected)

    def test_total_cost_duplicate_items(self):
        """Total cost correctly multiplies quantity."""
        self.cart.add_item("apple", 1.50)
        self.cart.add_item("apple", 1.50)
        self.assertEqual(self.cart.total_cost(), 3.00)

    def test_total_cost_multiple_quantities_mixed(self):
        """Total cost with mixed quantities."""
        self.cart.add_item("apple", 1.50)
        self.cart.add_item("apple", 1.50)
        self.cart.add_item("banana", 0.99)
        self.cart.add_item("banana", 0.99)
        self.cart.add_item("banana", 0.99)
        expected = (1.50 * 2) + (0.99 * 3)
        self.assertAlmostEqual(self.cart.total_cost(), expected, places=2)

    def test_total_cost_with_zero_price_item(self):
        """Total cost includes zero-price items."""
        self.cart.add_item("sample", 0.0)
        self.cart.add_item("apple", 1.50)
        self.assertEqual(self.cart.total_cost(), 1.50)

    def test_total_cost_float_precision(self):
        """Total cost handles float precision correctly."""
        self.cart.add_item("item1", 0.1)
        self.cart.add_item("item2", 0.2)
        # 0.1 + 0.2 in float arithmetic can have precision issues
        total = self.cart.total_cost()
        self.assertAlmostEqual(total, 0.3, places=2)

    def test_total_cost_large_quantities(self):
        """Total cost with large quantities."""
        self.cart.add_item("item", 0.01)
        for _ in range(1000):
            self.cart.add_item("item", 0.01)
        # Due to float accumulation, use places=1 for looser tolerance
        self.assertAlmostEqual(self.cart.total_cost(), 10.00, places=1)

    def test_total_cost_after_removal(self):
        """Total cost updates after item removal."""
        self.cart.add_item("apple", 1.50)
        self.cart.add_item("banana", 0.99)
        self.assertEqual(self.cart.total_cost(), 2.49)
        self.cart.remove_item("banana")
        self.assertEqual(self.cart.total_cost(), 1.50)

    def test_total_cost_after_clear(self):
        """Total cost after clearing cart."""
        self.cart.add_item("apple", 1.50)
        self.cart.add_item("banana", 0.99)
        self.cart.clear()
        self.assertEqual(self.cart.total_cost(), 0.0)

    # ============ Integration tests ============
    def test_workflow_add_remove_total(self):
        """Complete workflow: add, remove, calculate total."""
        self.cart.add_item("apple", 1.50)
        self.cart.add_item("banana", 0.99)
        self.cart.add_item("apple", 1.50)
        self.assertEqual(self.cart.total_cost(), 3.99)
        self.cart.remove_item("banana")
        self.assertEqual(self.cart.total_cost(), 3.00)

    def test_multiple_operations_sequence(self):
        """Test multiple operations in sequence."""
        # Build cart
        self.cart.add_item("apple", 1.50)
        self.cart.add_item("banana", 0.99)
        self.cart.add_item("orange", 2.00)
        self.assertEqual(len(self.cart.get_items()), 3)
        # Add more quantities
        self.cart.add_item("apple", 1.50)
        self.assertEqual(self.cart.get_items()["apple"]["quantity"], 2)
        # Check total
        total = self.cart.total_cost()
        self.assertGreater(total, 0)
        # Remove one
        self.cart.remove_item("banana")
        self.assertEqual(len(self.cart.get_items()), 2)

    def test_repr_string(self):
        """Test string representation."""
        self.cart.add_item("apple", 1.50)
        self.cart.add_item("banana", 0.99)
        repr_str = repr(self.cart)
        self.assertIn("ShoppingCart", repr_str)
        self.assertIn("2 items", repr_str)

    # ============ Edge cases ============
    def test_add_item_name_with_leading_trailing_spaces(self):
        """Item names with leading/trailing spaces are normalized."""
        self.cart.add_item("  apple  ", 1.50)
        self.cart.add_item("apple", 1.50)
        # Should be treated as same item (merged)
        items = self.cart.get_items()
        self.assertEqual(len(items), 1)
        self.assertEqual(items["apple"]["quantity"], 2)

    def test_total_cost_precision_rounding(self):
        """Total cost is rounded to 2 decimal places."""
        self.cart.add_item("item", 0.333)
        total = self.cart.total_cost()
        # Should be rounded to 2 decimals
        self.assertEqual(total, 0.33)


if __name__ == '__main__':
    unittest.main()
