"""test_greetings.py

Tests for the inclusive_greetings module.
"""

import unittest
from inclusive_greetings import PersonInfo, HonorificPreference, greet_person


class TestInclusiveGreetings(unittest.TestCase):
    def test_neutral_default(self):
        """Test default neutral honorific."""
        person = PersonInfo.create("Alex")
        self.assertEqual(greet_person(person), "Hello, Mx. Alex! Welcome.")
    
    def test_no_honorific(self):
        """Test explicitly requesting no honorific."""
        person = PersonInfo.create(
            "Sam",
            honorific_preference=HonorificPreference.NONE
        )
        self.assertEqual(greet_person(person), "Hello, Sam! Welcome.")
    
    def test_custom_honorific(self):
        """Test custom honorific preference."""
        person = PersonInfo.create(
            "Dr. Pat",
            honorific_preference=HonorificPreference.SPECIFIED,
            preferred_honorific="Dr."
        )
        self.assertEqual(greet_person(person), "Hello, Dr. Dr. Pat! Welcome.")
    
    def test_honorific_disabled(self):
        """Test with honorifics disabled."""
        person = PersonInfo.create("Jordan", use_honorific=False)
        self.assertEqual(greet_person(person), "Hello, Jordan! Welcome.")
    
    def test_empty_honorific(self):
        """Test that empty preferred honorific with SPECIFIED falls back to neutral."""
        person = PersonInfo.create(
            "Casey",
            honorific_preference=HonorificPreference.SPECIFIED,
            preferred_honorific=""
        )
        self.assertEqual(greet_person(person), "Hello, Mx. Casey! Welcome.")


if __name__ == '__main__':
    unittest.main()