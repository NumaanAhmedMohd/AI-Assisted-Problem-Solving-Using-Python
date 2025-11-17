def sum_even_odd(numbers):
    """Calculate the sum of even and odd numbers in a given list.
    
    This function takes a list of numbers and separately computes the sum of all
    even numbers and the sum of all odd numbers, returning both values as a tuple.
    
    Args:
        numbers (list): A list of integers to be processed.
    
    Returns:
        tuple: A tuple containing two integers (sum_of_evens, sum_of_odds).
               The first element is the sum of all even numbers in the list.
               The second element is the sum of all odd numbers in the list.
    
    Raises:
        TypeError: If the input is not a list or contains non-integer values.
        ValueError: If the list is empty.
    
    Examples:
        >>> sum_even_odd([1, 2, 3, 4, 5, 6])
        (12, 9)
        >>> sum_even_odd([2, 4, 6, 8])
        (20, 0)
        >>> sum_even_odd([1, 3, 5, 7])
        (0, 16)
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    if len(numbers) == 0:
        raise ValueError("List cannot be empty")
    
    for num in numbers:
        if not isinstance(num, int):
            raise TypeError("All elements in the list must be integers")
    
    sum_even = 0
    sum_odd = 0
    
    for num in numbers:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
    
    return (sum_even, sum_odd)


# Test cases
if __name__ == "__main__":
    # Test case 1: Mixed even and odd numbers
    test1 = [1, 2, 3, 4, 5, 6]
    print(f"Input: {test1}")
    print(f"Output: {sum_even_odd(test1)}")
    print(f"Expected: (12, 9)\n")
    
    # Test case 2: All even numbers
    test2 = [2, 4, 6, 8]
    print(f"Input: {test2}")
    print(f"Output: {sum_even_odd(test2)}")
    print(f"Expected: (20, 0)\n")
    
    # Test case 3: All odd numbers
    test3 = [1, 3, 5, 7]
    print(f"Input: {test3}")
    print(f"Output: {sum_even_odd(test3)}")
    print(f"Expected: (0, 16)\n")
