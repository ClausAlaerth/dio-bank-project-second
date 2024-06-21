# Bank Project - Part 2 - Downgraded to only functions, to abide by the project rules.

import os

main_menu = """
=================Bank System=================

[1] - Register User
[2] - Create Account
[3] - Deposit
[4] - Withdraw
[5] - Show Transactions
[6] - Show Users
[7] - Clear Terminal
[8] - Exit Program

=============================================
"""

transaction_list = []

balance = 0

value_chosen = 0
withdrawal_count = 0
w_amount_limit = 500.00
W_LIMIT_PER_DAY = 3

AGENCY = "0001"
users = []
accounts = []
account_number = 0


def register_user(name, birth, id, adress, *, account=accounts, user=users):

    for x in account:
        if id in x.values():
            print("\nThis ID is already registered.")
            return

    user.append({"name": name, "birth": birth, "id": id, "address": adress})

    print("\nNew user successfully added to the list!")


def create_account(id, *, user=users, account=accounts, agency=AGENCY):

    for y in user:
        if id in y.values():
            global account_number
            account_number += 1
            account.append({"id": id, "agency": agency,
                           "account_num": account_number})

            print("\nYour new account has been created successfully!")
            return

    for y in user:
        if id not in y.values():
            print(
                "\nThe user you want to create an account for, has not been registered.")
            return


def deposit(value, transactions):

    global balance
    if value > 0:
        balance += value
        transactions.append(f"Deposit - R$ {value:.2f}")

        print(f"\nAmount deposited: R$ {value:.2f}")
        print(f"\nBalance: R$ {balance:.2f}")

    else:
        print("Incorrect values.")
        return balance


def withdraw(*, limit_amount=w_amount_limit, limit_day=W_LIMIT_PER_DAY, transactions=transaction_list):

    global balance, value_chosen, withdrawal_count
    if withdrawal_count == limit_day:
        print("\nWithdrawal limit per day reached.")
        return

    elif value_chosen > limit_amount:
        print("\nThe limit withdrawn per operation is R$ 500,00.")
        return

    elif value_chosen > balance:
        print("\nBalance is insuficcient.")

    elif (value_chosen > 0) and (value_chosen <= balance):

        balance -= value_chosen
        transactions.append(f"Withdrawal - R$ {value_chosen:.2f}")

        print(f"\nAmount withdrawn: R$ {value_chosen:.2f}")
        print(f"\nBalance left: R$ {balance:.2f}")

        withdrawal_count += 1

    else:
        print("Incorrect values.")
        return balance


def show_transactions(balance, *, transactions=transaction_list):

    if not transactions:
        print("No transactions were made on this account.")
        return

    print("\n" + "-" * 45 + "\n")
    for x in transactions:
        print(x)

    print(f"\nCurrent balance: R$ {balance:.2f}")
    print("\n" + "-" * 45 + "\n")


def show_users(*, user=users, account=accounts):

    if not user:
        print("\nThere are no registered users.\n")
        return

    else:

        for x in user:
            print("\n" + "-" * 45 + "\n")
            print(f"Name: {x["name"]}")
            print(f"Citizenship ID: {x["id"]}")
            print(f"Birthdate: {x["birth"]}")
            print(f"Address: {x["address"]}\n")

            if account:
                for y in account:
                    if x["id"] in y.values():
                        print(f"Account: {y["account_num"]}")

        print("\n" + "-" * 45)


while True:

    print(main_menu)

    choice = input("=> ")

    if choice == "1":

        print("\nWe need to collect your credentials:\n")

        name = input("Insert your full name: ")
        birth = input("Insert your birthdate: ")
        id = input("Insert your Citizenship ID (Only Numbers): ")
        address = input("Insert your full address: ")

        register_user(name, birth, id, address)

    elif choice == "2":

        id_for_account = input(
            "\nInsert the ID for which you want an account: ")

        create_account(id_for_account)

    elif choice == "3":

        value_chosen = float(input("\nInsert the amount to deposit: "))

        deposit(value_chosen, transaction_list)

    elif choice == "4":

        value_chosen = float(input("\nInsert the amount to withdraw: "))

        withdraw()

    elif choice == "5":
        show_transactions(balance)

    elif choice == "6":
        show_users()

    elif choice == "7":
        os.system("cls")

    elif choice == "8":
        print("\nExiting program...\n")
        break

    else:
        print("\nInvallid choice.")
