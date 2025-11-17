def get_element(lst, idx):
    """Return element at idx or handle IndexError and return None."""
    try:
        return lst[idx]
    except IndexError:
        print(f"IndexError: index {idx} out of range (list length {len(lst)})")
        return None

# Demonstration
numbers = [1, 2, 3]
print(get_element(numbers, 5))  # handled, prints error message then None
print(get_element(numbers, 2))  # prints 3

# Alternative safe access using bounds check
if len(numbers) > 5:
    print(numbers[5])
else:
    print(f"Safe-check: index 5 out of range, last element is {numbers[-1]}")
