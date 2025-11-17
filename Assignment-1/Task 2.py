# ...existing code...
def is_prime(n: int) -> bool:
    """
    Return True if n is a prime number, otherwise False.
    Raises TypeError for non-integer inputs.
    """
    if not isinstance(n, int):
        raise TypeError("is_prime() requires an integer")
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
# ...existing code...

if __name__ == "__main__":
    s = input("Enter an integer to test for primality: ").strip()
    try:
        n = int(s)
    except ValueError:
        print("Please enter a valid integer.")
    else:
        print(f"{n} is prime." if is_prime(n) else f"{n} is not prime.")