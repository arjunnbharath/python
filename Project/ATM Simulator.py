money = 0
transactions = []
pin = 123


# ==============================
#        ATM FUNCTIONS
# ==============================

def check_balance(money):
    print("\n===== ACCOUNT BALANCE =====")
    print(f"Current Balance : ₹{money}")
    print("===========================\n")


def deposit_money(money):
    deposit = int(input("Enter amount to deposit: ₹"))

    if deposit <= 0:
        print("❌ Invalid amount!")

    else:
        money = money + deposit

        print(f"✅ ₹{deposit} deposited successfully.")
        print(f"💰 Current Balance : ₹{money}")

        transactions.append(
            f"Deposited ₹{deposit} | Balance ₹{money}"
        )

    return money, transactions


def withdraw_money(money):
    withdraw = int(input("Enter amount to withdraw: ₹"))

    if withdraw <= 0:
        print("❌ Invalid amount!")

    elif withdraw > money:
        print("❌ Insufficient balance!")

    else:
        money = money - withdraw

        print(f"✅ ₹{withdraw} withdrawn successfully.")
        print(f"💰 Current Balance : ₹{money}")

        transactions.append(
            f"Withdrawn ₹{withdraw} | Balance ₹{money}"
        )

    return money, transactions


def history(transactions):
    print("\n===== TRANSACTION HISTORY =====")

    if not transactions:
        print("No transactions yet.")

    else:
        for number, transaction in enumerate(transactions, start=1):
            print(f"{number}. {transaction}")

    print("===============================\n")


# ==============================
#        CHANGE PIN
# ==============================

def change_pin(pin):

    print("\n===== Change PIN =====")

    new_pin = int(input("Enter the new PIN: "))

    pin = new_pin

    print("✅ PIN changed successfully!")

    return pin


# ==============================
#        LOGIN AGAIN
# ==============================

def login(money, transactions, pin):

    login_choice = input(
        "\nDo you want to login again? Press (y/n): "
    )

    login_choice = login_choice.lower()

    if login_choice == "y":

        welcome(money, transactions, pin)

    else:

        print("\nLogging out....")
        print("Have a great day! 👋")
        print("\n" + "=" * 25)


# ==============================
#        ATM MENU
# ==============================

def atm_menu(money, transactions, pin):

    while True:

        print("\n========== ATM ==========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Change PIN")
        print("6. Exit")
        print("=========================")

        choice = input("Enter your choice: ")

        if choice == "1":

            check_balance(money)

        elif choice == "2":

            money, transactions = deposit_money(money)

        elif choice == "3":

            money, transactions = withdraw_money(money)

        elif choice == "4":

            history(transactions)

        elif choice == "5":

            pin = change_pin(pin)

        elif choice == "6":

            print("\nThank you for using our ATM! 💳")

            return money, transactions, pin

        else:

            print("❌ Invalid choice! Please select 1-6.")


# ==============================
#        PIN AUTHENTICATION
# ==============================

def welcome(money, transactions, pin):

    print("================================")
    print("       WELCOME TO PYTHON BANK")
    print("================================")

    attempt = 0
    max_attempts = 3

    while attempt < max_attempts:

        password = int(input("Enter your PIN: "))

        if password == pin:

            print("\n✅ Login successful!")
            print("Welcome to your account. 💳")

            money, transactions, pin = atm_menu(
                money,
                transactions,
                pin
            )

            # Ask whether user wants to login again
            login(money, transactions, pin)

            break

        else:

            attempt = attempt + 1

            remaining = max_attempts - attempt

            if remaining > 0:

                print(
                    f"❌ Incorrect PIN! "
                    f"You have {remaining} attempt(s) left."
                )

            else:

                print("❌ Incorrect PIN!")


    # ==============================
    #        ACCOUNT LOCK
    # ==============================

    if attempt == max_attempts:

        print("\n🔒 ACCOUNT LOCKED")
        print("Too many incorrect PIN attempts.")


# ==============================
#        START ATM
# ==============================

welcome(money, transactions, pin)