
# Method 1: Using for loop with range()
def print_multiples_for_range(number):
    print(f"\nMethod 1: For Loop with range()")
    print(f"First 10 multiples of {number}:")
    print("-" * 40)
    for i in range(1, 11):
        multiple = number * i
        print(f"{number} x {i} = {multiple}")


# Method 2: Using while loop
def print_multiples_while(number):
    print(f"\nMethod 2: While Loop")
    print(f"First 10 multiples of {number}:")
    print("-" * 40)
    i = 1
    while i <= 10:
        multiple = number * i
        print(f"{number} x {i} = {multiple}")
        i += 1

# Main program
if __name__ == "__main__":
    print("=" * 50)
    print("PROGRAM: Print First 10 Multiples of a Number")
    print("=" * 50)
    
    # Take input from user
    try:
        number = int(input("\nEnter a number: "))
        
        # Execute all methods
        print_multiples_for_range(number)
        print_multiples_while(number)
        
    except ValueError:
        print("Error: Please enter a valid integer number!")
    except Exception as e:
        print(f"An error occurred: {e}")
