def greet_user(name, gender):
    if gender.lower() == "male":
        title = "Mr."
    else:
        title = "Mrs."
    return f"Hello, {title} {name}! Welcome."

# Example usage
print(greet_user("John", "male"))
print(greet_user("Mary", "female"))