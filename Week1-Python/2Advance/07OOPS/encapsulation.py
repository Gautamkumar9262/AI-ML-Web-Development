class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient funds or invalid withdrawal amount")

    def get_balance(self):
        return self.__balance

# Example usage
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(f"Current Balance: {account.get_balance()}")
# Trying to access the private attribute directly will raise an AttributeError
# print(account.__balance)  # Uncommenting this line will cause an error
# Output:
# Deposited: 500
# Withdrew: 200
# Current Balance: 1300
