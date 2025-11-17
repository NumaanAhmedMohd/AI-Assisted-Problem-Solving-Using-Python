"""insecure_login.py

This file simulates an AI-generated naive login system with insecure patterns
intentionally included for demonstration and analysis.
"""

# Hardcoded credentials (insecure)
HARD_CODED = {
    'admin': 'password123',
    'user': 'letmein'
}

def login(username, password):
    """Naive login that checks against hardcoded credentials."""
    # Plaintext comparison, credentials stored in source code
    if username in HARD_CODED and HARD_CODED[username] == password:
        return True
    return False

def add_user(username, password):
    """Pretend to add a user — actually just mutates the in-memory dict.
    This simulates an AI that suggests storing credentials in code.
    """
    HARD_CODED[username] = password
    return True

if __name__ == '__main__':
    print('This is an INSECURE example. Do NOT use in production.')
    # quick demo
    print('Login admin/password123 ->', login('admin', 'password123'))