"""analyze_login.py

Analyzes `insecure_login.py` and `secure_login.py` for insecure patterns.
Performs static checks (searches for strings/patterns) and small dynamic checks
like detecting hardcoded credential dictionaries.

Run: python analyze_login.py
"""

import ast
import importlib.util
import inspect
import json
import os
import re
import sys

BASE = os.path.dirname(__file__)
INSECURE = os.path.join(BASE, 'insecure_login.py')
SECURE = os.path.join(BASE, 'secure_login.py')

def read(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception:
        return ''

def static_checks(src: str, filename: str) -> list:
    """Return list of findings (strings) for static analysis."""
    findings = []
    # Search for hardcoded password-like assignments
    # crude heuristics
    if re.search(r"password\s*=\s*['\"]", src, re.I):
        findings.append('Found assignments to variable named password (possible hardcoded)')
    if re.search(r"HARD[_-]?CODED|hard[_-]?coded", src, re.I):
        findings.append('Found term HARD_CODED/hardcoded')
    if re.search(r"sqlite3|pickle|eval\(|exec\(|os\.system|subprocess\\.", src):
        findings.append('Found potentially dangerous functions or modules (eval/exec/os.system/pickle)')
    if re.search(r"md5\(|sha1\(|sha224\(|sha384\(|sha512\(|hashlib\.md5", src):
        findings.append('Found usage of weak or unspecified hashing functions')
    if re.search(r"\b(passwords?|creds?|credentials?)\b\s*[:=]\s*\{", src, re.I):
        findings.append('Found inline dict-like credential storage')
    # look for plain json write of credentials
    if re.search(r"\.json\(|'credentials'|credentials_secure.json", src):
        findings.append('Mentions credentials JSON store (check if plaintext)')
    return findings

def check_insecure_dynamic(path: str) -> list:
    findings = []
    name = os.path.splitext(os.path.basename(path))[0]
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except Exception as e:
        findings.append(f'Failed to import {name}: {e}')
        return findings
    # check for HARD_CODED variable
    if hasattr(mod, 'HARD_CODED'):
        val = getattr(mod, 'HARD_CODED')
        if isinstance(val, dict) and val:
            findings.append(f'Module defines HARD_CODED with {len(val)} entries (hardcoded credentials)')
    # detect add_user that mutates global dict
    src = read(path)
    if re.search(r"add_user\(|HARD_CODED\[", src):
        findings.append('Adds/modifies in-memory HARD_CODED dict — credentials in code')
    return findings

def analyze_files():
    results = {}
    for p in [INSECURE, SECURE]:
        src = read(p)
        stat = static_checks(src, p)
        dyn = check_insecure_dynamic(p)
        results[os.path.basename(p)] = {
            'static_findings': stat,
            'dynamic_findings': dyn,
        }
    return results

def summarize(results):
    print('\nAnalysis summary:')
    for fname, res in results.items():
        print('\n- ' + fname)
        if not res['static_findings'] and not res['dynamic_findings']:
            print('  No obvious issues found.')
            continue
        for s in res['static_findings']:
            print('  [STATIC] ' + s)
        for d in res['dynamic_findings']:
            print('  [DYNAMIC] ' + d)

def smoke_test_secure():
    print('\nRunning smoke test against secure_login...')
    import secure_login as s
    # create a test user, then verify
    user = '__test__'
    pw = 'S3cure!pass'
    # cleanup existing
    if user in s.list_users():
        print('  test user already exists — skipping create')
    else:
        ok = s.create_user(user, pw)
        print(f'  create_user -> {ok}')
    ok2 = s.verify_user(user, pw)
    print(f'  verify_user -> {ok2}')
    # cleanup (remove from store) for cleanliness
    try:
        path = os.path.join(os.path.dirname(__file__), 'credentials_secure.json')
        with open(path, 'r+', encoding='utf-8') as f:
            data = json.load(f)
            data.pop(user, None)
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()
        print('  cleanup done')
    except Exception as e:
        print('  cleanup failed:', e)

if __name__ == '__main__':
    results = analyze_files()
    summarize(results)
    smoke_test_secure()
