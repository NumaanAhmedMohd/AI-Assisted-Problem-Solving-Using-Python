# Calculator Docstring Comparison

This document compares the manually written NumPy-style docstrings in
`calculator_manual.py` with the AI-generated module-level and function docstrings
in `calculator_ai.py`.

## Overview
Both modules implement the same four operations: `add`, `subtract`, `multiply`,
and `divide`. The implementations intentionally include the same runtime checks
(ensuring numeric inputs, raising exceptions on invalid input or division by
zero). The only differences are in documentation style and content.

## Key Differences

- **Module-level docstring**: `calculator_manual.py` includes a descriptive
  module-level header as part of the file top comment block; `calculator_ai.py`
  contains an AI-generated top-level docstring which is concise and notes that
  docstrings were AI-generated.

- **Function docstrings**:
  - Manual docstrings include a `Notes` section (where appropriate) and
    `Examples` blocks that provide usage examples and expected outputs.
  - AI docstrings are more concise: they cover `Parameters` and `Returns`, and
    include `Raises` for the `divide` function, but omit `Examples` and
    `Notes`.

- **Language and tone**:
  - Manual: Educational, explicit, includes examples, and explains types and
    expectations.
  - AI: Professional and concise, focuses on behavior and types, less
    explanatory text.

## Teaching Points
- Use AI-generated docstrings as a scaffold; add `Examples` and `Notes` when
  teaching or documenting non-trivial behavior.
- Manual docstrings are better for learners because examples show expected
  behavior. AI-generated docstrings are often excellent for consistent,
  production-oriented documentation.

## Suggested Hybrid Approach
1. Run AI to generate initial docstrings for all functions.
2. Add `Examples` and domain-specific `Notes` manually where helpful.
3. Review `Raises` sections for correctness and completeness.

## Files
- `calculator_manual.py` — Manual NumPy-style docstrings with examples.
- `calculator_ai.py` — AI-generated docstrings (module-level and functions).
