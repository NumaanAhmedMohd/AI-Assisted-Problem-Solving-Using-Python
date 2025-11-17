"""Grade assignment utility.

Rules:
 - 90-100 -> 'A'
 - 80-89  -> 'B'
 - 70-79  -> 'C'
 - 60-69  -> 'D'
 - <60    -> 'F'

Behavior for invalid inputs:
 - Booleans are rejected (they're subclasses of int but not valid scores here).
 - Non-numeric values raise ValueError.
 - NaN or infinite values raise ValueError.
 - Scores outside 0..100 raise ValueError.

This function prefers explicit validation over permissive coercion.
"""
from typing import Any
import math


def assign_grade(score: Any) -> str:
    """Return the letter grade for a numeric `score`.

    Raises ValueError for invalid inputs (non-numeric, bool, NaN/inf, out-of-range).
    """
    # reject booleans explicitly
    if isinstance(score, bool):
        raise ValueError("Boolean is not a valid score")

    if not isinstance(score, (int, float)):
        raise ValueError("Score must be a numeric type")

    # convert to float for range checks
    f = float(score)

    # reject NaN or infinite
    if math.isnan(f) or not math.isfinite(f):
        raise ValueError("Score must be a finite number")

    if f < 0 or f > 100:
        raise ValueError("Score must be between 0 and 100 inclusive")

    # grade mapping (inclusive lower bounds)
    if f >= 90.0:
        return 'A'
    if f >= 80.0:
        return 'B'
    if f >= 70.0:
        return 'C'
    if f >= 60.0:
        return 'D'
    return 'F'


if __name__ == '__main__':
    # Quick manual demo
    examples = [100, 90, 89.9, 80, 70, 69.5, 59.999, 0]
    for s in examples:
        print(s, '->', assign_grade(s))
