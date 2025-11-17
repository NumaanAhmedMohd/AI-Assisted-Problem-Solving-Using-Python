# ...existing code...
def is_prime(n: int) -> bool:

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

def reverse_string(s: str) -> str:
    """
    Return the reverse of the input string.
    Raises TypeError for non-string inputs.
    """
    if not isinstance(s, str):
        raise TypeError("reverse_string() requires a string")
    return s[::-1]
# ...existing code...

if __name__ == "__main__":
    choice = input("Choose (p)rime test or (r)everse string: ").strip().lower()
    if choice == "p":
        s = input("Enter an integer to test for primality: ").strip()
        try:
            n = int(s)
        except ValueError:
            print("Please enter a valid integer.")
        else:
            print(f"{n} is prime." if is_prime(n) else f"{n} is not prime.")
    elif choice == "r":
        s = input("Enter a string to reverse: ")
        print(reverse_string(s))
    else:
        print("Unknown option.")