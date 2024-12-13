class BankAccount:
    def __init__(self, depositor_name, account_number, account_type, balance):
        self.depositor_name = depositor_name
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
    def deposit(self, amount):
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
    def withdraw(self, amount):
                self.balance -= amount
                print(f"{amount} withdrawn. New balance: {self.balance}")
    def display_account_details(self): 
        print("Account Details")
        print(f"Name of Depositor: {self.depositor_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}")
account1 = BankAccount("Alice", "123456789", "Savings", 10000)
account1.display_account_details()
account1.deposit(5000)
account1.withdraw(2000)
account1.display_account_details() 
