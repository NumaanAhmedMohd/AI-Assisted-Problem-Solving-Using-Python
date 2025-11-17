def sum_even_odd_ai_version(numbers):
    """
    Computes the sum of even and odd numbers from a list.
    
    Takes a list of integers and returns a tuple with the sum of all even numbers
    and the sum of all odd numbers respectively.
    
    Args:
        numbers (list): A list containing integer values to be summed.
    
    Returns:
        tuple: A tuple of two integers (even_sum, odd_sum) where even_sum is the
               sum of all even numbers and odd_sum is the sum of all odd numbers.
    
    Raises:
        TypeError: If input is not a list or contains non-integer elements.
        ValueError: If the list is empty.
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
