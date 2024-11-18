import pandas as pd
import os

# Predefined username and password
correct_username = "admin"
correct_password = "password123"

# Prompt the user to enter their username and password
input_username = input("Enter your username: ")
input_password = input("Enter your password: ")

# Check if the entered username and password are correct
if input_username == correct_username and input_password == correct_password:
    print("Access granted! Welcome!")
    
    class banking:
        def __init__(self, balance, acc):
            self.balance = balance
            self.acc = acc
            self.transactions_file = f"transactions_{self.acc}.xlsx"

            # Initialize the Excel file if it doesn't exist
            if not os.path.exists(self.transactions_file):
                self.init_excel()

        def init_excel(self):
            df = pd.DataFrame(columns=["Transaction Type", "Amount", "Balance", "Account Number"])
            df.to_excel(self.transactions_file, index=False)

        def record_transaction(self, transaction_type, amount):
            new_balance = self.get_balance()
            df = pd.DataFrame({
                "Transaction Type": [transaction_type],
                "Amount": [amount],
                "Balance": [new_balance],
                "Account Number": [self.acc]
            })
            df.to_excel(self.transactions_file, index=False, header=False, startrow=len(pd.read_excel(self.transactions_file))+1, engine='openpyxl')

        def credit(self, amount):
            self.balance += amount
            print("Rs.", amount, "was credited")
            print("Total balance = ", self.get_balance())
            self.record_transaction("Credit", amount)

        def get_balance(self):
            return self.balance

        def debit(self, amount):
            if amount > self.balance:
                print("Insufficient balance!")
            else:
                self.balance -= amount
                print("Rs.", amount, "was debited")
                print("Total balance = ", self.get_balance())
                self.record_transaction("Debit", amount)
    
    # Create a banking object
    acc1 = banking(100000, 24566)
    print("Account Number:", acc1.acc)
    
    # Perform some transactions
    acc1.credit(2000)
    acc1.debit(78000)
else:
    print("Access denied! Incorrect username or password.")
