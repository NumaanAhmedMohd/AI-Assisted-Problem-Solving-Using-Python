from bank_account import BankAccount, InsufficientFundsError


def run_tests() -> None:
    # Create account with initial balance 100
    acct = BankAccount("Alice", balance=100.0)
    assert acct.balance() == 100.0

    # Deposit 50 -> balance 150
    new_bal = acct.deposit(50.0)
    assert abs(new_bal - 150.0) < 1e-9
    assert acct.balance() == 150.0

    # Withdraw 20 -> balance 130
    new_bal = acct.withdraw(20.0)
    assert abs(new_bal - 130.0) < 1e-9
    assert acct.balance() == 130.0

    # Attempt to withdraw more than available -> InsufficientFundsError
    try:
        acct.withdraw(1000.0)
    except InsufficientFundsError:
        pass
    else:
        raise AssertionError("Expected InsufficientFundsError for over-withdrawal")

    # Invalid operations should raise ValueError
    try:
        acct.deposit(-10.0)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for negative deposit")

    try:
        acct.withdraw(0.0)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for zero withdrawal")

    # Transaction history should reflect deposits and withdrawals
    tx = acct.get_transactions()
    assert any("Deposit: +50.00" in t for t in tx)
    assert any("Withdraw: -20.00" in t for t in tx)

    print("All BankAccount tests passed")


if __name__ == "__main__":
    run_tests()
