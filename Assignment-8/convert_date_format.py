"""Date format converter.

Converts dates from YYYY-MM-DD format to DD-MM-YYYY format.
"""

from typing import Any


def convert_date_format(date_str: Any) -> str:
    """Convert date string from YYYY-MM-DD to DD-MM-YYYY format.

    Args:
        date_str: A date string in YYYY-MM-DD format.

    Returns:
        str: Date string in DD-MM-YYYY format.

    Raises:
        TypeError: If date_str is not a string.
        ValueError: If date_str is not in valid YYYY-MM-DD format or
                    contains an invalid date.

    Examples:
        >>> convert_date_format("2023-10-15")
        '15-10-2023'
        >>> convert_date_format("2024-01-01")
        '01-01-2024'
        >>> convert_date_format("2024-12-31")
        '31-12-2024'
    """
    if not isinstance(date_str, str):
        raise TypeError("date_str must be a string")

    # Strip whitespace and check for empty
    date_str = date_str.strip()
    if not date_str:
        raise ValueError("date_str cannot be empty")

    # Check exact format: YYYY-MM-DD (10 characters)
    if len(date_str) != 10:
        raise ValueError("date_str must be in YYYY-MM-DD format (10 characters)")

    # Check separators
    if date_str[4] != '-' or date_str[7] != '-':
        raise ValueError("date_str must use '-' as separator (YYYY-MM-DD)")

    # Extract parts
    try:
        year_str = date_str[0:4]
        month_str = date_str[5:7]
        day_str = date_str[8:10]

        # Validate all parts are numeric
        year = int(year_str)
        month = int(month_str)
        day = int(day_str)
    except ValueError:
        raise ValueError("year, month, and day must be numeric in YYYY-MM-DD format")

    # Validate ranges
    if not (1 <= month <= 12):
        raise ValueError(f"month must be between 01 and 12, got {month:02d}")
    if not (1 <= day <= 31):
        raise ValueError(f"day must be between 01 and 31, got {day:02d}")

    # Validate day in month (considering leap years)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check for leap year
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    if is_leap:
        days_in_month[1] = 29

    max_day = days_in_month[month - 1]
    if day > max_day:
        raise ValueError(
            f"day {day:02d} is invalid for month {month:02d} "
            f"(max {max_day} days)"
        )

    # Convert to DD-MM-YYYY
    return f"{day:02d}-{month:02d}-{year:04d}"


if __name__ == '__main__':
    # Quick demo
    examples = [
        "2023-10-15",
        "2024-01-01",
        "2024-12-31",
        "2024-02-29",
        "1999-12-31",
    ]
    for date_str in examples:
        result = convert_date_format(date_str)
        print(f"{date_str} → {result}")
