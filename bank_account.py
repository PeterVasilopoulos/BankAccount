class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0):
        # Assign attribute values
        self.int_rate = int_rate
        self.balance = balance
    
    # Deposit 
    def deposit(self, amount):
        self.balance += amount
        return self

    # Withdraw
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insuffiencet funds: Charging a $5 fee")
            self.balance -= amount
        return self

    # Display account info
    def display_account_info(self):
        print(f"Interest Rate: {self.int_rate}, Balance: {self.balance}")
        return self

    # Yield interest
    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self



account1 = BankAccount(0.01, 200)
account1.deposit(10).deposit(20).deposit(50).withdraw(100).yield_interest().display_account_info()

account2 = BankAccount()
account2.deposit(1000).deposit(150).withdraw(900).withdraw(100).withdraw(10).withdraw(20).yield_interest().display_account_info()