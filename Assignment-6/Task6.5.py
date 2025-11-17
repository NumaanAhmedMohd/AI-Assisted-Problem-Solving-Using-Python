
class BankAccount:
    
    def __init__(self, account_number, account_holder, initial_balance=0.0):
       
        self.account_number = account_number
        self.account_holder = account_holder
        
        # Validate initial balance
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.balance = float(initial_balance)
    
    def deposit(self, amount):
       
        if amount <= 0:
            print("Error: Deposit amount must be positive!")
            return False
        
        self.balance += amount
        print(f"Deposit successful! Amount deposited: ${amount:.2f}")
        return True
    
    def withdraw(self, amount):
      
        if amount <= 0:
            print("Error: Withdrawal amount must be positive!")
            return False
        
        if amount > self.balance:
            print(f"Error: Insufficient balance! Current balance: ${self.balance:.2f}")
            return False
        
        self.balance -= amount
        print(f"Withdrawal successful! Amount withdrawn: ${amount:.2f}")
        return True
    
    def get_balance(self): 
        return self.balance
    
    def display_balance(self):
        print(f"\nAccount Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance:.2f}")
    
    def display_account_info(self):
        print("\n" + "=" * 50)
        print("ACCOUNT INFORMATION")
        print("=" * 50)
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ${self.balance:.2f}")
        print("=" * 50)


if __name__ == "__main__":
    print("=" * 60)
    print("LOGIC ERROR DEMONSTRATION - Infinite Loop")
    print("=" * 60)
    print("\nProblem: count_down_incorrect() function has a logic error")
    print("Error: Uses n += 1 (increment) instead of n -= 1 (decrement)")
    print("Result: Infinite loop because n never decreases, always stays >= 0")
    print("\n" + "-" * 60)
    print("CORRECTED VERSION DEMONSTRATION:")
    print("-" * 60)
    
    
    print("\n" + "=" * 60)
    print("WARNING: Do not run count_down_incorrect() - it will cause infinite loop!")
    print("=" * 60)
    print("\n" + "=" * 60)
    print("BANK ACCOUNT MANAGEMENT SYSTEM")
    print("=" * 60)
    
    try:
        # Create a bank account
        print("\nCreating new bank account...")
        account_number = input("Enter account number: ")
        account_holder = input("Enter account holder name: ")
        
        initial_balance_input = input("Enter initial balance (press Enter for $0.00): ")
        initial_balance = float(initial_balance_input) if initial_balance_input else 0.0
        
        # Initialize bank account
        account = BankAccount(account_number, account_holder, initial_balance)
        print("\nAccount created successfully!")
        account.display_account_info()
        
        # Menu-driven program
        while True:
            print("\n" + "-" * 60)
            print("MENU:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Display Account Info")
            print("5. Exit")
            print("-" * 60)
            
            choice = input("Enter your choice (1-5): ")
            
            if choice == "1":
                amount = float(input("Enter amount to deposit: $"))
                account.deposit(amount)
                account.display_balance()
            
            elif choice == "2":
                amount = float(input("Enter amount to withdraw: $"))
                account.withdraw(amount)
                account.display_balance()
            
            elif choice == "3":
                balance = account.get_balance()
                print(f"\nCurrent Balance: ${balance:.2f}")
            
            elif choice == "4":
                account.display_account_info()
            
            elif choice == "5":
                print("\nThank you for using Bank Account Management System!")
                print("\n" + "=" * 60)
                print("CODE ANALYSIS:")
                print("=" * 60)
               
                break
            
            else:
                print("Invalid choice! Please enter a number between 1-5.")
        
    except ValueError as e:
        print(f"Error: {e}")
        print("Please enter valid numeric values.")
    except Exception as e:
        print(f"An error occurred: {e}")
