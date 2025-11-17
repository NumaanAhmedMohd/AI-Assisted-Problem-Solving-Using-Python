import unittest

from is_valid_email import is_valid_email


class TestIsValidEmail(unittest.TestCase):
    def test_valid_simple(self):
        self.assertTrue(is_valid_email("user@example.com"))

    def test_valid_subdomain(self):
        self.assertTrue(is_valid_email("user.name@sub.example.co.uk"))

    def test_valid_with_plus_and_hyphen(self):
        # plus and hyphen allowed inside local part in our lightweight validator
        self.assertTrue(is_valid_email("u-ser+tag@example.io"))

    def test_missing_at(self):
        self.assertFalse(is_valid_email("userexample.com"))

    def test_multiple_at(self):
        self.assertFalse(is_valid_email("user@@example.com"))

    def test_no_dot(self):
        # domain must contain a dot (we require a '.' after the '@')
        self.assertFalse(is_valid_email("user@example"))

    def test_starts_with_dot(self):
        self.assertFalse(is_valid_email(".user@example.com"))

    def test_local_ends_with_dot(self):
        self.assertFalse(is_valid_email("user.@example.com"))

    def test_domain_starts_with_dot(self):
        self.assertFalse(is_valid_email("user@.example.com"))

    def test_ends_with_dot(self):
        self.assertFalse(is_valid_email("user@example.com."))

    def test_leading_space(self):
        self.assertFalse(is_valid_email(" user@example.com"))

    def test_trailing_space(self):
        self.assertFalse(is_valid_email("user@example.com "))

    def test_empty_string(self):
        self.assertFalse(is_valid_email(""))

    def test_non_string(self):
        self.assertFalse(is_valid_email(None))

    def test_empty_local(self):
        self.assertFalse(is_valid_email("@example.com"))

    def test_empty_domain(self):
        self.assertFalse(is_valid_email("user@"))


if __name__ == "__main__":
    unittest.main()
