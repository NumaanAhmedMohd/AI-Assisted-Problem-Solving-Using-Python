def sum_to_n_for_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
def sum_to_n_while_loop(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total
def sum_to_n_recursive(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return n + sum_to_n_recursive(n - 1)
def sum_to_n_formula(n):
    return n * (n + 1) // 2

if __name__ == "__main__":
    print("=" * 60)
    print("SUM OF FIRST N NUMBERS PROGRAM")
    print("=" * 60)
    
    try:
        n = int(input("\nEnter a positive integer (n): "))
        
        if n < 0:
            print("Error: Please enter a positive integer!")
        else:
            print("\n" + "=" * 60)
            print("RESULTS USING DIFFERENT LOOPING METHODS:")
            print("=" * 60)
            
            result1 = sum_to_n_for_loop(n)
            print(f"For Loop: {result1}")
            
            result2 = sum_to_n_while_loop(n)
            print(f"While Loop: {result2}")
            
            result3 = sum_to_n_recursive(n)
            print(f"Recursive: {result3}")
            
            result4 = sum_to_n_formula(n)
            print(f"Mathematical Formula: {result4}")
            
            print("\n" + "=" * 60)
            print("EXPLANATION:")
            print("=" * 60)
            print("""
1. FOR LOOP:
   - Iterates from 1 to n using range(1, n+1)
   - Accumulates sum in a variable
   - Simple and readable
   - Time Complexity: O(n)
   - Space Complexity: O(1)

2. WHILE LOOP:
   - Uses counter variable initialized to 1
   - Continues until counter > n
   - Manual counter incrementation
   - Time Complexity: O(n)
   - Space Complexity: O(1)

3. RECURSIVE:
   - Breaks problem into smaller subproblems
   - Base case: n <= 0 returns 0, n == 1 returns 1
   - Recursive case: n + sum(n-1)
   - Time Complexity: O(n)
   - Space Complexity: O(n) due to call stack

4. MATHEMATICAL FORMULA:
   - Uses formula: n * (n + 1) / 2
   - Most efficient method
   - No loops needed
   - Time Complexity: O(1)
   - Space Complexity: O(1)
            """)
            
    except ValueError:
        print("Error: Please enter a valid integer!")
    except Exception as e:
        print(f"An error occurred: {e}")
