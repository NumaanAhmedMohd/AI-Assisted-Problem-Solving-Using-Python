def classify_age_if_else(age: int) -> str:
    """
    Classify a person's age group using nested if-elif-else statements.
    
    Args:
        age: The person's age in years
        
    Returns:
        str: The age classification
        
    Raises:
        ValueError: If age is negative
    """
    if age < 0:
        raise ValueError("Age cannot be negative")
    
    if age <= 2:
        return "Infant"
    elif age <= 12:
        if age <= 4:
            return "Toddler"
        elif age <= 8:
            return "Child"
        else:
            return "Pre-teen"
    elif age <= 19:
        if age <= 16:
            return "Teenager"
        else:
            return "Young Adult"
    elif age <= 59:
        if age <= 35:
            return "Adult"
        else:
            return "Middle-aged Adult"
    else:
        if age <= 80:
            return "Senior"
        else:
            return "Elderly"


def classify_age_match(age: int) -> str:
    """
    Classify a person's age group using match-case statement (Python 3.10+).
    
    Args:
        age: The person's age in years
        
    Returns:
        str: The age classification
        
    Raises:
        ValueError: If age is negative
    """
    if age < 0:
        raise ValueError("Age cannot be negative")
    
    match age:
        case _ if age <= 2:
            return "Infant"
        case _ if age <= 4:
            return "Toddler"
        case _ if age <= 8:
            return "Child"
        case _ if age <= 12:
            return "Pre-teen"
        case _ if age <= 16:
            return "Teenager"
        case _ if age <= 19:
            return "Young Adult"
        case _ if age <= 35:
            return "Adult"
        case _ if age <= 59:
            return "Middle-aged Adult"
        case _ if age <= 80:
            return "Senior"
        case _:
            return "Elderly"


def classify_age_dict(age: int) -> str:
    """
    Classify a person's age group using a dictionary-based approach.
    
    Args:
        age: The person's age in years
        
    Returns:
        str: The age classification
        
    Raises:
        ValueError: If age is negative
    """
    if age < 0:
        raise ValueError("Age cannot be negative")
    
    age_ranges = [
        (2, "Infant"),
        (4, "Toddler"),
        (8, "Child"),
        (12, "Pre-teen"),
        (16, "Teenager"),
        (19, "Young Adult"),
        (35, "Adult"),
        (59, "Middle-aged Adult"),
        (80, "Senior"),
        (float('inf'), "Elderly")
    ]
    
    for max_age, classification in age_ranges:
        if age <= max_age:
            return classification