class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

my_account = BankAccount()

my_account.deposit(1000)
print(my_account.get_balance())   # Output: 1000

my_account.withdraw(500)
print(my_account.get_balance())   # Output: 500

my_account.withdraw(1000)   # Output: Insufficient funds
