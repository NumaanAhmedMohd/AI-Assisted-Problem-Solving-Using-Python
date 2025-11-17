from age_classifier import classify_age_if_else, classify_age_match, classify_age_dict


def test_age(age: int) -> None:
    """Test all three implementations with the given age."""
    print(f"\nClassifying age: {age}")
    print(f"Using if-else:  {classify_age_if_else(age)}")
    print(f"Using match:    {classify_age_match(age)}")
    print(f"Using dict:     {classify_age_dict(age)}")


def main() -> None:
    # Test with various ages across different ranges
    test_ages = [1, 3, 6, 10, 15, 18, 25, 45, 70, 90]
    
    for age in test_ages:
        test_age(age)
    
    # Test error case
    print("\nTesting error case (negative age):")
    try:
        classify_age_if_else(-1)
    except ValueError as e:
        print(f"Caught expected error: {e}")


if __name__ == "__main__":
    main()