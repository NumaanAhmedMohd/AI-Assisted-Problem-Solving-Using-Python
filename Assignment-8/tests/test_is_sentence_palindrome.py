import unittest

from is_sentence_palindrome import is_sentence_palindrome


class TestIsSentencePalindrome(unittest.TestCase):
    """Test cases for is_sentence_palindrome function."""

    # Valid palindromes
    def test_classic_palindrome(self):
        """Classic palindrome with mixed case, spaces, and punctuation."""
        self.assertTrue(is_sentence_palindrome("A man a plan a canal Panama"))

    def test_simple_lowercase_palindrome(self):
        """Simple lowercase palindrome."""
        self.assertTrue(is_sentence_palindrome("race car"))

    def test_palindrome_with_punctuation(self):
        """Palindrome with punctuation and question mark."""
        self.assertTrue(is_sentence_palindrome("Was it a car or a cat I saw?"))

    def test_single_word_palindrome(self):
        """Single word palindrome with mixed case."""
        self.assertTrue(is_sentence_palindrome("Madam"))

    def test_numeric_palindrome(self):
        """Palindrome with only numbers."""
        self.assertTrue(is_sentence_palindrome("12321"))

    def test_alphanumeric_palindrome(self):
        """Palindrome with mixed letters and numbers."""
        self.assertTrue(is_sentence_palindrome("A1B1A"))

    def test_palindrome_with_quotes(self):
        """Palindrome with quotes and apostrophe."""
        self.assertTrue(is_sentence_palindrome("No 'x' in Nixon"))

    def test_famous_palindrome(self):
        """Famous palindrome: Able was I ere I saw Elba."""
        self.assertTrue(is_sentence_palindrome("Able was I ere I saw Elba"))

    def test_palindrome_geese(self):
        """Palindrome: Do geese see God?"""
        self.assertTrue(is_sentence_palindrome("Do geese see God?"))

    def test_single_character(self):
        """Single character is a palindrome."""
        self.assertTrue(is_sentence_palindrome("a"))

    def test_two_same_characters(self):
        """Two identical characters form a palindrome."""
        self.assertTrue(is_sentence_palindrome("aa"))

    def test_empty_string(self):
        """Empty string is considered a palindrome."""
        self.assertTrue(is_sentence_palindrome(""))

    def test_only_spaces(self):
        """String with only spaces (cleaned to empty) is a palindrome."""
        self.assertTrue(is_sentence_palindrome("   "))

    def test_only_punctuation(self):
        """String with only punctuation (cleaned to empty) is a palindrome."""
        self.assertTrue(is_sentence_palindrome("!!!???"))

    def test_numbers_with_space(self):
        """Numbers with space, palindromic."""
        self.assertTrue(is_sentence_palindrome("12 21"))

    def test_camelcase_palindrome(self):
        """CamelCase palindrome (case-insensitive)."""
        self.assertTrue(is_sentence_palindrome("RaceCar"))

    def test_palindrome_with_hyphens(self):
        """Palindrome with hyphens."""
        self.assertTrue(is_sentence_palindrome("a-b-a"))

    def test_palindrome_with_mixed_punctuation(self):
        """Palindrome with various punctuation marks."""
        self.assertTrue(is_sentence_palindrome("A! B! A"))

    # Invalid palindromes (should return False)
    def test_non_palindrome_hello(self):
        """Simple non-palindrome."""
        self.assertFalse(is_sentence_palindrome("hello"))

    def test_non_palindrome_python(self):
        """Non-palindrome: 'python'."""
        self.assertFalse(is_sentence_palindrome("python"))

    def test_non_palindrome_abc(self):
        """Non-palindrome: 'abc'."""
        self.assertFalse(is_sentence_palindrome("abc"))

    def test_non_palindrome_12345(self):
        """Non-palindrome numeric."""
        self.assertFalse(is_sentence_palindrome("12345"))

    def test_non_palindrome_sentence(self):
        """Non-palindrome sentence."""
        self.assertFalse(is_sentence_palindrome("This is not a palindrome"))

    def test_almost_palindrome_off_by_one(self):
        """Almost palindrome but not quite."""
        self.assertFalse(is_sentence_palindrome("racecarx"))

    # Edge cases and invalid inputs
    def test_none_input_raises_type_error(self):
        """None should raise TypeError."""
        with self.assertRaises(TypeError):
            is_sentence_palindrome(None)

    def test_integer_input_raises_type_error(self):
        """Integer should raise TypeError."""
        with self.assertRaises(TypeError):
            is_sentence_palindrome(12345)

    def test_list_input_raises_type_error(self):
        """List should raise TypeError."""
        with self.assertRaises(TypeError):
            is_sentence_palindrome(["a", "b", "a"])

    def test_float_input_raises_type_error(self):
        """Float should raise TypeError."""
        with self.assertRaises(TypeError):
            is_sentence_palindrome(3.14)

    def test_dict_input_raises_type_error(self):
        """Dict should raise TypeError."""
        with self.assertRaises(TypeError):
            is_sentence_palindrome({"key": "value"})

    # Boundary cases
    def test_single_space(self):
        """Single space (cleaned to empty) is palindrome."""
        self.assertTrue(is_sentence_palindrome(" "))

    def test_many_spaces_between_letters(self):
        """Palindrome with many spaces between letters."""
        self.assertTrue(is_sentence_palindrome("a   b   a"))

    def test_palindrome_all_caps(self):
        """Palindrome in all uppercase."""
        self.assertTrue(is_sentence_palindrome("RACECAR"))

    def test_palindrome_all_lowercase(self):
        """Palindrome in all lowercase."""
        self.assertTrue(is_sentence_palindrome("racecar"))

    def test_long_palindrome(self):
        """Long palindrome."""
        self.assertTrue(is_sentence_palindrome("Was it a car or a cat I saw?"))

    def test_palindrome_with_numbers_and_letters_mixed(self):
        """Palindrome with mixed numbers, letters, and punctuation."""
        self.assertTrue(is_sentence_palindrome("A1b1A"))

    def test_very_long_non_palindrome(self):
        """Very long non-palindrome."""
        self.assertFalse(is_sentence_palindrome("The quick brown fox jumps over the lazy dog"))

    def test_palindrome_with_special_chars(self):
        """Palindrome with various special characters."""
        self.assertTrue(is_sentence_palindrome("A@b#c$b@A"))


if __name__ == '__main__':
    unittest.main()
