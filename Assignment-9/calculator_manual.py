"""
calculator_manual.py
Manual implementation of a simple calculator module with NumPy-style docstrings.

This module provides four basic arithmetic functions: add, subtract, multiply,
and divide. Each function includes a NumPy-style docstring written manually,
including parameter types, return types, examples, and raised exceptions where
appropriate.
"""

from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """
    Add two numbers.

    Parameters
    ----------
    a : int or float
        First addend.
    b : int or float
        Second addend.

    Returns
    -------
    int or float
        The sum of `a` and `b`.

    Notes
    -----
    This function accepts integers and floats and returns the appropriate
    numeric type.

    Examples
    --------
    >>> add(2, 3)
    5
    >>> add(2.5, 1.5)
    4.0
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be int or float")
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """
    Subtract one number from another.

    Parameters
    ----------
    a : int or float
        Minuend.
    b : int or float
        Subtrahend.

    Returns
    -------
    int or float
        The result of `a - b`.

    Examples
    --------
    >>> subtract(10, 3)
    7
    >>> subtract(5.5, 2.0)
    3.5
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be int or float")
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """
    Multiply two numbers.

    Parameters
    ----------
    a : int or float
        First factor.
    b : int or float
        Second factor.

    Returns
    -------
    int or float
        The product `a * b`.

    Examples
    --------
    >>> multiply(3, 4)
    12
    >>> multiply(2.5, 4)
    10.0
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be int or float")
    return a * b


def divide(a: Number, b: Number) -> Number:
    """
    Divide one number by another.

    Parameters
    ----------
    a : int or float
        Dividend.
    b : int or float
        Divisor.

    Returns
    -------
    float
        The result of `a / b` as a float.

    Raises
    ------
    ZeroDivisionError
        If `b` is zero.
    TypeError
        If either argument is not an int or float.

    Examples
    --------
    >>> divide(10, 2)
    5.0
    >>> divide(7, 2)
    3.5
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be int or float")
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b


if __name__ == "__main__":
    # Quick sanity checks when run directly
    tests = [
        ("add", 2, 3),
        ("subtract", 10, 4),
        ("multiply", 6, 7),
        ("divide", 20, 4),
    ]

    print("Running manual calculator sanity checks:\n")
    for name, x, y in tests:
        if name == "add":
            print(f"add({x}, {y}) = {add(x, y)}")
        elif name == "subtract":
            print(f"subtract({x}, {y}) = {subtract(x, y)}")
        elif name == "multiply":
            print(f"multiply({x}, {y}) = {multiply(x, y)}")
        elif name == "divide":
            print(f"divide({x}, {y}) = {divide(x, y)}")
