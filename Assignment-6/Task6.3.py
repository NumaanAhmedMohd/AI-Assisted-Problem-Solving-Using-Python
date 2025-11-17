def classify_age_nested(age):
    if age < 0:
        return "Invalid age"
    elif age <= 2:
        return "Infant"
    elif age <= 12:
        return "Child"
    elif age <= 17:
        return "Teenager"
    elif age <= 64:
        if age <= 25:
            return "Young Adult"
        elif age <= 39:
            return "Adult"
        else:
            return "Middle-aged Adult"
    elif age <= 79:
        return "Senior"
    else:
        return "Elderly"


def classify_age_simple(age):
    if age < 0:
        return "Invalid age"
    elif 0 <= age <= 2:
        return "Infant"
    elif 3 <= age <= 12:
        return "Child"
    elif 13 <= age <= 17:
        return "Teenager"
    elif 18 <= age <= 25:
        return "Young Adult"
    elif 26 <= age <= 39:
        return "Adult"
    elif 40 <= age <= 64:
        return "Middle-aged Adult"
    elif 65 <= age <= 79:
        return "Senior"
    else:
        return "Elderly"


def classify_age_ternary(age):
    if age < 0:
        return "Invalid age"
    return ("Infant" if age <= 2 else
            "Child" if age <= 12 else
            "Teenager" if age <= 17 else
            "Young Adult" if age <= 25 else
            "Adult" if age <= 39 else
            "Middle-aged Adult" if age <= 64 else
            "Senior" if age <= 79 else
            "Elderly")


if __name__ == "__main__":
    print("Age Classification Program")
    print("0-2: Infant | 3-12: Child | 13-17: Teenager | 18-25: Young Adult")
    print("26-39: Adult | 40-64: Middle-aged | 65-79: Senior | 80+: Elderly")
    print("-" * 60)
    
    try:
        age = int(input("\nEnter age: "))
        
        print(f"\nNested If-Elif-Else: {classify_age_nested(age)}")
        print(f"Simple If-Elif-Else: {classify_age_simple(age)}")
        print(f"Ternary Operators: {classify_age_ternary(age)}")
        
    except ValueError:
        print("Error: Please enter a valid integer age!")
