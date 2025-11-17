import string
def is_sentence_palindrome(sentence):
    # Remove punctuation, spaces, and convert to lowercase
    cleaned = ''.join(
        char.lower() for char in sentence if char.isalnum())
    return cleaned == cleaned[::-1]# 🧪 AI-generated test cases
test_cases = {
    "A man a plan a canal Panama": True,
    "No lemon, no melon": True,
    "Was it a car or a cat I saw?": True,
    "Madam In Eden, I'm Adam": True,
    "Never odd or even": True,
    "Hello, world!": False,"Step on no pets": True,
    "Eva, can I see bees in a cave?": True,
    "This is not a palindrome": False,
    "": True,  # Empty string is trivially a palindrome
    "12321": True, "12345": False,
    "Able was I, ere I saw Elba": True,
    "No 'x' in Nixon": True,
    "Palindrome": False}
# 📊 Run test suite
print("Running test suite...\n")
for sentence, expected in test_cases.items():
    result = is_sentence_palindrome(sentence)
    status = "✅ Passed" if result == expected else "❌ Failed"
    print(f"Input: {repr(sentence):40} → Output: {result} (Expected: {expected}) → {status}")
# 🧑‍💻 User input
print("\nTry your own sentence:")
user_input = input("Enter a sentence: ")
if is_sentence_palindrome(user_input):
    print("✅ It's a palindrome!")
else:
    print("❌ Not a palindrome.")
