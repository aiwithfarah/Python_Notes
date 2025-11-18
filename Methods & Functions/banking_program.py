# Python Banking Program
# 1. Show Balance
# 2. Deposit
# 3. Withrawal

def show_balace(balance):
    print(f"Your balance is ${balance:.2f}")


def deposit():
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0:
        print("{amount} is not a valid amount!")
        return 0
    else:
        return amount


def withdrawal(balance):
    amount = float(input("Enter amount to be withdrawn: "))

    if amount > balance:
        print("Insufficient Funds")
        return 0
    if amount < 0:
        print(f"{amount} is an Invalid Amount! Must ve greater than zero")
        return 0
    else:
        return amount


def main():

    balance = 0
    isRunning = True  # when set to false we will exit the program

    while isRunning:
        print("*****  BANKING PROGRAM  *****")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withrawal")
        print("4. Exit")
        print("-------------------------")

        choice = input("Enter your choice: (1-4) ")
        if choice == '1':
            show_balace(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdrawal(balance)
        elif choice == '4':
            isRunning = False
        else:
            print("That is not a valid choice!")

    print("Thankyou! Have a Nice Day!")


if __name__ == '__main__':
    main()
