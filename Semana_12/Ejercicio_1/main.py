# This is the main file. It controls the bank system menu

from BankAccount import SavingsAccount
from menu import menu_option


def main():

    # Create a savings account with an initial balance
    # and a minimum required balance
    account = SavingsAccount(1000, 200)

    # Main program loop
    while True:

        # Display the menu and get the user's choice
        option = menu_option()

        # Show account balance
        if option == 1:
            account.show_balance()

        # Withdraw money from the account
        elif option == 2:
            account.withdraw_money()

        # Deposit money into the account
        elif option == 3:
            account.deposit_money()

        # Exit the program
        elif option == 4:
            print("Goodbye!")
            break


# Execute the program
if __name__ == "__main__":
    main()