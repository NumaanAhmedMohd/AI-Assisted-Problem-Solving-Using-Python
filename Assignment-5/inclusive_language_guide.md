# Inclusive Language Guidelines

This document provides guidelines for creating inclusive greetings and avoiding assumptions about gender identity.

## Key Principles

1. Default to gender-neutral language
   - Use "Mx." as a neutral honorific
   - Allow users to specify their preferred honorific
   - Provide option for no honorific

2. Avoid assumptions
   - Don't assume gender based on name
   - Don't require gender information unless necessary
   - Allow self-identification when gender info is needed

3. Use inclusive language
   - Replace "Sir/Madam" with "Greetings" or person's name
   - Use "they/them" instead of "he/she"
   - Use "everyone/folks/team" instead of "guys"

## Implementation Details

The `inclusive_greetings.py` module implements these principles:

1. `PersonInfo` class
   - Stores name and greeting preferences
   - Defaults to neutral honorific (Mx.)
   - Allows custom honorific specification
   - Supports opting out of honorifics

2. Preference handling
   - `HonorificPreference.NEUTRAL`: Uses "Mx."
   - `HonorificPreference.SPECIFIED`: Uses custom honorific
   - `HonorificPreference.NONE`: No honorific
   - `use_honorific`: Boolean to disable honorifics entirely

## Examples

```python
# Default (neutral)
person = PersonInfo.create("Alex")
# Result: "Hello, Mx. Alex! Welcome."

# No honorific
person = PersonInfo.create("Sam", honorific_preference=HonorificPreference.NONE)
# Result: "Hello, Sam! Welcome."

# Custom honorific
person = PersonInfo.create(
    "Pat",
    honorific_preference=HonorificPreference.SPECIFIED,
    preferred_honorific="Dr."
)
# Result: "Hello, Dr. Pat! Welcome."
```

## Testing

Run the tests to verify inclusive behavior:
```bash
python -m unittest test_greetings.py
```

## Analyzing Code

Check code for non-inclusive language:
```bash
python analyze_inclusiveness.py <filename>
```

## Further Reading

- [LGBTQ+ Inclusive Language Guide](https://www.hrc.org/resources/lgbtq-inclusive-language-dos-and-donts)
- [Gender-Inclusive Language](https://www.un.org/en/gender-inclusive-language/)
- [APA Style Guide on Bias-Free Language](https://apastyle.apa.org/style-grammar-guidelines/bias-free-language/)