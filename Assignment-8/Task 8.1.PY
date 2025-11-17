import re
def is_valid_email(email):
    # Must contain exactly one @
    if email.count('@') != 1:
        return False
    # Must contain at least one dot
    if '.' not in email:
        return False
    # Must not start or end with special characters
    if re.match(r'^[\W_]', email) or re.search(r'[\W_]$', email):
        return False

    # Basic structure: local@domain.tld
    pattern = r'^[A-Za-z0-9]+[A-Za-z0-9._-]*@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.match(pattern, email) is not None

# 🧪 Test cases
test_emails = {
    "valid@example.com": True,
    "user.name@domain.co.in": True,
    "user@domain": False,
    "user@@domain.com": False,
    "@domain.com": False,
    "user@domain.com.": False,
    "user@.com": False,
    "user@domain..com": False,
    "user@domain.c": False,
    "user@domain.com": True,
    "user_name@domain.com": True,
    "user-name@domain.com": True,
    ".user@domain.com": False,
    "user@domain.com-": False
}

# ✅ Run test cases
print("Running test cases...\n")
for email, expected in test_emails.items():
    result = is_valid_email(email)
    status = "✅ Passed" if result == expected else "❌ Failed"
    print(f"{email:30} → {'Valid' if result else 'Invalid'} (Expected: {'Valid' if expected else 'Invalid'}) → {status}")

# 🧑‍💻 User input
print("\nTry your own email:")
user_email = input("Enter an email to validate: ")
if is_valid_email(user_email):
    print("✅ This email is valid.")
else:
    print("❌ This email is invalid.")
