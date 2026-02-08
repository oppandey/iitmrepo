class Account:
    def __init__(self, accid, owner, balance=0.0):
        self.accid = int(accid)
        self.owner = owner
        self.balance = float(balance)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance   

    def withdraw(self, amount):
        pass

    def showaccountdetails(self):
        return f"Account ID: {self.accid}, Owner: {self.owner}, Balance: {self.balance}"

class SavingsAccount(Account):
    def __init__(self, accid, owner, balance=0.0, minbal=0.0):
        super().__init__(accid, owner, balance)
        self.minbal = float(minbal)

    def withdraw(self, amount):
        if self.balance - amount < self.minbal:
            raise ValueError("Cannot withdraw beyond minimum balance.")
        return super().withdraw(amount)
    
class CurrentAccount(Account):
    def __init__(self, accid, owner, balance=0.0, overdraft_limit=0.0):
        super().__init__(accid, owner, balance)
        self.overdraft_limit = float(overdraft_limit)

    def withdraw(self, amount):
        if self.balance - amount < -self.overdraft_limit:
            raise ValueError("Cannot withdraw beyond overdraft limit.")
        return super().withdraw(amount)
    