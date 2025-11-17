def convert_date_format(date_str):
    try:
        parts = date_str.split('-')
        if len(parts) != 3:
            return "Invalid format"
        
        year, month, day = parts
        if not (year.isdigit() and month.isdigit() and day.isdigit()):
            return "Invalid format"
        
        year, month, day = int(year), int(month), int(day)
        
        if month < 1 or month > 12 or day < 1 or day > 31:
            return "Invalid date"
        
        return f"{str(day).zfill(2)}-{str(month).zfill(2)}-{year}"
    
    except Exception:
        return "Error"

# 🧪 AI-generated test cases
test_cases = {
    "2023-10-15": "15-10-2023",
    "1999-01-01": "01-01-1999",
    "2020-12-31": "31-12-2020",
    "2023-2-5": "05-02-2023",             # Single-digit month/day
    "2023-13-01": "Invalid date",         # Invalid month
    "2023-00-10": "Invalid date",         # Month zero
    "2023-11-00": "Invalid date",         # Day zero
    "2023-11-32": "Invalid date",         # Day out of range
    "abcd-10-15": "Invalid format",       # Non-numeric year
    "2023-10-xx": "Invalid format",       # Non-numeric day
    "2023/10/15": "Invalid format",       # Wrong separator
    "": "Invalid format",                 # Empty string
    "2023-10": "Invalid format",          # Missing day
    "2023-10-15-01": "Invalid format"     # Extra part
}

# 📊 Run test suite
print("Running test suite...\n")
for date_str, expected in test_cases.items():
    result = convert_date_format(date_str)
    status = "✅ Passed" if result == expected else "❌ Failed"
    print(f"Input: {repr(date_str):20} → Output: {result:15} (Expected: {expected}) → {status}")

# 🧑‍💻 User input
print("\nTry your own date:")
user_input = input("Enter a date in YYYY-MM-DD format: ")
print("Converted format:", convert_date_format(user_input))
