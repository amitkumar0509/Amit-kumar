username = "panditdinesh"
password ="Rajgrih@t732453753"

input_username = input("Enter your username: ")
input_password = input("Enter your password: ")

if input_username == username and input_password == password:
    print("Access granted! Welcome!")
    
    class banking:
        def __init__(self,balance,acc):
            self.balance = balance
            self.acc = acc
    
        def credit(self,amount):
            self.balance += amount
            print("Rs.",amount,"was credited")
            print("Total balance = ",self.get_balance())
        def get_balance(self):
            return self.balance
        def debit(self,amount):
            self.balance -= amount
            print("Rs.",amount,"was debited")
            print("Total balance = ",self.get_balance())
        
    acc1 = banking(100000,24566)
    print(acc1.acc)
    acc1.credit(2000877)
            

else:
    print("Access denied!")
