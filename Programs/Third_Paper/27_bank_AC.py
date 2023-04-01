class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be greater than zero."
        else:
            self.balance += amount
            return f"Successfully deposited {amount}. New balance is {self.balance}."
    
    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be greater than zero."
        elif amount > self.balance:
            return "Insufficient funds."
        else:
            self.balance -= amount
            return f"Successfully withdrew {amount}. New balance is {self.balance}."
    
    def get_balance(self):
        return f"Account balance is {self.balance}."

my_account1 = BankAccount("1234567890", "Vinayak", 1000)
my_account2 = BankAccount("1234567891", "Vishal", 2000)


print(my_account1.deposit(500))    # Output: "Successfully deposited 500. New balance is 1500."
print(my_account1.withdraw(200))  # Output: "Successfully withdrew 200. New balance is 1300"
print(my_account1.get_balance())   # Output: "Account balance is 1300."
print()
print(my_account2.deposit(0))    # Output: "Deposit amount must be greater than zero."
print(my_account2.withdraw(3000))  # Output: "Insufficient funds"
print(my_account2.get_balance())   # Output: "Account balance is 2000."

