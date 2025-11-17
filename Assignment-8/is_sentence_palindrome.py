"""Sentence palindrome checker.

A palindrome ignores case, spaces, and punctuation.
Only alphanumeric characters are considered.

Example: "A man a plan a canal Panama" → True
"""

from typing import Any


def is_sentence_palindrome(sentence: Any) -> bool:
    """Return True if `sentence` is a palindrome (ignoring case, spaces, punctuation).

    Args:
        sentence: A string to check.

    Returns:
        bool: True if the sentence is a palindrome, False otherwise.

    Raises:
        TypeError: If `sentence` is not a string.

    Examples:
        >>> is_sentence_palindrome("A man a plan a canal Panama")
        True
        >>> is_sentence_palindrome("race car")
        True
        >>> is_sentence_palindrome("hello")
        False
        >>> is_sentence_palindrome("")
        True
    """
    if not isinstance(sentence, str):
        raise TypeError("sentence must be a string")

    # Keep only alphanumeric characters (letters and digits)
    # Convert to lowercase for case-insensitive comparison
    cleaned = ''.join(char.lower() for char in sentence if char.isalnum())

    # Compare cleaned string with its reverse
    return cleaned == cleaned[::-1]


if __name__ == '__main__':
    # Quick manual demo
    examples = [
        "A man a plan a canal Panama",
        "race car",
        "hello",
        "Was it a car or a cat I saw?",
        "Madam",
        "",
        "12321",
        "Do geese see God?",
    ]
    for s in examples:
        print(f"{s!r:40} → {is_sentence_palindrome(s)}")
