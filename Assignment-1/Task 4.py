# ...existing code...
def factorial_recursive(n: int) -> int:

    if not isinstance(n, int):
        raise TypeError("factorial_recursive() requires an integer")
    if n < 0:
        raise ValueError("factorial_recursive() requires a non-negative integer")
    # Base case: 0! == 1! == 1
    if n <= 1:
        return 1
    # Recursive step
    return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:

    if not isinstance(n, int):
        raise TypeError("factorial_iterative() requires an integer")
    if n < 0:
        raise ValueError("factorial_iterative() requires a non-negative integer")
    result = 1
    # Multiply result by each integer from 2 through n
    for i in range(2, n + 1):
        result *= i
    return result
# ...existing code...

if __name__ == "__main__":
    # Prompt the user to choose recursive or iterative implementation
    choice = input("Choose factorial method — (r)ecursive or (i)terative [r/i]: ").strip().lower()

    # Prompt the user for the number to compute factorial of
    s = input("Enter a non-negative integer: ").strip()
    try:
        n = int(s)
    except ValueError:
        print("Please enter a valid integer.")
    else:
        if n < 0:
            print("Please enter a non-negative integer.")
        else:
            # Call the selected implementation and print the result
            if choice in ("r", "recursive"):
                print(f"{n}! = {factorial_recursive(n)}")
            else:
                print(f"{n}! = {factorial_iterative(n)}")