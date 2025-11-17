
from typing import List, Optional
import threading


class InsufficientFundsError(Exception):
    pass


class BankAccount:


    def __init__(self, owner: str, balance: float = 0.0, thread_safe: bool = False) -> None:

        if balance < 0:
            raise ValueError("Initial balance cannot be negative")

        self.owner = owner
        self._balance = float(balance)
        self._transactions: List[str] = []
        # Use a lock only when thread safety is requested to avoid unnecessary overhead
        self._lock: Optional[threading.Lock] = threading.Lock() if thread_safe else None

    def deposit(self, amount: float) -> float:

        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        # Acquire lock if present to make operation atomic
        if self._lock:
            with self._lock:
                self._balance += amount
        else:
            self._balance += amount

        # Record a simple transaction (keeps things human readable)
        self._transactions.append(f"Deposit: +{amount:.2f}")
        return self._balance

    def withdraw(self, amount: float) -> float:
        """Withdraw a positive amount from the account and return the new balance.

        Raises:
            ValueError: If amount is not positive.
            InsufficientFundsError: If amount is greater than the available balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        # Perform check and mutation under lock if available
        if self._lock:
            with self._lock:
                if amount > self._balance:
                    raise InsufficientFundsError("Insufficient funds for withdrawal")
                self._balance -= amount
        else:
            if amount > self._balance:
                raise InsufficientFundsError("Insufficient funds for withdrawal")
            self._balance -= amount

        self._transactions.append(f"Withdraw: -{amount:.2f}")
        return self._balance

    def balance(self) -> float:
        """Return the current balance (read-only)."""
        # No mutation here; read is safe even without a lock in most contexts but
        # if strict consistency with concurrent writers is required, a lock can be used.
        return self._balance

    def get_transactions(self) -> List[str]:
        """Return a shallow copy of the transaction history."""
        return list(self._transactions)
