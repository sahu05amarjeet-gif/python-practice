#Banking Program

def show_balance(balance):
    print("-----------------------")
    print(f"Your balance is {balance:.2f}rs")
    print("-----------------------")

def deposit():
    print("---------------------------------------------------")
    amt = float(input("Enter the amount you want to deposit: "))
    print("---------------------------------------------------")
    if amt < 0:
        print("------------------------------------------------------------")
        print("Your amount cannot be less than zero or negative, Try again!")
        print("------------------------------------------------------------")
        return 0
    else:
        print("************************************************************")
        print("The money has been successfully deposited to your account")
        print("************************************************************")
        return amt    

def withdraw(balance):
    print("--------------------------------------------------------------------------")
    amount = float(input("Enter the amount you want to withdraw from your account: "))
    print("--------------------------------------------------------------------------")

    if amount <= 0:
        print("-------------------------------------------")
        print("You cannot withdraw zero rupees, Try again!")
        print("-------------------------------------------")
        return 0
    elif amount > 50000:
        print("------------------------------------")
        print("You can take upto 50,000rs at a time")
        print("------------------------------------")
        return 0
    elif balance < amount:
        print("---------------------------------------------")
        print("You don't have enough balance in your account")
        print("---------------------------------------------")
        return 0
    else:
        print("************************************************************")
        print("The amount has been successfully withdrawn from your account")
        print("************************************************************")
        return amount

def main():
    balance = 0
    is_running = True

    while (is_running):
        print("Python Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("Not a valid choice")
    print("Thankyou! Have a nice day")
    
if __name__ == '__main__':
    main()


