from typing import Callable
import time


def sum_to_n_for(n: int) -> int:
    """
    Calculate sum of first n natural numbers using a for loop.
    
    Args:
        n: The upper limit of numbers to sum (inclusive)
        
    Returns:
        int: Sum of numbers from 1 to n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def sum_to_n_while(n: int) -> int:
    """
    Calculate sum of first n natural numbers using a while loop.
    
    Args:
        n: The upper limit of numbers to sum (inclusive)
        
    Returns:
        int: Sum of numbers from 1 to n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total


def sum_to_n_formula(n: int) -> int:
    """
    Calculate sum of first n natural numbers using mathematical formula: n * (n + 1) / 2
    
    Args:
        n: The upper limit of numbers to sum (inclusive)
        
    Returns:
        int: Sum of numbers from 1 to n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    return n * (n + 1) // 2  # Using integer division for exact result


def time_function(func: Callable[[int], int], n: int, iterations: int = 1000) -> float:
    """
    Measure the average execution time of a function over multiple iterations.
    
    Args:
        func: Function to measure
        n: Input value for the function
        iterations: Number of times to run the function
        
    Returns:
        float: Average execution time in milliseconds
    """
    start = time.perf_counter()
    for _ in range(iterations):
        func(n)
    end = time.perf_counter()
    return (end - start) * 1000 / iterations  # Convert to milliseconds