"""Simple email validator per project requirements.

Requirements enforced:
- Must contain exactly one '@'.
- Must contain a '.' in the domain (after the '@').
- Must not start or end with a special character: first and last characters must be alphanumeric.
- Should not allow multiple '@'.

Assumptions (inferred):
- "Special characters" means any non-alphanumeric character for the first/last position.
- A '.' must appear in the domain portion (after the '@').
- Spaces are not allowed.
"""

from typing import Any


def is_valid_email(email: Any) -> bool:
    """Return True if `email` meets the simplified validation rules.

    Rules implemented:
    - email must be a string
    - exactly one '@'
    - at least one '.' in the domain (after '@')
    - first and last characters must be alphanumeric
    - no leading/trailing dot in local or domain
    - no spaces

    This is intentionally lightweight and does not attempt to fully
    implement RFC5322.
    """
    if not isinstance(email, str):
        return False
    if not email:
        return False
    # no spaces allowed
    if " " in email:
        return False
    # exactly one '@'
    if email.count("@") != 1:
        return False
    # first and last chars must be alphanumeric
    if not (email[0].isalnum() and email[-1].isalnum()):
        return False

    local, domain = email.split("@", 1)
    # non-empty local and domain
    if not local or not domain:
        return False
    # require a dot in the domain
    if "." not in domain:
        return False
    # disallow local or domain starting/ending with dot
    if local[0] == "." or local[-1] == ".":
        return False
    if domain[0] == "." or domain[-1] == ".":
        return False

    return True


if __name__ == "__main__":
    # quick manual smoke-checks
    samples = [
        "user@example.com",
        "user.name@example.co.uk",
        ".badstart@example.com",
        "user@@example.com",
    ]
    for s in samples:
        print(s, is_valid_email(s))
