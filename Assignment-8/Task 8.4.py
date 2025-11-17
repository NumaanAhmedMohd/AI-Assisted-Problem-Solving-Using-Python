
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        if not isinstance(name, str) or not isinstance(price, (int, float)) or price < 0:
            return "Invalid input"
        self.items[name] = price
        return f"Added {name} for ₹{price}"

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            return f"Removed {name}"
        else:
            return "Item not found"

    def total_cost(self):
        return sum(self.items.values())

# 🧪 AI-generated test cases
def run_tests():
    cart = ShoppingCart()

    print("🧪 Test 1: Add valid items")
    cart.add_item("Apple", 30)
    cart.add_item("Banana", 10)
    cart.add_item("Milk", 50)
    print("Expected total: 90 →", "✅ Passed" if cart.total_cost() == 90 else "❌ Failed")

    print("\n🧪 Test 2: Remove an item")
    cart.remove_item("Banana")
    print("Expected total: 80 →", "✅ Passed" if cart.total_cost() == 80 else "❌ Failed")

    print("\n🧪 Test 3: Remove non-existent item")
    result = cart.remove_item("Bread")
    print("Expected: 'Item not found' →", "✅ Passed" if result == "Item not found" else "❌ Failed")

    print("\n🧪 Test 4: Add item with invalid price")
    result = cart.add_item("Eggs", -20)
    print("Expected: 'Invalid input' →", "✅ Passed" if result == "Invalid input" else "❌ Failed")

    print("\n🧪 Test 5: Add item with invalid name type")
    result = cart.add_item(123, 20)
    print("Expected: 'Invalid input' →", "✅ Passed" if result == "Invalid input" else "❌ Failed")

    print("\n🧪 Test 6: Add duplicate item (should overwrite)")
    cart.add_item("Apple", 40)
    print("Expected total: 90 →", "✅ Passed" if cart.total_cost() == 90 else "❌ Failed")

    print("\n🧪 Test 7: Empty cart")
    empty_cart = ShoppingCart()
    print("Expected total: 0 →", "✅ Passed" if empty_cart.total_cost() == 0 else "❌ Failed")

# 🧑‍💻 Interactive user input
def user_interface():
    cart = ShoppingCart()
    print("\n🛒 Welcome to the Shopping Cart!")
    while True:
        print("\nChoose an option:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View total cost")
        print("4. Exit")
        choice = input("Enter your choice (1–4): ")

        if choice == "1":
            name = input("Enter item name: ")
            try:
                price = float(input("Enter item price: "))
            except ValueError:
                print("❌ Invalid price format.")
                continue
            print(cart.add_item(name, price))

        elif choice == "2":
            name = input("Enter item name to remove: ")
            print(cart.remove_item(name))

        elif choice == "3":
            print(f"🧾 Total cost: ₹{cart.total_cost()}")

        elif choice == "4":
            print("👋 Exiting. Thank you for shopping!")
            break

        else:
            print("❌ Invalid choice. Please select 1–4.")

# Run tests and start user interface
if __name__ == "__main__":
    run_tests()
    user_interface()
