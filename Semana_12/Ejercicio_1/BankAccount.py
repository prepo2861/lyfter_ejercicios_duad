"""
Bank account system using inheritance.

BankAccount:
- Stores the account balance.
- Allows deposits and withdrawals.

SavingsAccount:
- Inherits from BankAccount.
- Has a minimum balance requirement.
- Prevents withdrawals that would leave the account
  below the minimum balance.
"""


class BankAccount:

    # Initialize the account balance
    def __init__(self, balance):

        self.balance = balance

    # Deposit money into the account
    def deposit_money(self):

        try:

            # Request the deposit amount
            cash_deposit = int(
                input(
                    "Please enter the amount of money "
                    "that you want to deposit: "
                )
            )

            # Validate that the amount is positive
            if cash_deposit <= 0:
                raise ValueError

            # Add the deposit to the current balance
            self.balance += cash_deposit

            print("*****************************************************")

            print(
                f"The amount that you deposited is: "
                f"${cash_deposit}\n"
                f"And your new balance is: "
                f"${self.balance}"
            )

            print("*****************************************************")

            input("\nPress Enter to return to menu...")

            return self.balance

        except ValueError:

            print(
                "You must enter a positive number! "
                "Please try again."
            )

    # Withdraw money from the account
    def withdraw_money(self):

        # Check if there is money available
        if self.balance <= 0:

            print("You don't have money in your account!")
            return

        try:

            # Request the withdrawal amount
            cash_withdrawal = int(
                input(
                    "Please enter the amount "
                    "you want to withdraw: "
                )
            )

            # Validate that the amount is positive
            if cash_withdrawal <= 0:
                raise ValueError

            # Verify that the account has enough funds
            if cash_withdrawal > self.balance:

                print(
                    "You can't withdraw this amount. "
                    "Please try again."
                )

                return

            # Update the balance
            self.balance -= cash_withdrawal

            print("*****************************************************")

            print(
                f"The amount that you withdrew is: "
                f"${cash_withdrawal}\n"
                f"And your new balance is: "
                f"${self.balance}"
            )

            print("*****************************************************")

            input("\nPress Enter to return to menu...")

        except ValueError:

            print(
                "Error, you must enter a positive number!"
            )

    # Display the current balance
    def show_balance(self):

        print(f"Current balance: ${self.balance}")


# SavingsAccount inherits from BankAccount
class SavingsAccount(BankAccount):

    # Initialize balance and minimum balance
    def __init__(self, balance, min_balance):

        super().__init__(balance)

        self.min_balance = min_balance

    # Override the withdraw method
    def withdraw_money(self):

        # Check if the account has any available balance
        if self.balance <= 0:

            print("You don't have money in your account!")
            return

        try:

            # Request the withdrawal amount
            cash_withdrawal = int(
                input(
                    "Please enter the amount "
                    "you want to withdraw: "
                )
            )

            # Validate that the amount is positive
            if cash_withdrawal <= 0:
                raise ValueError

            # Verify that the withdrawal does not
            # exceed the current balance
            if cash_withdrawal > self.balance:

                print(
                    "You can't withdraw this amount. "
                    "Please try again."
                )

                return

            # Calculate the new balance
            new_balance = (
                self.balance - cash_withdrawal
            )

            # Verify that the new balance does not
            # fall below the minimum balance
            if new_balance < self.min_balance:

                print("*******************************************")

                print(
                    "The withdrawal would leave the "
                    "account below the minimum balance.\n"
                    f"Your minimum balance is: "
                    f"${self.min_balance}"
                )

                print("*******************************************")

                input(
                    "\nPress Enter to return to menu..."
                )

                return

            # Update the balance
            self.balance = new_balance

            print("*************************************************")

            print(
                f"The amount that you withdrew is: "
                f"${cash_withdrawal}\n"
                f"And your new balance is: "
                f"${self.balance}"
            )

            print("*************************************************")

            input(
                "\nPress Enter to return to menu..."
            )

        except ValueError:

            print(
                "Error, you must enter a positive number!"
            )

    # Display the balance and minimum balance
    def show_balance(self):

        print("********************************************************")

        print(
            f"Your current balance is: "
            f"${self.balance}"
        )

        print(
            f"Your minimum balance is: "
            f"${self.min_balance}"
        )

        print("********************************************************")

        input("\nPress Enter to return to menu...")