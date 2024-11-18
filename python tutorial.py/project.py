def deposit():
    while True:
    amount= input("WHAT WOULD YOU LIKE TO DEPOSIT? $")
        if amount.isdigit():
    amount= int(amount)
        if amount > 0:
                break
        else:
                print("Amount must be greater than 0.")
    else:
        print("please enter a number.")
            
    return amount
deposit()

            
