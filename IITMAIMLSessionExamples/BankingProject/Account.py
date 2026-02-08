class Account:
    # Constructor to initialize account ID, owner, and balance
    def __init__(self, accid, owner, balance=0):
        self.accid = int(accid)
        self.owner = owner
        self.balance = balance

    # Method to deposit an amount to the account
    def deposit(self, amount=0):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            raise ValueError("Deposit amount must be positive.")#Use ValueError for invalid deposit amounts
        
    def withdraw(self, amount=0):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: {amount}. New balance: {self.balance}")
            else:
                raise ValueError("Insufficient funds for withdrawal.")  # Use ValueError for insufficient funds
        else:
            raise ValueError("Withdrawal amount must be positive.")  # Use ValueError for invalid withdrawal amounts
        
    def showaccountdetails(self):
        return f"Account ID: {self.accid}, Owner: {self.owner}, Balance: {self.balance}"    
    
accobj1 = Account(101, "Alice", 10000)
accobj1.deposit(20000)
print(accobj1.showaccountdetails())