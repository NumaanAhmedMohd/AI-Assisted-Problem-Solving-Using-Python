def assign_grade(score):
    # Validate input type
    if not isinstance(score, (int, float)):
        return "Invalid input"
    
    # Validate score range
    if score < 0 or score > 100:
        return "Invalid input"
    
    # Grade assignment logic
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# 🧪 AI-generated test cases
test_cases = {
    100: "A",               # Upper boundary
    90: "A",                # Lower boundary of A
    89: "B",                # Upper boundary of B
    80: "B",                # Lower boundary of B
    79: "C",                # Upper boundary of C
    70: "C",                # Lower boundary of C
    69: "D",                # Upper boundary of D
    60: "D",                # Lower boundary of D
    59: "F",                # Just below D
    0: "F",                 # Lower boundary of F
    -5: "Invalid input",    # Negative score
    105: "Invalid input",   # Above max score
    "eighty": "Invalid input", # Non-numeric string
    None: "Invalid input",     # Null input
    85.5: "B",              # Float input
    "": "Invalid input",       # Empty string
}

# 📊 Run test suite
print("Running test suite...\n")
for score, expected in test_cases.items():
    result = assign_grade(score)
    status = "✅ Passed" if result == expected else "❌ Failed"
    print(f"Input: {repr(score):10} → Output: {result:15} (Expected: {expected}) → {status}")

# 🧑‍💻 User input
print("\nTry your own score:")
user_input = input("Enter a score (0–100): ")

try:
    score = float(user_input) if '.' in user_input else int(user_input)
except ValueError:
    score = user_input  # Keep as string if not convertible

print("Grade:", assign_grade(score))
