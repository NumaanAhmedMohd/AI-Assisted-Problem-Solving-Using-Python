from typing import Iterable, TypeVar, Any, List

T = TypeVar("T")

def find_max_iterative(lst: Iterable[T]) -> T:

    if isinstance(lst, str):
        raise TypeError("find_max_iterative() expects a list/iterable of numbers, not a string")
    try:
        it = iter(lst)
    except TypeError:
        raise TypeError("find_max_iterative() expects an iterable")
    try:
        current_max = next(it)
    except StopIteration:
        raise ValueError("find_max_iterative() received an empty iterable")
    for x in it:
        if x > current_max:
            current_max = x
    return current_max


def find_max_builtin(lst: Iterable[T]) -> T:

    if isinstance(lst, str):
        raise TypeError("find_max_builtin() expects a list/iterable of numbers, not a string")
    try:
        return max(lst)
    except TypeError:
        raise TypeError("find_max_builtin() expects an iterable")

def _parse_numbers(s: str) -> List[Any]:
    """
    Parse user input into a list of ints/floats.
    Accepts numbers separated by spaces and/or commas.
    """
    if not s.strip():
        return []
    tokens = [t for part in s.split(",") for t in part.split()]
    nums = []
    for tok in tokens:
        try:
            if "." in tok:
                nums.append(float(tok))
            else:
                nums.append(int(tok))
        except ValueError:
            # try float conversion for cases like "1e3"
            try:
                nums.append(float(tok))
            except ValueError:
                raise ValueError(f"Invalid number token: {tok!r}")
    return nums


if __name__ == "__main__":
    inp = input("Enter numbers separated by space or comma (e.g. 1 2 3 or 1,2,3): ").strip()
    try:
        numbers = _parse_numbers(inp)
    except ValueError as e:
        print("Error parsing input:", e)
    else:
        if not numbers:
            print("No numbers provided.")
        else:
            print("find_max_iterative ->", find_max_iterative(numbers))
            print("find_max_builtin   ->", find_max_builtin(numbers))