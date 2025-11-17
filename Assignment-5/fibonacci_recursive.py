"""fibonacci_recursive.py

Recursive Fibonacci implementation and an optional memoized version.

Provides:
- fib(n): plain recursive implementation (0-based: fib(0)=0, fib(1)=1)
- fib_memo(n): memoized version for efficiency

Includes input validation, comments, and a tiny CLI demo.
"""

from typing import Dict


def fib(n: int) -> int:
    """Compute the n-th Fibonacci number using plain recursion.

    Args:
        n: Non-negative integer index (0-based). fib(0)=0, fib(1)=1.

    Returns:
        The n-th Fibonacci number as an integer.

    Raises:
        TypeError: if n is not an integer.
        ValueError: if n is negative.

    Note:
        This implementation uses plain recursion and has exponential time
        complexity O(2^n). It is educational but not suitable for large n.
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError('n must be an integer')
    if n < 0:
        raise ValueError('n must be non-negative')

    # Base cases: directly return for n==0 and n==1
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive case: fib(n) = fib(n-1) + fib(n-2)
    # Each call splits into two recursive calls until base cases.
    return fib(n - 1) + fib(n - 2)


def fib_memo(n: int, cache: Dict[int, int] = None) -> int:
    """Compute the n-th Fibonacci number using recursion with memoization.

    Args:
        n: Non-negative integer index (0-based).
        cache: optional dict used to store previously computed values.

    Returns:
        The n-th Fibonacci number as an integer.

    Raises:
        TypeError: if n is not an integer.
        ValueError: if n is negative.

    This version stores intermediate results in `cache` to reduce time
    complexity to O(n) and space O(n) due to the cache.
    """
    if not isinstance(n, int):
        raise TypeError('n must be an integer')
    if n < 0:
        raise ValueError('n must be non-negative')

    if cache is None:
        cache = {}

    # If we already computed fib(n), return it to avoid repeated work
    if n in cache:
        return cache[n]

    # Base cases
    if n == 0:
        cache[0] = 0
        return 0
    if n == 1:
        cache[1] = 1
        return 1

    # Compute and store the result
    result = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    cache[n] = result
    return result


if __name__ == '__main__':
    # Demo: print fib(0..10)
    for i in range(11):
        print(f'fib({i}) = {fib(i)}')

    # Show memoized version for a larger n
    print('fib_memo(30) =', fib_memo(30))
