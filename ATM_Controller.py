# ATM
# 1. Account_Login
# 2. Logout
# 3. Deposit
# 4. Withdraw
# 5. Transfer
# 6. See Balance
# 7.EXIT


account1 = 1111
pw1 = 7777
balance1 = 55000

account2 = 2222
pw2 = 5555
balance2 = 80000

log = -1

run = True
while run:
    print("<Login Status>")
    if log == 1:
        print(account1, "Login Processing...")
    elif log == 2:
        print(account2, "Login Processing...")
    else:
        print("Logout")

    print("1.Login")
    print("2.Logout")
    print("3.Deposit")
    print("4.Withdraw")
    print("5.Transfer")
    print("6.Balance")
    print("0.Exit")

    choice = int(input("MENU : "))
    if choice == 1:
        if log == -1:
            acc = int(input("ID  : "))
            pw = int(input("PW  : "))

            if acc == account1 and pw == pw1:
                log = 1
                print(account1, "Welcome.")
            elif acc == account2 and pw == pw2:
                log = 2
                print(account2, "Welcome.")
            else:
                print("Please check your account and passwords.")
        else:
            if log == 1:
                print(account1, "Login Processing...")
            elif log == 2:
                print(account2, "Login Processing...")
    elif choice == 2:
        if log != -1:
            log = -1
            print("Logged Out.")
        else:
            print("Please Login.")
    elif choice == 3:
        if log != -1:
            money = int(input("Deposit amount : "))

            if log == 1:
                balance1 += money
            elif log == 2:
                balance2 += money
        else:
            print("Please Login.")

    elif choice == 4:
        if log != -1:
            money = int(input("Withdraw amount : "))

            if log == 1:
                if money <= balance1:
                    balance1 -= money
                else:
                    print("lack of Balance.")
            elif log == 2:
                if money <= balance2:
                    balance2 -= money
                else:
                    print("lack of Balance.")
        else:
            print("Please Login.")
    elif choice == 5:
        if log != -1:
            acc = int(input("recipient's account : "))

            if log == 1:
                if acc == account2:
                    money = int(input("Transfer amount : "))

                    if money <= balance1:
                        balance1 -= money
                        balance2 += money
                    else:
                        print("lack of Balance.")
                else:
                    print("Please check your account.")
            elif log == 2:
                if acc == account1:
                    money = int(input("Transfer amount : "))

                    if money <= balance2:
                        balance2 -= money
                        balance1 += money
                    else:
                        print("lack of Balance.")
                else:
                    print("Please check your account.")
        else:
            print("Please Login.")
    elif choice == 6:
        if log != -1:
            print("balance1 =", balance1)
            print("balance2 =", balance2)
        else:
            print("Please Login.")
    elif choice == 0:
        run = False
        print("Program Exit")
