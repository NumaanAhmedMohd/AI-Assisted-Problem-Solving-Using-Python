def print_multiples_for(number: int) -> None:
    """
    Print the first 10 multiples of a given number using a for loop.
    
    Args:
        number: The number to find multiples of
    """
    print(f"\nFirst 10 multiples of {number} using for loop:")
    for i in range(1, 11):
        multiple = number * i
        print(f"{number} x {i} = {multiple}")


def print_multiples_while(number: int) -> None:
    """
    Print the first 10 multiples of a given number using a while loop.
    
    Args:
        number: The number to find multiples of
    """
    print(f"\nFirst 10 multiples of {number} using while loop:")
    i = 1
    while i <= 10:
        multiple = number * i
        print(f"{number} x {i} = {multiple}")
        i += 1


def print_multiples_do_while(number: int) -> None:
    """
    Print the first 10 multiples of a given number using a do-while style loop.
    Note: Python doesn't have a native do-while, so we simulate it.
    
    Args:
        number: The number to find multiples of
    """
    print(f"\nFirst 10 multiples of {number} using do-while style:")
    i = 1
    while True:
        multiple = number * i
        print(f"{number} x {i} = {multiple}")
        i += 1
        if i > 10:
            break