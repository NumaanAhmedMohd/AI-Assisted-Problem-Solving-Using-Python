"""run_fib_tests.py

Small test runner to verify fibonacci_recursive functions.
"""

from fibonacci_recursive import fib, fib_memo


def run_tests():
    tests = [
        (0, 0),
        (1, 1),
        (5, 5),
        (10, 55),
    ]
    all_ok = True
    for n, expected in tests:
        got = fib(n)
        ok = got == expected
        print(f'fib({n}) -> {got} (expected {expected}) ->', 'PASS' if ok else 'FAIL')
        all_ok = all_ok and ok
    # test memoized
    got = fib_memo(30)
    print('fib_memo(30) ->', got)
    # test input validation
    try:
        fib(-1)
        print('fib(-1) did not raise ValueError -> FAIL')
        all_ok = False
    except ValueError:
        print('fib(-1) raised ValueError -> PASS')
    try:
        fib(3.5)
        print('fib(3.5) did not raise TypeError -> FAIL')
        all_ok = False
    except TypeError:
        print('fib(3.5) raised TypeError -> PASS')

    return all_ok


if __name__ == '__main__':
    ok = run_tests()
    if ok:
        print('\nAll tests passed')
    else:
        print('\nSome tests failed')
