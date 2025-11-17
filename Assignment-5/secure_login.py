"""secure_login.py

Minimal secure login implementation using PBKDF2-HMAC for password hashing
and a JSON-backed credential store. Uses only Python standard library.

Features:
- create_user(username, password)
- verify_user(username, password)
- CLI for create/login

Security notes:
- No hardcoded credentials.
- Passwords are salted and hashed with pbkdf2_hmac using SHA256.
- Uses secrets.token_bytes for salt generation.
"""

import hashlib
import json
import os
import secrets
import time
from typing import Optional

CREDENTIALS_FILE = os.path.join(os.path.dirname(__file__), 'credentials_secure.json')
PBKDF2_ITERATIONS = 200_000

def _ensure_store():
    if not os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, 'w', encoding='utf-8') as f:
            json.dump({}, f)

def _load_store():
    _ensure_store()
    with open(CREDENTIALS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def _save_store(data):
    with open(CREDENTIALS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def _hash_password(password: str, salt: bytes, iterations:int=PBKDF2_ITERATIONS) -> str:
    dk = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, iterations)
    return dk.hex()

def create_user(username: str, password: str) -> bool:
    """Create a user with salted PBKDF2-HMAC-SHA256 password.

    Returns True on success, False if user already exists.
    """
    data = _load_store()
    if username in data:
        return False
    salt = secrets.token_bytes(16)
    pwd_hash = _hash_password(password, salt)
    data[username] = {
        'salt': salt.hex(),
        'hash': pwd_hash,
        'iterations': PBKDF2_ITERATIONS,
        'created_at': int(time.time())
    }
    _save_store(data)
    return True

def verify_user(username: str, password: str) -> bool:
    data = _load_store()
    user = data.get(username)
    if not user:
        # avoid leaking timing difference
        secrets.compare_digest('x', 'y')
        return False
    salt = bytes.fromhex(user['salt'])
    expected_hash = user['hash']
    iterations = int(user.get('iterations', PBKDF2_ITERATIONS))
    provided_hash = _hash_password(password, salt, iterations)
    return secrets.compare_digest(provided_hash, expected_hash)

def list_users() -> list:
    data = _load_store()
    return list(data.keys())

def _cli():
    import getpass
    print('Secure login demo (PBKDF2-HMAC-SHA256).')
    while True:
        cmd = input("Choose: [c]reate, [l]ogin, [q]uit> ").strip().lower()
        if cmd == 'q':
            break
        if cmd == 'c':
            username = input('Username: ').strip()
            password = getpass.getpass('Password: ')
            ok = create_user(username, password)
            print('Created' if ok else 'User exists')
        elif cmd == 'l':
            username = input('Username: ').strip()
            password = getpass.getpass('Password: ')
            if verify_user(username, password):
                print('Login successful')
            else:
                print('Login failed')
        else:
            print('Unknown command')

if __name__ == '__main__':
    _cli()
