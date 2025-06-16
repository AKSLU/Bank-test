class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return None
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return None
        if amount <= 0:
            return None
        self.balance -= amount

    def transfer_to(self, target_account, amount):
        self.withdraw(amount)
        target_account.deposit(amount)
