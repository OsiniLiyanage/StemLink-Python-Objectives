"""
SESSION 07 - Question 3: Bank Account
Topics: Classes, @property, @staticmethod, decorators, error handling

INSTRUCTIONS:  
Complete the BankAccount class below. Replace 'pass' with your code.
Run this file to test your implementation.
"""


class BankAccount:
    """A class to represent a bank account with deposits and withdrawals."""

    def __init__(self, owner:str, balance:float=0)-> None:
        """
        Initialize a new bank account.

        Args:
            owner (str): Account owner's name
            balance (int/float): Initial balance (default 0)

        Raises:
            ValueError: If initial balance is negative
        """
        # TODO: Validate balance is not negative (raise ValueError if it is)
        # TODO: Store owner name
        # TODO: Store balance in self._balance (private, use _ prefix)
        # TODO: Initialize empty transactions list: self._transactions = []
        if balance<0:
            raise ValueError("balance can't be negative")
        
        self.owner:str = owner
        self._balance:float = balance
        self._transactions:list[str]=[] 


    def deposit(self, amount:float)->None:
        """
        Deposit money into the account.

        Args:
            amount (int/float): Amount to deposit

        Raises:
            ValueError: If amount is not positive
        """
        # TODO: Validate amount is positive (raise ValueError if not)
        # TODO: Add to self._balance
        # TODO: Record transaction: f"Deposit: +${amount:.2f}"
        if not isinstance(amount,(int,float)) or amount<=0:
            raise ValueError("Amount should be positive")
        self._balance+= amount
        self._transactions.append(f"Deposit: +${amount:.2f}")

    def withdraw(self, amount:float)-> None:
        """
        Withdraw money from the account.

        Args:
            amount (int/float): Amount to withdraw

        Raises:
            ValueError: If amount is not positive or exceeds balance
        """
        # TODO: Validate amount is positive (raise ValueError if not)
        # TODO: Check if amount > balance (raise ValueError: "Insufficient funds!")
        # TODO: Subtract from self._balance
        # TODO: Record transaction: f"Withdrawal: -${amount:.2f}"
        if not isinstance(amount,(int,float)) or amount<=0:
            raise ValueError("s=amount should be positive.")
        if amount> self._balance:
            raise ValueError("Insufficient funds!")
        self._balance-=amount
        self._transactions.append(f"Withdrawal: -${amount:.2f}")

    @property
    def balance(self)->float:
        """
        Get the current account balance.

        Returns:
            int/float: Current balance
        """
        # TODO: Return self._balance
        return self._balance

    @property
    def status(self) ->str:
        """
        Get the account status based on balance.

        Returns:
            str: "Overdrawn" (< 0), "Low" (0-99), or "Good" (>= 100)
        """
        # TODO: Return appropriate status based on balance
        if self._balance>=100:
            return "Good"
        elif self._balance>= 0:
            return "Low"
        else:
            return "Overdrawn"

    @property
    def transaction_count(self):
        """
        Get the number of transactions.

        Returns:
            int: Length of transactions list
        """
        # TODO: Return length of self._transactions
        return len(self._transactions)

    @staticmethod
    def is_valid_amount(amount:float)-> bool:
        """
        Check if an amount is valid (positive number).

        Args:
            amount: Value to check

        Returns:
            bool: True if amount is a number and positive, False otherwise
        """
        # TODO: Check if amount is a number (int or float)
        # TODO: Check if amount is positive (> 0)
        # TODO: Return True only if both conditions are met
        return isinstance(amount,(int,float)) and amount>0

    def __str__(self)-> str:
        """
        Return a string representation of the account.

        Returns:
            str: Formatted account info

        Example:
            "Account(Alice, $550.00, Status: Good)"
        """
        # TODO: Create formatted string with owner, balance, and status
        # TODO: Format balance to 2 decimal places
        # TODO: Format: "Account({owner}, ${balance:.2f}, Status: {status})"
        return f"Account({self.owner}, ${self.balance:.2f}, Status: {self.status})"


# =============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# =============================================================================

def test_bank_account():
    """Test BankAccount class"""
    print("="*60)
    print("TESTING BANK ACCOUNT CLASS")
    print("="*60)

    # Test 1: Create account
    print("\n[Test 1] Creating account...")
    try:
        acc = BankAccount("Alice", 500)
        print("✓ PASS: Account created successfully")
    except Exception as e:
        print(f"✗ FAIL: {e}")
        return

    # Test 2: Check initial balance
    print("\n[Test 2] Checking initial balance...")
    if acc.balance == 500:
        print(f"✓ PASS: Balance = ${acc.balance:.2f}")
    else:
        print(f"✗ FAIL: Expected $500.00, got ${acc.balance:.2f}")

    # Test 3: Deposit
    print("\n[Test 3] Depositing money...")
    try:
        acc.deposit(100)
        if acc.balance == 600:
            print(f"✓ PASS: After deposit, balance = ${acc.balance:.2f}")
        else:
            print(f"✗ FAIL: Expected $600.00, got ${acc.balance:.2f}")
    except Exception as e:
        print(f"✗ FAIL: {e}")

    # Test 4: Withdraw
    print("\n[Test 4] Withdrawing money...")
    try:
        acc.withdraw(50)
        if acc.balance == 550:
            print(f"✓ PASS: After withdrawal, balance = ${acc.balance:.2f}")
        else:
            print(f"✗ FAIL: Expected $550.00, got ${acc.balance:.2f}")
    except Exception as e:
        print(f"✗ FAIL: {e}")

    # Test 5: Check status (Good)
    print("\n[Test 5] Checking account status...")
    if acc.status == "Good":
        print(f"✓ PASS: Status = '{acc.status}'")
    else:
        print(f"✗ FAIL: Expected 'Good', got '{acc.status}'")

    # Test 6: Transaction count
    print("\n[Test 6] Checking transaction count...")
    if acc.transaction_count == 2:
        print(f"✓ PASS: Transaction count = {acc.transaction_count}")
    else:
        print(f"✗ FAIL: Expected 2, got {acc.transaction_count}")

    # Test 7: String representation
    print("\n[Test 7] Testing __str__...")
    str_repr = str(acc)
    if "Alice" in str_repr and "550" in str_repr and "Good" in str_repr:
        print(f"✓ PASS: {str_repr}")
    else:
        print(f"✗ FAIL: String representation incorrect: {str_repr}")

    # Test 8: Insufficient funds
    print("\n[Test 8] Trying to withdraw more than balance...")
    try:
        acc.withdraw(10000)
        print("✗ FAIL: Should raise ValueError for insufficient funds")
    except ValueError as e:
        print(f"✓ PASS: ValueError raised: {e}")

    # Test 9: Negative deposit
    print("\n[Test 9] Trying to deposit negative amount...")
    try:
        acc.deposit(-50)
        print("✗ FAIL: Should raise ValueError for negative amount")
    except ValueError:
        print("✓ PASS: ValueError raised for negative amount")

    # Test 10: Static method - valid amounts
    print("\n[Test 10] Testing @staticmethod is_valid_amount...")
    if (BankAccount.is_valid_amount(50) and
        not BankAccount.is_valid_amount(-10) and
        not BankAccount.is_valid_amount("abc")):
        print("✓ PASS: is_valid_amount works correctly")
    else:
        print("✗ FAIL: is_valid_amount logic incorrect")

    # Test 11: Status transitions
    print("\n[Test 11] Testing status transitions...")
    acc2 = BankAccount("Bob", 600)
    acc2.withdraw(550)  # Balance = 50
    if acc2.status == "Low":
        print(f"✓ PASS: Low balance status = '{acc2.status}'")
    else:
        print(f"✗ FAIL: Expected 'Low', got '{acc2.status}'")

    # Test 12: Overdrawn status (if allowed)
    print("\n[Test 12] Testing edge cases...")
    acc3 = BankAccount("Charlie", 100)
    if acc3.balance == 100:
        print("✓ PASS: Default balance works")
    else:
        print(f"✗ FAIL: Default balance incorrect")

    print("\n" + "="*60)
    print("TESTS COMPLETE")
    print("="*60)


if __name__ == "__main__":
    test_bank_account()
    print("\n💡 TIP: Implement all methods to pass all tests!")
    print("💡 TIP: Use @property for balance and status!")
    print("💡 TIP: Use @staticmethod for is_valid_amount!")
    print("💡 TIP: Use self._balance (with underscore) for private data!")
