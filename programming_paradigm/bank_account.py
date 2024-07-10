# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initializes a BankAccount with an optional initial balance (default is 0).
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.
        """
        if amount > 0:
            self.account_balance += amount
            return True
        else:
            print("Invalid deposit amount. Please provide a positive value.")
            return False

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account if funds are sufficient.
        Returns True if successful, False otherwise.
        """
        if amount > 0 and self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        """
        Displays the current account balance.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")

# Example usage:
if __name__ == "__main__":
    account = BankAccount(100)  # Example starting balance
    account.deposit(50)
    account.withdraw(20)
    account.display_balance()
