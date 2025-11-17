import unittest
import math

from assign_grade import assign_grade


class TestAssignGrade(unittest.TestCase):
    def test_A_boundaries(self):
        self.assertEqual(assign_grade(100), 'A')
        self.assertEqual(assign_grade(99), 'A')
        self.assertEqual(assign_grade(90), 'A')

    def test_B_boundaries(self):
        self.assertEqual(assign_grade(89), 'B')
        self.assertEqual(assign_grade(80), 'B')
        self.assertEqual(assign_grade(89.9), 'B')

    def test_C_and_D_boundaries(self):
        self.assertEqual(assign_grade(79), 'C')
        self.assertEqual(assign_grade(70), 'C')
        self.assertEqual(assign_grade(69), 'D')
        self.assertEqual(assign_grade(60), 'D')

    def test_F_and_floor(self):
        self.assertEqual(assign_grade(59), 'F')
        self.assertEqual(assign_grade(0), 'F')
        self.assertEqual(assign_grade(59.999), 'F')

    def test_invalid_range(self):
        with self.assertRaises(ValueError):
            assign_grade(-5)
        with self.assertRaises(ValueError):
            assign_grade(105)

    def test_non_numeric_and_special(self):
        with self.assertRaises(ValueError):
            assign_grade("eighty")
        with self.assertRaises(ValueError):
            assign_grade(None)
        with self.assertRaises(ValueError):
            assign_grade(float('nan'))
        with self.assertRaises(ValueError):
            assign_grade(float('inf'))

    def test_numeric_string_and_bool(self):
        # We choose to reject numeric strings and booleans
        with self.assertRaises(ValueError):
            assign_grade("85")
        with self.assertRaises(ValueError):
            assign_grade(True)

    def test_precision_edges(self):
        self.assertEqual(assign_grade(60.0000000001), 'D')
        self.assertEqual(assign_grade(89.9999999999), 'B')


if __name__ == '__main__':
    unittest.main()
