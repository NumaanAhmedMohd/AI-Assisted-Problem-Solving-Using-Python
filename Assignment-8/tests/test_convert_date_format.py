import unittest

from convert_date_format import convert_date_format


class TestConvertDateFormat(unittest.TestCase):
    """Test cases for convert_date_format function."""

    # ============ Valid dates ============
    def test_example_from_spec(self):
        """Example from spec: 2023-10-15 → 15-10-2023."""
        self.assertEqual(convert_date_format("2023-10-15"), "15-10-2023")

    def test_first_day_of_year(self):
        """First day of year: 2024-01-01 → 01-01-2024."""
        self.assertEqual(convert_date_format("2024-01-01"), "01-01-2024")

    def test_last_day_of_year(self):
        """Last day of year: 2024-12-31 → 31-12-2024."""
        self.assertEqual(convert_date_format("2024-12-31"), "31-12-2024")

    def test_leap_year_feb_29(self):
        """Leap year Feb 29: 2024-02-29 → 29-02-2024."""
        self.assertEqual(convert_date_format("2024-02-29"), "29-02-2024")

    def test_leap_year_2000(self):
        """Leap year 2000: 2000-02-29 → 29-02-2000."""
        self.assertEqual(convert_date_format("2000-02-29"), "29-02-2000")

    def test_y2k_boundary(self):
        """Y2K boundary: 1999-12-31 → 31-12-1999."""
        self.assertEqual(convert_date_format("1999-12-31"), "31-12-1999")

    def test_current_date_approx(self):
        """Today's date (approx): 2025-11-14 → 14-11-2025."""
        self.assertEqual(convert_date_format("2025-11-14"), "14-11-2025")

    def test_old_date(self):
        """Old date: 1900-01-01 → 01-01-1900."""
        self.assertEqual(convert_date_format("1900-01-01"), "01-01-1900")

    def test_future_date(self):
        """Future date: 2099-12-31 → 31-12-2099."""
        self.assertEqual(convert_date_format("2099-12-31"), "31-12-2099")

    def test_all_same_digits(self):
        """All same digits: 2023-05-05 → 05-05-2023."""
        self.assertEqual(convert_date_format("2023-05-05"), "05-05-2023")

    def test_two_digit_day_month(self):
        """Two-digit day and month: 2024-04-20 → 20-04-2024."""
        self.assertEqual(convert_date_format("2024-04-20"), "20-04-2024")

    def test_single_digit_leading_zeros(self):
        """Date with leading zeros: 2023-01-09 → 09-01-2023."""
        self.assertEqual(convert_date_format("2023-01-09"), "09-01-2023")

    def test_mid_month_mid_day(self):
        """Mid-month, mid-day: 2023-06-15 → 15-06-2023."""
        self.assertEqual(convert_date_format("2023-06-15"), "15-06-2023")

    def test_feb_28_non_leap(self):
        """Feb 28 non-leap year: 2023-02-28 → 28-02-2023."""
        self.assertEqual(convert_date_format("2023-02-28"), "28-02-2023")

    def test_various_months(self):
        """Test various months with max days."""
        self.assertEqual(convert_date_format("2023-01-31"), "31-01-2023")
        self.assertEqual(convert_date_format("2023-03-31"), "31-03-2023")
        self.assertEqual(convert_date_format("2023-04-30"), "30-04-2023")
        self.assertEqual(convert_date_format("2023-11-30"), "30-11-2023")

    # ============ Invalid formats ============
    def test_invalid_separator_forward_slash(self):
        """Invalid separator: forward slash."""
        with self.assertRaises(ValueError):
            convert_date_format("2023/10/15")

    def test_invalid_separator_dot(self):
        """Invalid separator: dot."""
        with self.assertRaises(ValueError):
            convert_date_format("2023.10.15")

    def test_invalid_format_mm_dd_yyyy(self):
        """Wrong format: MM-DD-YYYY."""
        with self.assertRaises(ValueError):
            convert_date_format("10-15-2023")

    def test_invalid_format_already_dd_mm_yyyy(self):
        """Already in DD-MM-YYYY format."""
        with self.assertRaises(ValueError):
            convert_date_format("15-10-2023")

    def test_missing_leading_zero_month(self):
        """Missing leading zero in month."""
        with self.assertRaises(ValueError):
            convert_date_format("2023-1-15")

    def test_missing_leading_zero_day(self):
        """Missing leading zero in day."""
        with self.assertRaises(ValueError):
            convert_date_format("2023-10-5")

    def test_incomplete_date_missing_day(self):
        """Incomplete date: missing day."""
        with self.assertRaises(ValueError):
            convert_date_format("2023-10")

    def test_no_separators(self):
        """No separators."""
        with self.assertRaises(ValueError):
            convert_date_format("15102023")

    def test_empty_string(self):
        """Empty string."""
        with self.assertRaises(ValueError):
            convert_date_format("")

    def test_invalid_month_13(self):
        """Invalid month: 13."""
        with self.assertRaises(ValueError):
            convert_date_format("2023-13-01")

    def test_invalid_month_00(self):
        """Invalid month: 00."""
        with self.assertRaises(ValueError):
            convert_date_format("2023-00-15")

    def test_invalid_day_32(self):
        """Invalid day: 32."""
        with self.assertRaises(ValueError):
            convert_date_format("2023-10-32")

    def test_invalid_day_00(self):
        """Invalid day: 00."""
        with self.assertRaises(ValueError):
            convert_date_format("2023-10-00")

    def test_feb_30_non_leap(self):
        """Invalid date: Feb 30 (non-leap year)."""
        with self.assertRaises(ValueError):
            convert_date_format("2023-02-30")

    def test_feb_30_leap_year(self):
        """Invalid date: Feb 30 (leap year)."""
        with self.assertRaises(ValueError):
            convert_date_format("2024-02-30")

    def test_april_31(self):
        """Invalid date: April 31 (April has 30 days)."""
        with self.assertRaises(ValueError):
            convert_date_format("2023-04-31")

    def test_june_31(self):
        """Invalid date: June 31 (June has 30 days)."""
        with self.assertRaises(ValueError):
            convert_date_format("2023-06-31")

    # ============ Type errors ============
    def test_none_input(self):
        """None input raises TypeError."""
        with self.assertRaises(TypeError):
            convert_date_format(None)

    def test_integer_input(self):
        """Integer input raises TypeError."""
        with self.assertRaises(TypeError):
            convert_date_format(20231015)

    def test_float_input(self):
        """Float input raises TypeError."""
        with self.assertRaises(TypeError):
            convert_date_format(2023.10)

    def test_list_input(self):
        """List input raises TypeError."""
        with self.assertRaises(TypeError):
            convert_date_format(["2023", "10", "15"])

    def test_dict_input(self):
        """Dict input raises TypeError."""
        with self.assertRaises(TypeError):
            convert_date_format({"year": 2023, "month": 10, "day": 15})

    def test_tuple_input(self):
        """Tuple input raises TypeError."""
        with self.assertRaises(TypeError):
            convert_date_format(("2023", "10", "15"))

    # ============ Whitespace handling ============
    def test_leading_and_trailing_spaces(self):
        """Leading and trailing spaces should be stripped."""
        self.assertEqual(convert_date_format("  2023-10-15  "), "15-10-2023")

    def test_leading_space_only(self):
        """Leading space only should be stripped."""
        self.assertEqual(convert_date_format(" 2023-10-15"), "15-10-2023")

    def test_trailing_space_only(self):
        """Trailing space only should be stripped."""
        self.assertEqual(convert_date_format("2023-10-15 "), "15-10-2023")

    def test_only_spaces(self):
        """Only spaces raises ValueError."""
        with self.assertRaises(ValueError):
            convert_date_format("   ")

    # ============ Invalid content ============
    def test_literal_yyyy_mm_dd(self):
        """Literal string YYYY-MM-DD."""
        with self.assertRaises(ValueError):
            convert_date_format("YYYY-MM-DD")

    def test_datetime_with_time(self):
        """DateTime with time component."""
        with self.assertRaises(ValueError):
            convert_date_format("2023-10-15T10:30:00")

    def test_non_numeric_year(self):
        """Non-numeric year."""
        with self.assertRaises(ValueError):
            convert_date_format("20AB-10-15")

    def test_non_numeric_month(self):
        """Non-numeric month."""
        with self.assertRaises(ValueError):
            convert_date_format("2023-XX-15")

    def test_non_numeric_day(self):
        """Non-numeric day."""
        with self.assertRaises(ValueError):
            convert_date_format("2023-10-YY")

    def test_partial_date_too_short(self):
        """Partial date: too short."""
        with self.assertRaises(ValueError):
            convert_date_format("2023-10")

    def test_extra_characters(self):
        """Extra characters after valid date."""
        with self.assertRaises(ValueError):
            convert_date_format("2023-10-15x")

    def test_extra_separator(self):
        """Extra separator."""
        with self.assertRaises(ValueError):
            convert_date_format("2023-10-15-01")

    # ============ Edge cases - Leap years ============
    def test_leap_year_1996(self):
        """Leap year 1996: divisible by 4."""
        self.assertEqual(convert_date_format("1996-02-29"), "29-02-1996")

    def test_leap_year_2000(self):
        """Leap year 2000: divisible by 400."""
        self.assertEqual(convert_date_format("2000-02-29"), "29-02-2000")

    def test_non_leap_year_1900(self):
        """Non-leap year 1900: divisible by 100 but not 400."""
        with self.assertRaises(ValueError):
            convert_date_format("1900-02-29")

    def test_non_leap_year_2100(self):
        """Non-leap year 2100: divisible by 100 but not 400."""
        with self.assertRaises(ValueError):
            convert_date_format("2100-02-29")

    def test_non_leap_year_2023(self):
        """Non-leap year 2023: Feb has only 28 days."""
        with self.assertRaises(ValueError):
            convert_date_format("2023-02-29")

    # ============ Edge cases - Month days ============
    def test_jan_31(self):
        """January 31."""
        self.assertEqual(convert_date_format("2023-01-31"), "31-01-2023")

    def test_feb_28(self):
        """February 28 (non-leap)."""
        self.assertEqual(convert_date_format("2023-02-28"), "28-02-2023")

    def test_mar_31(self):
        """March 31."""
        self.assertEqual(convert_date_format("2023-03-31"), "31-03-2023")

    def test_apr_30(self):
        """April 30."""
        self.assertEqual(convert_date_format("2023-04-30"), "30-04-2023")

    def test_may_31(self):
        """May 31."""
        self.assertEqual(convert_date_format("2023-05-31"), "31-05-2023")

    def test_jun_30(self):
        """June 30."""
        self.assertEqual(convert_date_format("2023-06-30"), "30-06-2023")

    def test_jul_31(self):
        """July 31."""
        self.assertEqual(convert_date_format("2023-07-31"), "31-07-2023")

    def test_aug_31(self):
        """August 31."""
        self.assertEqual(convert_date_format("2023-08-31"), "31-08-2023")

    def test_sep_30(self):
        """September 30."""
        self.assertEqual(convert_date_format("2023-09-30"), "30-09-2023")

    def test_oct_31(self):
        """October 31."""
        self.assertEqual(convert_date_format("2023-10-31"), "31-10-2023")

    def test_nov_30(self):
        """November 30."""
        self.assertEqual(convert_date_format("2023-11-30"), "30-11-2023")

    def test_dec_31(self):
        """December 31."""
        self.assertEqual(convert_date_format("2023-12-31"), "31-12-2023")


if __name__ == '__main__':
    unittest.main()
