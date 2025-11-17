# Fibonacci (recursive) — explanation

This document explains the recursive Fibonacci function and provides
complexity analysis, edge cases, and suggestions for production use.

## Algorithm (plain recursion)

The Fibonacci sequence is defined as:
- fib(0) = 0
- fib(1) = 1
- fib(n) = fib(n-1) + fib(n-2) for n >= 2

A plain recursive implementation follows this mathematical definition directly: to compute fib(n), call fib(n-1) and fib(n-2) and add the results. The recursion bottoms out at the base cases fib(0) and fib(1).

## Complexity

- Plain recursion:
  - Time complexity: O(2^n) — the computation grows exponentially because the same subproblems are recomputed many times.
  - Space complexity: O(n) due to the call stack depth (maximum recursion depth equals n).

- Memoized recursion (top-down dynamic programming):
  - Time complexity: O(n) — each fib(k) for k<=n is computed once and cached.
  - Space complexity: O(n) for the cache plus O(n) for the recursion stack in the naive memoized recursion (can be reduced by using an iterative approach.)

## Edge cases

- Non-integer `n`: the function raises `TypeError`.
- Negative `n`: the function raises `ValueError` because Fibonacci is defined for non-negative integers in this context.
- Large `n`: the plain recursive function will be very slow; use memoization or an iterative/fast-doubling algorithm.

## Improvements for production

- Use an iterative approach (loop) to achieve O(n) time and O(1) space (only two accumulator variables needed).
- For very large n, use fast doubling algorithm which computes fib(n) in O(log n) time.
- Use memoization or caching when repeated calls for many n are expected.
- Consider big-integer handling (Python's int is arbitrary precision, but some languages need big-int libraries.)
- Add unit tests and benchmarks to ensure performance and correctness.

## Examples

fib(0) = 0
fib(1) = 1
fib(2) = 1
fib(3) = 2
fib(4) = 3
fib(5) = 5
fib(6) = 8

## Tests to try

- Check base cases: fib(0) -> 0, fib(1) -> 1
- Check a larger value: fib(10) -> 55
- Try memoized variant: fib_memo(50)

---

This document accompanies `fibonacci_recursive.py` which contains the code and inline comments.